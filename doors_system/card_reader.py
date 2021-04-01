# usr/bin/env python3
# -*- coding: utf8 -*-


import serial


class CardReader:
    @staticmethod
    def get_card_id():
        """Reads the given card and returns the ID of it,
        if not raises file not find error"""

        try:
            s = serial.Serial("/dev/ttyUSB0", 9600)
            print("Please, hold your card")
            data = s.readline()
            card_id = data.decode("ascii")[:16]
            s.close()
            return card_id
        except (OSError, serial.SerialException):
            raise FileNotFoundError("Card reader is not connected")
