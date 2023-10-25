# this program runs the game Pong where a ball goes back and forth and players control paddles and attempt to prevent the ball from hitting their side

import pygame


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Pong')   
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
      self.ball = Ball('white', 5, [250, 200], [5, 1.5], self.surface)
      self.left_paddle = Paddle(100, 175, 10, 50, 'white', self.surface)
      self.right_paddle = Paddle(400, 175, 10, 50, 'white', self.surface)
      self.paddle_speed = 10
      self.left_score = 0
      self.right_score = 0
      self.max_score = 11


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
            self.handle_keydown(event)
         elif event.type == pygame.KEYUP:
            self.handle_keyup(event)
            
   def handle_keydown(self, event):
      # handles the user pressing down a key
      # - self is the Game who the key creates an action in
      # - event is an EventType object from pygame that is used to determine key down events
      
      if event.key == pygame.K_q:
         self.left_paddle.get_speed(-self.paddle_speed)
      elif event.key == pygame.K_a:
         self.left_paddle.get_speed(self.paddle_speed)
      if event.key == pygame.K_p:
         self.right_paddle.get_speed(-self.paddle_speed)
      elif event.key == pygame.K_l:
         self.right_paddle.get_speed(self.paddle_speed)
   
   def handle_keyup(self, event):
      # handles the user releasing a key
      # - self is the Game who the key creates an action in
      # - event is an EventType object from pygame that is used to determine key up events      
      
      if event.key == pygame.K_q or event.key == pygame.K_a:
         self.left_paddle.get_speed(0)
      if event.key == pygame.K_p or event.key == pygame.K_l:
         self.right_paddle.get_speed(0)      

   def collide(self):
      # determines if the ball has collided with either of the paddles and if so reverses the horizontal direction of the ball
      # - self is type Game which the paddles and ball are present in
      
      if self.left_paddle.get_rect().collidepoint(self.ball.get_center()) and self.ball.get_velocity()[0] < 0:
         self.ball.bounce()
      if self.right_paddle.get_rect().collidepoint(self.ball.get_center()) and self.ball.get_velocity()[0] > 0:
         self.ball.bounce()      

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.ball.draw()
      self.left_paddle.draw()
      self.right_paddle.draw()
      self.draw_score()
      pygame.display.update() # make the updated surface appear on the display
      
   def draw_score(self):
      # draws the scores for both players in the top corners
      # - self is the Game in which the scores are drawn
      
      left_score_string = str(self.left_score)
      right_score_string = str(self.right_score)
      font_size = 80
      font = pygame.font.SysFont('', font_size, True)
      fg_color = pygame.Color('white')
      left_text_box = font.render(left_score_string, True, fg_color, self.bg_color)
      right_text_box = font.render(right_score_string, True, fg_color, self.bg_color)
      left_location = (0,0)
      right_location = (self.surface.get_width() - right_text_box.get_width(), 0)
      self.surface.blit(left_text_box, left_location)
      self.surface.blit(right_text_box, right_location)
      

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      
      self.ball.move()
      self.left_paddle.move()
      self.right_paddle.move()
      self.collide()
      self.set_score()
      
   def set_score(self):
      # updates the scores of each player
      # - self is the Game in which the scores are updated
      
      if self.ball.get_center()[0] + self.ball.get_radius() > self.surface.get_width():
         self.left_score += 1
      if self.ball.get_center()[0] < self.ball.get_radius():
         self.right_score += 1      

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      
      if self.left_score >= self.max_score or self.right_score >= self.max_score:
         self.continue_game = False
 
class Ball:
   # An object in this class represents a Dot that moves 
   
   def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
      # Initialize a Ball.
      # - self is the Ball to initialize
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
      # - self is the Ball being moved
      
      size = self.surface.get_size()
      for i in range(0,2):
         self.center[i] += self.velocity[i]
         if self.center[i] < self.radius:
            self.velocity[i] *= -1
         if self.center[i] + self.radius > size[i]:
            self.velocity[i] *= -1   
            
   def bounce(self):
      # reverses the horizontal direction of the ball
      # - self is the Ball which is being reversed
      
      self.velocity[0] *= -1
   
   def get_center(self):
      # gets the value of the center coordinates of the ball
      # - self is the Ball whose coordinates are found
      
      return self.center
   
   def get_radius(self):
      # gets the radius of the ball
      # - self is the Ball whose radius is found
      
      return self.radius
   
   def get_velocity(self):
      # gets the velocity of the ball
      # - self is the Ball whose velocity is being taken
      
      return self.velocity
   
   def draw(self):
      # Draw the dot on the surface
      # - self is the Ball being drawn
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)
      
class Paddle:
   def __init__(self, left, top, width, height, color, surface):
      # initialize a paddle object
      # - self is the Paddle object
      # - left is an int that is the left most coordinate of the Paddle
      # - top is an int that is the top most coordinate of the Paddle
      # - height is an int that is the height of the Paddle
      # - width is an int that is the width of the Paddle
      # - color is the pygame.Color of the Paddle
      # - surface is the surface that the Paddle is drawn on
      
      self.rect = pygame.Rect(left, top, width, height)
      self.color = pygame.Color(color)
      self.surface = surface
      self.velocity = 0
   
   def draw(self):
      # draws the rectangle on the surface
      # - self is type Paddle that is drawn
      
      pygame.draw.rect(self.surface, self.color, self.rect)
      
   def get_speed(self, paddle_speed):
      # sets the speed at which the paddle moves
      #  - paddle_speed is an int that determines how much the paddle moves
      
      self.velocity = paddle_speed
   
   def move(self):
      # moves the paddle and prevents the paddle from going off screen
      # - self is type Paddle that is being moved
      
      self.rect.move_ip(0, self.velocity)
      if self.rect.top <= 0:
         self.rect.top = 0
      if self.rect.bottom >= self.surface.get_height():
         self.rect.bottom = self.surface.get_height()
         
   def get_coords(self):
      # gets the coordinates of the Paddle
      # - self is type Paddle that the coordinates are apart of
      
      return (self.rect.left, self.rect.right, self.rect.top, self.rect.bottom)
   
   def get_rect(self):
      # returns the rectangle object of the Paddle
      # - self is type Paddle that the rectangle is being retrieved from
      
      return self.rect


main()