from doors_system.card import Card
from doors_system.cards import Cards

from unittest import TestCase, main
import time


class TestsCards(TestCase):
    def setUp(self):
        self.c1 = Card("6E536046010080FF")
        self.c2 = Card("445E6046010080FF")
        self.cards = Cards()

    def test_correct_cards_init(self):
        self.assertEqual([], self.cards.all_cards)

    def test_add_card(self):
        self.cards.add_card(self.c1)
        self.cards.add_card(self.c2)
        self.assertIn(self.c1, self.cards.all_cards)
        self.assertIn(self.c2, self.cards.all_cards)

    def test_add_same_card_twice(self):
        self.cards.add_card(self.c1)
        self.cards.add_card(self.c1)
        self.assertEqual(1, len(self.cards.all_cards))

    def test_remove_card_if_in_bd(self):
        self.cards.add_card(self.c1)
        self.cards.remove_card(self.c1)
        self.assertNotIn(self.c1, self.cards.all_cards)

    def test_remove_card_if_not_in_bd(self):
        self.cards.remove_card(self.c1)
        self.assertNotIn(self.c1, self.cards.all_cards)

    def test_find_card_by_id(self):
        self.c1 = Card("6E536046010080FF")
        self.cards.add_card(self.c1)
        expected = self.cards.find_card_by_id(self.c1.card_id)
        self.assertEqual(self.c1, expected)


if __name__ == "__main__":
    main()
