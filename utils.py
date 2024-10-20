"""Utility functions for interacting with the OpenAI API."""

import openai


def get_gpt_response(disease, doctor_question):
    """Generate a patient-like response based on a disease and a doctor's question using GPT."""

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

    except Exception as e:  # Handle API errors
        return f"Error with OpenAI API: {str(e)}"
