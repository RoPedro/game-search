# All fixed embeds (like error embeds) will be stored here

import nextcord

game_not_found = nextcord.Embed(
    title="No Games Found",
    description="No games matched your search. Try a different title or check your spelling.",
    color=nextcord.Color.red(),
)

deals_not_found = nextcord.Embed(  # TODO: Create error embeds in separate places
    title="Error finding Deals",
    description="Maybe it's not a PC game;\nCurrently, only PC is supported.",
    color=nextcord.Color.red(),
)
