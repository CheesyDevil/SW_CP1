#SW 2nd What Is My Grade

percent=input("what is your percentage in this class: ").strip().replace("%" , "")
percent=float(percent)

if percent >=92:
    grade="A" 
elif 92>percent>= 90:
    grade= "A-"
elif 90>percent>= 88:
    grade= "B+"
elif 88>percent>= 82:
    grade= "B"
elif 82>percent>= 80:
    grade= "B-"
elif 80>percent>= 78:
    grade= "C+"
elif 78>percent>= 72:
    grade= "C"
elif 72>percent>= 70:
    grade= "C-"
elif 70>percent>= 68:
    grade= "D+"
elif 68>percent>= 62:
    grade= "D"
elif 62>percent>= 60:
    grade= "D-"
else:
    grade= "F"

print(f"Your grade is a/n {grade}.")