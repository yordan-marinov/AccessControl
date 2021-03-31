from doors_system.card import Card
import datetime
import time


class Locker:
    __locker_stays_unlock = 5
    # time is set for 5 seconds by default

    def unlock_door(self, card: Card):
        print(f"Unlocking door with card: {card}/n")
        with open("door_usege.txt", "a") as f:
            st = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{card} used at {st}" + "\n ")

        time.sleep(5)

        print("Door is looked")
