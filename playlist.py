playlist = {
    'title': 'rock',
    'author': 'James',
    'songs':[
        {'title': 'song1', 'artist': ['blue1'], 'duration':2.5},
        {'title': 'song2', 'artist': ['blue2'], 'duration':2.5},
        {'title': 'song3', 'artist': ['blue3'], 'duration':2.5}
    ]
}

total_length = 0
for song in playlist['songs']:
    print(song)
    total_length += song['duration']


print(total_length)