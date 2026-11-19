import math
import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init()
history=[]


def sum(a,b):
    text=f"sum of two integers is {a + b}"
    engine.say(text)
    engine.runAndWait()
    return a + b
    
def product(a,b):
    text=f"product of two integers is {a * b}"
    engine.say(text)
    engine.runAndWait()
    return a * b
    
    
def subtract(a,b):
    text=f"difference of two integers is {a - b}"
    engine.say(text)
    engine.runAndWait()
    return a - b

def divison(a,b):
    text=f"divison of two integers is {a / b}"
    engine.say(text)
    engine.runAndWait()
    return a / b
def square(a):
    text=f"square of {a} is {a**2}"
    engine.say(text)
    engine.runAndWait()
    return a**2
def square_root(a):
    text=f"squareroot of {a} is {math.sqrt(a)}"
    engine.say(text)
    engine.runAndWait()
    return math.sqrt(a)
def logarithm(a):
    text=f"logarithm of {a} is {math.log(a)}"
    engine.say(text)
    engine.runAndWait()
    return math.log(a)
def sine(a):
    text=f"sine{a} is= {math.sin(math.radian(a))}"
    engine.say(text)
    engine.runAndWait()
    return math.sin(math.radians(a))
def cosine(a):
    text=f"cos{a} is = {math.cos(math.radian(a))}"
    engine.say(text)
    engine.runAndWait()
    return math.cos(math.radians(a))
def tangent(a):
    text=f"tan{a} is = {math.tan(math.radian(a))}"
    engine.say(text)
    engine.runAndWait()
    return math.tan(math.radians(a))
def log_base_10(a):
    text=f"base10 log of {a} is = {math.log10(a)}"
    engine.say(text)
    engine.runAndWait()
    return math.log10(a)
def antilog(a):
    text=f"antilog{a} is = {10**a}"
    engine.say(text)
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
        print("Select the method of input")
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
            num1=float(input("Enter the first number:"))
            num2=float(input("Enter the second number:"))
            result=sum(num1,num2)
            print(f"{num1} + {num2} = {result}")
            history.append(f"{num1} + {num2}={result}")
        elif choice == 2:
            num1=float(input("Enter the first number:"))
            num2=float(input("Enter the second number:"))
            result=subtract(num1,num2)
            print(f"{num1} - {num2} = {result}")
            history.append(f"{num1} - {num2}={result}")
        elif choice == 3:
            num1=float(input("Enter the first number:"))
            num2=float(input("Enter the second number:"))
            result=product(num1,num2)
            print(f"{num1} * {num2} = {result}")
            history.append(f"{num1} * {num2}={result}")
        elif choice == 4:
            num1=float(input("Enter the first number:"))
            num2=float(input("Enter the second number:"))
            result=division(num1,num2)
            if num2 > 0:
                print(f"{num1} / {num2} = {result}")
                history.append(f"{num1} / {num2}={result}")
            else:
                print("Scientific Error Cannot divide by 0")
        elif choice == 5:
            num1=float(input("Enter the number:"))
            result=square(num1)
            print(f"suare of {num1} is {result}")
            history.append(f"square of {num1}={result}")
        elif choice == 6:
            num1=float(input("Enter the number:"))
            if num1 > 0:
                result=square_root(num1)
                print(f"suareroot of {num1} is {result}")
                history.append(f"squareroot of {num1}={result}")
            else:
                print("Scientific Error enter a positive number")
        elif choice == 7:
            num1=float(input("Enter the number:"))
            result=logarithm(num1)
            print(f"log{num1} is {result}")
            history.append(f"log{num1} = {result}")
        elif choice == 8:
            num1=float(input("Enter the number:"))
            result=log_base_10(num1)
            print(f"log10 of {num1} is {result}")
            history.append(f"log10 of {num1} = {result}")
        elif choice == 9:
            num1=float(input("Enter the number:"))
            result=antilog(num1)
            print(f"Antilog of {num1} is {result}")
            history.append(f"Antilog of {num1} = {result}")
        elif choice == 10:
            num1=float(input("Enter the number:"))
            result=sine(num1)
            print(f"sin{num1} is {result}")
            history.append(f"sin{num1} = {result}")
        elif choice == 11:       
            num1=float(input("Enter the number:"))
            result=cosine(num1)
            print(f"cos{num1} is {result}")
            history.append(f"cos{num1} = {result}")
        elif choice == 12:
            num1=float(input("Enter the number:"))
            result=tangent(num1)
            print(f"tan{num1} is {result}")
            history.append(f"tan{num1} = {result}")
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

  
