class Game:
    def __init__(
        self,
        title: str | None = None,
        slug: str | None = None,
        developer: str | None = None,
        publisher: str | None = None,
        release_date: int | None = None,
        small_thumb: str | None = None,
        dominant_color: int | None = None,
    ):
        self.title = title
        self.slug = slug
        self.developer = developer
        self.publisher = publisher
        self.release_date = release_date
        self.small_thumb = small_thumb
        self.dominant_color = dominant_color

    # Methods
    def get_title(self):
        return self.title

    def get_slug(self):
        return self.slug

    def get_developer(self):
        return self.developer

    def get_publisher(self):
        return self.publisher

    def get_release_date(self):
        return self.release_date

    def get_year(self):
        from datetime import datetime

        dt_stamp = self.release_date
        return datetime.fromtimestamp(dt_stamp).strftime("%Y")  # type: ignore

    def get_small_thumb(self):
        return self.small_thumb

    def get_dominant_color(self):
        return self.dominant_color

    def find_dominant_color(self):
        import requests
        from io import BytesIO
        from PIL import Image

        url = self.get_small_thumb()
        response = requests.get(str(url))

        """
        Pixel resizing seems to be the sweetspot between performance and accuracy. K-Means would require
        more processing power and slower responses due to modest VPS performance.
        """
        img = Image.open(BytesIO(response.content))
        img = img.convert("RGBA")
        img = img.resize((1, 1), resample=0)
        img_tuple = img.getpixel((0, 0))
        self.dominant_color = "0x{:02x}{:02x}{:02x}".format(
            img_tuple[0], img_tuple[1], img_tuple[2]  # type: ignore
        )
