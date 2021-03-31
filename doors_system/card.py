from datetime import datetime, timedelta


class Card:
    __card_valid_period_days = 30
    # This shoud be 30 days but for testing is set to seconds

    def __init__(self, id):
        self.id = id
        self.expired_date = self.get_expired_date()

    @staticmethod
    def get_expired_date(period_days=__card_valid_period_days):
        end_date = datetime.now() + timedelta(seconds=period_days)
        # Should be days not seconds in timedelta paramerters
        end_timestamp = datetime.timestamp(end_date)
        return int(end_timestamp)

    def __repr__(self):
        return f"card id: {self.id} with expired date: {self.expired_date}"
