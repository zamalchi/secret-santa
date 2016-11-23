#!/usr/bin/env python

import random
import os

class SecretSanta:

  def play(self):
    self.generate()
    self.reveal()
    self.showResults()
    print("\n")
    save()

  def devPlay(self):
    self.generate()
    print
    self.showResults()

    for i in range(self.playerCount):
      print "Player {} got #{} and is buying for #{}".format(str(i+1).ljust(2), self.isSelfList[i], self.isBuyingForList[i])
    print

    self.save()

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

  def __init__(self, playerCount=None):
    self.__isSelfList = []
    self.__isBuyingForList = []

    if playerCount == None:
      playerCount = int(raw_input("Enter number of players : "))
    self.__playerCount = int(playerCount)

  def generate(self):

    # 1) generate list of n=self.playerCount numbers
    isSelfNumbers = [i for i in range(self.playerCount)]
    # 2) shuffle the list
    random.shuffle(isSelfNumbers)
    # 3) copy the list and append the original first element (in effect, shifting the second list by 1)
    isBuyingForNumbers = isSelfNumbers[1:] + [isSelfNumbers[0]]
    
    self.isSelfList = isSelfNumbers
    self.isBuyingForList = isBuyingForNumbers

  def reveal(self):
    
    def printWall():
      for i in range(50):
        print

    print "STARING REVEAL\n"

    for i in range(self.playerCount):
      raw_input("Player {}/{} press enter to see your match...".format(i+1, self.playerCount))
      printWall()
      print "Your number is {} and you are buying for {}.".format(self.isSelfList[i], self.isBuyingForList[i])
      raw_input("Press enter after you're done...")
      printWall()

  def showResults(self):
    
    def rowAdjustPrint(row):
      print(("|" + row).ljust(19) + "|")

    zipped = sorted(zip(self.isSelfList, self.isBuyingForList))

    print "SECRET SANTA RESULTS"
    print("####################")
    rowAdjustPrint("# IS BUYING FOR #")

    for pair in zipped:
      rowAdjustPrint("{} -----------  {}".format(str(pair[0]).ljust(2), pair[1]))
    print("####################")


  @property
  def playerCount(self):
    return self.__playerCount

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