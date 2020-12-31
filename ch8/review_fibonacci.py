# 입력 받기
n = int(input("n 번째 항: "))

# 변수 설정 및 초기값
fn = 0
fnext1 = 1
fnext2 = 1

# n번째 항 구하기
for i in range(n):
    fn = fnext1
    fnext1 = fnext2
    fnext2 = fnext1 + fn

# 출력
print("fn:", fn)
