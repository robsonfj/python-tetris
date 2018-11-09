from menu_scene import Menu
import pyglet
from cocos.director import director   

pyglet.resource.path = ['assets', 'assets/blocks'] # caminho para imagens e sprites
pyglet.resource.reindex()
pyglet.font.add_file('./assets/tetrominoes.ttf')

def run(wind_width=800, wind_height=600):
    print("Start Game")
    director.init(width=wind_width, height=wind_height, caption="TETRIS", fullscreen=False, resizable=False)

    director.run(Menu())

run(1024, 600)