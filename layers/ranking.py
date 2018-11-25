import cocos
from cocos.layer import Layer
from cocos.menu import MenuItem
import file_saver
import game_controller

''' 
Rank contem um dicionario com as chaves os scores 
e valor uma tupla com o nome do usuario e o tempo de jogo
'''
class Ranking(Layer):
    def __init__(self):
        self.fs = file_saver.File_Saver("rankings.txt")

        self.rank_list = {}
        self.load_rank()

        menu = cocos.menu.Menu("GAME OVER")
        menu.font_title["font_name"] = "Tetrominoes"
        menu.font_title["color"] = (214, 178, 152, 255)
        menu.font_item["font_name"] = "Tetrominoes"
        menu.font_item_selected["font_name"] = "Tetrominoes"
        
        menu_items = [
            MenuItem('menu', game_controller.game_controller.close_scene )
        ]

    def save_rank(self):# salva a lista de ranks em arquivo
        str_data = ""
        for (score,data) in self.rank_list.items():
            str_data +=str(score) +"/"+ str(data)+"\\n"
        self.fs.writeToFile(str_data)

    def load_rank(self):# le do arquivo e retorna uma lista com os rankings
        #TODO
        self.rank_list = {} 

    def reorder_rank(self):# reordena o rank de acordo com a pontuacao
        #TODO
        pass



Ranking_list ={134 : ("caio", "1:10"),515 : ("joao", "1:10")}
players_data = list(Ranking_list.values())
players_scores = list(Ranking_list.keys())
print(players_scores)
print(players_data)
for (score,data) in Ranking_list.items():
    str(score) +"/"+ str(data)+"\\n"