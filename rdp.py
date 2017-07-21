from lexer import Lexer
from collections import deque
statementno=1
assignmentno=1
condno=1
Eno=1
Tno=1
Edashno=1
Tdashno=1
Fno=1
def printMaraaa(tree):
	q=deque([1])
	temp_node = tree
	while temp_node is not None:
		#print(temp_node)
		if temp_node==1:
			print("")
		else:
			print (temp_node.label, end="\t")
			q.extend(temp_node.children)
			q.append(1)
			
		try:
			temp_node=q.popleft()
		except IndexError:
			return
def printMaraa(node):
	for child in node.children:
		print(node.label,"->",child.label)
	for child in node.children:
		printMaraa(child)
class Node(object):
	def __init__(self, label,contents):
		global statementno
		global assignmentno
		global condno
		global Eno
		global Tno
		global Edashno
		global Tdashno
		global Fno
		
		self.label = label
		if(label=="statement"):
			self.label = self.label +str(statementno)
			statementno =statementno+1
		elif(label=="assignment"):
			self.label = self.label +str(assignmentno)
			assignmentno =assignmentno+1
		elif(label=="cond"):
			self.label = self.label +str(condno)
			condno =condno+1
		elif(label=="E"):
			self.label = self.label +str(Eno)
			Eno =Eno+1
		elif(label=="T"):
			self.label = self.label +str(Tno)
			Tno =Tno+1
		elif(label=="F"):
			self.label = self.label +str(Fno)
			Fno =Fno+1
		elif(label=="Edash"):
			self.label = self.label +str(Edashno)
			Edashno =Edashno+1
		elif(label=="Tdash"):
			self.label = self.label +str(Tdashno)
			Tdashno =Tdashno+1
		self.children = []
		self.contents=contents
	def add_child(self, obj):
		self.children.append(obj)	
class rdpbt:
	def __init__(self):
		self.revsymtab={}
		with open("symtab.txt", "r") as self.revsymtab_file:
			while True:
				line = self.revsymtab_file.readline()
				if not line:
					break
				else:
					line = line.strip()
					words = line.split(" ")
					if(words[1] in self.revsymtab.keys()):
						self.revsymtab[words[1]].append(words[0])
					else:
						self.revsymtab[words[1]] =[words[0]]

		self.revsymtab_file.close()
		
		self.lexer=Lexer('ip2.txt')
		self.lexer.setIndex(-1)
		#for i in self.lexer.tokens:
			#print(i)
	def for_loop(self):
		node=Node("For","")
		
		pos=self.lexer.getIndex()
		if(self.lexer.next()[0]=='for'):
			if(self.lexer.next()[0]=='('):
				if(self.assignment(node)):
					if(self.lexer.next()[0]==';'):
						if(self.cond(node)):
							if(self.lexer.next()[0]==';'):
								if(self.assignment(node)):
										if(self.lexer.next()[0]==')'):
											if(self.lexer.next()[0]=='{'):
												if(self.statement(node)):
													if(self.lexer.next()[0]=='}'):
														print("digraph SyntaxTree{")
														printMaraa(node)
														print("}")
														return True
		self.lexer.setIndex(pos)
		
		return False
	
	def statement(self,parentNode):
		node=Node("statement","")
		pos=self.lexer.getIndex()
		if(self.assignment(node)):
			if(self.lexer.next()[0]==';'):
				parentNode.children.append(node)
				node1=Node("statement","")
				pos1=self.lexer.getIndex()
				if(self.statement(node1)):
					parentNode.children.append(node1)
					return True
				else:
					self.lexer.setIndex(pos1)
					return True
		node2=Node("epsillon","")
		parentNode.children.append(node2)
		self.lexer.setIndex(pos)
		return False 
	def assignment(self,parentNode):
		node=Node("assignment","")
		pos=self.lexer.getIndex()
		tok=self.lexer.next()
		if(tok[1]=='identifier'):
			node.children.append(Node(tok[0],""))
			pos1=self.lexer.getIndex()
			tok1=self.lexer.next()
			if(tok1[1]=='unary'):
				node1=Node(tok[0],"")
				node2=Node("unary"+tok1[0],"")
				node.children.append(node1)
				node.children.append(node2)
				parentNode.children.append(node)
				return True
			self.lexer.setIndex(pos1)
			if(self.lexer.next()[0] in self.revsymtab['assignment']):
				if(self.E(node)):
					parentNode.children.append(node)
					return True
		self.lexer.setIndex(pos)
		return True
	def cond(self,parentNode):
		node=Node("cond","")
		pos=self.lexer.getIndex()
		if(self.E(node)):
			if(self.lexer.next()[0] in self.revsymtab['comparision']):
				if(self.E(node)):
					parentNode.children.append(node)
					return True
		node1=Node("epsillon","")
		parentNode.children.append(node1)	
		return True
	def E(self,parentNode):
		node=Node("E","")
		pos=self.lexer.getIndex()
		if(self.T(node)):
			if(self.Edash(node)):
				parentNode.children.append(node)
				return True
		self.lexer.setIndex(pos)
		return False
	def T(self,parentNode):
		node=Node("T","")
		pos=self.lexer.getIndex()
		if(self.F(node)):
			if(self.Tdash(node)):
				parentNode.children.append(node)
				return True
		self.lexer.setIndex(pos)
		return False	
	def Edash(self,parentNode):
		node=Node("Edash","")
		pos=self.lexer.getIndex()
		if(self.lexer.next()[0]=='+'):
			if(self.T(node)):
				if(self.Edash(node)):
					parentNode.children.append(node)
					return True
		node1=Node("epsillon","")
		parentNode.children.append(node1)	
		self.lexer.setIndex(pos)
		return True # epsillon
	def Tdash(self,parentNode):
		node=Node("Tdash","")
		pos=self.lexer.getIndex()
		if(self.lexer.next()[0]=='*'):
			if(self.F(node)):
				if(self.Tdash(node)):
					parentNode.children.append(node)
					return True
		node1=Node("epsillon","")
		parentNode.children.append(node1)	
		self.lexer.setIndex(pos)
		return True # epsillon	
	def F(self,parentNode):
		node=Node("F","")
		pos=self.lexer.getIndex()
		if(self.lexer.next()[0]=='('):
			if(self.E(node)):
				if(self.lexer.next()[0]==')'):
					parentNode.children.append(node)	
					return True
		self.lexer.setIndex(pos)
		token=self.lexer.next()
		if(token[1]=='identifier' or token[1]=="number"):
			node.children.append(Node(token[0],""))
			parentNode.children.append(node)	
			return True
		else:
			self.lexer.setIndex(pos)
			return False

a=rdpbt()
a.for_loop()
