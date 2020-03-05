class eight_puzzle(dict):

	global visited,one,two,thr,fou,fiv,six,sev,eig,nin,g,l,h,t
	f=0
	g=0
	l=0
	h=0
	t=0
	visited = []

	def __init__(self):
		self = dict

	#making starting function -

	def start(self,rone,rtwo,rthr,rfou,rfiv,rsix,rsev,reig,rnin):
		#final state of the game -
		self.rone=rone
		self.rtwo=rtwo
		self.rthr=rthr
		self.rfou=rfou
		self.rfiv=rfiv
		self.rsix=rsix
		self.rsev=rsev
		self.reig=reig
		self.rnin=rnin
		self.id = 1

		#random initial state of the game -

		one=6
		two=8
		thr=5
		fou=4
		fiv=2
		six=3
		sev=1
		eig=7
		nin=0
		self[self.id] = [one,two,thr,fou,fiv,six,sev,eig,nin]
		self.check(one,two,thr,fou,fiv,six,sev,eig,nin)
		print(self)
		visited.append([one,two,thr,fou,fiv,six,sev,eig,nin])
		print(visited)
		while(f!=1):
			if(f!=1):
				print("1")
				self.move_up()
			if (f != 1):
				print("2")
				self.move_down()
			if (f != 1):
				print("3")
				self.move_left()
			if (f != 1):
				print("4")
				self.move_right()

	#checking if the game is over or not???

	def check(self,one,two,thr,fou,fiv,six,sev,eig,nin):
		global f
		f=0
		print("check is called - ")
		if self.rone==one and self.rtwo==two and self.rthr==thr and self.rfou==fou and self.rfiv==fiv and self.rsix==six and self.rsev==sev and self.reig==eig and self.rnin==nin:
			f=1
			print("Sucess")

	#definig a function for the tile to move upwards -

	def move_up(self):
		global g
		g = 0
		print("move up is called - ")
		n=len(self)
		for i in range(9):
			if self[n][i]==0:
				temp=i
				break
		if temp>5:
			print("cannot move up")
			g=1
		else:
			one = self[n][0]
			two=self[n][1]
			thr=self[n][2]
			fou=self[n][3]
			fiv=self[n][4]
			six=self[n][5]
			sev=self[n][6]
			eig=self[n][7]
			nin=self[n][8]
			v1 = self[n][temp]
			v2 = self[n][temp+3]
			v1,v2=v2,v1
			self.id=self.id+1
			self[self.id]=[one,two,thr,fou,fiv,six,sev,eig,nin]
			n=n+1
			self[n][temp]=v1
			self[n][temp+3]=v2
			self.check(self[n][0],self[n][1],self[n][2],self[n][3],self[n][4],self[n][5],self[n][6],self[n][7],self[n][8])
			flag = 0
			for i in range(n-1):
				if self[n][0] == visited[i][0] and self[n][1] == visited[i][1] and self[n][2] == visited[i][2] and self[n][3] == visited[i][
					3] and self[n][4] == visited[i][4] and self[n][5] == visited[i][5] and self[n][6] == visited[i][6] and self[n][7] == visited[i][
					7] and self[n][8] == visited[i][8]:
					flag = 1
					break
			if flag == 0:
				visited.append([one, two, thr, fou, fiv, six, sev, eig, nin])
				visited[n-1][temp] = v1
				visited[n-1][temp + 3] = v2
				print(self)
				print(visited)
			else:
				print("NO!!!")
				del self[self.id]
				self.id=self.id-1
				g=1
		if (f != 1) and (g==0):
			self.move_up()
		if (f != 1) and (h==0):
			self.move_down()
		if (f != 1) and (l==0):
			self.move_left()
		if (f != 1) and (t==0):
			self.move_right()

	#definig a function for the tile to move downwards -

	def move_down(self):
		global h
		h=0
		print("move down is called - ")
		n=len(self)
		for i in range(9):
			if self[n][i]==0:
				temp=i
				break
		if temp<3:
			print("cannot move down")
			h=1
		else:
			one = self[n][0]
			two=self[n][1]
			thr=self[n][2]
			fou=self[n][3]
			fiv=self[n][4]
			six=self[n][5]
			sev=self[n][6]
			eig=self[n][7]
			nin=self[n][8]
			v1 = self[n][temp]
			v2 = self[n][temp-3]
			v1,v2=v2,v1
			self.id=self.id+1
			self[self.id]=[one,two,thr,fou,fiv,six,sev,eig,nin]
			n=n+1
			self[n][temp]=v1
			self[n][temp-3]=v2
			self.check(self[n][0], self[n][1], self[n][2], self[n][3], self[n][4], self[n][5], self[n][6], self[n][7],
					   self[n][8])
			flag = 0
			for i in range(n-1):
				if self[n][0] == visited[i][0] and self[n][1] == visited[i][1] and self[n][2] == visited[i][2] and \
						self[n][3] == visited[i][
					3] and self[n][4] == visited[i][4] and self[n][5] == visited[i][5] and self[n][6] == visited[i][
					6] and self[n][7] == visited[i][
					7] and self[n][8] == visited[i][8]:
					flag = 1
					break
			if flag == 0:
				visited.append([one, two, thr, fou, fiv, six, sev, eig, nin])
				visited[n-1][temp]=v1
				visited[n-1][temp-3]=v2
				print(self)
				print(visited)
			else:
				print("NO!!!")
				del self[self.id]
				self.id=self.id-1
				h=1
		if (f != 1) and (g==0):
			self.move_up()
		if (f != 1) and (h==0):
			self.move_down()
		if (f != 1) and (l==0):
			self.move_left()
		if (f != 1) and (t==0):
			self.move_right()

	#definig a function for the tile to move leftwards -

	def move_left(self):
		global l
		l=0
		print("move left is called - ")
		n=len(self)
		for i in range(9):
			if self[n][i]==0:
				temp=i
				break
		if temp==2 or temp==5 or temp==8:
			print("cannot move left")
			l=1
		else:
			one = self[n][0]
			two=self[n][1]
			thr=self[n][2]
			fou=self[n][3]
			fiv=self[n][4]
			six=self[n][5]
			sev=self[n][6]
			eig=self[n][7]
			nin=self[n][8]
			v1 = self[n][temp]
			v2 = self[n][temp+1]
			v1,v2=v2,v1
			self.id=self.id+1
			self[self.id]=[one,two,thr,fou,fiv,six,sev,eig,nin]
			n=n+1
			self[n][temp]=v1
			self[n][temp+1]=v2
			self.check(self[n][0], self[n][1], self[n][2], self[n][3], self[n][4], self[n][5], self[n][6], self[n][7],
					   self[n][8])
			flag = 0
			for i in range(n-1):
				if self[n][0] == visited[i][0] and self[n][1] == visited[i][1] and self[n][2] == visited[i][2] and \
						self[n][3] == visited[i][
					3] and self[n][4] == visited[i][4] and self[n][5] == visited[i][5] and self[n][6] == visited[i][
					6] and self[n][7] == visited[i][
					7] and self[n][8] == visited[i][8]:
					flag = 1
					break
			if flag == 0:
				visited.append([one, two, thr, fou, fiv, six, sev, eig, nin])
				visited[n-1][temp]=v1
				visited[n-1][temp+1]=v2
				print(self)
				print(visited)
			else:
				print("NO!!!")
				del self[self.id]
				self.id=self.id-1
				l=1
		if (f != 1) and (g==0):
			self.move_up()
		if (f != 1) and (h==0):
			self.move_down()
		if (f != 1) and (l==0):
			self.move_left()
		if (f != 1) and (t==0):
			self.move_right()

#definig a function for the tile to move rightwards -

	def move_right(self):
		global t
		t=0
		print("move right is called - ")
		n=len(self)
		for i in range(9):
			if self[n][i]==0:
				temp=i
				break
		if temp==0 or temp==3 or temp==6:
			print("cannot move right")
			t=1
		else:
			one=self[n][0]
			two=self[n][1]
			thr=self[n][2]
			fou=self[n][3]
			fiv=self[n][4]
			six=self[n][5]
			sev=self[n][6]
			eig=self[n][7]
			nin=self[n][8]
			v1 = self[n][temp]
			v2 = self[n][temp-1]
			v1,v2=v2,v1
			self.id=self.id+1
			self[self.id]=[one,two,thr,fou,fiv,six,sev,eig,nin]
			n=n+1
			self[n][temp]=v1
			self[n][temp-1]=v2
			self.check(self[n][0], self[n][1], self[n][2], self[n][3], self[n][4], self[n][5], self[n][6], self[n][7],
					   self[n][8])
			flag = 0
			for i in range(n-1):
				if self[n][0] == visited[i][0] and self[n][1] == visited[i][1] and self[n][2] == visited[i][2] and \
						self[n][3] == visited[i][
					3] and self[n][4] == visited[i][4] and self[n][5] == visited[i][5] and self[n][6] == visited[i][
					6] and self[n][7] == visited[i][
					7] and self[n][8] == visited[i][8]:
					flag = 1
					break
			if flag == 0:
				visited.append([one, two, thr, fou, fiv, six, sev, eig, nin])
				visited[n-1][temp]=v1
				visited[n-1][temp-1]=v2
				print(self)
				print(visited)
			else:
				print("NO!!!")
				del self[self.id]
				self.id=self.id-1
				t=1
		if (f != 1) and (g==0):
			self.move_up()
		if (f != 1) and (h==0):
			self.move_down()
		if (f != 1) and (l==0):
			self.move_left()
		if (f != 1) and (t==0):
			self.move_right()

print("welcome to the eight_puzzle game --")
print("What do you want to be the end state of this game - ")
#rone=int(input("position of the first tile - "))
#rtwo=int(input("position of the second tile - "))
#rthr=int(input("position of the third tile - "))
#rfou=int(input("position of the fourth tile - "))
#rfiv=int(input("position of the fifth tile - "))
#rsix=int(input("position of the sixth tile - "))
#rsev=int(input("position of the seventh tile - "))
#reig=int(input("position of the eig tile - "))
#remp=int(input("position of the emp tile - "))

obj=eight_puzzle()
obj.start(1,2,3,4,5,6,7,8,0)