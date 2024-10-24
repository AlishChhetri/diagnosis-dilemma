# How to Play "Diagnosis Dilemma"

In **"Diagnosis Dilemma"**, you assume the role of a doctor trying to diagnose a patient (simulated by GPT-4) based on their responses to your questions. You will ask questions about symptoms and general health, and your goal is to identify the correct disease within three guesses.

---

## Step-by-Step Instructions

1. **Start the Game**:
   - You begin by selecting an anonymized disease from a drop-down menu on the homepage.
   - Once you’ve selected the disease, you will be redirected to the main game interface.

2. **Ask Questions**:
   - On the game page, you will find a chatbox where you can ask the patient (GPT-4) questions about their symptoms, history, or other relevant medical details.
   - Example questions include:
     - “Have you had a fever recently?”
     - “Do you have any muscle aches or fatigue?”
   - The patient's responses will give you clues to deduce what disease they have, but remember, the patient won’t directly reveal the disease name!

3. **Locking in Your Diagnosis**:
   - Once you feel confident or have gathered enough clues, click the **"Lock in answer"** button to make a guess.
   - You will then be prompted to enter your guess. You have **3 chances** to guess correctly.
   - If your guess is similar enough (80% match or higher) to the actual disease, you win! If your guess is incorrect, your remaining guesses will decrease, and you can keep asking more questions before trying again.

4. **Winning or Losing**:
   - If you guess correctly within 3 attempts, you win the game, and the correct disease will be revealed.
   - If you run out of guesses without identifying the correct disease, the game will end, and the actual disease will be revealed.

---

## Game Interface Breakdown

- **Homepage**: Select the anonymized disease to start the game.
- **Chat Page**: Ask questions to the patient via the chatbox. The patient (GPT-4) will respond based on the hidden disease.
- **Lock-in Page**: Once you think you’ve gathered enough clues, lock in your guess. You have up to 3 attempts to diagnose the patient correctly.

---

## Tips for Playing

- **Ask Specific Questions**: Start by asking general health questions and then narrow down based on the patient’s answers. Focus on symptoms that can help differentiate between similar diseases.
- **Don't Guess Too Soon**: Make sure to gather enough clues before using your guesses. Remember, you only have three chances to get it right.
- **Think About Symptom Clusters**: Some diseases may share similar symptoms, so ask follow-up questions if a response seems unclear.

---

By following these steps, you’ll be able to diagnose the patient efficiently and win the game. Happy diagnosing!

## How to Set Up and Start "Diagnosis Dilemma"

To get the game running locally on your machine, follow these steps:

---

### 1. **Install Dependencies with Poetry**

First, ensure you have **Poetry** installed. If you don’t have it yet, you can install Poetry by running:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

After installation, verify it by running:

```bash
poetry --version
```

If you need detailed instructions on installing Poetry, refer to [the official Poetry installation guide](https://python-poetry.org/docs/#installation).

---

### 2. **Clone the Repository**

If the game is hosted in a GitHub repository, start by cloning it to your local machine. Use the following command, replacing `REPO_URL` with the actual repository URL:

```bash
git clone REPO_URL
cd diagnosis-dilemma
```

---

### 3. **Install the Project Dependencies**

Once inside the project directory (e.g., `diagnosis-dilemma`), you can install the required Python packages by running the following command in your terminal:

```bash
poetry install
```

This will automatically install all the dependencies listed in the `pyproject.toml` file.

---

### 4. **Set Up Your OpenAI API Key**

Since the game relies on GPT-4 for generating patient responses, you need to set up your OpenAI API key.

1. Get your OpenAI API key from [OpenAI](https://platform.openai.com/).
2. Create a `.env` file in the project directory and add the following line:

```bash
KEY=your_openai_key_here

ORG=your_openai_org_key_here

```

This will ensure that the Flask app can communicate with the OpenAI API.

---

### 5. **Run the Application**

With everything set up, you can now run the Flask application locally.

1 - In your terminal, run:

```bash
poetry shell
```

This will activate the virtual environment managed by Poetry. Then, run:

```bash
python app.py
```

2 - By default, Flask will start a local server at **<http://127.0.0.1:5000/>**.

3 - Open your web browser and go to:

```bash
http://127.0.0.1:5000/
```

This will bring you to the game’s homepage, where you can select a disease and start playing.

---

### 6. **Playing the Game**

- After selecting a disease from the dropdown, you will be redirected to the chat interface where you can begin asking the patient (GPT-4) questions.
- When you’re ready to make a diagnosis, click the **"Lock in answer"** button to submit your guess.

---

### 7. **Stopping the Application**

To stop the application, simply return to your terminal where the Flask server is running and press **CTRL + C**.

---

### Troubleshooting

- If you encounter issues with the OpenAI API, ensure your `.env` file is properly configured with the correct API key.
- Make sure that Poetry has successfully installed all dependencies before running the app.

By following these steps, you'll be able to set up, run, and play **Diagnosis Dilemma** on your local machine.
