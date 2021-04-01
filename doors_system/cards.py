#!/usr/bin/env python3
# -*- coding: utf8 -*-


from doors_system.card import Card
from doors_system.locker import Locker

import time


class Cards:
    def __init__(self):
        """Inicialization of all cards in system and
        dinamicaly checking which of them are blocked or active"""

        self.all_cards = []

    @property
    def blocked_cards(self):
        """Geting all current blocked cards"""
        return [c for c in self.all_cards if self.is_out_of_date(c)]

    @property
    def active_cards(self):
        """Geting all current active cards"""
        return [c for c in self.all_cards if not self.is_out_of_date(c)]

    @staticmethod
    def is_out_of_date(obj):
        """Checks time which is out of date"""
        return obj.expired_date < int(time.time())

    def add_card(self, card: Card):
        """Apend card to the list of all cards"""
        self.all_cards.append(card)

    def find_card_by_id(self, card_id):
        """Finds and returns card by its ID property"""
        return [c for c in self.all_cards if c.card_id == card_id][0]

    def check_card(self, card_id):
        card = self.find_card_by_id(card_id)
        if card in self.active_cards:
            Locker().unlock_door(card)
        else:
            print("You do not have access")
