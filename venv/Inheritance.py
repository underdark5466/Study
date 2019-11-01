class modem():
    def __init__(self, year, firmware, licenses):
        self.year = year
        self.firmware = firmware
        self.licenses = licenses
    def define_model(self):
        if int(self.year) >= 2003 and int(self.year) <= 2007:
            print('model = UHP1000')
        elif int(self.year) >= 2008 and int(self.year) <= 2010:
            print ('model = UHP100')
        elif int(self.year) >= 2011 and int(self.year) <= 2018:
            print('model = UHP200')
        else:
            print('Wrong year')
    def actual_mode(self):
        if self.licenses == 'mesh':
            print('Your modem supports lolololo')
class new_modems(modem):
    def __init__(self, year, firmware, licenses):
        super().__init__(year, firmware, licenses)
        self.models = ['UHP3000','UHP4000','UHP5000']
    def describe_models(self):
        print(self.models)


random_modem = modem('2003','3.5.1','mesh')
random_modem.define_model()
random_modem.actual_mode()
random_modem = new_modems(1,2,3)
random_modem.describe_models()



