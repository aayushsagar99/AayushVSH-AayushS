import math
import time
print("WELCOME!!! Pick whatever math problem to solve!")
main=int(input("Enter 1 for simple, enter 2 for complex or enter 3 to exit: "))
if main==3:
    print("bye!")
    time.sleep(1)
    exit()
chances=3
if (main>3):
    print("Enter only 1, 2, or 3!")
    chances=chances-1
    if chances==1:
        print(chances," chance left!")
    else:
        print(chances," chances left!")
while main!=3:
    if main==1:
        print("simple")
        h=int(input("Enter 1 for addition, enter 2 for subtraction, enter 3 for multiplication, enter 4 for divition, or enter 5 to exit:"))
        if h==1:
            print("addition")
            time.sleep(1)
            ad=float(input("What is the first number to add: "))
            ad2=float(input("What is the second number to add: "))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{ad}+{ad2}={ad+ad2}")
        elif h==2:
            print("subtraction")
            time.sleep(1)
            su=float(input("What is the first number to subtract: "))
            su2=float(input("What is the second number to subtract: "))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{su}-{su2}={su-su2}")
        elif h==3:
            print("multiplication")
            time.sleep(1)
            mu=float(input("What is the first number to multiply: "))
            mu2=float(input("What is the second number to multiply: "))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{mu}*{mu2}={mu*mu2}")
        elif h==4:
            print("division")
            time.sleep(1)
            di=float(input("What is the first number to divide: "))
            di2=float(input("What is the second number to divide: "))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{di}/{di2}={di*di2}")
        elif h==5:
            print("bye!")
            time.sleep(1)
            exit()
    elif main==2:
        print("complex")
        j=int(input("Enter 1 for square root, enter 2 for cube root, enter 3 for circumfirence of a circle, enter 4 for powers, enter 5 for factorial or enter 6 to exit:"))
        if j==1:
            print("square root")
            time.sleep(1)
            sq=float(input("Which number should be square rooted:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"The square root of {sq} is {math.sqrt(sq)}")
            time.sleep(1)
        elif j==2:
            print("cube root")
            time.sleep(1)
            cb=float(input("Which number should be cube rooted:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"The square root of {cb} is {math.cbrt(cb)}")
            time.sleep(1)
        elif j==3:
            print("circumfirence")
            time.sleep(1)
            print(f"NOTE: The value of pi is {math.pi} | pi={math.pi}")
            d=float(input("What is the diameter:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"The circumfrence of the circle is {math.pi*d}")
            time.sleep(1)
        elif j==4:
            print("powers")
            time.sleep(1)
            ba=float(input("What is the base number:"))
            ex=int(input("What is the exponential number:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{ba}^{ex}={math.pow(ba, ex)}")
            time.sleep(1)
        elif j==5:
            print("factorial")
            time.sleep(1)
            fa=int(input("What is the factorial number:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{fa} factorial is {math.factorial(fa)}")
            time.sleep(1)
        elif j==6:
            print("bye!")
            time.sleep(1)
            exit()
        elif (j>6):
            print("Enter only 1, 2, 3, 4, or 5!")
            chances=chances-1
            if chances==1:
                print(chances," chance left!")
            else:
                print(chances," chances left!")
    elif chances==0:
        print("bye!")
        time.sleep(1)
        break