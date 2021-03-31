from doors_system.card import Card
from doors_system.cards import Cards
from doors_system.card_reader import CardReader
from doors_system.locker import Locker

import time


if __name__ == "__main__":
    c1 = Card(b"6E536046010080FF")
    c2 = Card(b"445E6046010080FF")

    cards = Cards()

    cards.add_card(c1)
    cards.add_card(c2)

    time_up = time.time() + 40
    now = time.time()
    # The while loop is set to run for 40 seconds for testing
    # while True:
    while now < time_up:
        cards.check_card(CardReader.get_card_id())
        
        now = time.time()
        
    print("Reader is up")
