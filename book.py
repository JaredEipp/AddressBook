#JaredEipp
#book.py
#addressbook

class Person:
	
	def __init__(self, n):
		self.name = n

	
	def addAddress(self, a):
		self.address = a

	def addEmail(self, e):
		self.email = e

	def addPhone(self, pn):
		self.phone = pn
