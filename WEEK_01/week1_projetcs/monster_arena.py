# import random 
# import math
# player={'name':input('What is your name? '),'curr_hp':100,'max_hp':100}
# enemy={'name':'Goblin','curr_hp':50,'max_hp':50 }

# def show_stats(player_data, enemy_data):
#     # Use f-strings to inject the values directly into the text
#     print(f"{player_data['name']}: {player_data['curr_hp']}/{player_data['max_hp']} HP")
#     print(f"{enemy_data['name']}: {enemy_data['curr_hp']}/{enemy_data['max_hp']} HP")

# # Call the function
# show_stats(player, enemy)
# while True:
#     player_move=input('1. Attack /n2. Heal /n choose:')
#     if player_move=='1':
#         actual_damage=20
#         enemy['curr_hp']-=actual_damage
#         print(f'goblin current hp is:{enemy['curr_hp']}')
#     enemy_move=random.randint(1,2)
#     if enemy_move==1:
#         actual_damage=20
#         player['curr_hp']-=actual_damage
#         print(f'player current hp is:{player['curr_hp']}')

        

        

"""1. Set up the Dictionaries:
Create two dictionaries, one named player and one named enemy.

Give both of them three keys: 'name', 'hp' (current health), and 'max_hp' (their maximum possible health).

Example: Give yourself 100 hp and the enemy 50 hp.

2. Create a Display Function:
Create a function called show_stats.

Give it two parameters: player_data and enemy_data.

Inside the function, write a couple of print() statements that display both characters' names and their current HP out of their Max HP. (e.g., "Sudarshan: 100/100 HP | Goblin: 50/50 HP")."""


# import random 
# import math 
# player={'name':input('what is your name ?'),'curr_hp':100,'max_hp':100}
# enemy={'name':'Goblin','curr_hp':100,'max_hp':100}

# def show_stats(player_data,enemy_data):
#     print(f"{player_data['name']}: {player_data['curr_hp']}/{player_data['max_hp']}")
#     print(f"{enemy_data['name']}: {enemy_data['curr_hp']}/{enemy_data['max_hp']}")
# show_stats(player,enemy)


# def start_battle():
#     while player['curr_hp']>=0 and enemy['curr_hp']>=0:
#         # show_stats(player, enemy)
#         print('__player turn__')
#         # __players turn__
#         action =input('\n[1] Attack\n[2] Heal\nChoose your action: ')
#         if action=='1':
#             p_dmg=random.randint(10,20)
#             enemy['curr_hp']-=p_dmg
#             print(f'you strike {enemy['name']} with {p_dmg} damage')
#             if enemy['curr_hp']<=0:
#                 print(f'you defeated {enemy['name']}')
#                 break
#         elif action=='2':
#             heal=random.randint(10,30)
#             print(f"you heal yourself for {heal} hp {player['curr_hp']}+={heal}")
#             player['curr_hp'] += heal
#             if player['curr_hp']>player['max_hp']:
#                 player['curr_hp']=player['max_hp']
#         print('__enemy turn__')
#         # __enemies turn__
#         action_e=random.randint(1,2)
#         if action_e==1:
#             e_dmg=random.randint(10,20)
#             player['curr_hp']-=e_dmg
#             print(f'{enemy['name']} strikes you with {e_dmg} damage')   
#         elif action_e==2:
#             heal=random.randint(10,30)
#             enemy['curr_hp']+=heal
#             if enemy['curr_hp']>enemy['max_hp']:
#                 enemy['curr_hp']=enemy['max_hp']
#                 # __check if player died after enemy hit__
#             elif player['curr_hp']<=0:
#                 print(f'{enemy['name']} defeated {player['name']}')
#                 break
# start_battle()
     




import random 

player = {'name': input('What is your name? '), 'curr_hp': 100, 'max_hp': 100}
enemy = {'name': 'Goblin', 'curr_hp': 100, 'max_hp': 100}

def show_stats(player_data, enemy_data):
    # Fixed the quote collisions by using double quotes on the outside
    print(f"\n{player_data['name']}: {player_data['curr_hp']}/{player_data['max_hp']} HP")
    print(f"{enemy_data['name']}: {enemy_data['curr_hp']}/{enemy_data['max_hp']} HP")
    print("-" * 20) # Added a little visual separator

def start_battle():
    while player['curr_hp'] > 0 and enemy['curr_hp'] > 0:
        
        show_stats(player, enemy) # Uncommented so we can see the health!
        
        print('\n__PLAYER TURN__')
        action = input('[1] Attack\n[2] Heal\nChoose your action: ')
        
        if action == '1':
            p_dmg = random.randint(10, 20)
            enemy['curr_hp'] -= p_dmg
            print(f"You strike {enemy['name']} for {p_dmg} damage!")
            
            # Check if enemy died
            if enemy['curr_hp'] <= 0:
                print(f"\n🎉 You defeated the {enemy['name']}! 🎉")
                break
                
        elif action == '2':
            heal = random.randint(10, 30)
            player['curr_hp'] += heal # Fixed: Actually adding the health!
            
            if player['curr_hp'] > player['max_hp']:
                player['curr_hp'] = player['max_hp']
                
            print(f"You drink a potion and heal for {heal} HP!")
            
        else:
            print("Invalid move! You trip and miss your turn.")

        print('\n__ENEMY TURN__')
        action_e = random.randint(1, 2)
        
        if action_e == 1:
            e_dmg = random.randint(10, 20)
            player['curr_hp'] -= e_dmg
            print(f"{enemy['name']} strikes you for {e_dmg} damage!")
            
            # Fixed: Moved the player death check here, right after they take damage!
            if player['curr_hp'] <= 0:
                print(f"\n💀 {enemy['name']} defeated you. GAME OVER. 💀")
                break
                
        elif action_e == 2:
            heal = random.randint(10, 30)
            enemy['curr_hp'] += heal
            
            if enemy['curr_hp'] > enemy['max_hp']:
                enemy['curr_hp'] = enemy['max_hp']
                
            print(f"The {enemy['name']} cowardly heals itself for {heal} HP!")

# Let the battle begin!
start_battle()