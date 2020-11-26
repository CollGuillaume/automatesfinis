#!/usr/bin/env python3
"""
Read an automaton and a word, returns:
 * ERROR if non deterministic
 * YES if word is recognized
 * NO if word is rejected
"""

import automaton
import sys
import pdb # for debugging

if len(sys.argv) != 3:
  usagestring = "Usage: {} <automaton-file.af> <word-to-recognize>"
  automaton.error(usagestring.format(sys.argv[0]))

automatonfile = sys.argv[1]  
word = sys.argv[2]

def isDeterminist(automaton):

    for state in automaton.statesdict:
        for alphabet in automaton.alphabet:
            if alphabet in automaton.statesdict[state].transitions:
                  if alphabet == "%" and len(automaton.statesdict[state].transitions[alphabet]) == 1 \
                      and list(automaton.statesdict[state].transitions[alphabet].keys())[0].name != state:
                      return False
                  if len(automaton.statesdict[state].transitions[alphabet])>1:
                      return False

    return True

def isRecognize(automate, mot:str)->bool:


    current_state = automate.initial

    if mot == automaton.EPSILON and current_state.is_accept:

      return True

    for letter in mot:
        if letter not in automate.alphabet:

            return False


    for letter in mot: 

        if letter in current_state.transitions:
            current_state = list(current_state.transitions[letter].keys())[0]
        else:
            return False


    if current_state.is_accept:
        return True