from address import Address

class Person:
    def __init__(self, fName:str, lName:str, dateOfBirth:str, phoneNumber:str, address):
        self.fName = fName
        self.lName = lName
        self.dateOfBirth = dateOfBirth
        self.phoneNumber = phoneNumber
        self.addresses = []

        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise 'Invalid Address...'
                
                self.addresses = address
        else:
            raise 'Invalid Address...'
        
    def add_address(self, address):
        if not isinstance(address, Address):
            raise 'Invalide Address...'
        
        self.addresses.append(address)