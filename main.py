"""
'Stranded'
By:
CS 370 Final Project

Brief:
In Stranded, you find yourself marooned on an island through some unfortunate events. In this game, your goal is to
survive and escape the island.

DEV NOTES:
I encourage you to look at the game concepts document, and reach out to us on discord if you have any questions.

STATUS UPDATES:
Finished framework for movement system, working on implementing a loop for in game actions.

"""

import Stranded_Objects as SO
import random

def initMap(myMap):
       for i in range(len(myMap)):
           for j in range(len(myMap[i])):
               (myMap[i][j]).coords = [i, j]
       return myMap
def emptyMap(x,y):
    myMap = []
    myMap = [["NULL" for i in range(x)] for j in range(y)]
    return myMap

def startGame(game):
    player = game.player # for easier accessing
    map = game.map # for easier accessing

    print("Five days ago, your cruise ship was caught in a terrible storm and torn apart.\n"
          "you managed to make it to a life boat alone, and you have no clue of the fate of your fellow passengers.\n"
          "Before you escaped you managed to take one item with you, what was it?\n")

    print("1. A repair kit for electronics. \n"
          "2. A machete \n"
          "3. A first aid kit. \n")

    machete = SO.Item("Machete", "A bladed tool used for clearing brush.")
    eKit = SO.Item("Electronics Kit", "A tool kit, which could be used to repair electronic equipment.")
    firstAid = SO.Item("First-Aid Kit", "Contains various medical supplies which can be used to heal you.")
    shovel = SO.Item("Shovel","A shovel, generally used for digging.")
    firstItem = input()
    if firstItem == "1":
        player.pickup(eKit)

    elif firstItem == "2":
        player.pickup(machete)

    elif firstItem == "3":
        player.pickup(firstAid)
    else:
        print("Invalid entry, for your failure you will receive a random item.")

    while True:
        print("What would you like to do?")
        print("1. Check Surroundings.\n"
              "2. Move to a different location.\n"
              "3. View your inventory.\n"
              "4. Use an item")
        action = input()
        if action == "1":
            continue

        elif action == "2":
            continue

        elif action == "3":
            player.listInventory()

        elif action == "4":
            continue

def initialize():
    print("Initializing...")

    # >>> LOCATION BUILDING STARTS HERE <<<
    #  These are location templates, we can use these when we're creating new locations, but we shouldn't use plain
    #  templates as a location, examples of this shown below.
    #  Permanently Impassable locations should be prefaced with i_
    #  Temporarily impassable locations should be prefaced with t_
    #  Open locations should be prefaced with n_
    #  Location names should be 4-5 characters, since we want our maps to be alligned
    i_lav = SO.Loc("Lava Flow", "A red hot stream of lava, there's no getting over this.",[],1)
    n_bch = SO.Loc("Beach", "A sandy beach with nothing on it",["FISH","SLEEP"],0)
    n_jng = SO.Loc("Jungle", "A vibrant jungle, full of life.",[],0)
    n_rad = SO.Loc("Radio Tower", "An abandoned radio tower",[], 0)
    t_occ = SO.Loc("Ocean", "The ocean, stretches on as far as the eye can see",[],2)
    # >>> MAP BUILDING AND INFORMATION <<<

    # Map for testing and dev work.
    # The demo map, the only purpose of the definition here is for outlining what will be in it once we're done
    # Dimensions: 3x4
    DemoMap = \
    [
        [[i_lav], [i_lav], [i_lav]],
        [[i_lav], [n_jng], [i_lav]],
        [[i_lav], [n_bch], [i_lav]],
        [[t_occ], [t_occ], [t_occ]]
    ]

    DemoMap = emptyMap(3,4) # Creates a 2D array map with dimensions XY filled with "NULL" rooms.
    # We need 6 Lava tiles, 3 Ocean Tiles, 1 Beach, and 1 Jungle tile, 1 Radio Tower.
    lav1=lav2=lav3=lav4=lav5=lav6 = i_lav
    occ1=occ2=occ3 = t_occ
    bch1 = n_bch
    jng1 = n_jng
    rad1 = n_rad
    DemoMap = \
        [
                        [lav3, rad1, lav4],
                        [lav2, jng1, lav5],
                        [lav1, bch1, lav6],
                        [occ1, occ2, occ3]
        ]
    DemoMap = initMap(DemoMap)

    IslandMap = [[]]  # Our map will be a 2D array of locations.

    IslandMap = DemoMap # For development I use the demomap for testing, will be changed once we have real maps
    print("Map initialized at ylen: ", len(IslandMap), " xlen: ", len(IslandMap[0]))
    player = SO.Player([],0,100,20,n_bch)  # Make the player character.

    return player, IslandMap  # What we are going to pass to the game function.

    print("Initializing finished...")

def main(): # Main will be our Main Menu
    print("Welcome to \'Stranded\'!")
    print("Make a selection:\n"
          "\t1. New Game\n"
          "\t2. Exit\n")
    selection = input()
    if selection == "1": # Input only takes strings.
        player,map = initialize() # Initialize returns two things, player and map.
        game = SO.Instance(player, map) # Create the game instance
        startGame(game)
        # By splitting up our main and our game, we can send the player back to the menu using main()


    else:
        exit("Thanks for playing!")

main()