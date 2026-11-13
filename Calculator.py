import math
import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init()
history=[]


def sum(a,b):
    engine.say("sum of two integers is",a + b)
    engine.runAndWait()
    return a + b
    
def product(a,b):
    engine.say("product of two integers is",a*b)
    engine.runAndWait()
    return a * b
    
    
def subtract(a,b):
    engine.say("difference of two integers is",a-b)
    engine.runAndWait()
    return a - b

def divison(a,b):
    engine.say("division of two integers is",a / b)
    engine.runAndWait()
    return a / b
def square(a):
    engine.say(f"square of {a} is {a**2}")
    engine.runAndWait()
    return a**2
def square_root(a):
    engine.say(f"squareroot of {a} is {math.sqrt(a)}")
    engine.runAndWait()
    return math.sqrt(a)
def logarithm(a):
    engine.say(f"logarithm of {a} is {math.log(a)}")
    engine.runAndWait()
    return math.log(a)
def sine(a):
    engine.say(f"sine{a} is= {math.sin(a)}")
    engine.runAndWait()
    return math.sin(math.radians(a))
def cosine(a):
    engine.say(f"cos{a} is = {math.cos(a)}")
    engine.runAndWait()
    return math.cos(math.radians(a))
def tangent(a):
    engine.say(f"tan{a} is = {math.tan(a)}")
    engine.runAndWait()
    return math.tan(math.radians(a))
def log_base_10(a):
    engine.say(f"base10 log of {a} is = {math.log10(a)}")
    engine.runAndWait()
    return math.log10(x)
def antilog(a):
    engine.say(f"antilog{a} is = {10**a}")
    engine.runAndWait()
    return 10**a
def show_history():
    if not history:
        print("No calculation.")
    else:
        print("\n Calculation history.")
        for item in history:
            print(item)
def clear_history():
    history.clear()
    print("History cleared")

def main():
    while True:

        print("========= An advance Caculator ===========")
        print("1.Adition(+)\n2.Subtraction(-)\n3.Multiplication(x)\n4.Division(/)\n5.square\n6.squareroot\n7.logarithm\n8.log_base10\n9.antilog\n10.sin\n11.cos\n12.tang\n13.show_history\n14.clear_history")
        
        print("1.talk\n2.Speak")
        method=int(input("choose input method:"))
    
        if method == 1:
            choice=int(input("Enter the choice:"))
        else :
            r=sr.Recognizer()
            with sr.Microphone() as source:
              print("Speak ...")
              audio= r.listen(source)
            try:
               text=r.recognize_google(audio)
               print("You said:",text)
               choice=int(text)
            except sr.UnknownValueError:
               print("Could not under stand you!")
               return
            except sr.RequestError:
               print("Internet Connection problem")
               return
        if choice == 1:
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the second number:"))
            print(f"{num1} + {num2} = {sum(num1,num2)}")
            history.append(f"{num1} + {num2}={sum(num1,num2)}")
        elif choice == 2:
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the second number:"))
            print(f"{num1} x {num2} = {product(num1,num2)}")
            history.append(f"{num1} * {num2}={product(num1,num2)}")
        elif choice == 3:
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the second number:"))
            print(f"{num1} - {num2} = {subtract(num1,num2)}")
            history.append(f"{num1} - {num2}={subtract(num1,num2)}")
        elif choice == 4:
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the second number:"))
            print(f"{num1} / {num2} = {divison(num1,num2)}")
            history.append(f"{num1} / {num2}={divison(num1,num2)}")
        elif choice == 5:
            num1=int(input("Enter the first number:"))
            print(f"suare of {num1} is {square(num1)}")
            history.append(f"square of {num1}={square(num1)}")
        elif choice == 6:
            num1=int(input("Enter the first number:"))
            print(f"suareroot of {num1} is {square_root(num1)}")
            history.append(f"squareroot of {num1}={square_root(num1)}")
        elif choice == 7:
            num1=int(input("Enter the first number:"))
            print(f"log{num1} is {logarithm(num1)}")
            history.append("flog{num1} = {logarithm(num1)}")
        elif choice == 8:
            num1=int(input("Enter the first number:"))
            print(f"log10 of {num1} is {log_base_10(num1)}")
            history.append(f"log10 of {num1} = {log_base_10(num1)}")
        elif choice == 9:
            num1=int(input("Enter the first number:"))
            print(f"Antilog of {num1} is {antilog(num1)}")
            history.append(f"Antilog of {num1} = {antilog(num1)}")
        elif choice == 10:
            num1=int(input("Enter the first number:"))
            print(f"sin{num1} is {sine(num1)}")
            history.append(f"sin{num1} = {sine(num1)}")
        elif choice == 11:       
            num1=int(input("Enter the first number:"))
            print(f"cos{num1} is {cosine(num1)}")
            history.append(f"cos{num1} = {cosine(num1)}")
        elif choice == 12:
            num1=int(input("Enter the first number:"))
            print(f"tan{num1} is {tangent(num1)}")
            history.append(f"tan{num1} = {tangent(num1)}")
        elif choice == 13:
            show_history()
        elif choice == 14:
            clear_history()
                    
        else:
            print("invalid choice")
            
        again=input("Do want to calculate again (yes/No)?")
        if again.lower().strip().replace(" ","") != "yes":
            break

if __name__=="__main__":
    main()

  
