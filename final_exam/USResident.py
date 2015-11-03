#  Problem 5 

# Paste here
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        # Write your code here
 	Person.__init__(self,name)
	try :
		["citizen", "legal_resident", "illegal_resident"].index(status)
		self.status=status
	except:
		raise ValueError()       
    def getStatus(self):
        """
        Returns the status
        """
        # Write your code here
	return self.status

