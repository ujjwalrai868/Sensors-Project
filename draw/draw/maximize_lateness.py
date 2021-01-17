import random
from numpy import random as r


def normal_maximum_lateness(tup):
	n=len(tup)
	tup_final=[]
	for i in range(n):
		temp=[]
		ran_val=random.randrange(1,n)
		temp.append(tup[i])
		temp.append(ran_val)
		tup_final.append(temp)
	tup_final.sort(key=lambda x:x[1])
	#print "tup_final is: ",tup_final
	tup=[]
	for i in range(len(tup_final)):
		tup.append(tup_final[i][0])
	#print "new tup is: ",tup
	max_lateness=0
	schedule=0
	for i in range(len(tup)):
		schedule=schedule+tup[i][0]
		#print "schedule is: ",schedule," and deadline is: ",tup[i][1]
		if(schedule-tup[i][1]>0):
			max_lateness=max_lateness+(schedule-tup[i][1])
	print "max_lateness is: ",max_lateness


def random_maximum_lateness(tup):
	n=len(tup)
	tup_final=[]
	for i in range(n):
		temp=[]
		ran_val=random.randrange(1,n)
		temp.append(tup[i])
		temp.append(ran_val)
		tup_final.append(temp)
	#print tup_final
	tup_final.sort(key=lambda x:x[1])
	#print "tup_final is: ",tup_final
	tup=[]
	for i in range(len(tup_final)):
		tup.append(tup_final[i][0])
	#print "new tup is: ",tup
	max_lateness=0
	schedule=0
	for i in range(len(tup)):
		schedule=schedule+tup[i][0]
		#print "schedule is: ",schedule," and deadline is: ",tup[i][1]
		if(schedule-tup[i][1]>0):
			max_lateness=max_lateness+(schedule-tup[i][1])
	print "max_lateness is: ",max_lateness


def greedy_maximum_lateness(tup):
	tup.sort(key=lambda x:x[1])
	max_lateness=0
	schedule=0
	#print tup
	#tup[i][1] is the deadline
	for i in range(len(tup)):
		schedule=schedule+tup[i][0]
		#print "schedule is: ",schedule," and deadline is: ",tup[i][1]
		if(schedule-tup[i][1]>0):
			max_lateness=max_lateness+(schedule-tup[i][1])
	print "max_lateness is: ",max_lateness

if __name__=="__main__":
	#tup=[[2,8],[4,9],[3,6],[2,15],[3,11],[1,9]]
	tup=[]
	n=int(input("Enter n: "))
	temp=[]
	temp1=[]
	for i in range(n):
		x=random.randrange(3,100)
		temp.append(x)
	s=sum(temp)
	i=0
	#print "len of temp is: ",len(temp)
	while i < n:
		#print "i is: ",i
		y=random.randrange(5, 1000)
		if y<temp[i]:
			continue
		else:
			temp1.append(y)
			i+=1
			
	for i in range(len(temp)):
		temp2=[]
		temp2.append(temp[i])
		temp2.append(temp1[i])
		tup.append(temp2)
	#print "tup is: ",tup
	greedy_maximum_lateness(tup)
	random_maximum_lateness(tup)
	tup=[]
	temp=[]
	temp1=[]
	for i in range(n):
		x=r.normal(loc=8, scale=3)
		temp.append(x)
	s=sum(temp)
	i=0
	while i < n:
		y=r.normal(loc=75, scale=10)
		if(y<temp[i]):
			continue
		else:
			temp1.append(y)
			i+=1
	for i in range(len(temp)):
		temp2=[]
		temp2.append(temp[i])
		temp2.append(temp1[i])
		tup.append(temp2)
	#print "tup is: ", tup
	greedy_maximum_lateness(tup)
	normal_maximum_lateness(tup)

