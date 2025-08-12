class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level data
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    # Increment song count
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # Add unique genres
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    # Add unique artists
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # Keep track of how many songs per genre
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    # Keep track of how many songs per artist
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1



s1 = Song("99 Problems", "Jay-Z", "Rap")
s2 = Song("Halo", "Beyonce", "Pop")
s3 = Song("Empire State of Mind", "Jay-Z", "Rap")

print(Song.count)  


print(Song.artists)  


print(Song.genres)  

print(Song.genre_count)  


print(Song.artist_count)  

