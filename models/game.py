class Game:
    def __init__(self, title: str | None, developer: str | None, release_date: str | None):
        self.title = title
        self.developer = developer
        self.release_date = release_date
        #self.publisher = publisher

    # Methods
    def get_title(self):
        return self.title

    def get_developer(self):
        return self.developer

    def get_release_date(self):
        return self.release_date

    '''
    def get_publisher(self):
        return self.publisher
    '''