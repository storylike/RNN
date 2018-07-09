import os

os.chdir(os.getcwd())
out = open('data_reversed.txt', 'w+')
with open('temp_reversed.txt','r') as f:
	line = f.readline()
	while line:
		data = line.strip().split('.')[1]
		out.write(data)
		line = f.readline()

out.close()


'''
os.chdir(os.getcwd())
out = open('data2.txt', 'w+')
li = []
with open('data.txt','r') as f:
    line = f.readline()
    while line:
        li.append(line)
        line = f.readline()

la = li[::-1]
for item in la:
    out.write(item)
out.close()
'''