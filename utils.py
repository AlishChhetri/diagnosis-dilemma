"""Utility functions for interacting with the OpenAI API."""

import openai
from config import diseases


def get_gpt_response(disease_key, doctor_question):
    """Generate a patient-like response based on a disease and a doctor's question using GPT."""

    try:
        # disease name and summary from the dictionary
        disease_name, disease_summary = diseases[disease_key]

        prompt = (
            f"You have the following disease: {disease_name}. "
            f"Use the following summary to assist your response: {disease_summary}. "
            f"Respond to the following question like a patient: {doctor_question}"
        )

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
