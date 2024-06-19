# 练习 8.7：专辑

def make_album(artist, album_name, songs=None):
    if songs:
        album_info = {
            'artist': artist,
            'album': album_name,
            'songs': songs
        }
    else:
        album_info = {
            'artist': artist,
            'album': album_name
        }
    return album_info

# 创建三个表示不同专辑的字典并打印
album1 = make_album("Artist1", "Album1")
print(album1)

album2 = make_album("Artist2", "Album2", 12)
print(album2)

album3 = make_album("Artist3", "Album3", 8)
print(album3)
