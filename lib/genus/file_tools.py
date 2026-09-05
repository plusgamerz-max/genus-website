import os
from google.genai import types

def create_file(path: str, content: str) -> str:
    with open(path, "w") as f:
        f.write(content)
    return "File created successfully"

'''
create_file_dec = types.FunctionDeclaration(
    name='create_file',
    description='Creates a file, relative paths allowed',

    parameters = types.Schema(
        type='OBJECT',

        properties={
            'path': types.Schema(type='STRING')
        },

        required=['path']
    )
)
'''

create_file_dec = {
    'name': 'create_file',
    'description': 'Creates a file, relative paths allowed',

    'parameters': {
        'type': 'OBJECT',

        'properties': {
            'path': {
                'type': 'STRING'
            }
        },

        'required': ['path'],
    }
}