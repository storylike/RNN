import os
os.chdir(os.getcwd())
out = open('data1.txt', 'w+')
with open('temp.txt','r') as f:
	line = f.readline()
	while line:
		data = line.strip().split('.')[1]
		out.write(data)
		line = f.readline()

out.close()
		