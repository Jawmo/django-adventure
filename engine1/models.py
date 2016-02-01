from django.db import models

class Game(models.Model):
    full_name = models.CharField(max_length=200)
    first_scene = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.full_name

class Scene(models.Model):
    game = models.ForeignKey(Game)
    full_name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    abbrev = models.CharField(max_length=200)
    
    def __str__(self):
        return self.full_name
        
class Path(models.Model):
    game = models.ForeignKey(Game)
    scene = models.ForeignKey(Scene)
    command = models.CharField(max_length=200)
    output = models.CharField(max_length=200)
    
    def __str__(self):
        return self.command + ":" + self.output
