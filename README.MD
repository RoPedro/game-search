# GameSearch: A Discord bot to search for videogames.

## Getting Started with Docker
First of all, you'll need to create a discord application in the [Discord Developers](https://discord.com/developers/) portal. For now, more detailed instructions are to be added, so follow [this](https://youtu.be/Oy5HGvrxM4o) fireship video on how to create a application on the portal, this will give you the application token used on the deployment.

### Using `docker run`
```sh
docker run \
-d \
--name gamesearch \
-e DISCORD_BOT_TOKEN="DISCORD_BOT_TOKEN" \
-e IGDB_CLIENT_ID="IGDB_CLIENT_ID" \
-e IGDB_TOKEN="IGDB_TOKEN_HERE" \
-e ITAD_TOKEN="ITAD_TOKEN_HERE" \
-e LANG="US" \
pedrolrmoreira/game-search
```

### Optional environment variables
```
ENV="production/development" # Default: production
LANG="US/BR" # Default: US
ITAD_TOKEN="ITAD_TOKEN" # Necessary if wants isThereAnyDeal integration
```

## How to get .env variables
- Check `.envexample` file

## Usage
The prefix you need to use before any command is `?` by default, and `.` in development mode.

To search for a game, use `?gs <game_name`. If you want to search for the remake or remaster of a game (e.g. Resident Evil 2 2019), append "remake" or "remaster" after the game name, like this: `?gs resident evil 2 remake`

`?gs` also supports popular abbreviations like:
- GTA (Grand Theft Auto);
- RE (Resident Evil);
- AC (Ace Combat):

If a game has a known abbbreviation, it's **probably** supported.
