def grade(score: str):
    try:
        score = int(score)  # convert string to int
    except Exception as e:
        print("Score should be numbers only.")
        return

    # Example grading logic
    if score >= 70:
        printGrade("A")
    elif score >= 60 and <= 69 :
        printGrade("B")
    elif score >= 50 and <= 59:
        printGrade("C")
    elif score >= 45 and <= 48:
        printGrade("D")
    elif score >= 40 and <= 44:
        printGrade("E")
    else:
        printGrade("F")


def printGrade(grade:str):
  print(f"Student's grade is {grade}")
