#!/usr/bin/env python

import argparse
from src.SecretSanta import *



def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", dest="players", type=str, action="store")
  parser.add_argument("--players", dest="players", type=str, action="store")

  parser.add_argument("-ns", dest="noSave", action="store_true")
  parser.add_argument("--no-save", dest="noSave", action="store_true")

  parser.add_argument("-f", dest="file", type=str, action="store")
  parser.add_argument("--file", dest="file", type=str, action="store")

  parser.add_argument("-d", dest="dev", action="store_true")
  parser.add_argument("--dev", dest="dev", action="store_true")

  args = parser.parse_args()

  players = []

  if args.players:
    if "," in args.players:
      players = args.players.split(",")
    else:
      players = int(args.players)

  if players:
    ss = SecretSanta(players)
  else:
    ss = SecretSanta()
  
  ss.generate()

  if not args.dev:
    ss.reveal()

  if not ss.playerNames or args.dev:
    ss.showResults()

  if not args.noSave:
    if args.file:
      ss.save(args.file)
    else:
      ss.save()

if __name__=="__main__":
  main()