"""Flask routes for handling game interactions and rendering templates."""

from flask import render_template, request, redirect, url_for, flash
from fuzzywuzzy import fuzz
from app import app
from config import diseases, game_state
from utils import get_gpt_response


@app.route("/", methods=["GET", "POST"])
def index():
    """Render the main page where the user selects a disease and starts the game."""

    if request.method == "POST":
        selected_disease = request.form.get("disease")

        # Set up initial game state
        game_state["selected_disease"] = selected_disease
        game_state["remaining_guesses"] = 3
        game_state["patient_responses"].clear()
        game_state["doctor_questions"].clear()
        game_state["game_over"] = False
        game_state["player_won"] = False

        return redirect(url_for("chat"))

    return render_template("index.html", diseases=diseases.keys())


@app.route("/chat", methods=["GET", "POST"])
def chat():
    """Render the chat interface where the player asks the patient questions."""

    if request.method == "POST":
        doctor_question = request.form.get("question")

        disease_key = game_state.get("selected_disease")  # Ensure a disease is selected

        if disease_key is None:
            flash("Please select a disease before asking questions.")
            return redirect(url_for("index"))

        # Get disease name and summary, and generate patient response
        disease_name, disease_summary = diseases.get(disease_key)
        game_state["doctor_questions"].append(doctor_question)

        # Call GPT for a response, passing both the disease name and its summary
        gpt_response = get_gpt_response(disease_key, doctor_question)
        game_state["patient_responses"].append(gpt_response)

        return redirect(url_for("chat"))

    doctor_patient_chat = zip(
        game_state["doctor_questions"], game_state["patient_responses"]
    )

    return render_template(
        "chat.html",
        doctor_patient_chat=doctor_patient_chat,
        game_state=game_state,
        diseases=diseases,
    )


@app.route("/lock_in_answer", methods=["GET", "POST"])
def lock_in_answer():
    """Lock in the player's guess and determine if they won the game."""

    if "selected_disease" not in game_state or not game_state["selected_disease"]:
        flash("No disease selected. Please start the game from the beginning.")
        return redirect(url_for("index"))

    if request.method == "POST":
        player_guess = request.form.get("guess")

        if not player_guess:
            flash("Please enter a guess.")
            return redirect(url_for("lock_in_answer"))

        player_guess = player_guess.strip().lower()
        actual_disease = diseases[game_state["selected_disease"]][
            0
        ].lower()  # Updated to access disease name

        similarity = fuzz.partial_ratio(player_guess, actual_disease)

        # Determine if the guess is correct
        if similarity >= 80 and len(player_guess) >= 3:
            game_state["player_won"] = True
            game_state["game_over"] = True
        else:
            # Decrement remaining guesses and check for game over
            game_state["remaining_guesses"] -= 1
            if game_state["remaining_guesses"] <= 0:
                game_state["player_won"] = False
                game_state["game_over"] = True
            else:
                flash(
                    f"Incorrect guess! You have {game_state['remaining_guesses']} attempts left."
                )

        return redirect(url_for("lock_in_answer"))

    return render_template(
        "lock_in_answer.html", game_state=game_state, diseases=diseases
    )
