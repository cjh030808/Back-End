from google import genai
from google.genai import types

env_relation_response_schema = types.Schema(
    type="object",
    properties={
        "related": types.Schema(type="boolean", description="Is the text about an environmental topic?"),
        "word": types.Schema(type="string", description="Word representing the environmental topic.", nullable=True),
    },
    required=["related"],
)


def anl_env_relation(text: str):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=text,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=env_relation_response_schema,
            system_instruction="""
You are an AI text analyzer. Your task is to analyze the user's text and populate the fields of the JSON schema according to the following logic:

- `related` field: Set to `true` if the text is about an environmental topic, otherwise set to `false`.
- `word` field: If `related` is `true`, provide a single noun that best represents the core environmental subject. This can be a concrete object (e.g., 'plastic', 'tree') or an abstract concept (e.g., 'Earth', 'gas'). If `related` is `false`, this field must be null.

Examples for the `word` field logic:
- For 'global warming', the word is 'Earth'.
- For 'illegal trash dumping', the word is 'Trash'.
- For 'carbon dioxide emissions', the word is 'Gas'.
""",
        ),
    )
    return response.text
