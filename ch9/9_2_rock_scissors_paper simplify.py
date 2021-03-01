import random

computer = random.choice(["가위", "바위", "보"])
user = input("가위 바위 보: ")

result = ""

if computer == user:
    result = "draw"
elif computer == "가위":
    if user == "보":
        result = "lose"
    else:
        result = "win"
elif computer == "바위":
    if user == "가위":
        result = "lose"
    else:
        result = "win"
else:
    if user == "바위":
        result = "lose"
    else:
        result = "win"
print("컴퓨터:", computer)
print(result)


        






