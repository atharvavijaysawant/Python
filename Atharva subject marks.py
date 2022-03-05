first_name=input("Enter your name:")
middle_name=input("Enter your name:")
surname=input("Enter you surname:")

eng_mark=int(input("Enter your English marks: "))
maths_mark=int(input("Enter your Maths marks: "))
sci_mark=int(input("Enter your Science marks: "))

avg=(eng_mark+maths_mark+sci_mark)/3


print("First name: ",first_name)
print("Middle name: ",middle_name)
print("surname: ",surname)


print("English Marks: ",eng_mark)
print("Maths Marks: ",maths_mark)
print("Science Marks: ",sci_mark)

print("Average Marks: ",avg)

if((avg>=90)and(avg<=100)):
    print("Grade is A")
elif((avg>=80)and(avg<=89)):
    print("Grade is B")
elif((avg>=70)and(avg<=79)):
    print("Grade is C")
elif((avg>=60)and(avg<=69)):
    print("Grade is D")
elif((avg>=0)and(avg<=59)):
    print("Grade is F")
