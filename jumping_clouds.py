n = int(input().strip())

clouds = [int(c) for c in input().strip().split(' ')]

current = 0

end = n - 1

jumps = 0



while current < end:

	if ((current + 2) <= end) and (clouds[current + 2] == 0):
		current += 2
		jumps += 1

	elif clouds[current + 1] == 0:
		current += 1
		jumps += 1
print(jumps)


#Input n = 7, clouds = [0 0 1 0 0 1 0]