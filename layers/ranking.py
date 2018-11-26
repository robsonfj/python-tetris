import cocos
import pyglet
from cocos.director import director
from cocos.layer import Layer
from cocos.text import Label
from cocos.layer import MultiplexLayer
from cocos.layer import ColorLayer
from cocos.menu import Menu
from cocos.menu import MenuItem
from cocos.menu import EntryMenuItem
from cocos.sprite import Sprite
#local libs
import file_saver
import game_controller

''' 
Rank contem um dicionario com as chaves os scores 
e valor uma tupla com o nome do usuario e o tempo de jogo
'''
class Ranking(Layer):
    def __init__(self, is_game_over=False):
        Layer.__init__(self)
        self.position = (0,0)
        self.anchor = (0,0)

        self.fs = file_saver.File_Saver("rankings.txt") #nome para o arquivo de ranking
        self.rank_dict = {}
        
        
        menu = Menu("")
        menu_items = []

        item = MenuItem('Voltar', self.on_quit)
        menu_items.append(item)
        item.position = ( 0, -220)
        if(is_game_over):
            menu.title = "GAME OVER"
            black_lyr = ColorLayer(0, 0, 0,0)
            self.add(black_lyr)
            black_lyr.width = int(director.window.width)
            black_lyr.height = int(director.window.height)
            black_lyr.position = (0, 0)
            black_lyr.opacity = 120
            self.player_name = "Player"
            input_item = EntryMenuItem('Nome:', self.on_text, "", 6)
            menu_items.append(input_item)
            input_item.position = ( 0, -90)

        else:
            menu.title = "RANKING"
        

        menu.font_title["font_name"] = "Tetrominoes"
        menu.font_title["color"] = (214, 178, 152, 255)
        menu.font_item["font_name"] = "Ravie"
        menu.font_item["font_size"] = 22
        menu.font_item_selected["font_name"] = "Ravie"
        menu.font_item_selected["font_size"] = 22

        
        menu.create_menu( menu_items )
        menu.on_quit = self.on_quit
        self.add(menu)


    def save_rank(self):# salva a dicionario de ranks em arquivo
        str_data = ""
        for (score,data) in self.rank_dict.items():
            str_data +=str(score) +"/"+ str(data)+"\n"
        self.fs.writeToFile(str_data)


    def load_rank(self):# le a lista de strings obtidas do arquivo e preenche o dicionario com os rankings
        try:
            list_data = self.fs.readFile()
            for data in list_data:
                splited = data.split("/")
                tmp = splited[1].replace("(","")
                tmp = tmp.replace(")","")
                tmp = tmp.replace("\n","")
                tmp = tmp.replace("'","")
                splited[1]= tmp.split(",")
                self.rank_dict[int(splited[0])] = (splited[1][0],splited[1][1])

        except Exception as e:
            print("Error! Ranking load_rank -",e)


    def add_rank(self, rank):
        if(type(rank) == dict):
            self.rank_dict = {**self.rank_dict, **rank} # junta os dois dicionarios

            self.reorder_rank() # reordena toda vez que adiciona para garantir que o primeiro sempre eh o maior
            self.save_rank()# salva no arquivo para manter atualizado

    def reorder_rank(self):# reordena o rank de acordo com a pontuacao
        ordered_list = sorted(self.rank_dict, reverse=True)
        old = self.rank_dict
        new = {}
        for i in ordered_list:
            new[i] = old[i]

        self.rank_dict = new

    def show_rank(self):# le o dicionario e preenche os labels com as infomacoes encontradas
        self.load_rank()
        self.add(Sprite(image=pyglet.resource.image('rank.png') , position=(director.window.width/2,50+director.window.height/2)))# rank template
        count = 0
        for (key, (name, time)) in self.rank_dict.items():
            lbn = Label(name, (315,405 - count*45), font_size = 14, font_name = "Ravie", align = "center",anchor_x = "left", color= (0, 0, 0, 255))
            lbs = Label(str(key), (510,405 - count*45), font_size = 14, font_name = "Ravie", align = "center",anchor_x = "center", color= (0, 0, 0, 255))
            lbt = Label(time, (680,405 - count*45), font_size = 14, font_name = "Ravie", align = "center",anchor_x = "center", color= (0, 0, 0, 255))
            
            self.add(lbn)
            self.add(lbs)
            self.add(lbt)
            count += 1
            if(count > 4):# sai depois de adicionar 5 dados no rank
                break

    def on_text(self, text):
        self.player_name = text

    def on_quit(self):# ao pressionar ESC executa este metodo
        if(type(self.parent) == MultiplexLayer):
            self.parent.parent.on_rank_exit()
        elif(type(self.parent) == Layer):
            self.parent.remove(self)