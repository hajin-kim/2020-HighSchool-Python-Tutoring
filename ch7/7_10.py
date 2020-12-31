n = int(input("입력 횟수: "))

for i in range(n):
	temp = int(input("값: "))
	if temp > n:
		n = temp

print("최댓값:", n)

