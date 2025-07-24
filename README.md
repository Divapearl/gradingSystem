# 🧮 Grading System

A simple Python-based grading system that takes a student's score as input and prints their corresponding grade using a defined grading scale.

---

## 📁 Project Structure

```
grading-system/
│
├── grader.py # Contains the grade calculation logic
├── main.py # Entry point for running the application
└── README.md # Documentation (this file)
```


---

## 🚀 How It Works

The program prompts the user to input a student's score (as a number). It then:

1. Validates the input to ensure it’s a number.
2. Converts the score to an integer.
3. Determines the grade based on the following scale:
   - **70 and above**: A  
   - **60 to 69**: B  
   - **50 to 59**: C  
   - **45 to 48**: D  
   - **40 to 44**: E  
   - **Below 40**: F

4. Prints the final grade using a helper function.

---

## ✅ Example

### Sample Run:

Starting grading system ......

Please enter student's grade: 66
Student's grade is B


---

## 📦 Requirements

No external dependencies — runs on standard Python 3.

---

## ▶️ How to Run

1. Ensure Python 3 is installed.
2. Open your terminal and navigate to the project folder.
3. Run:

```bash

python main.py

```
