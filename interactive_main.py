#!/usr/bin/env python

import readline # optional, will allow Up/Down/History in the console
import code

from src.SecretSanta import *

if __name__=="__main__":
  
  choice = raw_input("1 (play) or 2 (devPlay) : ")
  
  ss = SecretSanta()
  
  if choice == '1':
    ss.play()
  elif choice == '2':
    ss.devPlay()

  vars = globals().copy()
  vars.update(locals())
  shell = code.InteractiveConsole(vars)
  shell.interact()