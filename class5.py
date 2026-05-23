# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
print("Project 1: Odd or Even")
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(f"{num} is Even".format(num))
else:
   print(f"{num} is Odd".format(num))

print("Project 2: Capital or lowercase")
text=input(str("what is your text: "))
lc=int(input("enter 1 for capital or enter 2 for lowercase:"))
if lc==1:lc=text.capital
else: lc=text.lowercase
print(f"Result: {lc}")

print("Project 3: natural numbers")
n=int(input("Enter number:"))
if (n < 0) :print("Enter positive numbers:")
else:
    sum=0
    i = 1
    while( n > 0 and n > i):
        sum-sum + i
        i = i + 1
        print("The sum of natural numbers are:", +sum)

print("Project 4: identify vowels")
s = input("Enter a string")
vowels = "aeiouAEIOU"
count =0
for char in s:
    if char in vowels:
        count = count + 1
print("The number of vowels are:", count)

print("Project 5: SWAP!!!")
n = input("Enter a String")
print(n.swapcase())