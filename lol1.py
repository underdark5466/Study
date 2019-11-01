class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 6
    def set_number_served(self):
        print("Number is " + str(self.number_served))
    def increment_number_served(self,number):
        self.number_served += number
restik = Restaurant('malibu','meal')
restik.increment_number_served(34)
restik.set_number_served()