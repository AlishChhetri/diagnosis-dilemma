import openai

diseases = {
    "Disease 1": "Common cold",
    "Disease 2": "Migraine",
    "Disease 3": "Type 2 Diabetes",
    "Disease 4": "Snake bite",
    "Disease 5": "Appendicitis",
    "Disease 6": "Pneumonia",
    "Disease 7": "Urinary Tract Infection (UTI)",
    "Disease 8": "Mononucleosis",
    "Disease 9": "Asthma",
    "Disease 10": "Peptic Ulcer",
    "Disease 11": "Hypertension",
    "Disease 12": "Anemia",
    "Disease 13": "Strep Throat",
    "Disease 14": "Gallstones",
    "Disease 15": "Irritable Bowel Syndrome (IBS)",
    "Disease 16": "Covid-19",
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
