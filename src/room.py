class Room:
    def __init__(self,name,capacity):
        self.name= name
        self.capacity= capacity
        self.songs= []
        self.guest= []


    def check_in_guest(self, guest):
      self.guest.append(guest)
        