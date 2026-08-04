import os
import logging


def setup_logging():
    env = os.getenv("ENV")

    level = logging.DEBUG if env == "development" else logging.WARNING
    logging.basicConfig(
        level=level,
        format=(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
            if env == "development"
            else "%(levelname)s: %(message)s"
        ),
    )
