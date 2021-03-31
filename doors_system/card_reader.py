import serial


class CardReader:
    @staticmethod
    def get_card_id():
        print("Please, hold your card")
        try:
            s = serial.Serial("/dev/ttyUSB0", 9600)
            
        except FileNotFoundError("Check card reader connection"):
            return None
        
        data = s.readline()
        card_id = data[:16]
        return card_id

