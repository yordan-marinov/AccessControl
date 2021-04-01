from doors_system.card import Card
from doors_system.cards import Cards

from unittest import TestCase, main


class TestsCards(TestCase):
    def setUp(self):
        self.c1 = Card("6E536046010080FF")
        self.c2 = Card("445E6046010080FF")
        self.cards = Cards()

    def test_correct_cards_init(self):
        self.assertEqual([], self.cards.all_cards)

    def test_add_card(self):
        self.cards.add_card(self.c1)
        self.assertEqual(1, len(self.cards.all_cards))


if __name__ == "__main__":
    main()
