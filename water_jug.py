class water_jug(dict):

	#declaring some basic variables --

	global visited
	visited = []

	def __init__(self):
		self = dict

		
	def start(self,x,y,n,m):
		#initial states 's'-
		global visited 
		self.x=x 		#amount of water that the first jug can conatin
		self.y=y 		#amount of water that the second jug can conatin
		self.n=n
		self.m=m

		#after some operations - 
		
		self.x1=0
		self.x2=0
		self.id=1       #id of a particular node 
		self.p_id=None	#id of its parent node
		self[self.id] = [self.x1,self.x2,self.id,self.p_id]
		print(self)
		visited = [[self.x1,self.x2]]
		n1=40
		print("methods are called - ")
		print("")
		self.add_x()
		self.putin_y()
		self.add_x()
		self.putin_y()
		#self.putin_y()
		#self.putin_y()
		self.rem_y()

	#final goal - 

	def check(self):
		#n = len(self)
		for i,j in self.items():
			if j[0]==m and j[1]==n:
				print("found")
				break
			else:
				pass

	#all the possible operations possible with both of the jugs - -
	
	def add_x(self):

		#print("add x is called - ")
		global visited
		t = self.x1+self.x
		if t>=0 and t<=3:
			u = self.x2
			n1= len(visited)
			n2 = 2
			flag=True
			for i in range(n1):
				if visited[i][0]== t and visited[i][1]==u:
					flag=False
			if flag==True:		
				self.x1=self.x1+self.x
				self.p_id = self.id
				self.id =self.id + 1
				self[self.id] = [self.x1,self.x2,self.id,self.p_id]
				print(self)
				visited.append([self.x1,self.x2])
				print("visited - ")
				print(visited)
				self.check()
	
	def add_y(self):
		#print("add y is called - ")
		global visited
		t = self.x2
		u = self.x1
		if t<4:
			t=self.y
			n1= len(visited)
			n2 = 2
			flag=True
			for i in range(n1):
				if visited[i][0]== u and visited[i][1]==t:
					flag=False
			if flag==True:
				self.x2=self.y
				self.p_id = self.id
				self.id =self.id + 1
				self[self.id] = [self.x1,self.x2,self.id,self.p_id]
				print(self)
				visited.append([self.x1,self.x2])
				print("visited - ")
				print(visited)
				self.check()

	def rem_x(self):
		#print("remove x is called - ")
		t=self.x1-self.x
		if t>=0:
			u = self.x2
			n1= len(visited)
			n2 = 2
			flag=True
			for i in range(n1):
				if visited[i][0]== t and visited[i][1]==u:
					flag=False
			if flag==True:
				self.x1=self.x1-self.x
				d = {self.id:[self.x1,self.x2,self.id,self.p_id]}
				self.update(d)
				print(self)
				visited.append([t,self.x2])
				print("visited - ")
				print(visited)
		self.check()

	def rem_y(self):
		#print("remove y is called - ")
		t=0
		if t >= 0:
			u = self.x1
			n1= len(visited)
			n2 = 2
			flag=True
			for i in range(n1):
				if visited[i][0]== u and visited[i][1]==t:
					flag=False
			if flag==True:
				self.x2=0
				d = {self.id:[self.x1,self.x2,self.id,self.p_id]}
				self.update(d)
				print(self)
				visited.append([self.x1,t])
				print("visited - ")
				print(visited)
		self.check()

	def putin_x(self):
		#print("put in x is called - ")
		bef = self.x1
		t = self.x1+self.x2
		u=0
		#self.x1 = self.x1+self.x2
		if t>self.x:
			u = self.x2-(self.x-bef)
			#self.x2 = self.x2-(self.x-bef)
			t = self.x
			#self.x1=self.x
		n1= len(visited)
		n2 = 2
		flag=True
		for i in range(n1):
			if visited[i][0]== t and visited[i][1]==u:
				flag=False
		if flag == True:
			self.x1 = self.x1+self.x2
			if self.x1>self.x:
				self.x2 = self.x2-(self.x-bef)
				self.x1=self.x
			else:
				self.x2=0
			self.p_id = self.id
			self.id = self.id+1
			self[self.id] = [self.x1,self.x2,self.id,self.p_id]
			print(self)
			visited.append([self.x1,self.x2])
			print("visited - ")
			print(visited)
			self.check()
			
	def putin_y(self):
		#print("put in y is called - ")
		bef = self.x2
		t= self.x2+self.x1
		u=0
		#self.x2 = self.x2+self.y
		if t>self.y:
			u = self.x1-(self.y-bef)
			#self.x1 = self.x1-(self.y-bef)
			t = self.y
			#self.x2=self.y
		n1= len(visited)
		n2 = 2
		flag=True
		for i in range(n1):
			if visited[i][0]== u and visited[i][1]==t:
				flag=False
		if flag == True:
			self.x2 = self.x2+self.x1
			if self.x2>self.y:
				self.x1 = self.x1-(self.y-bef)
				self.x2=self.y
			else:
				self.x1=0
			self.p_id = self.id
			self.id = self.id+1
			self[self.id] = [self.x1,self.x2,self.id,self.p_id]
			print(self)
			visited.append([u,t])
			print("visited - ")
			print(visited)
			self.check()	

x = int(input("Enter the capacity of the first jug - "))
y = int(input("Enter the capacity of the second jug - "))

m = int(input("Enter the final amount of water that has to be in first jug - "))
n = int(input("Enter the final amount of water that has to be in second jug - "))

obj = water_jug()
obj.start(x,y,n,m)