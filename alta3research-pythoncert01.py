#!/usr/bin/env python3

"""
Author: Chad Hansen
Date:   04/30/2021

"""
import requests, sys

def main():
    search=""
    while True:
        idlist=[]

        search=input("Artist?")
        if search.lower() == "q":
            break
        maxresults=input("Max Results? ")
        if maxresults.lower() == "q":
            break
        artistresults=requests.get(f"https://api.artic.edu/api/v1/artworks/search?q={search}&size={maxresults}")
        
        for id in artistresults.json().get("data"):
            idlist.append(id['id'])

        for artid in idlist:
            artwork = requests.get(f"https://api.artic.edu/api/v1/artworks/{artid}")

            artimageurl=f"https://www.artic.edu/iiif/2/{artwork.json()['data']['image_id']}/full/843,/0/default.jpg"
            title=artwork.json()['data']['title']
            print(f"Artist: {artwork.json()['data']['artist_title']}")
            print(f"Title: {title}")
            print(f"Date: {artwork.json()['data']['date_display']}")
            print(f"Dimensions: {artwork.json()['data']['dimensions']}")
            print(f"Medium: {artwork.json()['data']['medium_display']}")
            print(f"Art ID: {artid}")
            print(f"Artist ID: {artwork.json()['data']['artist_id']}")
            print(f"Artist ID: {artwork.json()['data']['image_id']}")
            print(f"{artimageurl}")
            print("----------------")
            
            download=input("Would you like to download the image of this artwork? ")
            if download.lower() == "y":
                r = requests.get(artimageurl)

                downloadloc="/home/student/static/"+ title.replace(" ", "_") +".jpg"
                with open(downloadloc, 'wb') as f:
                    f.write(r.content)

                # Retrieve HTTP meta-data
                #print(r.status_code)
                #print(r.headers['content-type'])
                #print(r.encoding)


        print(len(idlist))
        print(idlist)





"""        for art in artwork.json().get('data'):
            print(type(art))
            
            print(f"Artist: {art['artist_title']}")
            print(f"Title: {art['title']}")
            print(f"Date: {art['date_display']}")
            print(f"Dimensions: {art['dimensions']}")
            print(f"ID: {art['id']}")
            print("*********")
    artwork = requests.get('https://api.artic.edu/api/v1/artworks?limit=20')
    #print(artwork.json().get("data"))
    for art in artwork.json().get('data'):
        print(f"Artist: {art['artist_title']}")
        print(f"Title: {art['title']}")
        print(f"Date: {art['date_display']}")
        print(f"Dimensions: {art['dimensions']}")
        print(f"ID: {art['id']}")
        print("*********")
"""

main()

