from song import Song


class Album:
    def __init__(self, name: str, *init_songs):
        self.name = name
        self.published = False
        self.songs = []
        self.init_songs = init_songs
        if init_songs:
            self.songs.extend(init_songs)

    def add_song(self, song: Song):
        """
        Adds the song to the album and returns "Song {song_name} has been added to the album {name}."
        If the song is single, returns "Cannot add {song_name}. It's a single"
        If the album is published, returns "Cannot add songs. Album is published."
        If the song is already added, return "Song is already in the album."
        """
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        if self.published:
            return 'Cannot add songs. Album is published.'
        if song in self.songs:
            return 'Song is already in the album.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        """
        Removes the song with the given name and returns "Removed song {song_name} from album {album_name}."
        If the song is not in the album, returns "Song is not in the album."
        If the album is published, returns "Cannot remove songs. Album is published."
        """
        if self.published:
            return 'Cannot remove songs. Album is published.'
        song_to_remove = [s for s in self.songs if s.name == song_name][0]
        if song_to_remove not in self.songs:
            return 'Song is not in the album.'
        self.songs.remove(song_to_remove)
        return f'Removed song {song_name} from album {self.name}.'

    def publish(self):
        """
        Publishes the album (set to True) and returns "Album {name} has been published."
        If the album is published, returns "Album {name} is already published."
        """
        if not self.published:
            self.published = True
            return f'Album {self.name} has been published.'
        return f'Album {self.name} is already published.'

    def details(self):
        """
        Returns the information of the album, with the songs in it, in the format:
        "Album {name}
         == {first_song_info}
         == {second_song_info}
         …
         == {n_song_info}"
        """
        result = [f'Album {self.name}']
        for s in self.songs:
            result.append(f'== {s.get_info()}')
        return '\n'.join(result) + '\n'
