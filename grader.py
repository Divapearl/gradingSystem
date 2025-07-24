def grade(score: str):
    try:
        score = int(score)  # convert string to int
        if score < 0 or score > 100:
            print("Score should be between 0 - 100")
    except Exception as e:
        print("Score should be numbers only.")
        return

    # Example grading logic
    if score >= 70:
        printGrade("A")
    elif score >= 60 and score <= 69 :
        printGrade("B")
    elif score >= 50 and score <= 59:
        printGrade("C")
    elif score >= 45 and score <= 48:
        printGrade("D")
    elif score >= 40 and score <= 44:
        printGrade("E")
    else:
        printGrade("F")


def printGrade(grade:str):
  print(f"Student's grade is {grade}")
