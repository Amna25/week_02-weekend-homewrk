import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room 
class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Jill",100)
        self.room = Room("ball", 50)

    def test_room_has_name(self):
        self.assertEqual("ball", self.room.name)
    def test_room_has_capacity(self):
        self.assertEqual(50, self.room.capacity)

    