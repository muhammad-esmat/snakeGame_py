#import libraries
import sys
# from collections import deque
import curses as curses
import random
import time
from oop_snake import snake

#init curses and screen
screen = curses.initscr()

#getmaxyx
scr_y, scr_x = screen.getmaxyx()

#initialize window
window = curses.newwin(scr_y, scr_x, 0, 0)

#hide the mouse cursur
curses.curs_set(0)

#allow input
window.keypad(1)

#set delay time
window.timeout(125)

#make list representing the middle of screen
mid = [scr_y // 2, scr_x // 2]

#initailize food coordinates list
food = (mid[0], mid[1])

#add food to screen
window.addch(food[0], food[1], curses.ACS_STERLING)

#make the snake object
player = snake([scr_y // 2, scr_x // 4])

#set initial key to right
key = curses.KEY_RIGHT

#start the game loop
while True:
   #get next key
   next_key = window.getch()
   
   #if no key is entered or snake moves in the same direction key stays right
   if (
       next_key == -1
       or player.line_of_motion() == "Vertical" and next_key in [curses.KEY_UP, curses.KEY_DOWN]
       or player.line_of_motion() == "Horizontal" and next_key in [curses.KEY_RIGHT, curses.KEY_LEFT]
   ):
      pass
   else:
      key = next_key
      
      if key == curses.KEY_UP:
          player.direction = "up"
      elif key == curses.KEY_DOWN:
          player.direction = "down"
      elif key == curses.KEY_RIGHT:
          player.direction = "right"
      elif key == curses.KEY_LEFT:
          player.direction = "left"

   #make new head based on direction and insert it into snake
   player_hit_food = player.move(mid, window, food)
 
   #check if snake ate food if so make it respawn somewhere else
   if player_hit_food:
      food = None
      while food is None:
         new_food = (
            random.randint(2,scr_y - 2),
            random.randint(2,scr_x - 2)
            )
         food = new_food if new_food not in player.setBody else None
      window.addch(food[0], food[1], curses.ACS_STERLING)

   
   if (
        player.head[0] in [1, scr_y-1] or
        player.head[1] in [1, scr_x-1]
   ):
      player.loser(mid, window)
      quit()
