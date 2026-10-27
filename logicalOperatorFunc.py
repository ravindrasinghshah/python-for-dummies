high_income = True
good_credit = False


if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

student = True
if not student:
    print("Student Eligible")
else:
    print("Student Not Eligible")

if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
