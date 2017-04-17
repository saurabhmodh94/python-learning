# CLASSES & OBJECTS

class Person:
    __name = ''
    __email = ''

    def __init__(self,name,email):
        self.__name=name
        self.__email=email

    def set_name(self,name):
        self.__name=name

    def set_email(self,email):
        self.__email=email

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def displayContact(self):
        print("{} can be reach at {}".format(self.__name,self.__email))

# brad=Person("Brad Pitt", "brad@gmail.com")
# # brad.set_name("Brad Pitt")
# # brad.set_email("brad@gmail.com")

# print(brad.get_name(),brad.get_email())
# brad.displayContact()

# INHERITANCE

class Customer(Person):
    __balance = 0

    def __init__(self,name,email,balance):
        self.__name=name
        self.__email=email
        self.__balance=balance
        # super(Customer,self).__init__(name,email) # TODO: solve error 
    
    def set_balance(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def displayDetails(self):
        print("Name: {} Email: {} Balance: {}".format(self.__name,self.__email,self.__balance))

john=Customer("john","john@gmail.com",100)
john.displayDetails()
