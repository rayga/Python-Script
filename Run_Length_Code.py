init = int(raw_input("Nilai : "))

i = 0
j = 0
first = 0
stdin = []
prev = ''
output = ''

while first < init :
	input = raw_input()
	stdin.append(input)
	first = first + 1

while i < len(stdin):
	if stdin[i] != prev:

		if (i):
			output = output + str(j)

		output = output + str(stdin[i])
		prev = stdin[i]
		j = 0

	j = j + 1
	i = i + 1

output = output + str(j)

print output
