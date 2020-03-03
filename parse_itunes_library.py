import plistlib
import mutagen
from pathlib import Path
from urllib.parse import unquote, urlparse

with open(Path("/Users/toph/Music/Library.xml").absolute(), "rb") as xml_file:
    itl = plistlib.load(xml_file)


def get_playlists_by_name(name):
    return [pl for pl in playlists if pl["Name"] == name]


def get_parent(pl):
    if "Parent Persistent ID" not in pl.keys():
        return None
    else:
        parent = [item for item in playlists if item["Playlist Persistent ID"] == pl["Parent Persistent ID"]][0]
        return parent

def get_ancestors(pl):
    this_pl = pl
    ancestors = []
    while "Parent Persistent ID" in this_pl.keys():
        this_plp = get_parent(this_pl)
        ancestors.append(this_plp)
        this_pl = this_plp
    return ancestors


def playlist_tracks(playlist):
    track_ids = [item["Track ID"] for item in playlist["Playlist Items"]]
    # return [track for i, track in itl["Tracks"].items() if track["Track ID"] in track_ids]
    playlist_tracks = []
    for track_id in track_ids:
        playlist_tracks.extend([track for i, track in itl["Tracks"].items() if track["Track ID"] == track_id])
    return playlist_tracks


tracks = []
for track_id, track_meta in itl["Tracks"].items():
    tracks.append(track_meta)

playlists = itl["Playlists"]




vibes = [pl for pl in playlists if pl["Name"] == "2. Vibes"][0]

vibe_leaves = [
    pl for pl in playlists
    if vibes in get_ancestors(pl)
    and "Folder" not in pl.keys()
]

vibe_tree = [
    pl for pl in playlists
    if vibes in get_ancestors(pl)
]




pl = playlists[76]
pl_track_ids = [item["Track ID"] for item in pl["Playlist Items"]]

pl_tracks = [track["Name"] for i, track in itl["Tracks"].items() if track["Track ID"] in pl_track_ids]

# Does not currently preserve order


to_buy = [pl for pl in playlists if pl["Name"] == "To Buy"][0]

tb_tracks = playlist_tracks(to_buy)

tb_tracks[0]



for track_dict in tb_tracks:
    print("\n")
    print(track_dict)
    track_filepath = Path(unquote(urlparse(track_dict["Location"]).path))
    track_file = mutagen.File(track_filepath)

    target_tags = ["©ART", "©alb", "©nam"]
    backup_tags = ["soar", "soal", "sonm"]
    source_keys = ["Artist", "Album", "Name"]

    for target, backup, source in zip(target_tags, backup_tags, source_keys):
        print("\n")
        tags = track_file.tags
        target_value = tags.get(target)
        print("Target: {}: {}".format(target, target_value))

        backup_value = tags.get(backup)
        print("Backup: {}: {}".format(backup, backup_value))

        source_value = track_dict.get(source)
        print("Source: {}: {}".format(source, source_value))

        if target_value is None or target_value == [""]:
            tags[target] = source_value
            print("Updated '{}'' with value '{}'".format(target, source_value))
            track_file.save()
        else:
            print("Did not update '{}'; already set to '{}'".format(target, target_value))