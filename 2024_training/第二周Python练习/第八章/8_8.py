# 练习 8.8：用户的专辑

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

# 创建一个while循环让用户输入信息
def get_album_info():
    while True:
        artist = input("Enter the artist's name (or 'quit' to finish): ")
        if artist.lower() == "quit":
            break
        album_name = input("Enter the album's name: ")
        songs = input("Enter the number of songs in the album (or 'quit' to finish): ")
        if songs.lower() == "quit":
            break
        songs = int(songs)
        album_info = make_album(artist, album_name, songs)
        print(album_info)

# 调用函数获取用户信息
get_album_info()
