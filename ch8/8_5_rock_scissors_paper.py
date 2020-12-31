import random

computer = random.choice(["가위", "바위", "보"])
user = input("가위, 바위, 보: ")

result = ""
if computer == user:
	result = "비겼습니다!"
elif computer == "가위":
	if user == "바위":
		result = "이겼습니다!"
	elif user == "보":
		result = "졌습니다!"
elif computer == "바위":
	if user == "보":
		result = "이겼습니다!"
	elif user == "가위":
		result = "졌습니다!"
elif computer == "보":
	if user == "가위":
		result = "이겼습니다!"
	elif user == "바위":
		result = "졌습니다!"

print("컴퓨터:", computer)
print(result)

