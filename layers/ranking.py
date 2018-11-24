from cocos.layer import Layer



Ranking_list ={"caio" : 134,"joao" : 135}
Ranking_list.update({"player_name" : "Player_score"})
players_names = list(Ranking_list.keys())[0]
players_scores = list(Ranking_list.values())[0]
print(players_scores)