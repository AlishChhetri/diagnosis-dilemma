from flask import Flask, render_template, request, redirect, url_for
from fuzzywuzzy import fuzz  # type: ignore
from dotenv import dotenv_values
import openai
import os

app = Flask(__name__)

# Load API credentials from .env file
CONFIG = dotenv_values(".env")

OPEN_AI_KEY = CONFIG.get("KEY") or os.environ.get("OPEN_AI_KEY")
OPEN_AI_ORG = CONFIG.get("ORG") or os.environ.get("OPEN_AI_ORG")

openai.api_key = OPEN_AI_KEY
openai.organization = OPEN_AI_ORG

# Example diseases and their names
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
}


# Placeholder for the current game session
game_state = {
    "selected_disease": None,
    "patient_responses": [],
    "doctor_questions": [],
    "game_over": False,
    "player_won": False,
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


# Route for home page to select a disease
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_disease = request.form.get("disease")
        game_state["selected_disease"] = selected_disease
        game_state["patient_responses"].clear()
        game_state["doctor_questions"].clear()
        game_state["game_over"] = False
        game_state["player_won"] = False
        return redirect(url_for("chat"))
    return render_template("index.html", diseases=diseases.keys())


# Chat route where doctor asks questions and patient responds
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        if "question" in request.form:
            doctor_question = request.form.get("question")
            game_state["doctor_questions"].append(doctor_question)

            disease_key = game_state["selected_disease"]
            disease_name = diseases[disease_key]

            # Generate dynamic response from the patient
            gpt_response = get_gpt_response(disease_name, doctor_question)

            game_state["patient_responses"].append(gpt_response)
            return redirect(url_for("chat"))

        elif "lock_in_answer" in request.form:
            return redirect(url_for("lock_in_answer"))

    doctor_patient_chat = zip(
        game_state["doctor_questions"], game_state["patient_responses"]
    )

    # Always pass the diseases and game_state to the template
    return render_template(
        "chat.html",
        doctor_patient_chat=doctor_patient_chat,
        game_state=game_state,
        diseases=diseases,
    )


@app.route("/lock_in_answer", methods=["GET", "POST"])
def lock_in_answer():
    if request.method == "POST":
        player_guess = request.form.get("guess").strip().lower()
        actual_disease = diseases[game_state["selected_disease"]].lower()

        # Use partial ratio to account for substring matches (e.g., "cold" for "Common cold")
        similarity = fuzz.partial_ratio(player_guess, actual_disease)

        # Ensure the guess has a reasonable length and matches the disease
        if similarity >= 80 and len(player_guess) >= 3:
            game_state["player_won"] = True
        else:
            game_state["player_won"] = False

        game_state["game_over"] = True
        return redirect(url_for("chat"))

    return render_template("lock_in_answer.html", diseases=diseases)


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
