f = open('bob1.txt')
songs = []
for line in f:
    line = line.rstrip().lstrip()
    line = line.replace(" ","_")
    song_name = line.split('"')
    songs.append(song_name)
song_list = []
i = 1
for song in songs:
	song_list.append(song[1]+'.wav')
	print str(i)+ '_' + song[1]
	i += 1
print song_list
f.close()