import logging
from nextcord import Interaction, ui, SelectOption

from src.commands import slug_search_command
from core.utils import build_prices_embed
from src.models.embeds import deals_not_found
from config.logger import setup_logging

setup_logging()
log = logging.getLogger(__name__)


class GamesDropdown(ui.Select):
    def __init__(self, games):
        if games is None:
            log.error("Game list is None")
            return None
        self.games = games[1:]
        options = []
        for game in self.games:  # Skip first game since it's already shown in the embed
            options.append(
                SelectOption(
                    label=f"{game.get_title()}",
                    description=game.get_year(),
                )
            )
        super().__init__(
            placeholder="Select a game to view details",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: Interaction) -> None:
        selected_game = self.values[0]
        game = next(
            g for g in self.games if g.get_title() == selected_game
        )  # loops games until match by title

        embed = slug_search_command(str(game.get_slug()))

        """ 
        embed= warns and breaks if for some reason it receives None.
        wrapping in a if block suppress the warning and gives the user error feedback. 
        """
        if embed is not None:
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(embed=embed)

            prices = await build_prices_embed(game)

            # If block needed because send() does not support None, therefore, interpreter complains.
            if prices is not None:
                await interaction.followup.send(embed=prices)
            else:
                await interaction.followup.send(embed=deals_not_found)
        else:
            await interaction.response.send_message(
                "An error ocurred. Please try again."
            )
