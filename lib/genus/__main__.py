from google.genai import types
import os
from . import api_key
from .genus import GeminiGenus

# Importing Tools
from . import file_tools as ft

# Config and contents
prompt = "Hello,"
tools = types.Tool(function_declarations=[ft.create_file_dec])

contents = [types.Content(
    role='user',
    parts=[types.Part.from_text(text=prompt)]
)]

config = types.GenerateContentConfig(
    system_instruction = "You are a helpful assistant. You are required to use your tools when needed.",

    tools=[tools],
    automatic_function_calling = types.AutomaticFunctionCallingConfig(
        disable = True
    ),
)

available_fun={
    'create_file': ft.create_file
}

# Main
agent = GeminiGenus(contents, config, available_fun=available_fun, model='gemini-3.6-flash')

try:
    while True:
        part = [types.Part.from_text(text=input("> "))]
        print(f"\n✦ -> {agent.chat(part).text}\n")
except KeyboardInterrupt:
    print("Exiting...")