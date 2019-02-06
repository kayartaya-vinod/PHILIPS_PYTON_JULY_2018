
def main():
	nums = [10, 20, [1, 2, 3, {5, 6, 7}]]
	square_of_nums = [square(n) for n in nums]

	print(nums)
	print(square_of_nums)


def square(n):
	if type(n) in (int, float): return n*n
	if type(n) == list: return [square(x) for x in n]
	if type(n) == set: return {square(x) for x in n}
	if type(n) == tuple: return tuple([square(x) for x in n])
	return None


if __name__ == '__main__':
	main()