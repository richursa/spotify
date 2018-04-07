his is richu
import sys
import os
try:
	if(sys.argv[1] =="-next"):
		os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")
	elif(sys.argv[1] == "-pause"):
		os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Pause");
	elif(sys.argv[1] =="-play"):
		os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play")
	elif(sys.argv[1] == "-prev"):
		os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")
		#os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")

	else:
		print "valid arguments are -play ,-pause , -prev ,-next"

except:
	print "valid arguments are -play ,-pause , -prev ,-next"


