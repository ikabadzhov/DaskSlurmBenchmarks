# modified for SET01 only!

from datetime import datetime
import matplotlib.pyplot as plt

NODES = [8, 16, 32, 64]

chunks = []
i = 0
chu = []
events = []
sandwich = []

for nds in NODES:
	with open("DREP_N{}_c32_f1000_p4096_r2/distrdf_timestamps.out".format(nds), "r") as f:
		for line in f:
			if line.startswith("python"):
				print(line[:-1])
			if line.startswith("Event"):
				chunks.append(chu)
				i +=1
				chu = []
				#print(line[11:-2])
				events.append(float(line[11:-2]))
			chu.append(line)


for i in range(len(chunks)):
	if i == 0:
		#print(chunks[i][:3])
		#print(chunks[i][-3:])
		begin_t = datetime.strptime(chunks[i][3][33:-1], "%y-%m-%d %H:%M:%S.%f")
		end_t = datetime.strptime(chunks[i][-3][31:-1], "%y-%m-%d %H:%M:%S.%f")
		
		sandwich.append((end_t - begin_t).total_seconds())
	elif i % 2 == 0:
		#print(chunks[i][:4])
		#print(chunks[i][-3:])
		begin_t = datetime.strptime(chunks[i][4][33:-1], "%y-%m-%d %H:%M:%S.%f")
		end_t = datetime.strptime(chunks[i][-3][31:-1], "%y-%m-%d %H:%M:%S.%f")
		sandwich.append((end_t - begin_t).total_seconds())
	else:
		#print(chunks[i][:1])
		#print(chunks[i][-3:])
		begin_t = datetime.strptime(chunks[i][1][33:-1], "%y-%m-%d %H:%M:%S.%f")
		end_t = datetime.strptime(chunks[i][-3][31:-1], "%y-%m-%d %H:%M:%S.%f")
		sandwich.append((end_t - begin_t).total_seconds())		


plt.plot(NODES, events[::2], marker='.', label="Event loop : cold run", color='blue')
plt.plot(NODES, events[1::2], marker='.', label="Event loop : hot run", color='red')
plt.plot(NODES, sandwich[::2], marker='.', label="Sandwich : cold run", color='green')
plt.plot(NODES, sandwich[1::2], marker='.', label="Sandwich : hot run", color='orange')
plt.ylabel('Seconds')
plt.xlabel('Number of Nodes')
plt.title('Run with fixed 4096 partitions and 1000 files')
plt.grid()
plt.legend()
#plt.xlim(.5+max(NODES), min(NODES)-.5)
#plt.yscale('log')
#plt.xscale('log', base=2)
#plt.yscale('log', base=2)
plt.show()
