"""Configuration file containing constants and game state variables."""

# Disease mappings
diseases = {
    "Disease 1": (
        "Common cold",
        "TODO: Provide summary for Common cold.",
    ),
    "Disease 2": (
        "Influenza",
        "TODO: Provide summary for Influenza.",
    ),
    "Disease 3": (
        "COVID-19",
        "TODO: Provide summary for COVID-19.",
    ),
    "Disease 4": (
        "Respiratory syncytial virus (RSV)",
        "TODO: Provide summary for Respiratory syncytial virus (RSV).",
    ),
    "Disease 5": (
        "Norovirus (stomach flu)",
        "TODO: Provide summary for Norovirus (stomach flu).",
    ),
    "Disease 6": (
        "Ebola",
        "TODO: Provide summary for Ebola.",
    ),
    "Disease 7": (
        "Dengue",
        "TODO: Provide summary for Dengue.",
    ),
    "Disease 8": (
        "Yellow fever",
        "TODO: Provide summary for Yellow fever.",
    ),
    "Disease 9": (
        "Human immunodeficiency virus (HIV)",
        "TODO: Provide summary for Human immunodeficiency virus (HIV).",
    ),
    "Disease 10": (
        "Genital herpes (HSV)",
        "TODO: Provide summary for Genital herpes (HSV).",
    ),
    "Disease 11": (
        "Human papilloma virus (HPV)",
        "TODO: Provide summary for Human papilloma virus (HPV).",
    ),
    "Disease 12": (
        "Chickenpox",
        "TODO: Provide summary for Chickenpox.",
    ),
    "Disease 13": (
        "Measles",
        "TODO: Provide summary for Measles.",
    ),
    "Disease 14": (
        "Polio",
        "TODO: Provide summary for Polio.",
    ),
    "Disease 15": (
        "Rabies",
        "TODO: Provide summary for Rabies.",
    ),
    "Disease 16": (
        "Smallpox",
        "TODO: Provide summary for Smallpox.",
    ),
    "Disease 17": (
        "Infectious mononucleosis (mono)",
        "TODO: Provide summary for Infectious mononucleosis (mono).",
    ),
}


# Game state
game_state = {
    "selected_disease": None,
    "patient_responses": [],
    "doctor_questions": [],
    "game_over": False,
    "player_won": False,
    "remaining_guesses": 3,
}
