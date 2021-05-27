playlist = {
    'title': 'patagonia bus', 
    'author': 'Saahil', 
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5}, 
        {'title': 'song2', 'artist': ['kitty', 'dj cat'], 'duration': 5.25},
        {'title': 'song3', 'artist': ['garfield'], 'duration': 2.0}
    ]
}

for song in playlist['songs']:
    print(song['duration'])