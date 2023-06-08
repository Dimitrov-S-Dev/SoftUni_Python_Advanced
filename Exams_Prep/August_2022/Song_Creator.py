def add_songs(*args):
    collection = {

    }
    for song_name, song_lyrics in args:
        if song_name not in collection:
            collection[song_name] = []
        if song_lyrics:
            for lyric in song_lyrics:
                collection[song_name].append(lyric)

    output = ""

    for name, lyrics in collection.items():
        output += f"- {name}\n"
        for lyric in lyrics:
            output += f"{lyric}\n"

    return output
