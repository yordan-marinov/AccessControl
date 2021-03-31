from doors_system.card import Card
import datetime
import time


class Locker:
    __locker_stays_unlock = 5
    # time is set for 5 seconds by default

    def unlock_door(self, card: Card):
        """Unlocks the door and hold the locker
        for time of 5 seconds by default"""

        print(f"Unlocking door with card: {card}/n")

        with open("door_usege.txt", "a") as f:
            st = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{card} used at {st}\n")

        print("Wait five seconds")
        time.sleep(self.__locker_stays_unlock)
