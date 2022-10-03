import sys
import wiki_copy
import os
import subprocess


if __name__ == "__main__":
    print("dl_videos mod is run directly")
    urls, dic, artist = wiki_copy.main()
    urls_unique = list(set(urls))
    with open("songs.txt", "w") as s:
        for url in urls_unique:
            s.write(url)
            s.write("\n")
    os.mkdir(artist + "_mp3_files")
    os.rename("songs.txt", "./" + artist + "_mp3_files/songs.txt")
    print("run bash file")

