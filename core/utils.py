from datetime import datetime

"""
DEPRECATION WARNING: under the hood, Nextcord uses `asyncio.iscoroutinefunction(value)` when importing it's
functions, which will be removed in Python 3.16. Before considering updating to 3.16, check for this 
compatibility issue on Nextcord.
"""

import logging

log = logging.getLogger(__name__)


# Don't crash if date is invalid
def convert_date(date_stamp):
    if date_stamp is None:
        return "Unknown"
    try:
        return datetime.fromtimestamp(date_stamp).strftime("%d/%m/%Y")
    except ValueError:
        return None
