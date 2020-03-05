class missonarie(dict):
	
	global visited
	visited = []

	def __init__(self):
		self = dict

	def start(self,m1,c1,m2,c2):
		self.m1=m1
		self.c1=c1
		self.m2=m2
		self.c2=c2
		self.pos=0
		self.id=1
		self[self.id] = [self.m1,self.c1,self.m2,self.c2,self.pos]
		print(self)
		visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
		print(visited)
		for i in range(6):
			self.both_m_f()
			self.both_c_f()
			self.both_m_b()
			self.both_c_b()
			self.one_m_f()
			self.one_c_f()
			self.one_m_b()
			self.one_c_b()
			self.one_m_c_f()
			self.one_m_c_b()
			

	def both_m_f(self):
		print("both_m_f - ")
		x1=self.m1
		x2=self.m2
		y1=self.c1
		y2=self.c2
		p=self.pos
		if p!=1:
			x2=x2+2
			x1=x1-2
			p=1
			if x1>=0 and x2>=0 and y1>=0 and y2>=0:
				n1 = len(visited)
				flag = True
				if x1!=0 and x2!=0:
					if y2>x2 or y1>x1:
						flag=False
						print("NO")
				for i in range(n1):
					if visited[i][0]==x1 and visited[i][1]==y1 and visited[i][2]==x2 and visited[i][3]==y2 and visited[i][4]==p:
						flag=False
				if flag==True:
					self.m2=self.m2+2
					self.m1=self.m1-2
					self.pos=1
					self.id=self.id+1
					self[self.id]=[self.m1,self.c1,self.m2,self.c2,self.pos]
					print("self - ")
					print(self)
					visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
					print("visited - ")
					print(visited)

	def both_c_f(self):
		print("both_c_f - ")
		x1=self.m1
		x2=self.m2
		y1=self.c1
		y2=self.c2
		p=self.pos
		if p!=1:
			y2=y2+2
			y1=y1-2
			p=1
			if x1>=0 and x2>=0 and y1>=0 and y2>=0:
				n1 = len(visited)
				flag = True
				if x1!=0 and x2!=0:
					if y2>x2 or y1>x1:
						flag=False
				for i in range(n1):
					if visited[i][0]==x1 and visited[i][1]==y1 and visited[i][2]==x2 and visited[i][3]==y2 and visited[i][4]==p:
						flag=False
				if flag==True:
					self.c2=self.c2+2
					self.c1=self.c1-2
					self.pos=1
					self.id=self.id+1
					self[self.id]=[self.m1,self.c1,self.m2,self.c2,self.pos]
					print("self - ")
					print(self)
					visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
					print("visited - ")
					print(visited)	

	def both_m_b(self):
		print("both_m_b - ")
		x1=self.m1
		x2=self.m2
		y1=self.c1
		y2=self.c2
		p=self.pos
		if p!=0:
			x2=x2-2
			x1=x1+2
			p=0
			if x1>=0 and x2>=0 and y1>=0 and y2>=0:
				n1 = len(visited)
				flag = True
				if x1!=0 and x2!=0:
					if y2>x2 or y1>x1:
						flag=False
				for i in range(n1):
					if visited[i][0]==x1 and visited[i][1]==y1 and visited[i][2]==x2 and visited[i][3]==y2 and visited[i][4]==p:
						flag=False
				if flag==True:
					self.m2=self.m2-2
					self.m1=self.m1+2
					self.pos=0
					self.id=self.id+1
					self[self.id]=[self.m1,self.c1,self.m2,self.c2,self.pos]
					print("self - ")
					print(self)
					visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
					print("visited - ")
					print(visited)

	def both_c_b(self):
		print("both_c_b - ")
		x1=self.m1
		x2=self.m2
		y1=self.c1
		y2=self.c2
		p=self.pos
		if p!=0:
			y2=y2-2
			y1=y1+2
			p=0
			if x1>=0 and x2>=0 and y1>=0 and y2>=0:
				n1 = len(visited)
				flag = True
				if x1!=0 and x2!=0:
					if y2>x2 or y1>x1:
						flag=False
				for i in range(n1):
					if visited[i][0]==x1 and visited[i][1]==y1 and visited[i][2]==x2 and visited[i][3]==y2 and visited[i][4]==p:
						flag=False
				if flag==True:
					self.c2=self.c2-2
					self.c1=self.c1+2
					self.pos=0
					self.id=self.id+1
					self[self.id]=[self.m1,self.c1,self.m2,self.c2,self.pos]
					print("self - ")
					print(self)
					visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
					print("visited - ")
					print(visited)

	def one_m_f(self):
		print("one_m_f - ")
		x1=self.m1
		x2=self.m2
		y1=self.c1
		y2=self.c2
		p=self.pos
		if p!=1:
			x2=x2+1
			x1=x1-1
			p=1
			if x1>=0 and x2>=0 and y1>=0 and y2>=0:
				n1 = len(visited)
				flag = True
				if x1!=0 and x2!=0:
					if y2>x2 or y1>x1:
						flag=False
				for i in range(n1):
					if visited[i][0]==x1 and visited[i][1]==y1 and visited[i][2]==x2 and visited[i][3]==y2 and visited[i][4]==p:
						flag=False
				if flag==True:
					self.m2=self.m2+1
					self.m1=self.m1-1
					self.pos=1
					self.id=self.id+1
					self[self.id]=[self.m1,self.c1,self.m2,self.c2,self.pos]
					print("self - ")
					print(self)
					visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
					print("visited - ")
					print(visited)

	def one_c_f(self):
		print("one_c_f - ")
		x1=self.m1
		x2=self.m2
		y1=self.c1
		y2=self.c2
		p=self.pos
		if p!=1:
			y2=y2+1
			y1=y1-1
			p=1
			if x1>=0 and x2>=0 and y1>=0 and y2>=0:
				n1 = len(visited)
				flag = True
				if x1!=0 and x2!=0:
					if y2>x2 or y1>x1:
						flag=False
				for i in range(n1):
					if visited[i][0]==x1 and visited[i][1]==y1 and visited[i][2]==x2 and visited[i][3]==y2 and visited[i][4]==p:
						flag=False
				if flag==True:
					self.c2=self.c2+1
					self.c1=self.c1-1
					self.pos=1
					self.id=self.id+1
					self[self.id]=[self.m1,self.c1,self.m2,self.c2,self.pos]
					print("self - ")
					print(self)
					visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
					print("visited - ")
					print(visited)

	def one_m_b(self):
		print("one_m_b - ")
		x1=self.m1
		x2=self.m2
		y1=self.c1
		y2=self.c2
		p=self.pos
		if p!=0:
			x2=x2-1
			x1=x1+1
			p=0
			if x1>=0 and x2>=0 and y1>=0 and y2>=0:
				n1 = len(visited)
				flag = True
				if x1!=0 and x2!=0:
					if y2>x2 or y1>x1:
						flag=False
				for i in range(n1):
					if visited[i][0]==x1 and visited[i][1]==y1 and visited[i][2]==x2 and visited[i][3]==y2 and visited[i][4]==p:
						flag=False
				if flag==True:
					self.m2=self.m2-1
					self.m1=self.m1+1
					self.pos=0
					self.id=self.id+1
					self[self.id]=[self.m1,self.c1,self.m2,self.c2,self.pos]
					print("self - ")
					print(self)
					visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
					print("visited - ")
					print(visited)

	def one_c_b(self):
		print("one_c_b - ")
		x1=self.m1
		x2=self.m2
		y1=self.c1
		y2=self.c2
		p=self.pos
		if p!=0:
			y2=y2-1
			y1=y1+1
			p=0
			if x1>=0 and x2>=0 and y1>=0 and y2>=0:
				n1 = len(visited)
				flag = True
				if x1!=0 and x2!=0:
					if y2>x2 or y1>x1:
						flag=False
				for i in range(n1):
					if visited[i][0]==x1 and visited[i][1]==y1 and visited[i][2]==x2 and visited[i][3]==y2 and visited[i][4]==p:
						flag=False
				if flag==True:
					self.c2=self.c2-1
					self.c1=self.c1+1
					self.pos=0
					self.id=self.id+1
					self[self.id]=[self.m1,self.c1,self.m2,self.c2,self.pos]
					print("self - ")
					print(self)
					visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
					print("visited - ")
					print(visited)

	def one_m_c_f(self):
		print("one_m_c_f - ")
		x1=self.m1
		x2=self.m2
		y1=self.c1
		y2=self.c2
		p=self.pos
		if p!=1:
			x2=x2+1
			y2=y2+1
			x1=x1-1
			y1=y1-1
			p=1
			if x1>=0 and x2>=0 and y1>=0 and y2>=0:
				n1 = len(visited)
				flag = True
				if x1!=0 and x2!=0:
					if y2>x2 or y1>x1:
						flag=False
				for i in range(n1):
					if visited[i][0]==x1 and visited[i][1]==y1 and visited[i][2]==x2 and visited[i][3]==y2 and visited[i][4]==p:
						flag=False
				if flag==True:
					self.m2=self.m2+1
					self.c2=self.c2+1
					self.m1=self.m1-1
					self.c1=self.c1-1
					self.pos=1
					self.id=self.id+1
					self[self.id]=[self.m1,self.c1,self.m2,self.c2,self.pos]
					print("self - ")
					print(self)
					visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
					print("visited - ")
					print(visited)

	def one_m_c_b(self):
		print("one_m_c_b - ")
		x1=self.m1
		x2=self.m2
		y1=self.c1
		y2=self.c2
		p=self.pos
		if p!=0:
			x2=x2-1
			y2=y2-1
			x1=x1+1
			y1=y1+1
			p=0
			if x1>=0 and x2>=0 and y1>=0 and y2>=0:
				n1 = len(visited)
				flag = True
				if x1!=0 and x2!=0:
					if y2>x2 or y1>x1:
						flag=False
				for i in range(n1):
					if visited[i][0]==x1 and visited[i][1]==y1 and visited[i][2]==x2 and visited[i][3]==y2 and visited[i][4]==p:
						flag=False
				if flag==True:
					self.m2=self.m2-1
					self.c2=self.c2-1
					self.m1=self.m1+1
					self.c1=self.c1+1
					self.pos=0
					self.id=self.id+1
					self[self.id]=[self.m1,self.c1,self.m2,self.c2,self.pos]
					print("self - ")
					print(self)
					visited.append([self.m1,self.c1,self.m2,self.c2,self.pos])
					print("visited - ")
					print(visited)



m1= int(input("No. of missonarie on the left hand "))
c1= int(input("No. of cannibals on the left hand "))
m2= int(input("No. of missonarie on the right hand "))
c2= int(input("No. of cannibals on the right hand "))

obj = missonarie()
obj.start(m1,c1,m2,c2)
