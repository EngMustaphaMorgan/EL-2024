#! /usr/bin/python3

#------------------------------------------------------------------------------------------------------------------
# Author      : Mostafa Morgan
# Date        : 13/6/2024
# Description :
#
#
#
#------------------------------------------------------------------------------------------------------------------

# import webbrowser module to open urls in your browser
import webbrowser

# create a dict with keys of url names and values of urls
fav_sites = {
    "01-yocto"         : "https://docs.yoctoproject.org/" ,
    "02-openemebedded" : "https://layers.openembedded.org/layerindex/branch/master/layers/" ,
    "03-cppreference"  : "https://en.cppreference.com/w/"
}

# method to take the url 
# get an obj ofr your web browser (i.e. firefox in my case)
# open the url in a new tab with the given url
def favouriteLinks( url ) :
    firefox = webbrowser.get('firefox')
    firefox.open_new_tab(url)
