from resources.text_resources import *
from entities.hero import Hero
from entities.enemy import Enemy
import random
import sys

logo_menu()
option = input()
if option == "1":
    # initial_history()
    name = input("Nome do seu herói? \n")
    hero = Hero(name)
    # pega os atributos do heroi em caso de bonus
    initial_life,initial_attack,initial_defense = hero.get_Life(), hero.get_Attack(), hero.get_Defense()
    progress = 0
    while progress <= 20 and hero.get_Life() > 0:
        option = random.choice(["Livre", "Combate"])
        if option == "Combate":
            enemy = Enemy()
            enemy_initial_life,enemy_initial_attack,enemy_initial_defense = enemy.get_Life(), enemy.get_Attack(), enemy.get_Defense()
            end_battle = False
            print(f"Você encontrou um {enemy.get_enemy()}\n")
            while hero.get_Life() > 0 and enemy.get_Life() > 0 and not end_battle:
                print(f"{hero.get_name()} - Vida: {hero.get_Life()}")
                print(f"{enemy.get_enemy()} - Vida: {enemy.get_Life()}\n")
                action = input("Qual sua ação: [1] Atacar [2] Defender [3] Fugir\n ")
                enemy_action = None                
                if action == "1":
                    print()
                    hero.make_attack(enemy)
                elif action == "2":
                    print("Você se defende nessa rodada e aumenta sua defesa em 30%\n")
                    hero.set_Defense(hero.get_Defense() + hero.get_Defense() * 0.3)
                elif action == "3":
                    print("Você fugiu da Batalha\n")
                    end_battle = True
                if enemy.get_Life() > 0:
                    enemy_action = random.choice(["1", "2"])
                    if enemy_action == "1":
                        enemy.make_attack(hero)
                    elif enemy_action == "2":
                        print("O inimigo se defende nessa rodada e aumenta sua defesa em 30%\n")
                        enemy.set_Defense(enemy.get_Defense() + enemy.get_Defense() * 0.3)
                else:
                    print(f"Você derrotou {enemy.get_enemy()}\n")
                    end_battle = True
                if action == "2":
                    hero.set_Defense(initial_defense)
                if enemy_action == "2":
                    enemy.set_Defense(enemy_initial_defense)
            if hero.get_Life() <= 0:
                sys.exit("Você morreu, game over")  
            progress+=1
        if option == "Livre":
            print("Você segue o caminho sem perigos\n")
            progress+=1
if option == "2":
    print("Options not supported in this version :(")
if option == "3":
    sys.exit("Leaving the game, see you later :)")
