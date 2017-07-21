import sys
import re
import collections
class Lexer:
	index=0
	tokens=[]
	n=0
	def __init__(self,ipfile):
		self.ipfile=ipfile
		comment_symbol = ["/"]
		symtab = {}
		#this function populates the symbol table from file symtab.txt
		def populate_symtab():
			#global symtab
			with open("symtab.txt", "r") as symtab_file:
				while True:
					line = symtab_file.readline()
					if not line:
						break
					else:
						line = line.strip()
						words = line.split(" ")
						symtab[words[0]] = words[1]
			symtab_file.close()

		#this function returns a character after looking ahead
		def lookahead(f):
			lookahead_char = f.read(1)
			return lookahead_char

		#this function removes comments
		def remove_comments(character, f):
			if(character in comment_symbol):
				next_char = lookahead(f)
				if next_char == "/":
					while f.read(1) != '\n':
						pass
				elif next_char == "*":
					while f.read(1) != '*':
						pass
					next_char1 = f.read(1)
					if(next_char1 == "/"):
						pass
					else:
						while f.read(1) != '*':
							pass
						next_char2 = f.read(1)
						if(next_char2 == "/"):
							pass
			return

		#this function generates identifiers
		def identifier_generator(character, f):
			back = ""
			final_string = ""
			temp_char = character
			while temp_char.isalpha():
				final_string = final_string + temp_char
				temp_char = f.read(1)
				back = temp_char
			if final_string in symtab:
				#print (final_string, symtab[final_string])
				self.tokens.append((final_string, symtab[final_string]))
			else:
				symtab[final_string] = "identifier"
				#print (final_string, symtab[final_string])
				self.tokens.append((final_string, symtab[final_string]))
			check(back, f)
			return

		#this function takes care of other symbols
		def other(character, f):
			back = ""
			final_string = ""
			temp_char = character
			if temp_char in symtab:
				final_string = final_string + temp_char
				temp_char = lookahead(f)
				back = temp_char
				final_string = final_string + temp_char
				if final_string in symtab:
					#print (final_string, symtab[final_string])
					self.tokens.append((final_string, symtab[final_string]))
				else:
					#print (character, symtab[character])
					self.tokens.append((character, symtab[character]))
					check(back, f)
			return

		#this function generates strings
		def string(character, f):
			string = '"'
			back = ""
			temp_char = f.read(1)
			while temp_char.isalpha():
				string = string + temp_char
				temp_char = f.read(1)
				back = temp_char
			if back == '"':
				string += '"'
			symtab[string] = "string"
			#print(string, symtab[string])
			self.tokens.append((string, symtab[string]))
			return

		def number(character, f):
			back = ""
			final_number = ""
			temp_char = character
			while temp_char.isdigit():
				final_number = final_number + temp_char
				temp_char = lookahead(f)
				back = temp_char
			symtab[final_number] = "number"
			#print (final_number, symtab[final_number])
			self.tokens.append((final_number, symtab[final_number]))
			check(back, f)
			return

		#this function checks every character
		def check(character, f):
			if character.isalpha():
				identifier_generator(character, f)
			elif character == symtab["/"]:
				remove_comments(character, f)
			elif character == '"':
				string(character, f)
			elif character.isdigit():
				number(character, f)
			else:
				other(character, f)
			return

		#this function reads the file, character by character after populating symbol table first
		def lexer():
			populate_symtab()
			##print symtab
			with open(ipfile, 'r+') as f:
				while True:
					character = f.read(1) #read character by character and if it exists, send it to function check
					if not character:
						break
					else:
						check(character, f)
			f.close()
			"""with open("symtab1.txt", "w") as symtab_file_repopulate:
				for i in symtab:
					temp_string = i + " " + symtab[i] + "\n"
					symtab_file_repopulate.write(temp_string)
			symtab_file_repopulate.close()"""
			self.tokens.append(['$','$'])
			#for i in self.tokens:
			#	print(i)
		lexer()
		self.n=len(self.tokens)
		
	def getToken(self):
		return self.tokens[self.index]
	def peek(self):
		if (index<n-1):
			return self.tokens[index+1]	
		else:
			return [-1,-1]
	def next(self):
		if (self.index<self.n-1):
			self.index+=1
			return self.tokens[self.index]
		else:
			return [-1,-1]
	def getIndex(self):
		return self.index
	def setIndex(self,index):
		self.index=index
#self.tokens=lexer()
"""
lexer=Lexer('ip.txt')
for i in lexer.tokens:
	print(i)

"""
