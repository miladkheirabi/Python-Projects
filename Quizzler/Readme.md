# 🧠 Quizzler — README (Python / Tkinter)

A small GUI quiz app (True/False) built with Python and Tkinter. This README documents the project structure, how to run it, known issues found in the code you shared, and quick fixes/suggestions.

## 📂 Project Structure
quizzler/
│
├── main.py              # Entry point — builds Question objects and starts UI
├── ui.py                # QuizInterface (Tkinter UI)
├── quiz_brain.py        # Quiz logic: next_question, check_answer, score
├── question_model.py    # SHOULD contain Question class (text + answer)
├── data.py              # question_data — list of dicts with "question" and "correct_answer"
└── images/              # true.png, false.png (used by UI)

## 🚀 Features
- Load questions from `data.py` into `Question` objects.
- Present questions in a GUI canvas with True / False buttons.
- Track and display the user's score live.
- Provide color feedback (green/red) and disable buttons at the end.

## 🛠 Requirements
- Python 3.x
- Tkinter (usually included with standard Python installers)
- No external pip packages required for the core app.

## ▶️ How to Run
1. Make sure `images/true.png` and `images/false.png` exist and paths are correct.  
2. From the project root run:
```
   python main.py
```
## File Responsibilities (quick reference)
- main.py
  - Imports `question_data`, builds `Question` objects, creates `QuizBrain`, launches `QuizInterface`.
  - Prints final score after UI finishes (note: with Tkinter's mainloop the print happens when program exits).

- ui.py (QuizInterface)
  - Builds the Tk window, canvas, score label, and True/False buttons.
  - Uses `quiz.next_question()` to get the question text and `quiz.check_answer()` for answers.

- question_model.py
  - **Should** contain a `Question` class like:
    class Question:
        def __init__(self, text: str, answer: str):
            self.text = text
            self.answer = answer
  - (In the code you provided, `question_model.py` contains a duplicate of the UI — that must be fixed.)

- quiz_brain.py
  - Handles question index, score, providing the next question, and checking the answer.
  - Note: fix a small typo at the top (`qimport html` → `import html`).

- data.py
  - A list `question_data` of dicts, each with keys `question` and `correct_answer`.

## Known Issues & Quick Fixes (from your shared code)
1. question_model.py currently contains the UI code — replace it with a proper `Question` class.  
   Example:
       class Question:
           def __init__(self, text, answer):
               self.text = text
               self.answer = answer

2. quiz_brain.py has a typo `qimport html` on the first line. Change to:
       import html

3. Make sure `data.py` keys match what `main.py` expects: `"question"` and `"correct_answer"`.  
   main.py uses:
       question_text = question["question"]
       question_answer = question["correct_answer"]

4. Image loading: `PhotoImage(file="images/true.png")` expects the working directory to be the project root. If you run from a different folder, provide absolute path or adjust `os.path.join`.

5. UI final prints: `print("You've completed the quiz")` and the final score are executed in `main.py` right after `QuizInterface(quiz)` — because `QuizInterface` starts `mainloop()`, those prints happen only after the GUI closes. That’s normal but worth noting.

## Troubleshooting
- If the images don't show, check that `images/true.png` and `images/false.png` are valid PNGs and the path is correct.
- If questions appear with HTML entities, `html.unescape()` in `next_question()` solves that.
- If buttons don't respond, ensure the `QuizInterface` methods `true()` and `false()` call `check_answer()` correctly (they do in your code).

## License & Attribution
- Feel free to reuse and adapt this project for practice and teaching. Add an MIT license file if you plan to publish it.

---  
Made with ❤️ in Python — good job finishing the app!  
