from itertools import permutations

def solution(a, b):
	if len(a) > len(b):
		return (-1)

	a_list = [int(''.join(i)) for i in sorted(list(set(permutations(a, len(a)))), reverse = True) if i[0] != '0']

	b = int(b)
	for i in a_list:
		if i < b:
			return i
	return (-1)

if __name__ == '__main__':
	a, b = input().split(' ')
	ret = solution(a, b)
	print(ret)