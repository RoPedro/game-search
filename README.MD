# GameSearch: A Discord bot to search for videogames.

# Running with docker

### Using `docker run` (Minimal, default setup)

```sh
docker run \
-d \
--name gamesearch \
-e DISCORD_BOT_TOKEN="DISCORD_BOT_TOKEN" \
-e IGDB_CLIENT_ID="IGDB_CLIENT_ID" \
-e IGDB_TOKEN="IGDB_TOKEN_HERE" \
-e ITAD_TOKEN="ITAD_TOKEN_HERE" \
pedrolrmoreira/game-search
```

### Additional environment variables

```
ENV="production/development" # Default: production
LANG="US/BR" # Default: US
```

## How to get .env variables

- Check `.envexample` file
