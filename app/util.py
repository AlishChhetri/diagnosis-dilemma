import openai

diseases = {
    "DISEASE 1": "Common cold",
    "DISEASE 2": "Migraine",
    "DISEASE 3": "Type 2 Diabetes",
    "DISEASE 4": "Snake bite",
    "DISEASE 5": "Appendicitis",
    "DISEASE 6": "Pneumonia",
    "DISEASE 7": "Urinary Tract Infection (UTI)",
    "DISEASE 8": "Mononucleosis",
    "DISEASE 9": "Asthma",
    "DISEASE 10": "Peptic Ulcer",
    "DISEASE 11": "Hypertension",
    "DISEASE 12": "Anemia",
    "DISEASE 13": "Strep Throat",
    "DISEASE 14": "Gallstones",
    "DISEASE 15": "Irritable Bowel Syndrome (IBS)",
    "DISEASE 16": "Covid-19",
}


# Function to generate GPT-based response
def get_gpt_response(disease, doctor_question):
    try:
        prompt = f"You have {disease}. Respond to the following question like a patient: {doctor_question}"

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a patient who answers the doctor's medical and small talk questions without naming the disease. If the doctor asks if you have a certain disease, state you are not sure and list more symptoms.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=150,
            n=1,
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error with OpenAI API: {str(e)}"
