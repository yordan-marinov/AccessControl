from unittest import TestCase, main

import time
from door_system.card import Card


class CardTests(TestCase):
    def setUp(self):
        self.c1 = Card("6E536046010080FF")
        self.c2 = Card("445E6046010080FF")

    def test_card_correct_init(self):
        self.assertEqual("6E536046010080FF", self.c1.card_id)
        self.assertEqual("445E6046010080FF", self.c2.card_id)
        
    def test_get_expired_date_is_returns_correct_timestamp_as_int(self):
        now = time.time()
        exparied_date = time.time() + 1
        self.assertEqual(int(now + 1), int(exparied_date))


if __name__ == "__main__":
    main()
