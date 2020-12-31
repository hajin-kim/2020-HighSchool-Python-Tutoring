# 입력
# n = int(input("n 번째 항: "))
n = 5

# 초기값
fn = 0
fnext1 = 1
fnext2 = 1

# n번째 구하기
for i in range(n):
	fn = fnext1
	fnext1 = fnext2
	fnext2 = fnext1 + fn

# 출력
print("fn:", fn)


