# snake - ladder game
import random
import pandas as pd

def roll_dice():
    return random.randint(1,6)

def start_game(grid_size,num_players):
    win_pos= grid_size*grid_size
    
    positions = {f"Player {i}":0 for i in range(1,num_players+1)}

    winner = 0
    game_history = {}
    dice_roll_history={}
    position_history = {}
    
    while not winner:
        
        for player in positions:

            dice_out = roll_dice()

            old_pos = positions[player]
            new_pos = old_pos+dice_out
            
            if new_pos>win_pos:
                new_pos=old_pos

            positions[player] = new_pos

            player_dices_history =dice_roll_history.get(player,[])
            player_dices_history.append(dice_out)
            dice_roll_history[player]=player_dices_history

            player_positio_history =position_history.get(player,[])
            player_positio_history.append(new_pos)
            position_history[player]=player_positio_history

            winner = 1 if new_pos==win_pos else 0
            
            game_history[player]= {
                    "Players":player,
                    "Dice Roll History":player_dices_history,
                    "Position History":player_positio_history,
                    "Win Status":winner


                }
            
            
            if winner:
                break
    
    return game_history



grid_size = int(input("Enter grid size: "))
num_players = int(input("Enter number of players: "))
result = start_game(grid_size,num_players)

data = pd.DataFrame(result.values())
print(data)

