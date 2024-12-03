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
                    "content": (
                        """
                        You are a patient interacting with a doctor. Respond to the doctor's medical 
                        and small talk questions in a natural and conversational way. Avoid naming the 
                        disease outright, but provide realistic and detailed symptoms or experiences 
                        related to the disease when prompted. If the doctor directly asks if you have 
                        a certain disease, respond with uncertainty (e.g., 'I'm not sure') and offer more 
                        symptoms or related experiences. Use small talk if appropriate to make the interaction 
                        feel genuine (e.g., express gratitude, ask the doctor for advice, or mention how you feel today). 
                        Adapt your responses based on the tone and context of the doctor's question, and keep your 
                        replies concise yet engaging. If the doctor asks for more information, provide additional
                        """
                    ),
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
