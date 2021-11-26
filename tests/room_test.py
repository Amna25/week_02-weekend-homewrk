import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room 
class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Jill",100)
        self.guest2=Guest("James", 200)

        self.room = Room("ball", 50)

    def test_room_has_name(self):
        self.assertEqual("ball", self.room.name)
    def test_room_has_capacity(self):
        self.assertEqual(50, self.room.capacity)
    def test_guest_start_off_empty(self):
        self.assertEqual([], self.room.guest)
    #guest empty list
    def test_guest_start_off_empty(self):
        self.assertEqual([], self.room.guest)
    #add guest
    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest2)
        self.assertEqual(2 ,len(self.room.guest))
    