"""Configuration file containing constants and game state variables."""

# Disease mappings
diseases = {
    "Disease 1": (
        "Common Cold",
        "A mild illness caused by viruses that affects the nose and throat. Symptoms include sneezing, a runny nose, and a sore throat."
    ),
    "Disease 2": (
        "Flu (Influenza)",
        "A contagious illness caused by the influenza virus. Symptoms include fever, chills, body aches, and fatigue."
    ),
    "Disease 3": (
        "COVID-19",
        "An illness caused by the coronavirus. Symptoms range from mild (fever, cough, fatigue) to severe (difficulty breathing)."
    ),
    "Disease 4": (
        "Chickenpox",
        "A common childhood illness caused by a virus, leading to itchy red spots all over the body."
    ),
    "Disease 5": (
        "Stomach Bug",
        "An infection causing diarrhea, stomach pain, and vomiting. Often spreads through contaminated food or water."
    ),
    "Disease 6": (
        "Pink Eye",
        "An infection or irritation of the eye that causes redness, itching, and watering. Often caused by bacteria or viruses."
    ),
    "Disease 7": (
        "Ear Infection",
        "A bacterial or viral infection in the middle ear, common in children. Symptoms include ear pain and trouble hearing."
    ),
    "Disease 8": (
        "Strep Throat",
        "A bacterial infection causing a sore throat, fever, and swollen glands. It's spread through close contact with others."
    ),
    "Disease 9": (
        "Athlete's Foot",
        "A fungal infection causing itching and redness on the feet, especially between the toes."
    ),
    "Disease 10": (
        "Poison Ivy",
        "An itchy rash caused by contact with poison ivy plants. The rash is caused by an allergic reaction to the plant's oil."
    ),
    "Disease 11": (
        "Mono",
        "An illness caused by the Epstein-Barr virus, leading to fatigue, fever, sore throat, and swollen glands."
    ),
    "Disease 12": (
        "Food Poisoning",
        "An illness caused by eating contaminated food. Symptoms include stomach pain, vomiting, and diarrhea."
    ),
    "Disease 13": (
        "Cold Sores",
        "Small, painful blisters around the mouth caused by the herpes simplex virus. They usually clear up on their own."
    ),
    "Disease 14": (
        "Hives",
        "Raised, itchy welts on the skin caused by an allergic reaction. They can appear anywhere on the body."
    ),
    "Disease 15": (
        "Ringworm",
        "A fungal infection causing a red, circular rash with clearer skin in the middle. It's not caused by a worm despite its name."
    ),
    "Disease 16": (
        "Head Lice",
        "Tiny insects that live in the hair and scalp, causing itching. They are spread through close contact."
    ),
    "Disease 17": (
        "Sunburn",
        "Red, painful skin caused by overexposure to the sun's UV rays. It can lead to peeling and long-term skin damage."
    ),
    "Disease 18": (
        "Hay Fever",
        "An allergic reaction to pollen, causing sneezing, itchy eyes, and a runny nose, especially during spring and summer."
    ),
    "Disease 19": (
        "Warts",
        "Small, rough growths on the skin caused by the human papillomavirus (HPV). They often appear on hands or feet."
    ),
    "Disease 20": (
        "Cavities",
        "Damage to a tooth caused by plaque and sugar, leading to holes in the teeth that may cause pain if untreated."
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
