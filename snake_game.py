#import libraries
import sys
print(sys.version)
import curses as curses
import random
import time

#If snake loses
def loser(mid, snake):
   score = get_score(snake)
   print("Snake hit!")
   print(f"snake[0] = {snake[0]}, snake[1:] = {snake[1:]} ")
   curses.beep()
   window.clear()
   window.refresh()
   window.addstr(mid[0], mid[1], score)
   window.refresh()
   window.getch()
   curses.endwin()
   quit()
   #Add more features

#init curses and screen
screen = curses.initscr()

#getmaxyx
scr_y, scr_x = screen.getmaxyx()

#hide the mouse cursur
curses.curs_set(0)

#init window
window = curses.newwin(scr_y, scr_x, 0, 0)

#allow input
window.keypad(1)

#set delay time
window.timeout(125)

#make variables representing snake head coordinates
snk_y = scr_y // 2
snk_x = scr_x // 4

#make list representing snake body coordinates
snake = [
   [snk_y, snk_x],
   [snk_y, snk_x - 1],
   [snk_y, snk_x - 2]
]

def get_score(snake):
    score = f"Score: {len(snake)}"

    return score

#Return snake direction
def snk_dirc(snk1, snk2):
   dirc = "H"
   if snk1[0] != snk2[0]:
      dirc = "V"
   
   return dirc


#make list representing the middle of screen
mid = [scr_y // 2, scr_x // 2]

#initailize food coordinates list
food = [mid[0], mid[1]]

#add food to screen
window.addch(food[0], food[1], curses.ACS_STERLING)

#Set the keys
KEY_RIGHT = 454
KEY_LEFT = 452
KEY_UP = 450
KEY_DOWN = 456

#set initial key to right
key = KEY_RIGHT

#start the game loop
while True:
   #get next key
   next_key = window.getch()
   
   #if no key is entered or snake moves in the same direction key stays right
   if next_key == -1 or snk_dirc(snake[0], snake[1]) == "V" and next_key in [KEY_UP, KEY_DOWN] or snk_dirc(snake[0], snake[1]) == "H" and next_key in [KEY_RIGHT, KEY_LEFT]:
      pass
   else:
      key = next_key

   #check if snake hit itself or walls
   if snake[0][0] in [1, scr_y-1] or snake[0][1] in [1, scr_x-1] or snake[0] in snake[1:]:
      loser(mid, snake)
   else:
      #make new head based on direction and insert it into snake
      new_head = [snake[0][0], snake[0][1]]
      if key == 454:
         new_head[1] += 1
      elif key == 452:
         new_head[1] -= 1
      elif key == 450:
         new_head[0] -= 1
      elif key == 456:
         new_head[0] += 1
      else:
         new_head[1] += 1

      snake.insert(0, new_head)
      
   #check if snake ate food if so make it respawn somewhere else
   if food == snake[0]:
      food = None
      while food is None:
         new_food = [
            random.randint(2,scr_y - 2), 
            random.randint(2,scr_x - 2)
            ]
         food = new_food if new_food not in snake else None

      window.addch(food[0], food[1], curses.ACS_STERLING)

   #else remove tail 
   else:
      tail = snake.pop()
      window.addch(tail[0], tail[1], ' ')
    
   #make snake
   window.addch(snake[0][0], snake[0][1], curses.ACS_DIAMOND)

   print("_______________________________________")

   print(curses.__name__)

