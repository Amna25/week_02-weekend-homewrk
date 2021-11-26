import unittest
from src.song import Song
class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Best Day","happy song")
        

    def test_song_has_nmae(self):
        self.assertEqual("Best Day", self.song.name)

    def test_song_has_type(self):
        self.assertEqual("happy song",self.song.type)
   
    