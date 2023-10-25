# This example demonstrates moving of a rectangle 
# press r key to move the green rectangle to the right edge of the window
# press l key to move the green rectangle to the left edge of the window
import pygame,random,math

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
      self.paddle_increment = 10
      self.paddle = Paddle(100,150,10,50,'white',self.surface)
      
                    
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
         elif event.type == pygame.KEYDOWN:
            self.handle_key_down(event)
         elif event.type == pygame.KEYUP:
            self.handle_key_up(event)
   def handle_key_down(self,event):
      # reponds to KEYDOWN event
      # - self is the Game object
      if event.key == pygame.K_r:
         self.paddle.set_horizontal_velocity(self.paddle_increment)
      elif event.key == pygame.K_l:
         self.paddle.set_horizontal_velocity(-self.paddle_increment)
   
   def handle_key_up(self,event):
      # responds to KEYUP event
      # - self is the Game object
      if event.key == pygame.K_r:
         self.paddle.set_horizontal_velocity(0)
      elif event.key == pygame.K_l:
         self.paddle.set_horizontal_velocity(0)         

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.paddle.draw()
      pygame.display.update() # make the updated surface appear on the display
   
   
   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      self.paddle.move()
      
   
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      pass
   
class Paddle:
   # An object in this class represents a Paddle that moves
   
   def __init__(self,x,y,width,height,color,surface):
      # - self is the Paddle object
      # - x, y are the top left corner coordinates of the rectangle of type int
      # - width is the width of the rectangle of type int
      # - height is the heightof the rectangle of type int
      # - surface is the pygame.Surface object on which the rectangle is drawn
      
      self.rect = pygame.Rect(x,y,width,height)
      self.color = pygame.Color(color)
      self.surface = surface
      self.horizontal_velocity = 0  # paddle is not moving at the start
   def draw(self):
      # -self is the Paddle object to draw
      pygame.draw.rect(self.surface,self.color,self.rect)
   def set_horizontal_velocity(self,horizontal_distance):
      # set the horizontal velocity of the Paddle object
      # -self is the Paddle object
      # -horizontal_distance is the int increment by which the paddle moves horizontally
      self.horizontal_velocity = horizontal_distance
   def move(self):
      # moves the paddle such that paddle does not move outside the window
      # - self is the Paddle object
      self.rect.move_ip(self.horizontal_velocity,0)
      if self.rect.right >= self.surface.get_width():
         self.rect.right = self.surface.get_width()
      elif self.rect.left  <= 0:
         self.rect.left = 0
      
      

main()