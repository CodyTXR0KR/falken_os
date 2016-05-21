#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import getpass
import subprocess

# Greeting includes current username
username = getpass.getuser()

# Display string
GREETING = '\n  Greetings {0},\n\n    Shall we play a game?\n\n'.format(username)
# Text to speech string
PHOENETIC_GREETING = 'Greetings {0}, shall we play a game?'.format(username)

# Dictionary used to populate games menu.  New options are added here.
GAMES = {
    "Chess": "google-chrome lichess.org",
    "Launch Steam": "steam",
    "Terraria": "steam steam://rungameid/105600",
    "Don't Starve Together": "steam steam://rungameid/322330",
    "Killing Floor": "steam steam://rungameid/1250",
    "Global Thermonuclear War": "\n  A strange game.\n  The only winning move is not to play.\n  How about a nice game of Chess?\n",
}

# Text-to-speech string also used for display due to lack of formatting chars
PHOENETIC_DESC = 'A strange game. The only winning move is not to play. How about a nice game of Chess?'

def slow_print(string, speed=0.05):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


def tts(string):
    args = ['spd-say', '"{0}"'.format(string)]
    subprocess.Popen(args)


def selection_menu():
    selection_menu = {}
    for i, key in enumerate(GAMES):
        selection_menu[i + 1] = key 
        sys.stdout.write('\t{0}. {1}\n'.format(str(i + 1), key))
        sys.stdout.flush()
        time.sleep(0.05)
    return selection_menu


def get_selection(selection_menu):
    while True:
        user_input = raw_input("\n    Make a selection: ").strip()
        if validate_selection(user_input):
            if int(user_input) in selection_menu:
                return selection_menu[int(user_input)]
        slow_print('\n  Invalid selection; "{0}".\n'.format(user_input))
        continue


def validate_selection(user_input):
    try:
        val = int(user_input)
        return True
    except ValueError:
        return False


def launch_selection(selection):
    sys.stdout.write('\n  Launching {0}'.format(selection))
    slow_print('.....')
    time.sleep(1)
    subprocess.call(GAMES[selection] + ' 2> /dev/null', shell=True)

if __name__ == "__main__":
    try:
        tts(PHOENETIC_GREETING)
        slow_print(GREETING)
        selections = selection_menu()
        selected = get_selection(selections)
        while selected == "Global Thermonuclear War":
            tts(PHOENETIC_DESC)
            slow_print(GAMES[selected], speed=0.05)
            selected = get_selection(selections)
        slow_print('\n OK.')
        launch_selection(selected)
    except KeyboardInterrupt:
        print("\n")
        sys.exit()
