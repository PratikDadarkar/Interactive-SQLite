import t1

#decide what to do
i=1
while i==1:
	var=input("Select One of insert|insertmany|delete|search : ")
	if var=='insert':
		t1.add_one()
	elif var=='insertmany':
		t1.add_many()       
	elif var=='delete':
		# Fd = input('Enter your First Name to delete it:')
		# Ld = input('Enter your Last Name to delete it:')
		# Ed = input('Enter your Email to delete it:')
		Rs = str(input('Enter the Row id(To find Search Your record) : '))
		t1.delete_one(Rs)
	elif var=='search':
		Fs = str(input('Enter your First Name to search it:'))
		Ls = str(input('Enter your Last Name to search it :'))
		Es = str(input('Enter your Email Address to search it:'))

		t1.where_record(Fs,Ls,Es)
	elif var=='exit':
		i+=1
		break
	else:
		print("This Function Is Not Available")
		



t1.show_all()    

#calling the function for inserting new records
# t1.add_one('Tom','Hiddleston','tom@gmail.com')

#calling the function for deleting a record 
# t1.delete_one('5')s

#to add many records
# alot = [
# 	('chris','evan','chris@gmail.com'),	
# 	('tony','stark','tony@gmail.com'),
# 	('gojo','satoru','gojo@gmail.com'),
# ]

# t1.add_many(alot)

# var_e=input("Enter your email id:")
# t1.where_record(var_e)

#to print all records in the table 
# t1.show_all()