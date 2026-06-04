import math
import time
def sce():
    i=int(input("Which one do tyou want to solve? enter 1 for square root or enter 2 for cube root:"))
    if i==1:
        sq=float(input("Which number should be square rooted:"))
        print("Thinking...")
        time.sleep(2.5)
        print(f"The square root of {sq} is {math.sqrt(sq)}")
    if i==2:
        cb=float(input("Which number should be cube rooted:"))
        print("Thinking...")
        time.sleep(2.5)
        print(f"The square root of {cb} is {math.cbrt(cb)}")
    else:
        print("bye!")
        time.sleep(1)
        exit()
if __name__ == "__main__": sce()