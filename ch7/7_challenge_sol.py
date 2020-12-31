n = int(input("n 번째 항: "))

fn = 0
fnext1 = 1
fnext2 = 1

for i in range(n):
	fn = fnext1
	fnext1 = fnext2
	fnext2 = fnext1 + fn

print("fn:", fn)

