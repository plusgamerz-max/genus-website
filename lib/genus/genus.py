from google.genai import Client, types
import os
        
class GeminiGenus:
    def __init__(self, contents, config, model='gemini-3.5-flash-lite', api_key=None, available_fun={}):
        # Initializes the GeminiGenus class with the provided parameters.

        self.model = model
        self.contents = contents if contents is not None else []
        self.config = config
        self.available_fun = available_fun if available_fun is not None else {}
        
        # Gets the API key from the environment variable if not provided
        if not api_key:
            api_key = os.getenv("GEMINI_API_KEY", None)

            if not api_key:
                raise KeyError("Gemini API Key is not set in the environment variables.")
        
        self.api_key = api_key
        self.client = Client(api_key=self.api_key)

    def generate_content(self): # Generates response using the Gemini API
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.contents,
            config=self.config,
        )
        return response
    
    def detect_funcall(self, response): # Detects if a model called a function
        if not response.function_calls:
            return False
        else:
            return True
    
    def execute_fun(self, response): # Runs all the functions that the model called
        detected = self.detect_funcall(response)

        if not detected:
            raise KeyError("No function was called")
        
        self.contents.append(response.candidates[0].content)

        for call in response.function_calls:

            if call.name not in self.available_fun:
                result = {"error": f"{call.name} is not an available function. Available"}
                continue

            # Execute the function
            try:
                result = self.available_fun[call.name](**call.args)
            except Exception as e:
                result = {"error": f"An unexpected error occured:\n {str(e)}"}

            self.contents.append(types.Content(
                role='user',
                parts=[types.Part.from_text(text=str(result))]
            ))

            return self.generate_content()
        
    def chat(self, part: list): # Main function to run the chat with the model, part needs to be generated

        # If a string was passed, convert it to a Part
        if isinstance(part, str):
            parts_list = [types.Part.from_text(text=part)]

        # If a single Part object was passed, wrap it in a list
        elif isinstance(part, types.Part):
            parts_list = [part]

        # If it's already a list, use it directly
        elif isinstance(part, list):
            parts_list = part
        else:
            raise ValueError("Invalid type for 'part'")

        self.contents.append(
            types.Content(
                role='user',
                parts=parts_list
            )
        )

        response = self.generate_content()

        while self.detect_funcall(response):
            response = self.execute_fun(response)

        return response