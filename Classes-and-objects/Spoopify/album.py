from song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def get_song(self, song_name):
        for song in self.songs:
            if song.name == song_name:
                return song

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        song = self.get_song(song_name)
        if song is None:
            return "Song is not in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        self.songs.remove(song)
        return f"Removed song {song.name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        output = [f"Album {self.name}"]
        for song in self.songs:
            output.append(f'== {song.get_info()}')
        return '\n'.join(output) + '\n'
