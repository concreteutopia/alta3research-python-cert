#!/usr/bin/env python3

"""
Author: Chad Hansen
Date:   04/30/2021

"""
import requests, sys
from PIL import Image
import numpy as np

def main():

    idlist=[]

    artist=input("Artist?")
    maxresults=input("Max Results? ")
    artistresults=requests.get(f"https://api.artic.edu/api/v1/artworks/search?q={artist}&size={maxresults}")
    
    #print(artistresults.json())
    for id in artistresults.json().get("data"):
        idlist.append(id['id'])

    #print(idlist)

    #artwork = requests.get(f"https://api.artic.edu/api/v1/artworks/{idlist[0]}")
    #print(artwork.json())
    #print(artwork.json().get('data').get('title'))
    #print(artwork.json().get('data').keys())
    for artid in idlist:
        #print(type(artid))
        #print(artid)
        artwork = requests.get(f"https://api.artic.edu/api/v1/artworks/{artid}")
        print(f"Artist: {artwork.json()['data']['artist_title']}")
        print(f"Title: {artwork.json()['data']['title']}")
        print(f"Date: {artwork.json()['data']['date_display']}")
        print(f"Dimensions: {artwork.json()['data']['dimensions']}")
        print(f"Medium: {artwork.json()['data']['medium_display']}")
        print(f"Art ID: {artid}")
        print(f"Artist ID: {artwork.json()['data']['artist_id']}")
        print(f"Artist ID: {artwork.json()['data']['image_id']}")
        print(f"https://www.artic.edu/iiif/2/{artwork.json()['data']['image_id']}/full/843,/0/default.jpg")
        print("----------------")
        
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

