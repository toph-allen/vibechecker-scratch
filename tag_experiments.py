from pathlib import Path
import mutagen
import urllib

m4a_url = 'file:///Users/toph/Music/iTunes/iTunes%20Media/Music/Minor%20Science/Whities%20012%20-%20Single/01%20Volumes.m4a'
m4a_filename = urllib.parse.urlparse(urllib.parse.unquote(m4a_filename)).path

m4a_filename = "/Users/toph/Music/iTunes/iTunes Media/Music/Peder Mannerfelt/Sissel & Bass 4 Ever - EP/04 Sissel & Bass (Perc Remix).m4a"
m4a_track = mutagen.File(m4a_filename)
m4a_tags = m4a_track.tags

mp3_filename = "/Users/toph/Music/iTunes/iTunes Media/Music/DOM TROJGA/Domownicy Różnoracy Cz.1/02 Hello Utopia.mp3"
mp3_track = mutagen.File(mp3_filename)
mp3_tags = mp3_track.tags

m4a_tags.keys()
mp3_tags.keys()


# Markers
m4a_markers_1 = m4a_tags["----:com.serato.dj:markers"]
m4a_markers_2 = m4a_tags["----:com.serato.dj:markersv2"]

mp3_markers_1 = mp3_tags["GEOB:Serato Markers_"]
mp3_markers_2 = mp3_tags["GEOB:Serato Markers2"]



track.keys()
for key in tags.keys():
    print("{}: {}".format(key, tags[key]))



# Pretty printing

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

pretty(m4a_tags)