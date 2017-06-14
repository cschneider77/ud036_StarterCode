import fresh_tomatoes
import media
"""This is a driver file to drive the functions in fresh_tomatoes and media to ultimately
create the desired web page."""


iron_man = media.Movie("Iron Man",
                        "Billionaire genius uses homemade flying Powered Armor to fight evil.", #quoting http://tvtropes.org/pmwiki/pmwiki.php/Laconic/IronMan
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://www.youtube.com/watch?v=tbMG2yTDXSY")
                        
incredible_hulk = media.Movie("The Incredible Hulk",
                        "Modern version of Jekyll and Hyde, but green.",  
                        "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",
                        "https://www.youtube.com/watch?v=xbqNb2PFKKA")
 
iron_man_2 = media.Movie("Iron Man 2",
                        "Bad guys steal Tony Stark's idea in order to use Powered Armor for evil.", 
                        "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                        "https://www.youtube.com/watch?v=BoohRoVA9WQ")

thor = media.Movie("Thor",
                        "Whosoever holds this hammer, if he be worthy, shall possess the power of Thor.", 
                        "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                        "https://www.youtube.com/watch?v=JOddp-nlNvQ")

captain_america = media.Movie("Captain America: The First Avenger",
                        "The classic patriotic superhero fights nazis.",
                        "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
                        "https://www.youtube.com/watch?v=JerVrbLldXw")
                        
avengers = media.Movie("The Avengers",
                        "S.H.I.E.L.D. calls together a band of superheroes to defend the world.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                        "https://www.youtube.com/watch?v=eOrNdBpGMv8")
                        
iron_man_3 = media.Movie("Iron Man 3",
                        "Tony Stark must fight while suffering from PTSD.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=oYSD2VQagc4")
                        
thor_dark_world = media.Movie("Thor: The Dark World",
                        "Thor must team up with his evil brother to fight a worse threat.",
                        "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",
                        "https://www.youtube.com/watch?v=npvJ9FTgZbM")

ca_winter_soldier = media.Movie("Captain America: The Winter Soldier",
                        "After an assassin tries to kill Nick Fury, Captain America chases after a new enemy.",
                        "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",
                        "https://www.youtube.com/watch?v=hvD6clUAWdA")
                        
guardians_galaxy = media.Movie("Guardians of the Galaxy",
                        "I am Groot.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                        "https://www.youtube.com/watch?v=d96cjJhvlMA")
                        
avengers_ultron = media.Movie("Avengers: Age of Ultron",
                        "Tony Stark designs a supercomputer.  It turns evil.",
                        "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                        "https://www.youtube.com/watch?v=tmeOjFno6Do")
                        
ant_man = media.Movie("Ant-Man",
                        "Size-changing ex-con who can talk to ants fights evil.",  #paraphrasing http://tvtropes.org/pmwiki/pmwiki.php/Laconic/AntMan
                        "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
                        "https://www.youtube.com/watch?v=pWdKf3MneyI")

doctor_strange = media.Movie("Doctor Strange",
                        "Maimed surgeon discovers magic is real.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                        "https://www.youtube.com/watch?v=Lt-U_t2pUHI")
                        
guardians_galaxy_2 = media.Movie("Guardians of the Galaxy: Volume 2",
                        "I am Groot.  I AM GROOT.",
                        "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                        "https://www.youtube.com/watch?v=dW1BIid8Osg")
                        
spiderman = media.Movie("Spiderman: Homecoming",
                        "Peter Parker finally becomes the Friendly Neighborhood Spiderman he was always meant to be.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                        "https://www.youtube.com/watch?v=n9DwoQ7HWvI")
                        
thor_ragnarok = media.Movie("Thor: Ragnarok",
                        "Thor must prevent the Norse Apocalypse.  And beat up the Hulk.",
                        "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                        "https://www.youtube.com/watch?v=v7MGUNV8MxU")
                        
avengers_infwar = media.Movie("Avengers: Infinity War",
                        "The Avengers team up with the Guardians of the Galaxy.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c5/Avengers_Infinity_War_logo_update.jpg",
                        "https://www.youtube.com/watch?v=3PyrgGTFp0E")  #Proper trailer not yet released.
'''
toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life", 
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")
                        
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris", 
             "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
             "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
             "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
             "https://www.youtube.com/watch?v=atLg2wQQxvU")
             
hunger_games = media.Movie("Hunger Games", "A really real reality show",
             "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
             "https://www.youtube.com/watch?v=PbA63a7H0bo")'''

movies = [iron_man, incredible_hulk, iron_man_2, thor, captain_america, avengers, iron_man_3, thor_dark_world, 
            ca_winter_soldier, guardians_galaxy, avengers_ultron, ant_man, doctor_strange, guardians_galaxy_2,
            spiderman, thor_ragnarok, avengers_infwar]
fresh_tomatoes.open_movies_page(movies)

