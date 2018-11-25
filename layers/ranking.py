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
    def __init__(self, show_menu=False,auto_show=True):
        Layer.__init__(self)
        self.position = (0,0)
        self.anchor = (0,0)

        self.fs = file_saver.File_Saver("rankings.txt") #nome para o arquivo de ranking
        self.rank_dict = {}
        self.load_rank()

        if(show_menu):
            menu = cocos.menu.Menu("GAME OVER")
            menu.font_title["font_name"] = "Tetrominoes"
            menu.font_title["color"] = (214, 178, 152, 255)
            menu.font_item["font_name"] = "Tetrominoes"
            menu.font_item_selected["font_name"] = "Tetrominoes"
            
            menu_items = [
                MenuItem('menu', game_controller.game_controller.close_scene )
            ]
            menu.create_menu( menu_items )
            self.add(menu)

        if(auto_show):
            self.show_rank()

    def save_rank(self):# salva a dicionario de ranks em arquivo
        str_data = ""
        for (score,data) in self.rank_dict.items():
            str_data +=str(score) +"/"+ str(data)+"\n"
        self.fs.writeToFile(str_data)

    def load_rank(self):# le do arquivo e retorna uma dicionario com os rankings
        #TODO
        self.rank_dict = {} 

    def add_rank(self, rank):
        if(type(rank) == dict):
            self.rank_dict = {**self.rank_dict, **rank} # junta os dois dicionarios

            self.reorder_rank() # reordena toda vez que adiciona para garantir que o primeiro sempre eh o maior
            self.save_rank()# salva no arquivo para manter atualizado

    def reorder_rank(self):# reordena o rank de acordo com a pontuacao
        #TODO
        pass

    def show_rank(self):# le o dicionario e preenche os labels com as infomacoes encontradas
        #TODO
        pass


Ranking_dict ={134 : ("caio", "1:10"),515 : ("joao", "1:10")}
#players_data = dict(Ranking_dict.values())
#players_scores = dict(Ranking_dict.keys())
for (score,data) in Ranking_dict.items():
    str(score) +"/"+ str(data)+"\n"