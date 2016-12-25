
def factorial(x):
	
	a = 1
	
	for i in range(1,x):
		a = a * (i+1)

	return a

def fact2(x):
	if x < 1:
		return 0
	if x == 1:
		return 1
	return x*fact2(x-1)


print(factorial(4))

print(fact2(4))
