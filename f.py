data = []
count = 0
with open('food.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(data)
print(len(data))
print(data[0])