from nextcord import ui

from src.models.menu import GamesDropdown


def build_menu(games):
    if len(games) >= 2:
        menu = ui.View()
        menu.add_item(GamesDropdown(games))
        return menu
    else:
        return None
