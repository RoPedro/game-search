class Game:
    def __init__(
        self,
        title: str | None = None,
        developer: str | None = None,
        publisher: str | None = None,
        release_date: str | None = None,
        small_thumb: str | None = None,
    ):
        self.title = title
        self.developer = developer
        self.publisher = publisher
        self.release_date = release_date
        self.small_thumb = small_thumb

    # Methods
    def get_title(self):
        return self.title

    def get_developer(self):
        return self.developer

    def get_publisher(self):
        return self.publisher

    def get_release_date(self):
        return self.release_date

    def get_small_thumb(self):
        return self.small_thumb