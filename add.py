list=["add", "age", "grade"]
def my_function (*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_function(int(input(f"Enter as many number as you want to {list[0]}:"))))
