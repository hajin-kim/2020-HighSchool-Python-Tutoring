year = int( input("연수 입력: ") )
result = "평년"

if year % 400 == 0:
	result = "윤년"
elif year % 100 == 0:
	result = "평년"
elif year % 4 == 0:
	result = "윤년"

print(result)

