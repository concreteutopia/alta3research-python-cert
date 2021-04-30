#!/usr/bin/env python3

"""
Author: Chad Hansen
Date:   04/30/2021

"""
import requests

def main():

    idlist=[]

    artist=input("Artist?")
    artistresults=requests.get(f"https://api.artic.edu/api/v1/artworks/search?q={artist}")
    
    #print(artistresults.json())
    for id in artistresults.json().get("data"):
        idlist.append(id['id'])

    #print(idlist)

    artwork = requests.get(f"https://api.artic.edu/api/v1/artworks/{idlist[0]}")
    #print(artwork.json())
    print(artwork.json().get('data').get('title'))
"""
    for artid in idlist:
        artwork = requests.get(f"https://api.artic.edu/api/v1/artworks/{artid}")
        #print(artwork.json().get('data'))
        for art in artwork.json().get('data'):
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

