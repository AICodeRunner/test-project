import openai
import os

# Sæt din OpenAI API-nøgle fra miljøvariabler
openai.api_key = os.getenv("OPENAI_API_KEY")

# Funktion til at forespørge OpenAI API
def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    test_prompt = "Hvad er maskinlæring?"
    response = get_openai_response(test_prompt)
    print(f"OpenAI's svar: {response}")
