#JaredEipp
#book.py
#addressbook
#First comment through git

class Person:
	
	def __init__(self, n):
		self.name = n

	def addAddress(self, a):
		self.address = a
	
	def addEmail(self, e):
		self.email = e
	
	def addPhone(self, pn):
		self.phone = pn
		
	def show(self):
		print("Name == " + self.name)
		print("Address == " + self.address)
		#print("Emai == " + self.email)
		#print("Phone Number == " + self.phone)















