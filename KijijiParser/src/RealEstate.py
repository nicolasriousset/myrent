# -*- coding: utf-8 -*-

class Asset:
	type = ""
	rent = ""
	rentedBy = ""
	address = ""
	dateListed = ""
	furnished = ""
	bathrooms = ""
	petFriendly = ""
	lastEdited = ""
	location = ""
	
	def __init__(self):
		self.data = []
		
	def __str__(self):
		return self.dateListed + ";" + self.type + ";" + self.address + ";" + self.rent + ";" + self.rentedBy+ ";" + self.furnished+ ";" + self.bathrooms+ ";" + self.petFriendly+ ";" + self.lastEdited+ ";" + self.location + "\n"

	def __repr__(self):
		return self.dateListed + ";" + self.type + ";" + self.address + ";" + self.rent + ";" + self.rentedBy+ ";" + self.furnished+ ";" + self.bathrooms+ ";" + self.petFriendly+ ";" + self.lastEdited+ ";" + self.location + "\n"

	def updateAttribute(self, attrName, value):
		attrName = attrName.lower().strip()
		value = value.strip()
		if attrName == "prix" or attrName == "price":
			self.rent = value
		elif attrName == "à louer par" or attrName == "for rent by":
			self.rentedBy = value
		elif attrName == "adresse" or attrName == "address":
			self.address = value
			if self.address.endswith("\nAfficher la carte"):
				self.address = self.address[:-20]
			elif self.address.endswith("\nView map"):
				self.address = self.address[:-11]
		elif attrName == "date de l'affichage" or attrName == "date d'affichage" or attrName == "date listed":
			self.dateListed = value
		elif attrName == "meublé" or attrName == "furnished":
			self.furnished = value
		elif attrName == "salles de bains (nb)" or attrName == "bathrooms (#)":
			self.bathrooms = value
		elif attrName == "animaux acceptés" or attrName == "pet friendly":
			self.petFriendly = value
		elif attrName == "last edited" or attrName == "dernière mise à jour":
			self.lastEdited = value
		elif attrName == "lieu" or attrName == "location":
			self.location = value
		else:
			print("Unknown attribute : '" + attrName + "'")