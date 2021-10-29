
from datetime import datetime
import sys

PATH = str(sys.argv[1])

print(PATH)

chunks = []
i = 0
chu = []

with open("{}/distrdf_timestamps.out".format(PATH), "r") as f:  # after running the .sh script
	for line in f:
		if line.startswith("python3"):
			chunks.append(chu)
			i +=1
			chu = []
		chu.append(line)

for i in range(1, len(chunks), 1):
	print(chunks[i][0][:-1])
	begin_t = datetime.strptime(chunks[i][1][33:-1], "%y-%m-%d %H:%M:%S.%f")
	end_t = datetime.strptime(chunks[i][-6][31:-1], "%y-%m-%d %H:%M:%S.%f")
	print(chunks[i][-3][:-1])  # Sandwich inside python
	print("Timer from Base.py", end_t - begin_t)
	print()
