import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner_and_tournament.Runner("Усэйн", speed=10)
        self.andrey = runner_and_tournament.Runner("Андрей", speed=9)
        self.nick = runner_and_tournament.Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            print(f"{key}: {value}")

    def test_usain_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.usain, self.nick)
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)].get(2) == "Ник")

    def test_andrey_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.andrey, self.nick)
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)].get(2) == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.usain, self.andrey, self.nick)
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)].get(3) == "Ник")


if __name__ == '__main__':
    unittest.main()
