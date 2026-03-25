import time

number = 5

while True:
    print(number, end="\r")  # end="\r" overwrites the same line
    time.sleep(1)            # Pauses execution for 1 second
    number -= 1   
    if number==0:
        break       # Increases the number
print("(‿∣‿) ｡◕‿◕｡ (｡◕‿◕｡)")