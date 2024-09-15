
# Function for nth fibonacci number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
	a = 0
	b = 1
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2, n):
			c = a + b
			a = b
			b = c
		return b

# Driver Program

# print(fibonacci(9))


def slow(num: int) -> int:
	_ = list()
	fib = fibonacci(num)
	fib_2 = fib**2
	return (fib+fib_2)

"""Calculation of fibonacci values inside of a list comprehension twice is expensive"""

numbers = [7, 6, 1, 4, 1, 8, 0, 6]

# old results implementations
# results = [slow(num) for num in numbers if slow(num) > 0]

# new version wih walrus assignment expression and single function call
results = [value for num in numbers if (value := slow(num)) > 0]

print(results)