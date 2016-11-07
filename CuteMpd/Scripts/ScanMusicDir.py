import os, sys

if sys.platform == 'win32':
    musicDir = "D:\Daten\Musik"
    playlistDir = "D:\Daten\Playlists"
else:
    musicDir = os.path.join('/var', 'lib', 'mpd', 'music')
    playlistDir = os.path.join('/var', 'lib', 'mpd', 'playlists')

print("Musicdir: {0}".format(musicDir))
print("PlaylistDir: {0}".format(playlistDir))


def createPlaylist(playlistDir, musicDir, folder):
    
    print("New File: {0}".format(folder))
    #file = open(playlistFilename, 'r+')
    fileList = []
    for root, dirs, files in os.walk(os.path.join(musicDir, folder)):
        for file in files:
            if file.endswith('.flac') or file.endswith('.mp3'):
                fileList.append(os.path.join(musicDir, folder, file))
                
    # Save the files
    playlistFilename = os.path.join(playlistDir, "{0}.m3u".format(folder))
    print("Create Playlist: {0}".format(playlistFilename))

    file=open(playlistFilename, 'w')
    for line in fileList:
        file.write("{0}\n".format(line))
        print("Soundfile: {0}".format(line)) 
    file.close()


for root, dirs, files in os.walk(musicDir):
    for dir in dirs:
        createPlaylist(playlistDir, musicDir, dir)
