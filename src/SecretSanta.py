#!/usr/bin/env python

import random
import os

class SecretSanta:

  def play(self):
    #### PLAY
    self.generate()
    self.reveal()
    # only show results in anonymous mode
    if not self.playerNames:
      self.showResults()
    print
    self.save()
    #### #### ####

  def devPlay(self):
    #### DEVELOPMENT PLAY
    self.generate()
    self.showResults()
    # only needed in anonymous mode, because showResults won't reveal which player has which numbers
    if not self.playerNames:
      for i in range(self.playerCount):
        print "Player {} got #{} and is buying for #{}".format(str(i+1).ljust(2), self.isSelfList[i], self.isBuyingForList[i])
    print
    self.save()
    #### #### ####

  def save(self):
    from time import strftime
    datetime = strftime("%Y-%m-%d-%H-%M-%S")

    choice = raw_input("Do you wish to save these results? (y/N) : ")
    if choice.lower() in ['y', 'yes']:
      if not os.path.exists("saved_games"):
        os.mkdir("saved_games")

      fileName = raw_input("Name of file (default is current datetime) : ")

      if fileName:
        filePath = os.path.join("saved_games", fileName)
        if os.path.isfile(filePath):
          filePath = filePath + datetime
      else:
        filePath = datetime

      results = sorted(zip(self.isSelfList, self.isBuyingForList))
      resultString = "\n".join(["# IS BUYING FOR #"] + ["{} -----------  {}".format(str(pair[0]).ljust(2), pair[1]) for pair in results])

      f = open(os.path.join("saved_games", filePath), 'w')
      f.write(resultString)
      f.close()
      print "Wrote results to 'saved_games/{}'\n".format(filePath)

  def __init__(self, players=None):
    self.__isSelfList = []
    self.__isBuyingForList = []

    # instantiate with an int : number of players
    if type(players) is int:
      self.__playerCount = players
      self.__playerNames = []

    # instantiate with a list : names of players
    elif type(players) is list:
      self.__playerCount = len(players)
      self.__playerNames = players[:]

    # if not supplied, manually get information
    elif players == None:
      self.__playerNames = []
      # get number of players
      self.__playerCount = int(raw_input("Enter number of players : "))
      # get game mode
      gameMode = raw_input("""
1) Named mode : Players will know who they are buying for
2) Anonymous mode : Players won't know, but the matches will all be public
Choice (1 or 2) : """)
      # if named game mode
      if gameMode == "1":
        print
        for i in range(self.__playerCount):
          # get n=playerCount names
          self.__playerNames.append(raw_input("Player {}/{} name : ".format(i+1, self.playerCount)))
        # keep the list sorted internally
        self.__playerNames.sort()

  def generate(self):
    # if names have been given (i.e. named mode)
    if self.playerNames:
      # 1) copy the list of names
      players = self.playerNames[:]
    # else no names have been given (i.e anonymous mode)
    else:
      # 1) generate list of n=self.playerCount numbers
      players = list(range(self.playerCount))
  
    # 2) shuffle the names
    random.shuffle(players)
    # 3) set the shuffled list to the selfList
    self.isSelfList = players
    # 4) set the buyingForList to be the 1-offset of the selfList
    self.isBuyingForList = self.isSelfList[1:] + [self.isSelfList[0]]

  def reveal(self):
    
    def printWall():
      for i in range(50):
        print

    # get the self and buyingFor lists zipped (to preserve the pairings) and sorted (to preserve anonymity)
    zipped = sorted(self.getZippedLists())
    
    print "\nSTARING REVEAL"
    print "Only the current player should see the match.\n"

    # enumerate to get the index value
    for i, pair in enumerate(zipped):
      
      # CALL FOR PLAYER
      # if named mode
      if self.playerNames:
        raw_input("Player '{}' press enter to see your match...".format(pair[0]))
      # else anonymous mode
      else:
        raw_input("Player {}/{} press enter to see your match...".format(i+1, self.playerCount))

      # hide data
      printWall()

      # REVEAL MATCH TO PLAYER
      # if named mode
      if self.playerNames:
        print "{}, you are buying for {}".format(pair[0], pair[1])
      else:
        print "Your number is {} and you are buying for {}.".format(pair[0], pair[1])
      
      # HAVE PLAYER RESET FOR NEXT PLAYER
      raw_input("Press enter after you're done...")
      # hide data
      printWall()


  def showResults(self):
    #### CONSTANTS
    BASE_SPACE_TO_FILL = 11
    FILL_CHAR = '-'
    BORDER_CHAR = '#'
    #### #### ####
    #### GENERATED CONSTANTS
    ZIP = sorted(self.getZippedLists())
    # the longest row (i.e. p1name + p2name for every pair --> max reduction)
    MAX_ROW_LENGTH = max([(len(str(row[0])) + len(str(row[1]))) for row in ZIP] + [BASE_SPACE_TO_FILL])
    #### #### ####
    #### INNER FUNCTIONS
    def printBorder():
      print BORDER_CHAR * (BASE_SPACE_TO_FILL + MAX_ROW_LENGTH)
    #### #### ####
    #### MAIN
    print "SECRET SANTA RESULT".center(MAX_ROW_LENGTH + BASE_SPACE_TO_FILL)
    printBorder()
    print "|#" + " IS BUYING FOR ".center(MAX_ROW_LENGTH + BASE_SPACE_TO_FILL - 4) + "#|"

    for pair in ZIP:
      p1mod = "|{} ".format(pair[0])
      p2mod = " {}|".format(pair[1])

      spaceToFill = (BASE_SPACE_TO_FILL + MAX_ROW_LENGTH) - (len(p1mod) + len(p2mod))
      modified = p1mod + (FILL_CHAR * spaceToFill) + p2mod 
      print modified
    
    printBorder()    
    #### #### ####
    


  def getZippedLists(self):
    return zip(self.isSelfList, self.isBuyingForList)

  @property
  def playerCount(self):
    return self.__playerCount

  @property
  def playerNames(self):
    return self.__playerNames

  @property
  def isSelfList(self):
    return self.__isSelfList

  @isSelfList.setter
  def isSelfList(self, val):
    self.__isSelfList = val

  @property
  def isBuyingForList(self):
    return self.__isBuyingForList

  @isBuyingForList.setter
  def isBuyingForList(self, val):
    self.__isBuyingForList = val