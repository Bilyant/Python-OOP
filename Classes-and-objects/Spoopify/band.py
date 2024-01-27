from album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        """
        Adds an album to the collection and returns
        "Band {band_name} has added their newest album {album_name}."
        If the album is already added, returns "Band {band_name} already has {album_name} in their library."
        """
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        """
        Removes the album from the collection and returns "Album {name} has been removed."
        If the album is published, returns "Album has been published. It cannot be removed."
        If the album is not in the collection, returns "Album {name} is not found."
        """
        album_to_remove = [a for a in self.albums if a.name == album_name][0]
        if album_to_remove.published:
            return 'Album has been published. It cannot be removed.'
        if album_to_remove not in self.albums:
            return f'Album {album_to_remove.name} is not found.'
        self.albums.remove(album_to_remove)
        return f'Album {album_to_remove.name} has been removed.'

    def details(self):
        """
        Returns the information of the band, with their albums, in this format:
        "Band {name}
         {album details}
         ...
         {album details}"
        """
        result = [f'Band {self.name}']
        for al in self.albums:
            result.append(al.details())
        return '\n'.join(result)
