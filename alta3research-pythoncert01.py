#!/usr/bin/env python3

"""
Author: Chad Hansen
Date:   04/30/2021
This script query's the Art Institute of Chicago's Collections APIs and prints information about the artworks it found.
You can search for an artist, artwork or phrase and decide the maxium number of results to return.
You can also download an image of the artwork to your ~/static/ directory

"""
import requests, sys
from subprocess import call
from os import name as osname

def clear():
    # check and make call for specific operating system
    call('clear' if osname =='posix' else 'cls')

def main():
    search=""
    while True:
        idlist=[]

        search=input("Enter artist, artwork or phrase to search for (Type 'q' to quit) >> ")
        if search.lower() == "q" or search.lower() == "quit":
            break
        maxresults=input("Enter maximum number of search results to display (Type 'q' to quit) >> ")
        if maxresults.lower() == "q" or maxresults.lower() == "quit": 
            break
        
        try:
            artistresults=requests.get(f"https://api.artic.edu/api/v1/artworks/search?q={search}&size={maxresults}")
        except requests.exceptions.RequestException as err:
            print("Couldn't query search api: {0}".format(err))
            break

        for id in artistresults.json().get("data"):
            idlist.append(id['id'])
        
        clear()

        for artid in idlist:
            try:
                artwork = requests.get(f"https://api.artic.edu/api/v1/artworks/{artid}")
                
                artist=artwork.json()['data']['artist_title']
                title=artwork.json()['data']['title']
                artworkdate=artwork.json()['data']['date_display']
                dimensions=artwork.json()['data']['dimensions']
                medium=artwork.json()['data']['medium_display']
                artistid=artwork.json()['data']['artist_id']
                artimageid=artwork.json()['data']['image_id']
                artimageurl=f"https://www.artic.edu/iiif/2/{artimageid}/full/843,/0/default.jpg"
               
                print(f"Artist: {artist}")
                print(f"Title: {title}")
                print(f"Date: {artworkdate}")
                print(f"Dimensions: {dimensions}")
                print(f"Medium: {medium}")
                print(f"Art ID: {artid}")
                print(f"Artist ID: {artistid}")
                print(f"Art Image ID: {artimageid}")
                print(f"{artimageurl}")
                print("----------------")

            except requests.exceptions.RequestException as err:
                print("Couldn't query artworks api: {0}".format(err))
                break
            except OSError as err:
                    print("OS Error! {0}".format(err))
            except:
                    print("Something unexpected happened! ", sys.exc_info()[0]) 
           
            download=input("Would you like to download the image of this artwork? ")
            if download.lower() == "y" or download.lower()=="yes":
                try:
                    r = requests.get(artimageurl)
                    downloadfile="/home/student/static/"+ title.replace(" ", "_") +".jpg"
                    with open(downloadfile, 'wb') as f:
                        f.write(r.content)
                    print(f"The image was downloaded successfully to: {downloadfile}")
                except requests.exceptions.RequestException as err:
                    print("Couldn't download file: {0}".format(err))
                except OSError as err:
                    print("Couldn't write file! {0}".format(err))    
                except:
                    print("Something unexpected happened! ", sys.exc_info()[0])
                

if __name__ == "__main__":
    main()

