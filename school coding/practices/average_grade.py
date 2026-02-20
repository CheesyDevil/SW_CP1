#SW 2nd Average Grade

grade_math=float(input("What is your grade in your math class?\n "))
grade_english=float(input("What is your grade in your english class?\n "))
grade_coding=float(input("What is your grade in your coding class?\n "))
grade_ceramics=float(input("What is your grade in your ceramics class?\n "))
grade_baking=float(input("What is your grade in your baking class?\n "))
grade_health=float(input("What is your grade in your health class?\n "))
grade_history=float(input("What is your grade in your history class?\n "))

total_grade=float(grade_health+grade_baking+grade_ceramics+grade_coding+grade_history+grade_english+grade_math)
average_grade=float(total_grade/7)
print("So your average grade is about", round(average_grade, 2))