# Udacity Full-Stack Web Developer Nano-Degree Program
## Project 01
### Chris Schneider

This is a simple program which generates a web page of six movie poster images with mouseover text
synopses and link to youtube trailers on click. 


### System Requirements

-Python installed on your machine.  Python can be installed from https://www.python.org/download/

-Pathing to the python directory in your shell.

### Installation

1. Create a fork of this project to your GitHub page.
2. In the git shell, change directory to where you would like to install
3. Type "git pull [user's github URL here]"

### Running
1. Change directory to /ud036_StarterCode/
2. Type python entertainment_center.py


### Components

**media.py**
This file contains the Movie class which accepts the title, a synopsis, link to poster image, and 
a youtube link to trailer as arguments to create a Movie object.

**fresh_tomatoes.py**
This file was provided by Udacity to enable ready creation of the web page.  
It takes as input an array list of Movie objects and outputs an html page of movie posters and
preview trailer links.  It then loads the newly created page in the default web browser in 
a new tab.
It has been modified from its original form to enable mouseover text on the poster images.

**entertainment_center.py**
This file defines six instances of the Movie class, applies them into an array, and calls the 
fresh_tomatoes.py file to create an html web page.
