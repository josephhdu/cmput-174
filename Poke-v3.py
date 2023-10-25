# CMPUT 174 Fall 2021 Section A6
# October 19
# Poke the Dots Version 3
# Implements all the steps of the todo list on
# https://docs.google.com/document/d/1bP8DJO6vMRYfwC2FeIGjQgK7mamTKK2Q1OfQ96j4y2w/edit
# Version 3 adds event handling for mouse clicks
# Bug fixed after class:
# Stop processing mouse events after game is over
# See the code change in handle_events():
# if self.continue_game and event.type == pygame.MOUSEBUTTONDOWN:


import pygame, random, math

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

def create_text_image(text_string, fontsize, fg_color, bg_color):
   text_font = pygame.font.SysFont('', fontsize)
   text_image = text_font.render(text_string, True, fg_color, bg_color)
   return text_image

def show_text(surface, text_string, location, fontsize, fg_color, bg_color):
   text_image = create_text_image(text_string, fontsize, fg_color, bg_color)
   surface.blit(text_image, location)

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
   
def distance(point1, point2):
   # points are tuples (x, y)
   # Compute distance from Pythagorean Theorem,
   # r**2 = dx**2 + dy**2, where dx and dy are the
   # differences in x- and y-coordinates of the points
   (x1, y1) = point1
   (x2, y2) = point2
   dx = x1 - x2
   dy = y1 - y2
   r = math.sqrt(dx ** 2  +  dy ** 2)
   return r
   
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
      self.score = 0
      
      # === game specific objects
      self.create_non_overlapping_dots()

   def create_non_overlapping_dots(self):
      # loop
      # - generate dots at random locations
      # - test if they touch or overlap
      # - if yes, stay in loop, repeat
      # - if no: we have valid dots, exit loop

      window_size = self.surface.get_size()
      have_valid_dots = False
      while not have_valid_dots:
         small_radius = 30
         small_center = random_location(small_radius, window_size)
         big_radius = 40
         big_center = random_location(big_radius, window_size)
         self.small_dot = Dot('red', small_radius, small_center,
                              [1, 2], self.surface)
         self.big_dot   = Dot('blue', big_radius, big_center,
                              [2, 1], self.surface)
         if not self.small_dot.collide(self.big_dot): # success!
            have_valid_dots = True
         
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
         self.game_Clock.tick(self.FPS) # run with at most FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if self.continue_game and event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mousedown(event)

   def handle_mousedown(self, event): # we are ignoring the event
      self.create_non_overlapping_dots()
      
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.small_dot.draw()
      self.big_dot.draw()
      self.show_score(self.score)
      if not self.continue_game:
         self.show_game_over_message()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      
      self.small_dot.move()
      self.big_dot.move()
      self.score = pygame.time.get_ticks()//1000

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      
      if self.small_dot.collide(self.big_dot):
         self.continue_game = False

   def show_score(self, score):   
      # Show the game score in white 72 font size at the top left corner
      text_string = 'Score:' + str(score)
      location = (0, 0)
      fontsize = 72
      fg_color = 'white'
      bg_color = 'black'
      show_text(self.surface, text_string, location, 
                fontsize, fg_color, bg_color)

   def show_game_over_message(self):
      # show in bottom left corner of the window 
      # in red 96 font size on blue background
      text_string = 'Game Over!'
      fontsize = 96
      fg_color = 'red'
      bg_color = 'blue'
      text_image = create_text_image(text_string, fontsize, 
                                     fg_color, bg_color)
      location = (0, self.surface.get_height() - text_image.get_height())
      self.surface.blit(text_image, location)

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
      
   def collide(self, dot):
      # does self collide with dot?
      centers_distance = distance(self.center, dot.center)
      sum_of_radii = self.radius + dot.radius
      return centers_distance < sum_of_radii

main()