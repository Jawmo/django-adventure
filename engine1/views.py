from django.shortcuts import render
from .models import Game, Scene, Path

def index(request):

    boxes = Game.objects.all()
    return render(request, 'engine1/index.html', {'game_list' : boxes})

def game(request, game_name):    
   
    if request.method == 'POST': 
        current_room = request.POST.get('scene_name', None)
        s = Scene.objects.get(abbrev = current_room) 
        in_dir = request.POST.get('textfield', None)
        
        try: 
            """Let's be sure that the direction input is a valid 
            command that is available in this scene. If not, throw 
            an error and redisplay the page."""
            move = s.path_set.get(command = in_dir)
            
        except (KeyError, Path.DoesNotExist):
            return render(request, 'engine1/game.html', {
                'box' : s,
                'error_message': 'Please enter a valid direction.'
            })
            
        else:
            new_box = Scene.objects.get(abbrev = move.output)
            return render(request, 'engine1/game.html', {'box' : new_box}) 
            
    else: 
        game = Game.objects.get(full_name = game_name)
        scene_one = Scene.objects.get(abbrev = game.first_scene)
        return render(request, 'engine1/game.html', {'box' : scene_one})     
