class PhotoAlbum:
    photos_per_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        # self.photos -> matrix representing an album with its pages
        self.photos = [['' for i in range(PhotoAlbum.photos_per_page)] for n in range(pages)]

    """ creates a new instance of PhotoAlbum. Note: Each page can contain 4 photos. """
    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count)

    """
    adds the photo in the first possible page and slot and return 
    "{label} photo added successfully on page {page_number(starting from 1)} slot {slot_number(starting from 1)}". 
    If there are no free slots left, return "No more free slots"
    """
    def add_photo(self, label):
        for page_idx in range(self.pages):
            for photo_idx in range(PhotoAlbum.photos_per_page):
                if self.photos[page_idx][photo_idx] == '':
                    self.photos[page_idx][photo_idx] = label
                    return f'{label} photo added successfully on page {page_idx + 1} slot {photo_idx + 1}'
        return f'No more free slots'

    """
    returns: 
    a string representation of each page and the photos in it. Each photo is marked with "[]", 
    and the page separation is made using 11 dashes (-). For example, if we have 1 page and 2 photos:
    -----------
    [] []
    -----------
    and if we have 2 empty pages:
    -----------
    
    -----------
    
    -----------

    """
    def display(self):
        page_separation = '-' * 11
        result = ''
        for page in range(self.pages):
            result += page_separation + '\n'
            current_page = []
            for photo in range(PhotoAlbum.photos_per_page):
                current_page.append('[]') if self.photos[page][photo] != '' else ''
            result += ' '.join(current_page) + '\n'
        return result + page_separation.rstrip()


album = PhotoAlbum(3)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
