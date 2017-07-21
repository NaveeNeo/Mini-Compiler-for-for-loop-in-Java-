revsymtab={}
with open("symtab.txt", "r") as revsymtab_file:
	while True:
		line = revsymtab_file.readline()
		if not line:
			break
		else:
			line = line.strip()
			words = line.split(" ")
			if(words[1] in revsymtab.keys()):
				revsymtab[words[1]].append(words[0])
			else:
				revsymtab[words[1]] =[words[0]]
				
revsymtab_file.close()
for i in revsymtab:
	print(i, revsymtab[i])
