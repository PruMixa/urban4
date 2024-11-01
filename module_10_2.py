import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies_left = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies_left > 0:
            self.enemies_left -= self.power
            self.days += 1
            time.sleep(1)
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies_left} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")