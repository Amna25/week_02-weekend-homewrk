import unittest
from src.guest import Guest
from src.song import Song
class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song("Best Day","happy song")
        self.song2 = Song("rainy days", "sad song")
        self.favourite_song= self.song, self.song2

        self.guest = Guest("Jill",100)

    def test_guest_has_name(self):
        self.assertEqual("Jill",self.guest.name)

    def test_guset_has_wallet(self):
        self.assertEqual(100, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.guest.add_song(self.song)
        self.assertEqual([self.song],self.guest.favourite_song)

    def test_can_add_song(self):
        self.guest.add_song(self.song)
        self.guest.add_song(self.song2)
        self.assertEqual(2, len(self.favourite_song))

    def test_has_enough_money(self):
        self.assertEqual(100, self.guest.enough_money())