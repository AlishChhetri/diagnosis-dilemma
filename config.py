"""Configuration file containing constants and game state variables."""

# Disease mappings
diseases = {
    "Disease 1": "Common cold",
    "Disease 2": "Influenza",
    "Disease 3": "COVID-19",
    "Disease 4": "Respiratory syncytial virus (RSV)",
    "Disease 5": "Norovirus (stomach flu)",
    "Disease 6": "Ebola",
    "Disease 7": "Dengue",
    "Disease 8": "Yellow fever",
    "Disease 9": "Human immunodeficiency virus (HIV)",
    "Disease 10": "Genital herpes (HSV)",
    "Disease 11": "Human papilloma virus (HPV)",
    "Disease 12": "Chickenpox",
    "Disease 13": "Measles",
    "Disease 14": "Polio",
    "Disease 15": "Rabies",
    "Disease 16": "Smallpox",
    "Disease 17": "Infectious mononucleosis (mono)",
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
