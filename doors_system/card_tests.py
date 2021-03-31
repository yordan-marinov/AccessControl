from unittest import TestCase, main

import time
from card import Card

# from doors_system.cards import Cards


class CardTests(TestCase):
    def setUp(self):
        self.c1 = Card()
        self.c2 = Card()

    def test_card_correct_init(self):
        self.assertEqual(1, self.c1.id)
        self.assertEqual(2, self.c2.id)


if __name__ == "__main__":
    main()
