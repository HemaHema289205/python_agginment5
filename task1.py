dict={'Alice':85 ,'Kavya': 75 ,'Hema':95}
stu_name = input("Enter the stuend's name: ")
if stu_name in dict:
    print(f"{stu_name}'s marks: {dict[stu_name]}")
else:
    print("Student mot found.")
