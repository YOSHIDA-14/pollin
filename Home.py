#importing requirements
import mysql.connector as mc
con=mc.connect(host="localhost",user="root",passwd="immastudyiniitgoa",database="E02")
cuz=con.cursor()
#creating a list to store the all usenames
admins=[]
# list of diffrent forms of greet
leaderboard=[]
import random 
greetings = [
    "Hello there, POLLLLIN user!",
    "Hey, POLLLLIN user, how can I assist you today?",
    "Hi there, welcome back to POLLLLIN!",
    "Greetings, valued POLLLLIN user!",
    "Good day! Welcome to POLLLLIN - where opinions matter.",
    "Hello and thank you for using POLLLLIN.",
    "Welcome to POLLLLIN, where your voice is heard.",
    "Hey, POLLLLIN user! Ready to start polling?",
    "Hello, fellow pollster! Let's gather some opinions!",
    "Greetings, survey champion! Ready to create polls?",
    "Welcome to the world of opinions at POLLLLIN.",
    "Hello, savvy poll creator! Let's get started with POLLLLIN!",
    "Hi, and happy polling at POLLLLIN!",
    "Greetings, discerning surveyor! Your insights matter.",
    "Hello, opinion enthusiast! Welcome back to POLLLLIN.",
]
#a code to generate a new greet every time a user runs the code
x=len(greetings)
y=random.randrange(0,x)
print(greetings[y])
#menu to to display the options that the users can use
print("What do you want to do now i have got you some options!")
print("1.PARTIZIPATE IN QUIZ \n2.LEADERBOARD\n3.ADMIN PREVILIGES ")
print("Type 1,2 or 3")
#to know what the user wants to do
response=int(input())
if response==1:
    print("Type you're Roll No : ")
    rolll=input()
    pas=input("enter youre password : ")
    cuz.execute("SELECT * FROM student")
    admin_list = cuz.fetchall()
    for i in admin_list:
        if i[0]==rolll :
            if i[2]==pas:
                cuz.execute("select*from questions")
                liy=cuz.fetchall()
                for i in liy:
                    
                    print(i[0])
                    print("option1:",i[1])
                    print("option2:",i[2])
                    print("option3:",i[3])
                    print("option4:",i[4])
                    answer=i[5]
                    res=input("Enter your Option 1, 2 , 3,  OR 4 :")
                    if res==answer:
                        cuz.execute(f"""update student set score=score+5 where roll="{rolll}" """)
                        con.commit()
                    else:
                        cuz.execute(f""" update student set score=score-1 where roll="{rolll}" """)
                        con.commit()
                    

    print("thank you your response has been recorded")

if response==2:
    cuz.execute("select*from student")
    lil=cuz.fetchall()
    for  i in lil:
        x=[i[1],i[3] ]
        leaderboard.append(x)
        # Sort the leaderboard in descending order based on the second element of each sublist
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)

    # Print the sorted leaderboard
    for record in sorted_leaderboard:
       print(f"{record[0]}: {record[1]}")




elif response == 3:
    g = True

    while g:
        username = input("USERNAME: ")
        password = input("PASSWORD: ")
        cuz.execute("SELECT * FROM admin")
        admin_list = cuz.fetchall()
        for x in admin_list:
            admins.append(x[0])
        for i in admin_list:
            if i[0] == username and i[1] == password:
                print("Good to see you again,", username)
                g = False
                
           
    print("1.Add a new admin")
    print("2.Host a Quiz")
    print("3.add a student")
    response=int(input("Type 1 or 2 or 3 : "))
    if response ==1:
        username=input("Enter the username")
        if username not in admins:
            password=input("enter your password")
            cuz.execute(f"insert into admin values('{username}','{password}')")
            con.commit()
            print("The admin has sucessfully been added!! congrats")
        else:
            print("Username aldready taken,Try a diffrent one!")
    if response==2:
        cuz.execute("delete from questions")
        Number=int(input("How many No of question"))
       
        for i in range(Number):
            question=input(f"Question {1+i}:")
            option1=input("Option1 : ")
            option2=input("option2 : ")
            option3=input("option3 : ")
            option4=input("option4 : ")
            answer=int(input("ANSWER: "))

            k=[question,option1,option2,option3,option4,answer,i+1]
            cuz.execute("INSERT INTO questions (question, o1, o2, o3, o4, ans, No) VALUES (%s, %s, %s, %s, %s, %s, %s)", (k[0], k[1], k[2], k[3], k[4], k[5],i+1))
            con.commit()
    if response==3:
        print("How many students do you wan to add? :")
        count=int(input())
        for i in range(count):
            print("student rollno: ")
            roll=input()
            name=input("Enter the Student's Name : ")
            password=input("Enter The password :")
            lit=[roll,name,password]
            cuz.execute(f"insert into student(roll,name,pass) values('{roll}','{name}','{password}')")
            con.commit()
            print("record added")

         








