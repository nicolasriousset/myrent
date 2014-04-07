# -*- coding: utf-8 -*-
import string

class Asset:
    type = "<Unknown>"
    rent = "<Unknown>"
    rentedBy = "<Unknown>"
    address = "<Unknown>"
    dateListed = "<Unknown>"
    furnished = "<Unknown>"
    bathrooms = "<Unknown>"
    petFriendly = "<Unknown>"
    lastEdited = "<Unknown>"
    location = "<Unknown>"
    description = "<Unknown>"
    
    def __init__(self):
        self.data = []
        
    def __str__(self):
        return self.type + "\t" + self.address + "\t" + self.rent + "\t" + self.rentedBy+ "\t" + self.furnished.__str__() + "\t" + self.bathrooms+ "\t" + self.petFriendly.__str__() + "\t" + self.dateListed + "\t" + self.lastEdited+ "\t" + self.location + "\t" + self.description + "\n"

    def __repr__(self):
        return self.__str__()

    def _parseBool(self, value):
        cleanValue = value.lower().strip()
        return cleanValue == "oui" or cleanValue == "yes"

    def _parseAddress(self, value):
        strippedValue = string.join(value.strip().split())
        if strippedValue.endswith("Afficher la carte"):
            return strippedValue[:-len("Afficher la carte")]
        elif strippedValue.endswith("View map"):
            return strippedValue[:-len("View map")]
        else:
            return strippedValue

    def parseType(self, value):
        cleanValue = value.lower().strip()
        if cleanValue == "bachelor/studio":
            return "1 1/2"
        elif cleanValue == "1 bedroom":
            return "2 1/2"
        elif cleanValue == "1 bedroom + den":
            return "3 1/2"
        elif cleanValue == "2 bedroom":
            return "4 1/2"
        elif cleanValue == "3 bedroom":
            return "5 1/2"
        elif cleanValue == "4+ bedroom" or cleanValue == "6 1/2 et +":
            return "6 1/2"
        else:
            return cleanValue[0:5]

    def _parsePrice(self, value):
        cleanValue = value.strip("$ \t\n\r").strip()
        if cleanValue.endswith(".00") or cleanValue.endswith(",00"):
            cleanValue = cleanValue[:-len(".00")]
        return cleanValue            

    def _parseRentedBy(self, value):
        cleanValue = value.lower().strip()
        if cleanValue == "propriétaire" or cleanValue == "owner":
            return "owner"
        elif cleanValue == "real estate agent" or cleanValue == "courtier immobilier":
            return "agent"
        else:
            return cleanValue
        
    def _parseBathroomsCount(self, value):
        value = value.replace(",", ".")
        if value.endswith(" bathrooms"):
            return value[:-10]
        elif value.endswith(" bathroom"):
            return value[:-9]
        elif value.endswith(" salle de bains"):
            return value[:-15]
        elif value.endswith(" salles de bains"):
            return value[:-16]
        else:
            return value

    def parseAttribute(self, attrName, value):
        cleanAttrName = attrName.lower().strip()
        cleanValue = value.strip()
        if cleanAttrName == "prix" or cleanAttrName == "price":
            self.rent = self._parsePrice(cleanValue)
        elif cleanAttrName == "à louer par" or cleanAttrName == "for rent by":
            self.rentedBy = self._parseRentedBy(cleanValue)
        elif cleanAttrName == "adresse" or cleanAttrName == "address":
            self.address = self._parseAddress(cleanValue)
        elif cleanAttrName == "date de l'affichage" or cleanAttrName == "date d'affichage" or cleanAttrName == "date listed":
            self.dateListed = cleanValue
        elif cleanAttrName == "meublé" or cleanAttrName == "furnished":
            self.furnished = self._parseBool(cleanValue)
        elif cleanAttrName == "salles de bains (nb)" or cleanAttrName == "bathrooms (#)":
            self.bathrooms = self._parseBathroomsCount(cleanValue)
        elif cleanAttrName == "animaux acceptés" or cleanAttrName == "pet friendly":
            self.petFriendly = self._parseBool(cleanValue)
        elif cleanAttrName == "last edited" or cleanAttrName == "dernière mise à jour":
            self.lastEdited = cleanValue
        elif cleanAttrName == "lieu" or cleanAttrName == "location":
            self.location = cleanValue
        else:
            print("Unknown attribute : '" + cleanAttrName + "'")
            
