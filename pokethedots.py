# Poke the Dots Version 1
# Implements the first ten steps of the todo list on
# https://docs.google.com/document/d/1bP8DJO6vMRYfwC2FeIGjQgK7mamTKK2Q1OfQ96j4y2w/edit

import pygame, random

# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Poke The Dots')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 
   
def show_text(surface, text_string, location, fontsize, fg_color, bg_color):
   text_font = pygame.font.SysFont('',24)
   text_image = text_font.render(text_string, True, fg_color, bg_color)
   surface.blit(text_image, location)
   
def show_score(self, score):
   self.surface
   text_string = 'Score:' + str(score)
   location = (0,0)
   fontsize = 72
   fg_color = 'white'
   bg_color = 'black'
   show_text(self.surface, text_string, location, fontsize, fg_color, bg_color)

def show_game_over_msg():
   text_string = 'Game Over!'
   location = (0,0)
   fontsize = 72
   fg_color = 'white'
   bg_color = 'black'
   show_text(self.surface, text_string, location, fontsize, fg_color, bg_color)   

def random_location(radius, window_size):
   # random location such that the whole dot is in the window
   # x coordinate of center = 
   #   random between radius and window width - radius
   # y coordinate of center = 
   #   random between radius and window height - radius
   width, height = window_size # tuple
   x = random.randint(radius, width - radius)
   y = random.randint(radius, height - radius)
   return [x, y]
   
# User-defined classes

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')
      
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      
      # === game specific objects
      window_size = surface.get_size()
      small_radius = 30
      small_center = random_location(small_radius, window_size)
      big_radius = 40
      big_center = random_location(big_radius, window_size)
      self.small_dot = Dot('red', small_radius, small_center, [1, 2], self.surface)
      self.big_dot = Dot('blue', big_radius, big_center, [2, 1], self.surface)
      self.max_frames = 150000000
      self.frame_counter = 0

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.small_dot.draw()
      self.big_dot.draw()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      
      self.small_dot.move()
      self.big_dot.move()
      self.frame_counter = self.frame_counter + 1

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      
      if self.frame_counter > self.max_frames:
         self.continue_game = False
         
   def show_text(surface, text_string, location, fontsize, fg_color, bg_color):
      text_font = pygame.font.SysFont('',24)
      text_image = text_font.render(text_string, True, fg_color, bg_color)
      surface.blit(text_image, location)
      
   def show_score(self, score):
      self.surface
      text_string = 'Score:' + str(score)
      location = (0,0)
      fontsize = 72
      fg_color = 'white'
      bg_color = 'black'
      show_text(self.surface, text_string, location, fontsize, fg_color, bg_color)
   


class Dot:
   # An object in this class represents a Dot that moves 
   
   def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
      # Initialize a Dot.
      # - self is the Dot to initialize
      # - color is the pygame.Color of the dot
      # - center is a list containing the x and y int
      #   coords of the center of the dot
      # - radius is the int pixel radius of the dot
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(dot_color)
      self.radius = dot_radius
      self.center = dot_center
      self.velocity = dot_velocity
      self.surface = surface
      
   def move(self):
      # Change the location of the Dot by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the Dot
      
      size = self.surface.get_size() # (500, 400)
      for i in range(0,2):
         self.center[i] = self.center[i] + self.velocity[i]
      for i in range(0,2):
         if self.center[i] < self.radius:
            # reached the minimum for this coordinate, turn back
            self.velocity[i] = - self.velocity[i]
         if self.center [i] + self.radius > size[i]:
            # reached the maximum for this coordinate, turn back
            self.velocity[i] = - self.velocity[i]

   def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)

main()