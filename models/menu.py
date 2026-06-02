from nextcord import Interaction, ui, SelectOption
from commands import slug_search_command


class GamesDropdown(ui.Select):
    def __init__(self, games):
        self.games = games[1:]
        options = []
        for game in self.games:  # Skip first game since it's already shown in the embed
            options.append(
                SelectOption(
                    label=game.get_title(),
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
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(
                "An error ocurred. Please try again."
            )
