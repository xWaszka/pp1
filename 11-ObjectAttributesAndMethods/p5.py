class Music():
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year

    

    def __str__(self):
        return f"Performer:\t{self.artist}\nSong:\t\t{self.track_title}\nAlbum:\t\t{self.album}\nYear:\t\t{self.year}"

song1= Music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
print()
print(song1)
print()
