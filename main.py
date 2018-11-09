from menu import Tetris_Menu
from cocos.director import director   


def run(wind_width=800, wind_height=600):
    print("Start Game")
    director.init(width=wind_width, height=wind_height, caption="TETRIS", fullscreen=False)

    main_menu = Tetris_Menu(director)
    director.run(main_menu.scene)

run(800, 600)