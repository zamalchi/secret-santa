#!/usr/bin/env python

import readline # optional, will allow Up/Down/History in the console
import code

from src.SecretSanta import *

if __name__=="__main__":
  
  ss = SecretSanta(["Erin", "Jake", "Syl", "Adriana"])
  ss.generate()
  ss.showResults()

  vars = globals().copy()
  vars.update(locals())
  shell = code.InteractiveConsole(vars)
  shell.interact()