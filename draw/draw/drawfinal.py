#Assign ranking for the service providers (need to use db)
# How to assign the ranking of the service providers
#---Based on the prefference list of dffrernt users
#---1.




#Program to implement draw with partial and full prefference list
import random
import copy
from random import shuffle
import os
os.system('clear')
'''filename=['Draw_best_allocation.txt','Draw_efficiency_loss.txt','Random_best_allocation.txt','Random_efficiency_loss.txt','d2_best_allocation.txt','d2_efficiency_loss.txt','d4_best_allocation.txt','d4_efficiency_loss.txt','d8_best_allocation.txt','d8_efficiency_loss.txt']
while(len(filename)!=0):
	file_name=filename.pop(0)
	fo=open(str(file_name),'w')
	fo.close()'''
def file_initialize(filename):
	while(len(filename)!=0):
		file_name=filename.pop(0)
		fo=open(str(file_name),'w')
		fo.close()

# L-less than, G-greater , E-equal, P-partial,F-full
LP=['LP_Draw_best_allocation.txt','LP_Draw_efficiency_loss.txt','LP_Random_best_allocation.txt','LP_Random_efficiency_loss.txt','LP_d2_best_allocation.txt','LP_d2_efficiency_loss.txt','LP_d4_best_allocation.txt','LP_d4_efficiency_loss.txt','LP_d8_best_allocation.txt','LP_d8_efficiency_loss.txt']
LF=['LF_Draw_best_allocation.txt','LF_Draw_efficiency_loss.txt','LF_Random_best_allocation.txt','LF_Random_efficiency_loss.txt','LF_d2_best_allocation.txt','LF_d2_efficiency_loss.txt','LF_d4_best_allocation.txt','LF_d4_efficiency_loss.txt','LF_d8_best_allocation.txt','LF_d8_efficiency_loss.txt']
GP=['GP_Draw_best_allocation.txt','GP_Draw_efficiency_loss.txt','GP_Random_best_allocation.txt','GP_Random_efficiency_loss.txt','GP_d2_best_allocation.txt','GP_d2_efficiency_loss.txt','GP_d4_best_allocation.txt','GP_d4_efficiency_loss.txt','GP_d8_best_allocation.txt','GP_d8_efficiency_loss.txt']
GF=['GF_Draw_best_allocation.txt','GF_Draw_efficiency_loss.txt','GF_Random_best_allocation.txt','GF_Random_efficiency_loss.txt','GF_d2_best_allocation.txt','GF_d2_efficiency_loss.txt','GF_d4_best_allocation.txt','GF_d4_efficiency_loss.txt','GF_d8_best_allocation.txt','GF_d8_efficiency_loss.txt']
EP=['EP_Draw_best_allocation.txt','EP_Draw_efficiency_loss.txt','EP_Random_best_allocation.txt','EP_Random_efficiency_loss.txt','EP_d2_best_allocation.txt','EP_d2_efficiency_loss.txt','EP_d4_best_allocation.txt','EP_d4_efficiency_loss.txt','EP_d8_best_allocation.txt','EP_d8_efficiency_loss.txt']
EF=['EF_Draw_best_allocation.txt','EF_Draw_efficiency_loss.txt','EF_Random_best_allocation.txt','EF_Random_efficiency_loss.txt','EF_d2_best_allocation.txt','EF_d2_efficiency_loss.txt','EF_d4_best_allocation.txt','EF_d4_efficiency_loss.txt','EF_d8_best_allocation.txt','EF_d8_efficiency_loss.txt']

#Variable initialization for draw
EP_Draw_best_allocation=0
EP_Draw_efficiency_loss=0
LP_Draw_efficiency_loss=0
LP_Draw_best_allocation=0
GP_Draw_best_allocation=0
GP_Draw_efficiency_loss=0
EF_Draw_efficiency_loss=0
EF_Draw_best_allocation=0
LF_Draw_efficiency_loss=0
LF_Draw_best_allocation=0
GF_Draw_efficiency_loss=0
GF_Draw_best_allocation=0
#Variable initialization for Random
EP_Random_best_allocation=0
EP_Random_efficiency_loss=0
LP_Random_best_allocation=0
LP_Random_efficiency_loss=0
GP_Random_best_allocation=0
GP_Random_efficiency_loss=0
EF_Random_best_allocation=0
EF_Random_efficiency_loss=0
LF_Random_best_allocation=0
LF_Random_efficiency_loss=0
GF_Random_best_allocation=0
GF_Random_efficiency_loss=0
#Variable initialization for deviaiation
EP_d2_best_allocation=0
EP_d2_efficiency_loss=0
EP_d4_best_allocation=0
EP_d4_efficiency_loss=0
EP_d8_best_allocation=0
EP_d8_efficiency_loss=0
LP_d2_best_allocation=0
LP_d2_efficiency_loss=0
LP_d4_best_allocation=0
LP_d4_efficiency_loss=0
LP_d8_best_allocation=0
LP_d8_efficiency_loss=0
GP_d2_best_allocation=0
GP_d2_efficiency_loss=0
GP_d4_best_allocation=0
GP_d4_efficiency_loss=0
GP_d8_best_allocation=0
GP_d8_efficiency_loss=0
EF_d2_best_allocation=0
EF_d2_efficiency_loss=0
EF_d4_best_allocation=0
EF_d4_efficiency_loss=0
EF_d8_best_allocation=0
EF_d8_efficiency_loss=0
LF_d2_best_allocation=0
LF_d2_efficiency_loss=0
LF_d4_best_allocation=0
LF_d4_efficiency_loss=0
LF_d8_best_allocation=0
LF_d8_efficiency_loss=0
GF_d2_best_allocation=0
GF_d2_efficiency_loss=0
GF_d4_best_allocation=0
GF_d4_efficiency_loss=0
GF_d8_best_allocation=0
GF_d8_efficiency_loss=0
ch=int(input('Enter 1 to run with partial prefference list\n Any OTHER INTEGER for full prefference list::\t'))
ratio=int(input('Enter \n1   When No of Service providers equal to number of users  m=n\n2   When No of Users is less than no Service Providers m<n\n3   When No of Users is greater than no of service providers m>n\n'))
if(ch==1):	#Partial
	if(ratio==1):	#Equal
		file_initialize(EP)
	elif(ratio==2):	#Less
		file_initialize(LP)
	elif(ratio==3):	#Greater
		file_initialize(GP)
else:	#Full
	if(ratio==1):	#Equal m=n
		file_initialize(EF)
	elif(ratio==2):	#Less
		file_initialize(LF)
	elif(ratio==3):	#G
		file_initialize(GF)
def draw_write(m):
	if(ch==1):
		if(ratio==1):
			file_write('EP_Draw_best_allocation.txt',str(EP_Draw_best_allocation),m)
			file_write('EP_Draw_efficiency_loss.txt',str(EP_Draw_efficiency_loss),m)
		elif(ratio==2):
			file_write('LP_Draw_best_allocation.txt',str(LP_Draw_best_allocation),m)
			file_write('LP_Draw_efficiency_loss.txt',str(LP_Draw_efficiency_loss),m)
		elif(ratio==3):
			file_write('GP_Draw_best_allocation.txt',str(GP_Draw_best_allocation),m)
			file_write('GP_Draw_efficiency_loss.txt',str(GP_Draw_efficiency_loss),m)
	else:	#FULL
		if(ratio==1):
			file_write('EF_Draw_best_allocation.txt',str(EF_Draw_best_allocation),m)
			file_write('EF_Draw_efficiency_loss.txt',str(EF_Draw_efficiency_loss),m)
		elif(ratio==2):
			file_write('LF_Draw_best_allocation.txt',str(LF_Draw_best_allocation),m)
			file_write('LF_Draw_efficiency_loss.txt',str(LF_Draw_efficiency_loss),m)
		elif(ratio==3):
			file_write('GF_Draw_best_allocation.txt',str(GF_Draw_best_allocation),m)
			file_write('GF_Draw_efficiency_loss.txt',str(GF_Draw_efficiency_loss),m)

def random_write(m):
	if(ch==1):
		if(ratio==1):
			file_write('EP_Random_best_allocation.txt',str(EP_Random_best_allocation),m)
			file_write('EP_Random_efficiency_loss.txt',str(EP_Random_efficiency_loss),m)
		elif(ratio==2):
			file_write('LP_Random_best_allocation.txt',str(LP_Random_best_allocation),m)
			file_write('LP_Random_efficiency_loss.txt',str(LP_Random_efficiency_loss),m)
		elif(ratio==3):
			file_write('GP_Random_best_allocation.txt',str(GP_Random_best_allocation),m)
			file_write('GP_Random_efficiency_loss.txt',str(GP_Random_efficiency_loss),m)
	else:
		if(ratio==1):
			file_write('EF_Random_best_allocation.txt',str(EF_Random_best_allocation),m)
			file_write('EF_Random_efficiency_loss.txt',str(EF_Random_efficiency_loss),m)
		elif(ratio==2):
			file_write('LF_Random_best_allocation.txt',str(LF_Random_best_allocation),m)
			file_write('LF_Random_efficiency_loss.txt',str(LF_Random_efficiency_loss),m)
		elif(ratio==3):
			file_write('GF_Random_best_allocation.txt',str(GF_Random_best_allocation),m)
			file_write('GF_Random_efficiency_loss.txt',str(GF_Random_efficiency_loss),m)

def deviation_write(m):
	if(ch==1):	#Partial
		if(ratio==1):
			file_write('EP_d2_best_allocation.txt',str(EP_d2_best_allocation),m)
			file_write('EP_d2_efficiency_loss.txt',str(EP_d2_efficiency_loss),m)
			file_write('EP_d4_best_allocation.txt',str(EP_d4_best_allocation),m)
			file_write('EP_d4_efficiency_loss.txt',str(EP_d4_efficiency_loss),m)
			file_write('EP_d8_best_allocation.txt',str(EP_d8_best_allocation),m)
			file_write('EP_d8_efficiency_loss.txt',str(EP_d8_efficiency_loss),m)
		if(ratio==2):	#Less<
			file_write('LP_d2_best_allocation.txt',str(LP_d2_best_allocation),m)
			file_write('LP_d2_efficiency_loss.txt',str(LP_d2_efficiency_loss),m)
			file_write('LP_d4_best_allocation.txt',str(LP_d4_best_allocation),m)
			file_write('LP_d4_efficiency_loss.txt',str(LP_d4_efficiency_loss),m)
			file_write('LP_d8_best_allocation.txt',str(LP_d8_best_allocation),m)
			file_write('LP_d8_efficiency_loss.txt',str(LP_d8_efficiency_loss),m)

		elif(ratio==3):
			file_write('GP_d2_best_allocation.txt',str(GP_d2_best_allocation),m)
			file_write('GP_d2_efficiency_loss.txt',str(GP_d2_efficiency_loss),m)
			file_write('GP_d4_best_allocation.txt',str(GP_d4_best_allocation),m)
			file_write('GP_d4_efficiency_loss.txt',str(GP_d4_efficiency_loss),m)
			file_write('GP_d8_best_allocation.txt',str(GP_d8_best_allocation),m)
			file_write('GP_d8_efficiency_loss.txt',str(GP_d8_efficiency_loss),m)

	else:	#Full
		if(ratio==1):
			file_write('EF_d2_best_allocation.txt',str(EF_d2_best_allocation),m)
			file_write('EF_d2_efficiency_loss.txt',str(EF_d2_efficiency_loss),m)
			file_write('EF_d4_best_allocation.txt',str(EF_d4_best_allocation),m)
			file_write('EF_d4_efficiency_loss.txt',str(EF_d4_efficiency_loss),m)
			file_write('EF_d8_best_allocation.txt',str(EF_d8_efficiency_loss),m)
			file_write('EF_d8_efficiency_loss.txt',str(EF_d8_efficiency_loss),m)
		if(ratio==2):	#Less<
			file_write('LF_d2_best_allocation.txt',str(LF_d2_best_allocation),m)
			file_write('LF_d2_efficiency_loss.txt',str(LF_d2_efficiency_loss),m)
			file_write('LF_d4_best_allocation.txt',str(LF_d4_efficiency_loss),m)
			file_write('LF_d4_efficiency_loss.txt',str(LF_d4_efficiency_loss),m)
			file_write('LF_d8_best_allocation.txt',str(LF_d8_best_allocation),m)
			file_write('LF_d8_efficiency_loss.txt',str(LF_d8_efficiency_loss),m)

		elif(ratio==3):
			file_write('GF_d2_best_allocation.txt',str(GF_d2_best_allocation),m)
			file_write('GF_d2_efficiency_loss.txt',str(GF_d2_efficiency_loss),m)
			file_write('GF_d4_best_allocation.txt',str(GF_d4_efficiency_loss),m)
			file_write('GF_d4_efficiency_loss.txt',str(GF_d4_efficiency_loss),m)
			file_write('GF_d8_best_allocation.txt',str(GF_d8_best_allocation),m)
			file_write('GF_d8_efficiency_loss.txt',str(GF_d8_efficiency_loss),m)


counter11=0	#To perform file_writeoperation one time						#322-325
total_agent=0
def outer():
	loop_check='Y'
	while(loop_check=='Y' or loop_check=='y'):
		main()
		global_var_initialize()
		loop_check=input('Enter Y or y to run the Program for new data::\t')	

def main():
	global total_agent
	print('ratio',ratio)	#m,n values
	if(ratio==1):
		n=int(input("Enter the number of Users / Service providers  "))
		m=n
	if(ratio==2):
		print('M<N')
		m=int(input('Enter the number of Users M  '))
		n=int(input('Enter the number of Service Providers N  '))
	elif(ratio==3):
		print('M>N')
		m=int(input('Enter the number of Users M  '))
		n=int(input('Enter the number of Service Providers N  '))
	total_agent+=m
	initialization(n,m)
	choice=int(input('Enter 1 to run the program:  \n Any other integer to exit::  \t'))
	if(choice==1):
		main()
	global counter11
	if(counter11==0):
		draw_write(total_agent)
		random_write(total_agent)
		deviation_write(total_agent)
		
		counter11+=1

def global_var_initialize():
	#Variable initialization for draw
	global EP_Draw_best_allocation,EP_Draw_efficiency_loss,LP_Draw_efficiency_loss,LP_Draw_best_allocation,GP_Draw_best_allocation,GP_Draw_efficiency_loss
	EP_Draw_best_allocation=0
	EP_Draw_efficiency_loss=0
	LP_Draw_efficiency_loss=0
	LP_Draw_best_allocation=0
	GP_Draw_best_allocation=0
	GP_Draw_efficiency_loss=0
	global EF_Draw_efficiency_loss,EF_Draw_best_allocation,LF_Draw_efficiency_loss,LF_Draw_best_allocation,GF_Draw_efficiency_loss,GF_Draw_best_allocation
	EF_Draw_efficiency_loss=0
	EF_Draw_best_allocation=0
	LF_Draw_efficiency_loss=0
	LF_Draw_best_allocation=0
	GF_Draw_efficiency_loss=0
	GF_Draw_best_allocation=0
	#Variable initialization for Random
	global EP_Random_best_allocation,EP_Random_efficiency_loss,LP_Random_best_allocation,LP_Random_efficiency_loss,GP_Random_best_allocation,GP_Random_efficiency_loss
	EP_Random_best_allocation=0
	EP_Random_efficiency_loss=0
	LP_Random_best_allocation=0
	LP_Random_efficiency_loss=0
	GP_Random_best_allocation=0
	GP_Random_efficiency_loss=0
	global EF_Random_best_allocation,EF_Random_efficiency_loss,LF_Random_best_allocation,LF_Random_efficiency_loss,GF_Random_best_allocation,GF_Random_efficiency_loss
	EF_Random_best_allocation=0
	EF_Random_efficiency_loss=0
	LF_Random_best_allocation=0
	LF_Random_efficiency_loss=0
	GF_Random_best_allocation=0
	GF_Random_efficiency_loss=0
	#Variable initialization for deviaiation
	global EP_d2_best_allocation,EP_d2_efficiency_loss,EP_d4_best_allocation,EP_d4_efficiency_loss,EP_d8_best_allocation,EP_d8_efficiency_loss
	EP_d2_best_allocation=0
	EP_d2_efficiency_loss=0
	EP_d4_best_allocation=0
	EP_d4_efficiency_loss=0
	EP_d8_best_allocation=0
	EP_d8_efficiency_loss=0
	global LP_d2_best_allocation,LP_d2_efficiency_loss,LP_d4_best_allocation,LP_d4_efficiency_loss,LP_d8_best_allocation,LP_d8_efficiency_loss
	LP_d2_best_allocation=0
	LP_d2_efficiency_loss=0
	LP_d4_best_allocation=0
	LP_d4_efficiency_loss=0
	LP_d8_best_allocation=0
	LP_d8_efficiency_loss=0
	global GP_d2_best_allocation,GP_d2_efficiency_loss,GP_d4_best_allocation,GP_d4_efficiency_loss,GP_d8_best_allocation,GP_d8_efficiency_loss
	GP_d2_best_allocation=0
	GP_d2_efficiency_loss=0
	GP_d4_best_allocation=0
	GP_d4_efficiency_loss=0
	GP_d8_best_allocation=0
	GP_d8_efficiency_loss=0
	global EF_d2_best_allocation,EF_d2_efficiency_loss,EF_d4_best_allocation,EF_d4_efficiency_loss,EF_d8_best_allocation,EF_d8_efficiency_loss
	EF_d2_best_allocation=0
	EF_d2_efficiency_loss=0
	EF_d4_best_allocation=0
	EF_d4_efficiency_loss=0
	EF_d8_best_allocation=0
	EF_d8_efficiency_loss=0
	global LF_d2_best_allocation,LF_d2_efficiency_loss,LF_d4_best_allocation,LF_d4_efficiency_loss,LF_d8_best_allocation,LF_d8_efficiency_loss
	LF_d2_best_allocation=0
	LF_d2_efficiency_loss=0
	LF_d4_best_allocation=0
	LF_d4_efficiency_loss=0
	LF_d8_best_allocation=0
	LF_d8_efficiency_loss=0
	global GF_d2_best_allocation,GF_d2_efficiency_loss,GF_d4_best_allocation,GF_d4_efficiency_loss,GF_d8_best_allocation,GF_d8_efficiency_loss
	GF_d2_best_allocation=0
	GF_d2_efficiency_loss=0
	GF_d4_best_allocation=0
	GF_d4_efficiency_loss=0
	GF_d8_best_allocation=0
	GF_d8_efficiency_loss=0
	global counter11,total_agent
	counter11=0	#To perform file_writeoperation one time
	total_agent=0
		
def initialization(n,m):
	allotted_list=list()
	final_assignment=list()
	final_assignment=[-.1 for i in range(m)]
	agent_preff_list=list()
	if(ch == 1): #Partial prefference list initialization
		for i in range(m):
			range_ch=random.randint(1,n)
			a=random.sample(range(0,n),range_ch)
			agent_preff_list.append(a)
	else:	#Full prefference list initialization
		for i in range(m):
			a=random.sample(range(0,n),n)
			agent_preff_list.append(a)
	#print('Agent-ID\t Prefference-List')
	#for i in range(m):
	#	print(i,'\t\t',agent_preff_list[i])
	draw_sequence=list()
	draw_sequence=random.sample(range(0,m),m)
	#print('Draw_Sequence',draw_sequence)
	d_allotted_list=copy.deepcopy(allotted_list)
	d_final_assignment=copy.deepcopy(final_assignment)
	d_draw_sequence=copy.deepcopy(draw_sequence)
	d_agent_preff_list=copy.deepcopy(agent_preff_list)
	d1_allotted_list=copy.deepcopy(allotted_list)
	d1_final_assignment=copy.deepcopy(final_assignment)
	d1_draw_sequence=copy.deepcopy(draw_sequence)
	d1_agent_preff_list=copy.deepcopy(agent_preff_list)
	algo_draw(d_draw_sequence,d_final_assignment,d_allotted_list,agent_preff_list,n,m)
	algo_random(draw_sequence,final_assignment,allotted_list,agent_preff_list,n,m)
	algo_deviation(d1_draw_sequence,d1_final_assignment,d1_allotted_list,d1_agent_preff_list,n,m,2)
	algo_deviation(d1_draw_sequence,d1_final_assignment,d1_allotted_list,d1_agent_preff_list,n,m,4)
	algo_deviation(d1_draw_sequence,d1_final_assignment,d1_allotted_list,d1_agent_preff_list,n,m,8)

def algo_draw(d_draw_sequence,d_final_assignment,d_allotted_list,agent_preff_list,n,m):
	#print(d_draw_sequence)
	while(len(d_draw_sequence)!=0):
		agent_id=d_draw_sequence.pop(0)
		house_no=fun_house(agent_id,agent_preff_list[agent_id],d_allotted_list)
		d_allotted_list.append(house_no)
		d_final_assignment[agent_id]=house_no
	print('Allocation in CSAM-IcomP')
	#print('Allocation in draw')
	#print('AgentID\t\tHouse')
	#for i in range(m):
	#	print(i,'\t\t',d_final_assignment[i])
	result=list()
	result=eff_loss_bst_all(d_final_assignment,agent_preff_list,n)
	print('Efficiency Loss',result[0])
	print('Best Allocation',result[1])
	if(ch==1):
		if(ratio==1):
			global EP_Draw_best_allocation,EP_Draw_efficiency_loss 
			EP_Draw_best_allocation+=result[1]
			EP_Draw_efficiency_loss+=result[0]
		elif(ratio==2):
			global LP_Draw_best_allocation,LP_Draw_efficiency_loss
			LP_Draw_efficiency_loss+=result[0]
			LP_Draw_best_allocation+=result[1]			
			#filename1='LP_Draw_best_allocation.txt'
			#filename2='LP_Draw_efficiency_loss.txt'
		elif(ratio==3):
			global GP_Draw_best_allocation,GP_Draw_efficiency_loss
			GP_Draw_best_allocation+=result[1]
			GP_Draw_efficiency_loss+=result[0]
			#filename1='GP_Draw_best_allocation.txt'
			#filename2='GP_Draw_efficiency_loss.txt'
	else:	#FULL
		if(ratio==1):
			global EF_Draw_efficiency_loss
			EF_Draw_efficiency_loss+=result[0]
			global EF_Draw_best_allocation
			EF_Draw_best_allocation+=result[1]
		elif(ratio==2):
			global LF_Draw_best_allocation,LF_Draw_efficiency_loss
			LF_Draw_efficiency_loss+=result[0]
			LF_Draw_best_allocation+=result[1]
		elif(ratio==3):
			global GF_Draw_best_allocation,GF_Draw_efficiency_loss
			GF_Draw_efficiency_loss+=result[0]
			GF_Draw_best_allocation+=result[1]

def fun_house(agent_id,agent_preff_list,d_allotted_list):	#To find the house no
	for i in range(len(agent_preff_list)):
		if(agent_preff_list[i] in d_allotted_list):
			continue
		else:
			return(agent_preff_list[i])
#Code for random-allocation
def algo_random(draw_sequence,final_assignment,allotted_list,agent_preff_list,n,m):
	d7_agent_preff_list=copy.deepcopy(agent_preff_list)
	d3_draw_sequence=copy.deepcopy(draw_sequence)
	shuffle(d3_draw_sequence)
	#print(d3_draw_sequence)
	m1=len(draw_sequence)
	counter=1
	while(len(d3_draw_sequence)!=0):
		agent_id=d3_draw_sequence.pop(0)
		length_preff_list=len(d7_agent_preff_list[agent_id])	#Length of the prefference list of the agent
		if(length_preff_list==0):
			continue
		secure_random=random.SystemRandom()
		house_no=secure_random.choice(d7_agent_preff_list[agent_id])
		final_assignment[agent_id]=house_no
		algo_delete(house_no,d7_agent_preff_list,m1)	#To delete the house allotted from all the agents prefference list
	print('Allocation in Random')
	#print('AgentID\t\tHouse_No')
	#for i in range(m1):
	#	if(final_assignment[i]==-.1):
	#		print(i,'\t\t','None')
	#	else:
	#		print(i,'\t\t',final_assignment[i])
	result=list()
	result=eff_loss_bst_all(final_assignment,agent_preff_list,n)
	if(ch==1):
		if(ratio==1):
			global EP_Random_best_allocation,EP_Random_efficiency_loss 
			EP_Random_best_allocation+=result[1]
			EP_Random_efficiency_loss+=result[0]
		elif(ratio==2):
			global LP_Random_best_allocation,LP_Random_efficiency_loss
			LP_Random_best_allocation+=result[1]
			LP_Random_efficiency_loss+=result[0]
		elif(ratio==3):
			global GP_Random_best_allocation,GP_Random_efficiency_loss
			GP_Random_best_allocation+=result[1]
			GP_Random_efficiency_loss+=result[0]
	else:
		if(ratio==1):
			global EF_Random_best_allocation,EF_Random_efficiency_loss
			EF_Random_best_allocation+=result[1]
			EF_Random_efficiency_loss+=result[0]
		elif(ratio==2):
			global LF_Random_best_allocation, LF_Random_efficiency_loss
			LF_Random_best_allocation+=result[1]
			LF_Random_efficiency_loss+=result[0]
		elif(ratio==3):
			global GF_Random_best_allocation,GF_Random_efficiency_loss
			GF_Random_best_allocation+=result[1]
			GF_Random_efficiency_loss+=result[0]
	print('Efficiency loss',result[0])
	print('Best allocation',result[1])

def algo_delete(house_no,d7_agent_preff_list,m1):
	for i in range(m1):
		if(house_no in d7_agent_preff_list[i]):
			d7_agent_preff_list[i]=[x for x in d7_agent_preff_list[i] if x!=house_no]

def algo_deviation(d1_draw_sequence,d1_final_assignment,d1_allotted_list,d1_agent_preff_list,n,m,k):
	m1=len(d1_draw_sequence)
	d2_agent_preff_list=copy.deepcopy(d1_agent_preff_list)
	d2_allotted_list=copy.deepcopy(d1_allotted_list)
	d2_draw_sequence=copy.deepcopy(d1_draw_sequence)
	d2_final_assignment=copy.deepcopy(d1_final_assignment)
	dev=int((m1+1)/k)	#To select the number of agents deviated
	a=random.sample(range(0,m1),dev)
	#print('The agents deviate are:',a)
	for i in range(len(a)):
		#print(d1_agent_preff_list[a[i]])
		shuffle(d2_agent_preff_list[a[i]])
		#print(d1_agent_preff_list[a[i]])
	print('After Deviation::::')
	#print('Agent-ID\t\tPrefference List')
	#for i in range(m1):
		#print(i,'\t\t',d2_agent_preff_list[i])
	#print(d2_draw_sequence)
	m1=len(d2_draw_sequence)
	while(len(d2_draw_sequence)!=0):
		agent_id=d2_draw_sequence.pop(0)
		house_no=fun_house(agent_id,d2_agent_preff_list[agent_id],d2_allotted_list)
		d2_allotted_list.append(house_no)
		d2_final_assignment[agent_id]=house_no
	print('Allocation in Deviation n/',k)
	#print('AgentID\t\tHouse')
	#for i in range(m1):
	#	print(i,'\t\t',d2_final_assignment[i])
	result=list()
	result=eff_loss_bst_all(d2_final_assignment,d1_agent_preff_list,n)
	print('Efficiency Loss',result[0])
	print('Best Allocation',result[1])
	if(ch==1):	#Partial
		if(ratio==1):
			if(k==2):
				global EP_d2_best_allocation,EP_d2_efficiency_loss
				EP_d2_best_allocation+=result[1]
				EP_d2_efficiency_loss+=result[0]
			elif(k==4):
				global EP_d4_best_allocation,EP_d4_efficiency_loss
				EP_d4_best_allocation+=result[1]
				EP_d4_efficiency_loss+=result[0]
			elif(k==8):
				global EP_d8_best_allocation,EP_d8_efficiency_loss
				EP_d8_best_allocation+=result[1]
				EP_d8_efficiency_loss+=result[0]
		if(ratio==2):	#Less<
			if(k==2):
				global LP_d2_best_allocation,LP_d2_efficiency_loss
				LP_d2_best_allocation+=result[1]
				LP_d2_efficiency_loss+=result[0]
			elif(k==4):
				global LP_d4_best_allocation,LP_d4_efficiency_loss
				LP_d4_best_allocation+=result[1]
				LP_d4_efficiency_loss+=result[0]
			elif(k==8):
				global LP_d8_best_allocation,LP_d8_efficiency_loss
				LP_d8_best_allocation+=result[1]
				LP_d8_efficiency_loss+=result[0]
		elif(ratio==3):
			if(k==2):
				global GP_d2_best_allocation,GP_d2_efficiency_loss
				GP_d2_best_allocation+=result[1]
				GP_d2_efficiency_loss+=result[0]
			elif(k==4):
				global GP_d4_best_allocation,GP_d4_efficiency_loss
				GP_d4_best_allocation+=result[1]
				GP_d4_efficiency_loss+=result[0]
			elif(k==8):
				global GP_d8_best_allocation,GP_d8_efficiency_loss
				GP_d8_best_allocation+=result[1]
				GP_d8_efficiency_loss+=result[0]
	else:	#Full
		if(ratio==1):
			if(k==2):
				global EF_d2_best_allocation,EF_d2_efficiency_loss
				EF_d2_best_allocation+=result[1]
				EF_d2_efficiency_loss+=result[0]
			elif(k==4):
				global EF_d4_best_allocation,EF_d4_efficiency_loss
				EF_d4_best_allocation+=result[1]
				EF_d4_efficiency_loss+=result[0]
			elif(k==8):
				global EF_d8_best_allocation,EF_d8_efficiency_loss
				EF_d8_best_allocation+=result[1]
				EF_d8_efficiency_loss+=result[0]
		if(ratio==2):	#Less<
			if(k==2):
				global LF_d2_best_allocation,LF_d2_efficiency_loss
				LF_d2_best_allocation+=result[1]
				LF_d2_efficiency_loss+=result[0]
			elif(k==4):
				global LF_d4_best_allocation,LF_d4_efficiency_loss
				LF_d4_best_allocation+=result[1]
				LF_d4_efficiency_loss+=result[0]
			elif(k==8):
				global LF_d8_best_allocation,LF_d8_efficiency_loss
				LF_d8_best_allocation+=result[1]
				LF_d8_efficiency_loss+=result[0]
		elif(ratio==3):
			if(k==2):
				global GF_d2_best_allocation,GF_d2_efficiency_loss
				GF_d2_best_allocation+=result[1]
				GF_d2_efficiency_loss+=result[0]
			elif(k==4):
				global GF_d4_best_allocation,GF_d4_efficiency_loss
				GF_d4_best_allocation+=result[1]
				GF_d4_efficiency_loss+=result[0]
			elif(k==8):
				global GF_d8_best_allocation,GF_d8_efficiency_loss
				GF_d8_best_allocation+=result[1]
				GF_d8_efficiency_loss+=result[0]

def eff_loss_bst_all(d_final_assignment,agent_preff_list,n):
	output=list()
	eloss=0
	m=len(agent_preff_list)
	for i in range(m):
		if(isinstance(d_final_assignment[i],int)):
			t=agent_preff_list[i].index(d_final_assignment[i])
			eloss+=t
		else:
			eloss+=n	#eloss is n for unassigned agents
	#print('eloss',eloss)
	output.append(eloss)
	#To find best Allocation
	bst_allocation=0
	for i in range(m):
		if(d_final_assignment[i]==agent_preff_list[i][0]):
			bst_allocation+=1
	#print('best allocation',bst_allocation)
	output.append(bst_allocation)		
	return(output)

def file_write(filename,value,n):
	fo=open(str(filename),'a')
	#str1=os.getcwd()
	#print('current_directory',str1)
	fo.write(str(n))
	fo.write('\t')
	fo.write(value)
	fo.write('\n')
	fo.close()
outer()
