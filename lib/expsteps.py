# 1   2   3   4   5    6    7
# 1 + 2 + 4 + 8 + 16 + 32 + 64

def compute_steps(number_of_steps):
	total = 1
	for step in range(1, number_of_steps):
		total += 2**(step)
	return total

assert compute_steps(2) == 3
assert compute_steps(3) == 7
assert compute_steps(4) == 15
assert compute_steps(5) == 31
assert compute_steps(6) == 63

exp_km = compute_steps(30) / 1000
times_to_moon = exp_km / 384400

print('Step 30: {}'.format(exp_km))
print('Times to moon: {}'.format(times_to_moon))
print('Finished Ok')
