from math import ceil
from typing import List, TypeVar, Type

T = TypeVar("T", bound="TrivialClass")


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = self.__build_photos()
        self.current_row_index = 0

    @classmethod
    def from_photos_count(cls: T, photos_count) -> T:
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        if len(self.photos[self.current_row_index]) == 4:
            self.current_row_index += 1
            try:
                self.photos[self.current_row_index].append(label)
                return f"{label} photo added successfully on page " \
                       f"page_number{self.current_row_index + 1} " \
                       f"slot {len(self.photos[self.current_row_index])}"
            except IndexError:
                return f"No more free slots"

        """
        def add_photo(self, label: str):
        for row, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page " \
                       f"page_number{row + 1} slot {len(page)}"
        return f"No more free slots"
        """

    def display(self) -> str:
        delimiter = "-" * 11
        output = delimiter + "\n"
        for page in self.photos:
            page_str = ' '.join(['[]' for _ in page])
            output += page_str + "\n" + delimiter + "\n"

        return output.strip()

    def __build_photos(self):
        matrix = []
        for _ in range(self.pages):
            matrix.append([] * self.PHOTOS_PER_PAGE)
        return matrix

