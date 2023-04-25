import pygame
from pygame.math import Vector2
#-**import pygame
from constants import SQUARE_SIZE, FPS, LOG_SKIN_SPRITES, LOG_SKINS, VECHILE_SKIN_SPRITES, VECHILE_SKINS, DEBUG_TOGGLE, LEFT, RIGHT
"""
File for the classes: Vehicle, Jogger, Log, Turtle 
"""


# [(X, Y), Amount In Group , Direction, Speed, Sprite, Time difference between spawns, Time for a new group to spawn]
VEHICLES = [
  [Vector2(600,640), 3, LEFT, SQUARE_SIZE * .04,VECHILE_SKINS.BASIC_1, 4 * FPS, 6 * FPS], # race_car1
  [Vector2(-40,600), 3, RIGHT, SQUARE_SIZE * .03,VECHILE_SKINS.TRACTOR, 4 * FPS, 8 * FPS], # tractor # 0.02
  [Vector2(600, 560), 3, LEFT, SQUARE_SIZE * .03,VECHILE_SKINS.SPACESHIP, 4 * FPS, 8 * FPS], # space_ship # 0.019
  [Vector2(-40,520), 3, RIGHT, SQUARE_SIZE * .08,VECHILE_SKINS.WHITE, 4 * FPS, 8 * FPS], # race_car2 
  [Vector2(600, 480), 3, LEFT, SQUARE_SIZE * .06,VECHILE_SKINS.BASIC_2, 4 * FPS, 8 * FPS], # truck
  [Vector2(600, 440), 3, LEFT, SQUARE_SIZE *.03,VECHILE_SKINS.PINK , 4 * FPS, 8 * FPS] 
  # normal_car
]
# list size 5 including 0
"""
Lane 7 is log - individual
Lane 6 turtle
Lane 5 is log - group
Lane 4 is turtle
Lane 3 is log - individual
Lane 2 is log - group
Lane 1 is turtle 
"""
LOGS = [
  [Vector2(-40, 280), 2, RIGHT, SQUARE_SIZE * .05,LOG_SKINS.BASIC, 0, 5 * FPS], # space_ship # 0.019
  [Vector2(-40, 240), 1, RIGHT, SQUARE_SIZE * .03,LOG_SKINS.BASIC, 0, 6 * FPS], # race_car2 
  [Vector2(-40, 160), 1, RIGHT, SQUARE_SIZE * .06,LOG_SKINS.BASIC, 0, 6 * FPS], # truck
  [Vector2(-40, 80), 3, RIGHT, SQUARE_SIZE *.03, LOG_SKINS.BASIC, 4 * FPS, 8 * FPS] # normal_car
]
#list size three including 0

TURTLES = [
  [Vector2(600,320), 3, LEFT, SQUARE_SIZE * .06, pygame.image.load("Turtle/Turtle_sample.png"), .3 * FPS, 2* FPS], #turtle lane 1
  [Vector2(600,200), 3, LEFT, SQUARE_SIZE * .03, pygame.image.load("Turtle/Turtle_sample.png"), .3 * FPS, 2.5 * FPS], #turtle lane 2
  [Vector2(600, 120), 3, LEFT, SQUARE_SIZE * .03, pygame.image.load("Turtle/Turtle_sample.png"),  .3 * FPS, 3 * FPS], #turtle lane 1
#list size 2 including 0 
]




#the spaceship and truck are same speeed
#race_car1 race_car2, normal_car and space_ship are same speed
"""*element 0 = x coordinate
     element 1 = y coordinate
   element 2 = vehicle amount
   element 3 = direction
   element 4 = speed val
   elemenent 5 = png name to draw
   element 6 = amount of time between cars
   element 7 = amoutn of time between groups of car
   """ 
class MovingObject(pygame.sprite.Sprite):
    def __init__(self, properties, lane_num):
        super().__init__()

        pos = properties[0]
        # Sets the position
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        # Direction it should be moving
        self.direction = properties[2]

        # Speed at which the object moves
        self.speed = properties[3]

        # Lane its present in
        self.lane_num = lane_num

    def movement(self):
        direction = 1 if self.direction else -1
        self.rect.x += self.speed * direction

        if DEBUG_TOGGLE and (self.lane_num == 1 or self.lane_num == 2):
            print("Coords: " + str(self.rect.x) + ", " + str(self.rect.y))
            print("Speed: " + str(self.speed))

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # This should be overridden by anything that can be hitchhiked
    def can_hitchhike(self):
        return False

class Vehicle(MovingObject):
  def __init__(self, lane_num):
    vehicle_properties = VEHICLES[lane_num]
    
    self.image = VECHILE_SKIN_SPRITES[vehicle_properties[4]]
    self.rect = self.image.get_rect()

    super().__init__(vehicle_properties, lane_num)

class Jogger:
  def __init__(self, x_input, y_input):
    self.x = x_input
    self.y = y_input
  
  def draw(self, screen):
    pass # Code will go here

class Turtle(MovingObject):
  def __init__(self, lane_num):
    
    turtle_properties = TURTLES[lane_num]

    # Variables for animation
    self.current_anim = 0
    self.anim_counter = 0

    self.skin = turtle_properties[5]

    # At some point we need to add the other parts to the turtle animation - Moth
    self.image_list = ["Turtle/Turtle_sample.png", "Turtle/Turtle_sample.png", "Turtle/Turtle_sample.png"]
    self.image = pygame.image.load(self.image_list[self.current_anim])
    self.rect = self.image.get_rect()

    super().__init__(TURTLES[lane_num], lane_num)
    #self.image.set_colorkey((255, 255, 255)) # RGB for white
    #self.image = pygame.image.load("Vehicle_skin/Tractor_2main.png")
  
  def draw(self, screen):
    # Updates the animation frames
    self.anim_counter += 1
    if self.anim_counter >= 20:
      self.current_anim += 1
      self.anim_counter = 0

      if self.current_anim == len(self.image_list):
        self.current_anim = 0
    
    super().draw(screen)

  def can_hitchhike(self):
    return True

class Log(MovingObject):
  def __init__(self, lane_num):
    log_properties = LOGS[lane_num]
    
    self.image = LOG_SKIN_SPRITES[log_properties[4]]

    self.rect = self.image.get_rect()

    super().__init__(LOGS[lane_num], lane_num)
    #self.image.set_colorkey((255, 255, 255)) # RGB for white
    #self.image = pygame.image.load("Vehicle_skin/Tractor_2main.png")

  def can_hitchhike(self):
    return True

class Snake:
  
  def __init__(self, x_input, y_input):
    super().__init__()
    self.x = x_input
    self.y = y_input
    
  def draw(self, screen):
    pass


    

