# modified for SET01 only!

from datetime import datetime
import sys

PATH = str(sys.argv[1])

chunks = []
i = 0
chu = []

with open("{}/distrdf_timestamps.out".format(PATH), "r") as f:  # after running the .sh script
	for line in f:
		chu.append(line)
		if line.startswith("cores"):
			chunks.append(chu)
			i +=1
			chu = []
		


for i in range(0, len(chunks), 1):

	if i % 3 == 0:
		print()
		print(chunks[i][2][:-1])
		print(chunks[i][-1][:-1])  # Sandwich inside python
		begin_t = datetime.strptime(chunks[i][3][33:-1], "%y-%m-%d %H:%M:%S.%f")
		end_t = datetime.strptime(chunks[i][-4][31:-1], "%y-%m-%d %H:%M:%S.%f")
		print("Timer from Base.py", end_t - begin_t)
	else:
		print(chunks[i][-1][:-1])  # Sandwich inside python
		begin_t = datetime.strptime(chunks[i][0][33:-1], "%y-%m-%d %H:%M:%S.%f")
		end_t = datetime.strptime(chunks[i][-4][31:-1], "%y-%m-%d %H:%M:%S.%f")
		print("Timer from Base.py", end_t - begin_t)		
