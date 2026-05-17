# notebooks/test_groq.py
import os
from dotenv import load_dotenv
from groq import Groq

# Charger la cle depuis .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERREUR : GROQ_API_KEY non trouvee dans .env")
    exit()

# Creer le client Groq
client = Groq(api_key=api_key)

# Premier appel
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system",
         "content": "Tu es un assistant medical senegalais. Reponds en francais simple. Maximum 3 phrases."},
        {"role": "user",
         "content": "Quels sont les symptomes du paludisme ?"}
    ],
    max_tokens=200,
    temperature=0.3
)

print("=== Reponse de Llama 3 ===")
print(response.choices[0].message.content)
print(f"\nTokens utilises : {response.usage.total_tokens}")
# Test des temperatures
for temp in [0.0, 0.5, 1.0]:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Tu es un assistant medical senegalais. Maximum 2 phrases."},
            {"role": "user", "content": "Patient : F, 28 ans, Dakar. Diagnostic : paludisme 72%. Explique."}
        ],
        max_tokens=150,
        temperature=temp
    )
    print(f"\n=== Temperature {temp} ===")
    print(response.choices[0].message.content)