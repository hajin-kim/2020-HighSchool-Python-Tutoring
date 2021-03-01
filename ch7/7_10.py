n = int(input("입력 횟수: "))

if n > 0:
	maximum = int(input("값: "))
	for i in range(n-1):
		temp = int(input("값: "))
		if temp > maximum:
			maximum = temp

	print("최댓값:", maximum)

