n = int(input().strip())
number_of_clouds = [int(tmp) for tmp in input().strip().split(' ')]
current = 0
end = n - 1
jumps = 0



while current < end:
    
	if ((current + 2) <= end) and (number_of_clouds[current + 2] == 0):
		current += 2
		jumps += 1

	elif number_of_clouds[current + 1] == 0:
		current += 1
		jumps += 1
print(jumps)