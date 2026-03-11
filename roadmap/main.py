from google import genai
from google.genai import types

API_KEY = "AIzaSyBuOK43KOX_pdszXmT0Gxs_YbvbjFiR2L0"

def roadmap(input:str):
    API_KEY = "AIzaSyBuOK43KOX_pdszXmT0Gxs_YbvbjFiR2L0"
    client = genai.Client(api_key=API_KEY)

    instruction = "your work is to create a roadmap for the given topic.#format : step name + a small description + two youtube link for reference , be short 7 to 8 steps is ok. give step by step so that i can show it in my ui"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction=instruction),
        contents=input
    )
    return response.text
