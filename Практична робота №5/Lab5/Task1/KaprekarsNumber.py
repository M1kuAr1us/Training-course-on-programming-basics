def kaperkar_number(num):
    if num < 0:
        return -1, -1

    num_sqrt = str(num ** 2)
    length = len(str(num))
    num_left = num_sqrt[:-length] or "0"
    num_right = num_sqrt[-length:]

    if int(num_left) + int(num_right) == num:
        return int(num_left), int(num_right)
    else:
        return -1, -1

num = int(input("Enter a number: "))
left_part, right_part = kaperkar_number(num)
if left_part != -1:
    print(f"{num} - Kaperkar number: {left_part} + {right_part} = {left_part + right_part}")
else:
    print(f"{num} is not a Kaprekar number.")