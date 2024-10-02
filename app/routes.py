from flask import Blueprint, render_template, request, redirect, url_for
from app.utils import get_gpt_response, diseases
from app.game_state import game_state
from fuzzywuzzy import fuzz  # type: ignore

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_disease = request.form.get("disease")
        game_state["selected_disease"] = selected_disease
        game_state["patient_responses"].clear()
        game_state["doctor_questions"].clear()
        game_state["game_over"] = False
        game_state["player_won"] = False
        return redirect(url_for("main.chat"))
    return render_template("index.html", diseases=diseases.keys())


@main.route("/chat", methods=["GET", "POST"])
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
            return redirect(url_for("main.chat"))

        elif "lock_in_answer" in request.form:
            return redirect(url_for("main.lock_in_answer"))

    doctor_patient_chat = zip(
        game_state["doctor_questions"], game_state["patient_responses"]
    )

    return render_template(
        "chat.html",
        doctor_patient_chat=doctor_patient_chat,
        game_state=game_state,
        diseases=diseases,
    )


@main.route("/lock_in_answer", methods=["GET", "POST"])
def lock_in_answer():
    if request.method == "POST":
        player_guess = request.form.get("guess").strip().lower()
        actual_disease = diseases[game_state["selected_disease"]].lower()

        # Use partial ratio to account for substring matches
        similarity = fuzz.partial_ratio(player_guess, actual_disease)

        if similarity >= 80 and len(player_guess) >= 3:
            game_state["player_won"] = True
        else:
            game_state["player_won"] = False

        game_state["game_over"] = True
        return redirect(url_for("main.chat"))

    return render_template("lock_in_answer.html", diseases=diseases)
