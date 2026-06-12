query_fields = [
    "name",
    "slug",
    "involved_companies.company.name",
    "involved_companies.developer",
    "involved_companies.publisher",
    "first_release_date",
    "cover.url",
    "external_games.external_game_source.name",
    "external_games.uid",
]

def getFields():
    fields = query_fields[0]
    for field in query_fields[1:]:
        fields = fields + f", {field}"
        
    return fields