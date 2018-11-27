from game_controller import game_controller

def start(): 
    game_controller.init(1024, 600)
    game_controller.run()

start()