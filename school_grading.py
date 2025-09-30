
students = [("James",92), ("John",74), ("Ada",59), ("Jack",86),("Bitrus", 68)]

for name, score in students:

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: {score}, {grade}")

