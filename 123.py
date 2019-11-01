class Modem():
    def __init__(self, year, firmware, licenses):
        self.year = year
        self.firmware = firmware
        self.licenses = licenses
    def name(self):
        print(self.year + self.firmware + self.licenses)
class NewModem(Modem):
    def __init__(self, year, firmware, licenses):
        super().__init__(year, firmware, licenses)




random2 = NewModem('1','2','3')
#print(random2.name())