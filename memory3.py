# Pre-Poke Framework
# Implements a general game template for games with animation
# You must use this template for all your graphical lab assignments
# and you are only allowed to include additional modules that are part of
# the Python Standard Library; no other modules are allowed
import pygame
import time
import random
# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Memory')   
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
      self.board_size = 4
      self.board = []
      self.image_list = []
      self.load_images()
      self.create_board()
      self.score_counter = 0
      self.selected_tiles = []
      self.match_counter = 0


   def load_images(self):
      # load the images from the files and into the image_list
      image_1 = pygame.image.load('image1.bmp')
      self.image_list.append(image_1)
      image_2 = pygame.image.load('image2.bmp')
      self.image_list.append(image_2)
      image_3 = pygame.image.load('image3.bmp')
      self.image_list.append(image_3)
      image_4 = pygame.image.load('image4.bmp')
      self.image_list.append(image_4)
      image_5 = pygame.image.load('image5.bmp')
      self.image_list.append(image_5)
      image_6 = pygame.image.load('image6.bmp')
      self.image_list.append(image_6)
      image_7 = pygame.image.load('image7.bmp')
      self.image_list.append(image_7)
      image_8 = pygame.image.load('image8.bmp')
      self.image_list.append(image_8)
      self.image_list = self.image_list + self.image_list
      random.shuffle(self.image_list)

   def display_score(self):
      score_str = str(self.score_counter)
      font_size = 70
      font = pygame.font.SysFont('', font_size, True)
      fg_color = pygame.Color('white')
      score_board = font.render(score_str, True, fg_color, self.bg_color)
      score_location = (self.surface.get_width() - score_board.get_width(), 0)
      self.surface.blit(score_board, score_location)

   def create_board(self):
      width = 100
      height = 100
      img = 0
      # for each row index
      for row_index in range(0, self.board_size):
         # create row as an empty list
         row = []
         # for each column index
         for col_index in range(0, self.board_size):
            # create tile using row index and column index
            image = self.image_list[img]
            img +=1
            x = col_index * width
            y = row_index * height
            tile = Tile(x, y, width, height, image,self.surface)
            # append tile to row
            row.append(tile)
         # append row to board
         self.board.append(row)

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
         elif event.type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(event)

   def handle_mouse_up(self, event):
      # event.pos is the location of the mouse click
      # Ask each tile if it has been selected
      for row in self.board:
         for tile in row:
            if tile.select(event.pos):
               tile.hidden = False
               self.selected_tiles.append(tile)

   def compare_tiles(self):
      if len(self.selected_tiles) == 2:
         if self.selected_tiles[0].content != self.selected_tiles[1].content:
            time.sleep(0.5)
            self.selected_tiles[0].hidden = True
            self.selected_tiles[1].hidden = True
         else:
            self.match_counter += 1
         self.selected_tiles = []

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      for row in self.board:
         for tile in row:
            tile.draw()
      self.display_score()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      self.score_counter = pygame.time.get_ticks()//1000
      self.compare_tiles()

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      if self.match_counter == 8:
         self.continue_game = False

class Tile:
   # an object of this class represents a Rectangular Tile

   def __init__(self, x, y, width, height, image, surface):
      # Initialize a tile to contain a ' '
      # - x is the int x coord of the upper left corner
      # - y is the int y coord of the upper left corner
      # - width is the int width of the tile
      # - height is the int height of the tile
      # - surface is pygame.Surface object on which a Tile object is drawn on

      self.rect = pygame.Rect(x, y, width, height)
      self.surface = surface
      self.color = pygame.Color('white')
      self.border_width = 3
      self.hidden_image = pygame.image.load('image0.bmp')
      self.hidden = True
      self.content = image

   def select(self,pos):
      if self.rect.collidepoint(pos):
         return True
      else:
         return False

# maybe change this a bit
   def draw(self):
      # draws a Tile object
      # -self is the Tile object to draw
      location = (self.rect.x, self.rect.y)
      if self.hidden:
         self.surface.blit(self.hidden_image, location)
      else:
         self.surface.blit(self.content, location)
      pygame.draw.rect(self.surface, self.color, self.rect, self.border_width)

# can keep this it is from tic tac toe
   def draw_content(self):
      font = pygame.font.SysFont('', 133)  # height of the surface is 400 //3 = 133
      text_box = font.render(self.content, True, self.color)
      # text_box is a pygame.Surface object - get the rectangle from the surface
      rect1 = text_box.get_rect()
      # rect1  <---->  self.rect
      rect1.center = self.rect.center
      location = (rect1.x, rect1.y)
      self.surface.blit(text_box, location)

main()