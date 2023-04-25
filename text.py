import pygame
"""
This file will included classes like normal score, high score, timer, lives, etc
"""
class TimerText:
  def __init__(self):
    self.image = pygame.Rect(360, 740, 160, 30)# x, y, width, height
    self.color = (0, 255, 0)
    self.x = self.image.x
    self.y = self.image.y
    self.original_width = self.image.width
    
    
    pass
  
  def draw(self, screen, percentage_scale):
    '''self.image = pygame.transform.scale(self.image, (self.original_width * percentage_scale, 30))'''
    self.image.width = self.original_width * percentage_scale
    # screen.blit(self.image, (self.x, self.y))
    pygame.draw.rect(screen, self.color, self.image)
    pass

  def times_Up(self, percentage_scale):
    """returns boolean that determines in main while loop if game should be stopped"""
    pass

class ScoreText:
  def __init__(self,x_input, y_):
    pass
    
class LivesText:
  def __init__(self, x_input, y_input):
    pass
  
  def draw(self, screen):
    pass

class HighScoreText:
  def __init__(self, x_input, y_input):
    pass
  
  def draw(self, screen):
    pass

class NormalScoreText:
  def __init__(self, x_input, y_input):
    pass
  
  def draw(self, screen):
    pass
