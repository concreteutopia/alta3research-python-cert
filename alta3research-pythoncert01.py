#!/usr/bin/env python3

"""
Author: Chad Hansen
Date:   04/30/2021
This script query's the Art Institute of Chicago's Collections API
and prints information about the artworks it found.
You can search for an artist, artwork or phrase and decide the maxium number of results to return.

You can also download an image of the artwork to your ~/static/ directory

If you do not know what to search for, simply press <enter> and a random search will be made for you.

Requirements: requests
    https://pypi.org/project/requests/
    To install: python3 -m pip install requests
Usage: python3 alta3research-pythoncert01.py
"""

import sys
import random
from subprocess import call
from os import name as osname
import requests

def clear():
    """function to clear the screen"""
    # check and make call for specific operating system
    call('clear' if osname =='posix' else 'cls')

def main():
    """this is main()"""
    search=""
    while True:
        idlist=[]
        randomlist=["warhol","van gogh","picasso","wirsum","gladys nilsson","frank stella",
                "diego rivera","ancient egyptian","aztec","edward hopper","cats","hokusai",
                "willem de kooning","jackson pollock","david hockney","takashi murakami",
                "lichtenstein","christopher wool","pop art","keith haring","alexander calder",
                "contemporary art","modern art","gerhard richter","lighthouse"]

        #Input search query or choose a random search from randomlist if no search is provided.
        print("Enter artist, artwork or phrase to search for. (ex: Picasso, Andy Warhol, cats, Van Gogh, Monet, Chicago)")
        search=input("<Enter> for random search, type 'q' to quit) >> ")
        if search.lower() == "q" or search.lower() == "quit":
            break
        if search == "":
            search=random.choice(randomlist)
            print(f"Your randomly chosen search is: {search}!")
        #Input maximum number of results to be displayed.  Trap for q, quit or input that is not a number.
        maxresults=input("Enter maximum number of search results to display (Type 'q' to quit) >> ")
        if maxresults.lower() == "q" or maxresults.lower() == "quit":
            break
        try:
            int(maxresults)
        except ValueError:
            print("That's not a number!")
            break
        #Query the collections search api with the search criteria and the maximum number of results to display
        #Trap any errors and exit thrown by the api.
        try:
            artistresults=requests.get(f"https://api.artic.edu/api/v1/artworks/search?q={search}&size={maxresults}")
        except requests.exceptions.RequestException as err:
            print("Couldn't query search api: {0}".format(err))
            break
        except OSError as err:
            print("OS Error! {0}".format(err))
        except SystemError:
            print("Something unexpected happened! ", sys.exc_info()[0])
        #Parse the search results, grab the artwork id and put it in a list.
        #We need the artwork id to query the artworks api to get the full artwork details
        for resultsid in artistresults.json().get("data"):
            idlist.append(resultsid['id'])
        clear()
        #For every id in the list, display the artwork details
        #and prompt to download the file
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
            #trap errors thrown by the api or requests
            except requests.exceptions.RequestException as err:
                print("Couldn't query artworks api: {0}".format(err))
                break
            except OSError as err:
                print("OS Error! {0}".format(err))
            except SystemError:
                print("Something unexpected happened! ", sys.exc_info()[0])
            #if the artwork has an image id, ask if it should be downloaded.  trap on any errors.
            if artimageid is not None:
                download=input("Would you like to download the image of this artwork? (Type 'q' to return to the search prompt.)")
                if download.lower() == "y" or download.lower()=="yes":
                    try:
                        #use requests to download the artwork image
                        #then write it to a file, trap errors
                        downloadreq = requests.get(artimageurl)
                        #save to static directory for easy viewing
                        downloadfile="/home/student/static/"+ title.replace(" ", "_") +".jpg"
                        with open(downloadfile, 'wb') as localfile:
                            localfile.write(downloadreq.content)
                        print(f"The image was downloaded successfully to: {downloadfile}")
                    except requests.exceptions.RequestException as err:
                        print("Couldn't download file: {0}".format(err))
                    except OSError as err:
                        print("Couldn't write file! {0}".format(err))
                    except SystemError:
                        print("Something unexpected happened! ", sys.exc_info()[0])
                elif download.lower() == "q" or download.lower()=="quit":
                    #a break here returns us to the top of the while loop to the search query
                    break
                elif download.lower() == "n" or download.lower()=="no":
                    #continue will  go to the top of the for loop and to next artwork
                    continue
                else:
                    print("Invalid input! Moving on....")
            else:
                print("Artwork image does not exist!")
            print("----------------")
        clear()

if __name__ == "__main__":
    main()
