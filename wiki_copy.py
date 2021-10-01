import wikipedia
import requests as req
import sys
from bs4 import BeautifulSoup

def main():
    while True:
        try:
            artist = input("What artist would you like to download songs from? ")
        except Exception as e:
            print("not a valid input")
            continue
        else:
            break
    words = artist.split(" ")
    if len(words) > 1:
        new_words = [word[0].upper() + word[1:] + "_" for word in words]
        print(new_words)
        url_art = ''.join(new_words)
    
    else:
        url_art = artist[0].upper() +  artist[1:] + "_"
    
    url = "https://en.wikipedia.org/wiki/"+url_art+ "discography"

    print("Url:" + url)

    response = req.get(url).text
    soup = BeautifulSoup(response, 'lxml')

 
    my_tables = soup.find_all('table',{'class':'wikitable plainrowheaders'})

    song_list = []
    for table in my_tables:
        for row in table.find_all("tr")[1:]:
            for th in row.find_all("th",{'scope':'row'}):
                song = th.text
                song_list.append(song.replace('"', ''))

    try:
        from googlesearch import search
    except ImportError:
            print("No module named 'google' found")
    youtube_urls = []
    youtube_dic = {}


    for song in song_list[:100]:
        query = "Youtube" + artist + song
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            youtube_urls.append(j)
            youtube_dic[song] = j

    return (youtube_urls, youtube_dic, artist)



if __name__ == "__main__":
    print("wiki mod is run directly")
    main()
else:
    print("wiki mod is imported into another module")


