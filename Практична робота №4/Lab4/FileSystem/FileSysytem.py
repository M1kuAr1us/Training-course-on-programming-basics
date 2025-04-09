import os
import re

pattern = re.compile(r"^(?P<artist>.+?) - (?P<track>\d{2}) (?P<title>.+?) \((?P<year>\d{4})\)\.mp3$")

files = [f for f in os.listdir('.') if f.endswith('.mp3')]

for old_name in files:
    match = pattern.match(old_name)

    artist = match.group("artist")
    track = match.group("track")
    title = match.group("title")
    year = match.group("year")

    new_dir = os.path.join(artist, f"{year} {artist}")
    os.makedirs(new_dir, exist_ok=True)

    new_name = os.path.join(new_dir, f"{track} {title}.mp3")

    os.rename(old_name, new_name)

    print(f"{old_name} -> {new_name}")