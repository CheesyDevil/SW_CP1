# SW 2nd Idiot proof

name=input("What is your name? ").strip().lower().title()


phone=input("What is your phone number? ").strip().replace("-" , "").replace(" " , "")
phone_list=list(phone)
phone_list.insert(3, " ")
phone_list.insert(7, " ")
phone= "".join(phone_list)
print(phone)

gpa=input("What is your GPA? ").strip()
gpa=float(gpa)
(gpa_r)=round(gpa, 2)
gpa_s=str(gpa_r)
print(gpa_s)

print("So your real name is " + name + " your real phone number is " , phone , " and your GPA is about" , gpa_s ,".")