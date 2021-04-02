# /usr/bin/env python3
# -*- coding: utf8 -*-


from doors_system.card import Card
from doors_system.locker import Locker

import time


class Cards:
    def __init__(self):
        """Inicialization of all cards in system and
        dinamicaly checking which of them are blocked or active"""

        self.all_cards = []
        self.all_cards_ids = set()

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
        if card.card_id not in self.all_cards_ids:
            self.all_cards.append(card)
            self.all_cards_ids.add(card.card_id)
        # else:
            # print(f"{card} is already regestered")

    def remove_card(self, card: Card):
        if card.card_id in self.all_cards_ids:
            self.all_cards.remove(card)
            self.all_cards_ids.remove(card.card_id)
        # else:
            # print(f"{card} does not exists")

    def find_card_by_id(self, card_id):
        """Finds and returns card by its ID property"""
        return [c for c in self.all_cards if c.card_id == card_id][0]

    def check_card(self, card_id):
        card = self.find_card_by_id(card_id)
        if card in self.active_cards:
            Locker().unlock_door(card)
        else:
            print("You do not have access")
