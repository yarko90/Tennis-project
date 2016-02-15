from django.db import models
# Create your models here.
class Player(models.Model):
    GUID=models.CharField(max_length=36)
    name=models.CharField(max_length=100)
    total_games=models.CharField(max_length=3)
    win_rate=models.CharField(max_length=7)
    svoi_podachi=models.CharField(max_length=9)
    chuz_podachi=models.CharField(max_length=9)
    set_rate=models.CharField(max_length=7)
    game_rate=models.CharField(max_length=7)
    break_point=models.CharField(max_length=9)
    def finder (name):
        return Player.name==name
    #def __str__(self):
    #   return self.TotalGames
class Game(models.Model):
    GUID=models.CharField(max_length=36)
    tournament=models.CharField(max_length=100)
    time=models.DateTimeField(max_length=30)
    players=models.CharField(max_length=200)
    coeff=models.CharField(max_length=13)
    result=models.CharField(max_length=30)

