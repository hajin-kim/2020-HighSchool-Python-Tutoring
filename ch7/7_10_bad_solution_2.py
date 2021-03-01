n = int(input("입력 횟수: "))

maximum = 0
for i in range(n):
	temp = int(input("값: "))
	if temp > maximum:
		maximum = temp

print("최댓값:", maximum)

