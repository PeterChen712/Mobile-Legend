import pygame
import time
import random
from abc import ABC, abstractclassmethod
from classnya import Layla, Miya, Fanny, Yin, Uranus, Belerick, Sun, Martis, Estes, Gord


class TextColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


''' BATAS CLASS '''


def status_player_1(pemain_1):
    print("-"*100)
    print(f"{'Status player 1'.center(100)}")
    print(f"Build       : {pemain_1.getBuild()}")
    print(f"Health      : {pemain_1.getHealth()}")
    print(f"Power       : {pemain_1.getPower()}")
    print(f"Magic       : {pemain_1.getMagic()}")
    print(f"Armor       : {pemain_1.getArmor()}")
    print(f"Mana        : {pemain_1.getMana()}")

def status_player_2(pemain_2):
    print("-"*100)
    print(f"{'Status player 2'.center(100)}")
    print(f"Build       : {pemain_2.getBuild()}")
    print(f"Health      : {pemain_2.getHealth()}")
    print(f"Power       : {pemain_2.getPower()}")
    print(f"Magic       : {pemain_2.getMagic()}")
    print(f"Armor       : {pemain_2.getArmor()}")
    print(f"Mana        : {pemain_2.getMana()}")

def status_com_1(pemain_1):
    print("-"*100)
    print(f"{'Status Computer 1'.center(100)}")
    print(f"Build       : {pemain_1.getBuild()}")
    print(f"Health      : {pemain_1.getHealth()}")
    print(f"Power       : {pemain_1.getPower()}")
    print(f"Magic       : {pemain_1.getMagic()}")
    print(f"Armor       : {pemain_1.getArmor()}")
    print(f"Mana        : {pemain_1.getMana()}")

def status_com_2(pemain_2):
    print("-"*100)
    print(f"{'Status Computer 2'.center(100)}")
    print(f"Build       : {pemain_2.getBuild()}")
    print(f"Health      : {pemain_2.getHealth()}")
    print(f"Power       : {pemain_2.getPower()}")
    print(f"Magic       : {pemain_2.getMagic()}")
    print(f"Armor       : {pemain_2.getArmor()}")
    print(f"Mana        : {pemain_2.getMana()}")

def status_com(pemain_2):
    print("-"*100)
    print(f"{'Status Computer'.center(100)}")
    print(f"Build       : {pemain_2.getBuild()}")
    print(f"Health      : {pemain_2.getHealth()}")
    print(f"Power       : {pemain_2.getPower()}")
    print(f"Magic       : {pemain_2.getMagic()}")
    print(f"Armor       : {pemain_2.getArmor()}")
    print(f"Mana        : {pemain_2.getMana()}")



def cek_p1(pemain_1):
    print("-"*100)
    print(f"{'Cek Player 1'.center(98)}")
    print(f"Hero              : {pemain_1.getName()}")
    print(f"Sisa nyawa        : {pemain_1.getHealth()}")
    print(f"Sisa armor        : {pemain_1.getArmor()}")
    print(f"Sisa mana         : {pemain_1.getMana()}")
    print("-"*100)

def cek_p2(pemain_2):
    print("-"*100)
    print(f"{'Cek Player 2'.center(98)}")
    print(f"Hero              : {pemain_2.getName()}")
    print(f"Sisa nyawa        : {pemain_2.getHealth()}")
    print(f"Sisa armor        : {pemain_2.getArmor()}")
    print(f"Sisa mana         : {pemain_2.getMana()}")
    print("-"*100)

def cek_com1(pemain_1):
    print("-"*100)
    print(f"{'Cek Computer 1'.center(98)}")
    print(f"Hero              : {pemain_1.getName()}")
    print(f"Sisa nyawa        : {pemain_1.getHealth()}")
    print(f"Sisa armor        : {pemain_1.getArmor()}")
    print(f"Sisa mana         : {pemain_1.getMana()}")
    print("-"*100)

def cek_com2(pemain_2):
    print("-"*100)
    print(f"{'Cek Computer 2'.center(98)}")
    print(f"Hero              : {pemain_2.getName()}")
    print(f"Sisa nyawa        : {pemain_2.getHealth()}")
    print(f"Sisa armor        : {pemain_2.getArmor()}")
    print(f"Sisa mana         : {pemain_2.getMana()}")
    print("-"*100)

def cek_com(pemain_2):
    print("-"*100)
    print(f"{'Cek Computer'.center(98)}")
    print(f"Hero              : {pemain_2.getName()}")
    print(f"Sisa nyawa        : {pemain_2.getHealth()}")
    print(f"Sisa armor        : {pemain_2.getArmor()}")
    print(f"Sisa mana         : {pemain_2.getMana()}")
    print("-"*100)

list_hero = ["Layla", "Miya", "Fanny", "Yin", "Uranus", "Belerick", "Sun", "Martis", "Estes", "Gord"]

def Audio(path_audio):
    pygame.mixer.init()
    pygame.mixer.music.load(path_audio)
    pygame.mixer.music.play()

def daftar_Hero():
    print("Berikut daftar hero Python Legend : ")
    for i, hero in enumerate(list_hero, start=1):
        print(f"{i}. {hero}")

def Banned():
    while True:
        # print('-'*100)
        Audio("Audio\Announcer\DraftPIck\Announcer.draftpick01.ogg.ogx")
        time.sleep(2)
        ban = input("Please ban a hero : ")
        urutan = ['1','2','3','4','5','6','7','8','9','10']
        if ban in urutan:
            if ban == '1':
                if "Layla" not in list_hero:
                    print("Hero sudah diban")
                else:
                    list_hero[0] = (" ")
                    break
            elif ban == '2':
                if "Miya" not in list_hero:
                    print("Hero sudah diban")
                else:
                    list_hero[1] = (" ")
                    break
            elif ban == '3':
                if "Fanny" not in list_hero:
                    print("Hero sudah diban")
                else:
                    list_hero[2] = (" ")
                    break
            elif ban == '4':
                if "Yin" not in list_hero:
                    print("Hero sudah diban")
                else:
                    list_hero[3] = (" ")
                    break
            elif ban == '5':
                if "Uranus" not in list_hero:
                    print("Hero sudah diban")
                else:
                    list_hero[4] = (" ")
                    break
            elif ban == '6':
                if "Belerick" not in list_hero:
                    print("Hero sudah diban")
                else:
                    list_hero[5] = (" ")
                    break
            elif ban == '7':
                if "Sun" not in list_hero:
                    print("Hero sudah diban")
                else:
                    list_hero[6] = (" ")
                    break
            elif ban == '8':
                if "Martis" not in list_hero:
                    print("Hero sudah diban")
                else:
                    list_hero[7] = (" ")
                    break
            elif ban == '9':
                if "Estes" not in list_hero:
                    print("Hero sudah diban")
                else:
                    list_hero[8] = (" ")
                    break
            elif ban == '10':
                if "Gord" not in list_hero:
                    print("Hero sudah diban")
                else:
                    list_hero[9] = (" ")
                    break
        else:
            print("Mohon masukkan pilihan yang benar")

def pick(p1, p2, pick_hero):
    pick_hero.clear()
    print("Daftar hero :")
    for i, hero in enumerate(list_hero, start=1):
        print(f"{i}. {hero}")
    print('-'*100)

    print(f"{p1}'s turn")
    cek = True
    while True:
        if cek == False:
            break
        Audio("Audio\Announcer\DraftPIck\Announcer.draftpick02.ogg.ogx")
        time.sleep(2)
        pick1 = input("Please pick a hero : ")
        if pick1 == "1":
            picking = "Layla"
        elif pick1 == "2":
            picking = "Miya"
        elif pick1 == "3":
            picking = "Fanny"
        elif pick1 == "4":
            picking = "Yin"
        elif pick1 == "5":
            picking = "Uranus"
        elif pick1 == "6":
            picking = "Belerick"
        elif pick1 == "7":
            picking = "Sun"
        elif pick1 == "8":
            picking = "Martis"
        elif pick1 == "9":
            picking = "Estes"
        elif pick1 == "10":
            picking = "Gord"
        
        while True:
            optional = input(f"Are you sure want to pick {picking}? (yes/no): ").lower()
            if optional == 'yes':
                pick_hero.append(picking)
                if picking == "Layla":
                    print("Layla : Ready, Go!")
                    Audio("Audio\Layla\Audio181-select.ogg.ogx")
                    time.sleep(2)
                elif picking == "Miya":
                    print("Miya : I am the moonlight that breaks through the darkness")
                    Audio("Audio\Miya\Audio011-v2-select.ogg.ogx")
                    time.sleep(3)
                elif picking == "Fanny":
                    print("Fanny : Sir, what's your command?")
                    Audio("Audio\Fanny\Fanny.new.select.ogg.ogx")
                    time.sleep(2)
                elif picking == "Yin":
                    print("Yin : I am Yin, and always will be — no matter what")
                    Audio("Audio\Yin\Yin.select.ogg.ogx")
                    time.sleep(4)
                elif picking == "Uranus":
                    print("Uranus : Hmm... Uranus has awakened")
                    Audio("Audio/Uranus/Uranus.select.ogg.ogx")
                    time.sleep(5)
                elif picking == "Belerick":
                    print("Belerick : Mighty oaks from little acorns grow")
                    Audio("Audio\Belerick\Belerick.new.select.ogg.ogx")
                    time.sleep(4)
                elif picking == "Sun":
                    print("Sun : I hope they're stronger than me")
                    Audio("Audio\Sun\Sun.select.ogg.ogx")
                    time.sleep(2)
                elif picking == "Martis":
                    print("Martis : [laughs] Three thousand worlds, and not a single worthy foe!")
                    Audio("Audio\Martis\Martis.select.ogg.ogx")
                    time.sleep(9)
                elif picking == "Estes":
                    print("Estes : Hello, my friend")
                    Audio("Audio\Estes\Estes.select.ogg.ogx")
                    time.sleep(1)
                elif picking == "Gord":
                    print("Gord : There's no time to chit chat")
                    Audio("Audio\Gord\Gord.select.ogg.ogx")
                    time.sleep(2)
                cek = False
                break

            elif optional == 'no':
                break
            else:
                print("Mohon jawab yes/no")
        else:
            print("Mohon masukkan pilihan yang benar")
            print('-'*100)

    print('-'*100)


    print(f"{p2}'s turn")
    cek = True
    while True:
        if cek == False:
            break
        Audio("Audio\Announcer\DraftPIck\Announcer.draftpick02.ogg.ogx")
        time.sleep(2)
        pick2 = input("Please pick a hero : ")
        if pick2 == "1":
            pickinggg = "Layla"
        elif pick2 == "2":
            pickinggg = "Miya"
        elif pick2 == "3":
            pickinggg = "Fanny"
        elif pick2 == "4":
            pickinggg = "Yin"
        elif pick2 == "5":
            pickinggg = "Uranus"
        elif pick2 == "6":
            pickinggg = "Belerick"
        elif pick2 == "7":
            pickinggg = "Sun"
        elif pick2 == "8":
            pickinggg = "Martis"
        elif pick2 == "9":
            pickinggg = "Estes"
        elif pick2 == "10":
            pickinggg = "Gord"

        if pickinggg == picking:
            print("Hero sudah dipilih")
            print('-'*100)
        elif pickinggg in list_hero:
            while True:
                optional = input(f"Are you sure want to pick {pickinggg}? (yes/no): ").lower()
                if optional == 'yes':
                    pick_hero.append(pickinggg)
                    if pickinggg == "Layla":
                        print("Layla : Ready, Go!")
                        Audio("Audio\Layla\Audio181-select.ogg.ogx")
                        time.sleep(1)
                    elif pickinggg == "Miya":
                        print("Miya : I am the moonlight that breaks through the darkness")
                        Audio("Audio\Miya\Audio011-v2-select.ogg.ogx")
                        time.sleep(3)
                    elif pickinggg == "Fanny":
                        print("Fanny : Sir, what's your command?")
                        Audio("Audio\Fanny\Fanny.new.select.ogg.ogx")
                        time.sleep(2)
                    elif pickinggg == "Yin":
                        print("Yin : I am Yin, and always will be — no matter what")
                        Audio("Audio\Yin\Yin.select.ogg.ogx")
                        time.sleep(4)
                    elif pickinggg == "Uranus":
                        print("Uranus : Hmm... Uranus has awakened")
                        Audio("Audio/Uranus/Uranus.select.ogg.ogx")
                        time.sleep(5)
                    elif pickinggg == "Belerick":
                        print("Belerick : Mighty oaks from little acorns grow")
                        Audio("Audio\Belerick\Belerick.new.select.ogg.ogx")
                        time.sleep(4)
                    elif pickinggg == "Sun":
                        print("Sun : I hope they're stronger than me")
                        Audio("Audio\Sun\Sun.select.ogg.ogx")
                        time.sleep(2)
                    elif pickinggg == "Martis":
                        print("Martis : [laughs] Three thousand worlds, and not a single worthy foe!")
                        Audio("Audio\Martis\Martis.select.ogg.ogx")
                        time.sleep(9)
                    elif pickinggg == "Estes":
                        print("Estes : Hello, my friend")
                        Audio("Audio\Estes\Estes.select.ogg.ogx")
                        time.sleep(1)
                    elif pickinggg == "Gord":
                        print("Gord : There's no time to chit chat")
                        Audio("Audio\Gord\Gord.select.ogg.ogx")
                        time.sleep(2)
                    cek = False
                    break
                elif optional == 'no':
                    break
                else:
                    print("Mohon jawab yes/no")
        else:
            print("Mohon masukkan pilihan yang benar")
            print('-'*100)

    return pick_hero

def pickAI(p1, p2, pick_hero):
    pick_hero.clear()
    print("Daftar hero :")
    for i, hero in enumerate(list_hero, start=1):
        print(f"{i}. {hero}")
    print('-'*100)

    print(f"{p1}'s turn")
    cek = True
    while True:
        if cek == False:
            break
        Audio("Audio\Announcer\DraftPIck\Announcer.draftpick02.ogg.ogx")
        time.sleep(2)
        pick1 = input("Please pick a hero : ")
        if pick1 == "1":
            picking = "Layla"
        elif pick1 == "2":
            picking = "Miya"
        elif pick1 == "3":
            picking = "Fanny"
        elif pick1 == "4":
            picking = "Yin"
        elif pick1 == "5":
            picking = "Uranus"
        elif pick1 == "6":
            picking = "Belerick"
        elif pick1 == "7":
            picking = "Sun"
        elif pick1 == "8":
            picking = "Martis"
        elif pick1 == "9":
            picking = "Estes"
        elif pick1 == "10":
            picking = "Gord"

        while True:
            optional = input(f"Are you sure want to pick {picking}? (yes/no): ").lower()
            if optional == 'yes':   
                list_hero.remove(picking)                 
                pick_hero.append(picking)
                if picking == "Layla":
                    print("Layla : Ready, Go!")
                    Audio("Audio\Layla\Audio181-select.ogg.ogx")
                    time.sleep(2)
                elif picking == "Miya":
                    print("Miya : I am the moonlight that breaks through the darkness")
                    Audio("Audio\Miya\Audio011-v2-select.ogg.ogx")
                    time.sleep(3)
                elif picking == "Fanny":
                    print("Fanny : Sir, what's your command?")
                    Audio("Audio\Fanny\Fanny.new.select.ogg.ogx")
                    time.sleep(2)
                elif picking == "Yin":
                    print("Yin : I am Yin, and always will be — no matter what")
                    Audio("Audio\Yin\Yin.select.ogg.ogx")
                    time.sleep(4)
                elif picking == "Uranus":
                    print("Uranus : Hmm... Uranus has awakened")
                    Audio("Audio/Uranus/Uranus.select.ogg.ogx")
                    time.sleep(5)
                elif picking == "Belerick":
                    print("Belerick : Mighty oaks from little acorns grow")
                    Audio("Audio\Belerick\Belerick.new.select.ogg.ogx")
                    time.sleep(4)
                elif picking == "Sun":
                    print("Sun : I hope they're stronger than me")
                    Audio("Audio\Sun\Sun.select.ogg.ogx")
                    time.sleep(2)
                elif picking == "Martis":
                    print("Martis : [laughs] Three thousand worlds, and not a single worthy foe!")
                    Audio("Audio\Martis\Martis.select.ogg.ogx")
                    time.sleep(9)
                elif picking == "Estes":
                    print("Estes : Hello, my friend")
                    Audio("Audio\Estes\Estes.select.ogg.ogx")
                    time.sleep(1)
                elif picking == "Gord":
                    print("Gord : There's no time to chit chat")
                    Audio("Audio\Gord\Gord.select.ogg.ogx")
                    time.sleep(2)
                cek = False
                break

            elif optional == 'no':
                break
            else:
                print("Mohon jawab yes/no")
        else:
            print("Mohon masukkan pilihan yang benar")
            print('-'*100)

    print('-'*100)

    print(f"{p2}'s turn")
    Audio("Audio\Announcer\DraftPIck\Announcer.draftpick02.ogg.ogx")
    time.sleep(2)
    pick2 = random.choice(list_hero)
    if pick2 == "Layla":
        print("Layla : Ready, Go!")
        Audio("Audio\Layla\Audio181-select.ogg.ogx")
        time.sleep(1)
        pick_hero.append("Layla")
    elif pick2 == "Miya":
        print("Miya : I am the moonlight that breaks through the darkness")
        Audio("Audio\Miya\Audio011-v2-select.ogg.ogx")
        time.sleep(3)
        pick_hero.append("Miya")
    elif pick2 == "Fanny":
        print("Fanny : Sir, what's your command?")
        Audio("Audio\Fanny\Fanny.new.select.ogg.ogx")
        time.sleep(2)
        pick_hero.append("Fanny")
    elif pick2 == "Yin":
        print("Yin : I am Yin, and always will be — no matter what")
        Audio("Audio\Yin\Yin.select.ogg.ogx")
        time.sleep(4)
        pick_hero.append("Yin")
    elif pick2 == "Uranus":
        print("Uranus : Hmm... Uranus has awakened")
        Audio("Audio/Uranus/Uranus.select.ogg.ogx")
        time.sleep(5)
        pick_hero.append("Uranus")
    elif pick2 == "Belerick":
        print("Belerick : Mighty oaks from little acorns grow")
        Audio("Audio\Belerick\Belerick.new.select.ogg.ogx")
        time.sleep(4)
        pick_hero.append("Belerick")
    elif pick2 == "Sun":
        print("Sun : I hope they're stronger than me")
        Audio("Audio\Sun\Sun.select.ogg.ogx")
        time.sleep(2)
        pick_hero.append("Sun")
    elif pick2 == "Martis":
        print("Martis : [laughs] Three thousand worlds, and not a single worthy foe!")
        Audio("Audio\Martis\Martis.select.ogg.ogx")
        time.sleep(9)
        pick_hero.append("Martis")
    elif pick2 == "Estes":
        print("Estes : Hello, my friend")
        Audio("Audio\Estes\Estes.select.ogg.ogx")
        time.sleep(1)
        pick_hero.append("Estes")
    elif pick2 == "Gord":
        print("Gord : There's no time to chit chat")
        Audio("Audio\Gord\Gord.select.ogg.ogx")
        time.sleep(2)
        pick_hero.append("Gord")
    else:
        None

    return pick_hero


def pickcom(p1, p2, pick_hero):
    pick_hero.clear()
    print("Daftar hero :")
    for i, hero in enumerate(list_hero, start=1):
        print(f"{i}. {hero}")
    print('-'*100)

    print(f"{p1}'s turn")
    Audio("Audio\Announcer\DraftPIck\Announcer.draftpick02.ogg.ogx")
    time.sleep(2)
    pick1 = random.choice(list_hero)
    list_hero.remove(pick1)
    if pick1 == "Layla":
        print("Layla : Ready, Go!")
        Audio("Audio\Layla\Audio181-select.ogg.ogx")
        time.sleep(1)
        pick_hero.append("Layla")
    elif pick1 == "Miya":
        print("Miya : I am the moonlight that breaks through the darkness")
        Audio("Audio\Miya\Audio011-v2-select.ogg.ogx")
        time.sleep(3)
        pick_hero.append("Miya")
    elif pick1 == "Fanny":
        print("Fanny : Sir, what's your command?")
        Audio("Audio\Fanny\Fanny.new.select.ogg.ogx")
        time.sleep(2)
        pick_hero.append("Fanny")
    elif pick1 == "Yin":
        print("Yin : I am Yin, and always will be — no matter what")
        Audio("Audio\Yin\Yin.select.ogg.ogx")
        time.sleep(4)
        pick_hero.append("Yin")
    elif pick1 == "Uranus":
        print("Uranus : Hmm... Uranus has awakened")
        Audio("Audio/Uranus/Uranus.select.ogg.ogx")
        time.sleep(5)
        pick_hero.append("Uranus")
    elif pick1 == "Belerick":
        print("Belerick : Mighty oaks from little acorns grow")
        Audio("Audio\Belerick\Belerick.new.select.ogg.ogx")
        time.sleep(4)
        pick_hero.append("Belerick")
    elif pick1 == "Sun":
        print("Sun : I hope they're stronger than me")
        Audio("Audio\Sun\Sun.select.ogg.ogx")
        time.sleep(2)
        pick_hero.append("Sun")
    elif pick1 == "Martis":
        print("Martis : [laughs] Three thousand worlds, and not a single worthy foe!")
        Audio("Audio\Martis\Martis.select.ogg.ogx")
        time.sleep(9)
        pick_hero.append("Martis")
    elif pick1 == "Estes":
        print("Estes : Hello, my friend")
        Audio("Audio\Estes\Estes.select.ogg.ogx")
        time.sleep(1)
        pick_hero.append("Estes")
    elif pick1 == "Gord":
        print("Gord : There's no time to chit chat")
        Audio("Audio\Gord\Gord.select.ogg.ogx")
        time.sleep(2)
        pick_hero.append("Gord")
    else:
        None

    print(f"{p2}'s turn")
    Audio("Audio\Announcer\DraftPIck\Announcer.draftpick02.ogg.ogx")
    time.sleep(2)
    pick2 = random.choice(list_hero)
    if pick2 == "Layla":
        print("Layla : Ready, Go!")
        Audio("Audio\Layla\Audio181-select.ogg.ogx")
        time.sleep(1)
        pick_hero.append("Layla")
    elif pick2 == "Miya":
        print("Miya : I am the moonlight that breaks through the darkness")
        Audio("Audio\Miya\Audio011-v2-select.ogg.ogx")
        time.sleep(3)
        pick_hero.append("Miya")
    elif pick2 == "Fanny":
        print("Fanny : Sir, what's your command?")
        Audio("Audio\Fanny\Fanny.new.select.ogg.ogx")
        time.sleep(2)
        pick_hero.append("Fanny")
    elif pick2 == "Yin":
        print("Yin : I am Yin, and always will be — no matter what")
        Audio("Audio\Yin\Yin.select.ogg.ogx")
        time.sleep(4)
        pick_hero.append("Yin")
    elif pick2 == "Uranus":
        print("Uranus : Hmm... Uranus has awakened")
        Audio("Audio/Uranus/Uranus.select.ogg.ogx")
        time.sleep(5)
        pick_hero.append("Uranus")
    elif pick2 == "Belerick":
        print("Belerick : Mighty oaks from little acorns grow")
        Audio("Audio\Belerick\Belerick.new.select.ogg.ogx")
        time.sleep(4)
        pick_hero.append("Belerick")
    elif pick2 == "Sun":
        print("Sun : I hope they're stronger than me")
        Audio("Audio\Sun\Sun.select.ogg.ogx")
        time.sleep(2)
        pick_hero.append("Sun")
    elif pick2 == "Martis":
        print("Martis : [laughs] Three thousand worlds, and not a single worthy foe!")
        Audio("Audio\Martis\Martis.select.ogg.ogx")
        time.sleep(9)
        pick_hero.append("Martis")
    elif pick2 == "Estes":
        print("Estes : Hello, my friend")
        Audio("Audio\Estes\Estes.select.ogg.ogx")
        time.sleep(1)
        pick_hero.append("Estes")
    elif pick2 == "Gord":
        print("Gord : There's no time to chit chat")
        Audio("Audio\Gord\Gord.select.ogg.ogx")
        time.sleep(2)
        pick_hero.append("Gord")
    else:
        None

    return pick_hero




def rank_p1(hero_pilihan):
    while True:
        print(f"Berikut daftar build Python Legend :\n1. Blande of Despair (+200 power)\n2. Guardian Helmet (+5000 health)\n3. Antique Cuirass (+500 armor)\n4. Enchanted Talisman (+3000 mana)")
        pilih_build = input("Choose your build : ")
        if pilih_build == '1':
            build_1 = "Blande of Despair"
            break
        elif pilih_build == '2':
            build_1 = "Guardian Helmet"
            break
        elif pilih_build == '3':
            build_1 = "Antique Cuirass"
            break
        elif pilih_build == '4':
            build_1 = "Enchanted Talisman"
            break
        else:
            print("Mohon pilih yang benar")
            print('-'*100)

    if hero_pilihan[0] == "Layla":
        player1 = Layla(build_1)
    elif hero_pilihan[0] == "Miya":
        player1 = Miya(build_1)
    elif hero_pilihan[0] == "Fanny":
        player1 = Fanny(build_1)
    elif hero_pilihan[0] == "Yin":
        player1 = Yin(build_1)
    elif hero_pilihan[0] == "Uranus":
        player1 = Uranus(build_1)
    elif hero_pilihan[0] == "Belerick":
        player1 = Belerick(build_1)
    elif hero_pilihan[0] == "Sun":
        player1 = Sun(build_1)
    elif hero_pilihan[0] == "Martis":
        player1 = Martis(build_1)
    elif hero_pilihan[0] == "Estes":
        player1 = Estes(build_1)
    elif hero_pilihan[0] == "Gord":
        player1 = Gord(build_1)

    return player1

def AI_p1(hero_pilihan):
        print(f"Berikut daftar build Python Legend :\n1. Blande of Despair (+200 power)\n2. Guardian Helmet (+5000 health)\n3. Antique Cuirass (+500 armor)\n4. Enchanted Talisman (+3000 mana)")
        daftar = ["1", "2", "3", "4"]
        pilih_build = random.choice(daftar)
        print(f"Choose your build : {pilih_build}")
        if pilih_build == '1':
            build_1 = "Blande of Despair"
        elif pilih_build == '2':
            build_1 = "Guardian Helmet"
        elif pilih_build == '3':
            build_1 = "Antique Cuirass"
        elif pilih_build == '4':
            build_1 = "Enchanted Talisman"

        if hero_pilihan[0] == "Layla":
            player1 = Layla(build_1)
        elif hero_pilihan[0] == "Miya":
            player1 = Miya(build_1)
        elif hero_pilihan[0] == "Fanny":
            player1 = Fanny(build_1)
        elif hero_pilihan[0] == "Yin":
            player1 = Yin(build_1)
        elif hero_pilihan[0] == "Uranus":
            player1 = Uranus(build_1)
        elif hero_pilihan[0] == "Belerick":
            player1 = Belerick(build_1)
        elif hero_pilihan[0] == "Sun":
            player1 = Sun(build_1)
        elif hero_pilihan[0] == "Martis":
            player1 = Martis(build_1)
        elif hero_pilihan[0] == "Estes":
            player1 = Estes(build_1)
        elif hero_pilihan[0] == "Gord":
            player1 = Gord(build_1)

        return player1


def AI_p2(hero_pilihan):
        print(f"Berikut daftar build Python Legend :\n1. Blande of Despair (+200 power)\n2. Guardian Helmet (+5000 health)\n3. Antique Cuirass (+500 armor)\n4. Enchanted Talisman (+3000 mana)")
        daftar = ["1", "2", "3", "4"]
        pilih_build = random.choice(daftar)
        print(f"Choose your build : {pilih_build}")
        if pilih_build == '1':
            build_2 = "Blande of Despair"
        elif pilih_build == '2':
            build_2 = "Guardian Helmet"
        elif pilih_build == '3':
            build_2 = "Antique Cuirass"
        elif pilih_build == '4':
            build_2 = "Enchanted Talisman"

        if hero_pilihan[1] == "Layla":
            player2 = Layla(build_2)
        elif hero_pilihan[1] == "Miya":
            player2 = Miya(build_2)
        elif hero_pilihan[1] == "Fanny":
            player2 = Fanny(build_2)
        elif hero_pilihan[1] == "Yin":
            player2 = Yin(build_2)
        elif hero_pilihan[1] == "Uranus":
            player2 = Uranus(build_2)
        elif hero_pilihan[1] == "Belerick":
            player2 = Belerick(build_2)
        elif hero_pilihan[1] == "Sun":
            player2 = Sun(build_2)
        elif hero_pilihan[1] == "Martis":
            player2 = Martis(build_2)
        elif hero_pilihan[1] == "Estes":
            player2 = Estes(build_2)
        elif hero_pilihan[1] == "Gord":
            player2 = Gord(build_2)

        return player2

def rank_p2(hero_pilihan):
    while True:
        print(f"Berikut daftar build Python Legend :\n1. Blande of Despair (+200 power)\n2. Guardian Helmet (+5000 health)\n3. Antique Cuirass (+500 armor)\n4. Enchanted Talisman (+3000 mana)")
        pilih_build = input("Choose your build : ")
        if pilih_build == '1':
            build_2 = "Blande of Despair"
            break
        elif pilih_build == '2':
            build_2 = "Guardian Helmet"
            break
        elif pilih_build == '3':
            build_2 = "Antique Cuirass"
            break
        elif pilih_build == '4':
            build_2 = "Enchanted Talisman"
            break
        else:
            print("Mohon pilih yang benar")
            print('-'*100)

    if hero_pilihan[1] == "Layla":
        player2 = Layla(build_2)
    elif hero_pilihan[1] == "Miya":
        player2 = Miya(build_2)
    elif hero_pilihan[1] == "Fanny":
        player2 = Fanny(build_2)
    elif hero_pilihan[1] == "Yin":
        player2 = Yin(build_2)
    elif hero_pilihan[1] == "Uranus":
        player2 = Uranus(build_2)
    elif hero_pilihan[1] == "Belerick":
        player2 = Belerick(build_2)
    elif hero_pilihan[1] == "Sun":
        player2 = Sun(build_2)
    elif hero_pilihan[1] == "Martis":
        player2 = Martis(build_2)
    elif hero_pilihan[1] == "Estes":
        player2 = Estes(build_2)
    elif hero_pilihan[1] == "Gord":
        player2 = Gord(build_2)

    return player2




def detail(pilih):
        if pilih == 'Layla':
            print("Skill 1  : Layla menembakkan laser panas")
            print("Skill 2  : Layla melempar bomb panas yang membuat power Layla bertambah 10")
            print("Ultimate : Layla menembakkan laser super mematikan!! yang membuat armor musuh hancur")
        elif pilih == "Miya":
            print("Skill 1  : Miya menggunakan kekuatan elfnya untuk membuat panah berganda yang meningkatkan")
            print("           power miliknya sebesar 15 dan healthnya sebesar 15")
            print("SKill 2  : Miya membuat hujan panah!! segera lariii")
            print("Ultimate : Miya mehilang dan mendapatkan kekuatan dari kaum elf")
        elif pilih == "Fanny":
            print("Skill 1  : Gak terlalu berdamage, tapi boleh juga")
            print("Skill 2  : Fanny akan terbang sebanyak energi yang dia punya dan memberikan stack sebanyak")
            print("           jumlah kabelnya")
            print("Ultimate : Fanny melakukan burst damage yang sangat sakit tergantung dari banyak kabelnya")
        elif pilih == "Yin":
            print("Skill 1  : Yin menampar lawannya dengan tangan ninjutsu yang membuat Yin mendapatkan 20 health")
            print("Skill 2  : Yin melakukan dash ke arah lawan sehingga mendapatkan 20 armor tambahan")
            print("Ultimate : Yin menjadi tak sadarkan diri setelah dirasuki oleh Tsukuna, yang membuat dia")
            print("           melampiaskan skill 1 dan skill 2 sembarangan")
        elif pilih == "Uranus":
            print("Skill 1  : Uranus menerbangkan piring kematian yang membuat dia mendapatkan 100 tambahan health")
            print("Skill 2  : Karena Uranus anak orang kaya, dia membeli 100 armor tambahan")
            print("Ultimate : Karena Uranus anak dokter, dia mendapat previllage health sebanyak 2000")
        elif pilih == "Belerick":
            print("Skill 1  : Belerick menjadi seperti tugas praktikum yang menghilangkan kekuatan dan kesenangan")
            print("           orang lain (-20 power lawan)")
            print("Skill 2  : Belerick merupakan spesies tumbuhan yang perlu banyak air, sehingga ketika mendapat air")
            print("           maka akan menambah health sebanyak 100")
            print("Ultimate : Belerick mencuri mana lawan (-20) dan power lawan (-20) untuk menambah healthnya (+200).")
            print("           Sama seperti koruptor saja....")
        elif pilih == "Sun":
            print("Skill 1  : Sun mencabut rambutnya dan terciptalah bunshin (+30 power)")
            print("Skill 2  : Sun adu mekanik dengan lawannya")
            print("Ultimate : Sun berubah menjadi mode serius (3 x power)")
        elif pilih == "Martis":
            print("Skill 1  : Martis jepit lawan dengan jepitan maut")
            print("Skill 2  : Martis melakukan dual pedang sehingga menambah armor 30 dan health 10")
            print("Ultimate : Martis ngamuk dan menjadi menjadi raja Ashura dan mengambil semua power lawan")
            print("           menjadi miliknya")
        elif pilih == "Estes":
            print("Skill 1  : Estes melakukan pertolongan pertama")
            print("Skill 2  : Estes menyerang menggunakan magic")
            print("Ultimate : Plotwist, ternyata Estes bapaknya Uranus sehingga ultinya mirip")
        elif pilih == "Gord":
            print("Skill 1  : Cuman serangan biasa :)")
            print("Skill 2  : Sama seperti skill 1 :)")
            print("Ultimate : Kamehamehaaa!!!")
        print("-"*100)

def ranked():
    username_P = []
    pick_hero = []
    p1 = input("Username player 1 : ")
    username_P.append(p1)
    p2 = input("Username player 2 : ")
    username_P.append(p2)

    print('-'*100)
    daftar_Hero()
    print('-'*100)

    print(f"{p1}'s turn")
    Banned()
    print('-'*100)

    print(f"{p2}'s turn")
    Banned()
    print('-'*100)

    hero_pilihan = pick(p1, p2, pick_hero)

    print('-'*100)
    print(f"{p1} memilih hero {TextColor.WARNING}{hero_pilihan[0]}{TextColor.ENDC}")
    detail_p1 = hero_pilihan[0]
    detail(detail_p1)
    pemain_1 = rank_p1(hero_pilihan)
    pemain_1.build()
    status_player_1(pemain_1)

    print('-'*100)
    print(f"{p2} memilih hero {TextColor.WARNING}{hero_pilihan[1]}{TextColor.ENDC}")
    detail_p2 = hero_pilihan[1]
    detail(detail_p2)
    pemain_2 = rank_p2(hero_pilihan)
    pemain_2.build()
    status_player_2(pemain_2)

    print('-'*100)

    return pemain_1, pemain_2, username_P

def VSAI():
    username_P = []
    pick_hero = []
    p1 = input("Username player 1 : ")
    username_P.append(p1)
    print("Username player 2 : Computer")
    username_P.append("Computer")

    print('-'*100)
    daftar_Hero()
    print('-'*100)
    hero_pilihan = pickAI(p1, "Computer", pick_hero)
    # print(hero_pilihan)

    print('-'*100)
    print(f"{p1} memilih hero {TextColor.WARNING}{hero_pilihan[0]}{TextColor.ENDC}")
    detail_p1 = hero_pilihan[0]
    detail(detail_p1)
    pemain_1 = rank_p1(hero_pilihan)
    pemain_1.build()
    status_player_1(pemain_1)

    print('-'*100)
    print(f"Computer memilih hero {TextColor.WARNING}{hero_pilihan[1]}{TextColor.ENDC}")
    detail_p2 = hero_pilihan[1]
    detail(detail_p2)
    pemain_2 = AI_p2(hero_pilihan)
    pemain_2.build()
    status_com(pemain_2)
    
    print('-'*100)

    return pemain_1, pemain_2, username_P


def com():
    print("Username player 1 : Computer 1")
    print("Username player 2 : Computer 2")
    username_P = ["Computer 1", "Computer 2"]
    pick_hero = []

    print('-'*100)
    daftar_Hero()
    print('-'*100)
    hero_pilihan = pickcom("Computer 1", "Computer 2", pick_hero)

    print('-'*100)
    print(f" Computer 1 memilih hero {TextColor.WARNING}{hero_pilihan[0]}{TextColor.ENDC}")
    detail_p1 = hero_pilihan[0]
    detail(detail_p1)
    pemain_1 = AI_p1(hero_pilihan)
    pemain_1.build()
    status_com_1(pemain_1)

    print('-'*100)
    print(f"Computer 2 memilih hero {TextColor.WARNING}{hero_pilihan[1]}{TextColor.ENDC}")
    detail_p2 = hero_pilihan[1]
    detail(detail_p2)
    pemain_2 = AI_p2(hero_pilihan)
    pemain_2.build()
    status_com_2(pemain_2)
    
    print('-'*100)

    return pemain_1, pemain_2, username_P


def bertarung(pemain_1, pemain_2, username_P):
    print(f"Battle Field start in...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    Audio("Audio\Announcer\Start\Announcer.start01.ogg.ogx")
    print("Welcome to Python Legends!")
    time.sleep(3.5)
    Audio("Audio\Announcer\Start\Announcer.start02.ogg.ogx")
    print("Five seconds 'till the enemy reaches the battlefield, smash them!")
    time.sleep(6)
    Audio("Audio\Announcer\Start\Announcer.start03.ogg.ogx")
    print("All troops deployed!")
    time.sleep(3)
    print('-'*100)

    x = pemain_1.getName()
    if x == "Layla":
        Hero_1 = Layla("Build")
    elif x == "Miya":
        Hero_1 = Miya("Build")
    elif x == "Fanny":
        Hero_1 = Fanny("Build")
    elif x == "Yin":
        Hero_1 = Yin("Build")
    elif x == "Uranus":
        Hero_1 = Uranus("Build")
    elif x == "Belerick":
        Hero_1 = Belerick("Build")
    elif x == "Sun":
        Hero_1 = Sun("Build")
    elif x == "Martis":
        Hero_1 = Martis("Build")
    elif x == "Estes":
        Hero_1 = Estes("Build")
    elif x == "Gord":
        Hero_1 = Gord("Build")


    y = pemain_2.getName()
    if y == "Layla":
        Hero_2 = Layla("Build")
    elif y == "Miya":
        Hero_2 = Miya("Build")
    elif y == "Fanny":
        Hero_2 = Fanny("Build")
    elif y == "Yin":
        Hero_2 = Yin("Build")
    elif y == "Uranus":
        Hero_2 = Uranus("Build")
    elif y == "Belerick":
        Hero_2 = Belerick("Build")
    elif y == "Sun":
        Hero_2 = Sun("Build")
    elif y == "Martis":
        Hero_2 = Martis("Build")
    elif y == "Estes":
        Hero_2 = Estes("Build")
    elif y == "Gord":
        Hero_2 = Gord("Build")

    return Hero_1, Hero_2

def run_rank(Hero_1, Hero_2, pemain_1, pemain_2, username_P):
    ronde = 0
    while True:
        ronde += 1
        if pemain_1.getHealth() <= 0:
            Audio("Audio\Announcer\End\Announcer.end01.ogg.ogx")
            print(f'The Winner is {TextColor.WARNING}{username_P[1]}{TextColor.ENDC}')
            time.sleep(1)
            exit()
        elif pemain_2.getHealth() <= 0:
            Audio("Audio\Announcer\End\Announcer.end01.ogg.ogx")
            print(f'The Winner is {TextColor.WARNING}{username_P[0]}{TextColor.ENDC}')
            time.sleep(1)
            exit()

        print(f"{'-'*100}\n{'ROUND '.rjust(50)}{ronde}\n{'-'*100}")
        
        if ronde%4 != 0:
            print(f"{username_P[0]}'s turn")
            while True:
                print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ulti(locked)")
                skill = input("=> ")
                if skill == '1':
                    Hero_1.skill_1(target = pemain_2)
                    break
                elif skill == '2':
                    Hero_1.skill_2(target = pemain_2)
                    break
                elif skill == '3':
                    print("Skill terkunci")
                    print('-'*100)
                else:
                    print("Mohon masukkan 1 atau 2")
                    print('-'*100)
            cek_p2(pemain_2)


            print(f"{username_P[1]}'s turn")
            while True:
                print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ulti(locked)")
                skill = input("=> ")
                if skill == '1':
                    Hero_2.skill_1(target = pemain_1)
                    break
                elif skill == '2':  
                    Hero_2.skill_2(target = pemain_1)
                    break
                elif skill == '3':
                    print("Skill terkunci")
                    print('-'*100)
                else:
                    print("Mohon masukkan 1 atau 2")
                    print('-'*100)
            cek_p1(pemain_1)

        else:
            print(f"{username_P[0]}'s turn")
            while True:
                print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ultimate")
                skill = input("=> ")
                if skill == '1':
                    Hero_1.skill_1(target = pemain_2)
                    break
                elif skill == '2':
                    Hero_1.skill_2(target = pemain_2)
                    break
                elif skill == '3':
                    Hero_1.Ulti(target = pemain_2)
                    break
                else:
                    print("Mohon masukkan 1, 2 atau 3")
                    print('-'*100)
            cek_p2(pemain_2)
                    

            print(f"{username_P[1]}'s turn")
            while True:
                print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ultimate")
                skill = input("=> ")
                if skill == '1':
                    Hero_2.skill_1(target = pemain_1)
                    break
                elif skill == '2':  
                    Hero_2.skill_2(target = pemain_1)
                    break
                elif skill == '3':
                    Hero_2.Ulti(target = pemain_1)
                    break
                else:
                    print("Mohon masukkan 1, 2 atau 3")
                    print('-'*100)
            cek_p1(pemain_1)


def run_VS(Hero_1, Hero_2, pemain_1, pemain_2, username_P):
    ronde = 0
    while True:
        ronde += 1
        if pemain_1.getHealth() <= 0:
            Audio("Audio\Announcer\End\Announcer.end01.ogg.ogx")
            print(f'The Winner is {TextColor.WARNING}Computer{TextColor.ENDC}')
            time.sleep(1)
            exit()
        elif pemain_2.getHealth() <= 0:
            Audio("Audio\Announcer\End\Announcer.end01.ogg.ogx")
            print(f'The Winner is {TextColor.WARNING}{username_P[0]}{TextColor.ENDC}')
            time.sleep(1)
            exit()

        print(f"{'-'*100}\n{'ROUND '.rjust(50)}{ronde}\n{'-'*100}")
        
        if ronde%4 != 0:
            print(f"{username_P[0]}'s turn")
            while True:
                print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ulti(locked)")
                skill = input("=> ")
                if skill == '1':
                    Hero_1.skill_1(target = pemain_2)
                    break
                elif skill == '2':
                    Hero_1.skill_2(target = pemain_2)
                    break
                elif skill == '3':
                    print("Skill terkunci")
                    print('-'*100)
                else:
                    print("Mohon masukkan 1 atau 2")
                    print('-'*100)
            cek_com(pemain_2)


            print(f"Computer's turn")
            print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ulti(locked)")
            pilih_skill = ['1', '2']
            skill = random.choice(pilih_skill)
            print(f"=> {skill}")
            if skill == '1':
                Hero_2.skill_1(target = pemain_1)
            elif skill == '2':  
                Hero_2.skill_2(target = pemain_1)
            cek_p1(pemain_1)

        else:
            print(f"{username_P[0]}'s turn")
            while True:
                print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ultimate")
                skill = input("=> ")
                if skill == '1':
                    Hero_1.skill_1(target = pemain_2)
                    break
                elif skill == '2':
                    Hero_1.skill_2(target = pemain_2)
                    break
                elif skill == '3':
                    Hero_1.Ulti(target = pemain_2)
                    break
                else:
                    print("Mohon masukkan 1, 2 atau 3")
                    print('-'*100)
            cek_com(pemain_2)
                    

            print(f"Computer's turn")
            print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ultimate")
            pilih_skill = ['1', '2', '3']
            skill = random.choice(pilih_skill)
            print(f"=> {skill}")
            if skill == '1':
                Hero_2.skill_1(target = pemain_1)
            elif skill == '2':  
                Hero_2.skill_2(target = pemain_1)
            elif skill == '3':
                Hero_2.Ulti(target = pemain_1)
            cek_p1(pemain_1)


def run_com(Hero_1, Hero_2, pemain_1, pemain_2, username_P):
    ronde = 0
    while True:
        ronde += 1
        if pemain_1.getHealth() <= 0:
            Audio("Audio\Announcer\End\Announcer.end01.ogg.ogx")
            print(f'The Winner is {TextColor.WARNING}Computer 2{TextColor.ENDC}')
            time.sleep(1)
            exit()
        elif pemain_2.getHealth() <= 0:
            Audio("Audio\Announcer\End\Announcer.end01.ogg.ogx")
            print(f'The Winner is {TextColor.WARNING}Computer 1{TextColor.ENDC}')
            time.sleep(1)
            exit()

        print(f"{'-'*100}\n{'ROUND '.rjust(50)}{ronde}\n{'-'*100}")

        if ronde%4 != 0:
            print(f"Computer 1's turn")
            print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ulti(locked)")
            pilih_skill = ['1', '2']
            skill = random.choice(pilih_skill)
            print(f"=> {skill}")
            if skill == '1':
                Hero_1.skill_1(target = pemain_2)
            elif skill == '2':  
                Hero_1.skill_2(target = pemain_2)
            cek_com2(pemain_2)

            print(f"Computer 2's turn")
            print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ulti(locked)")
            pilih_skill = ['1', '2']
            skill = random.choice(pilih_skill)
            print(f"=> {skill}")
            if skill == '1':
                Hero_2.skill_1(target = pemain_1)
            elif skill == '2':  
                Hero_2.skill_2(target = pemain_1)
            cek_com1(pemain_1)

        else:
            print(f"Computer 1's turn")
            print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ultimate")
            pilih_skill = ['1', '2', '3']
            skill = random.choice(pilih_skill)
            print(f"=> {skill}")
            if skill == '1':
                Hero_1.skill_1(target = pemain_2)
            elif skill == '2':  
                Hero_1.skill_2(target = pemain_2)
            elif skill == '3':
                Hero_1.Ulti(target = pemain_2)
            cek_com2(pemain_2)                    

            print(f"Computer 2's turn")
            print(f"Choose your skill :\n1. Skill 1\n2. Skill 2 \n3. Ultimate")
            pilih_skill = ['1', '2', '3']
            skill = random.choice(pilih_skill)
            print(f"=> {skill}")
            if skill == '1':
                Hero_2.skill_1(target = pemain_1)
            elif skill == '2':  
                Hero_2.skill_2(target = pemain_1)
            elif skill == '3':
                Hero_2.Ulti(target = pemain_1)
            cek_com1(pemain_1)

        



''' PROGRAM UTAMA '''

print(f"{'='*100}\n{'WELCOME TO PYTHON LEGEND'.center(100)}\n{'-'*100}")
while True:
    print(f"{'-'*100}\nPilih battle field :\n1. Ranked \n2. VS AI\n3. Computer vs Computer")
    battle = input("Pilihan kamu : ")
    print('-'*100)
    if battle == '1' or battle == '2' or battle == '3':
        if battle == '1':
            print(f"Kamu memilih {TextColor.FAIL}RANKED{TextColor.ENDC}")
            while True:
                print("1. Lanjutkan\n2. Batal")
                opsi = input("Pilihan : ")
                if opsi == '1' or opsi == '2':
                    if opsi == '1':
                        print('-'*100)
                        pemain_1, pemain_2, username_P = ranked()
                        Hero_1, Hero_2 = bertarung(pemain_1, pemain_2, username_P)
                        run_rank(Hero_1, Hero_2, pemain_1, pemain_2, username_P)
                        break
                    else:
                        break
                else:
                    print("Mohon pilih 1 atau 2")
        elif battle == '2':
            print(f"Kamu memilih {TextColor.WARNING}VS AI{TextColor.ENDC}")
            while True:
                print("1. Lanjutkan\n2. Batal")
                opsi = input("Pilihan : ")
                if opsi == '1' or opsi == '2':
                    if opsi == '1':
                        print('-'*100)
                        pemain_1, pemain_2, username_P = VSAI()
                        Hero_1, Hero_2 = bertarung(pemain_1, pemain_2, username_P)
                        run_VS(Hero_1, Hero_2, pemain_1, pemain_2, username_P)
                        break
                    else:
                        break
                else:
                    print("Mohon pilih 1 atau 2")
        elif battle == '3':
            print(f"Kamu memilih {TextColor.WARNING}Computer vs Computer{TextColor.ENDC}")
            while True:
                print("1. Lanjutkan\n2. Batal")
                opsi = input("Pilihan : ")
                if opsi == '1' or opsi == '2':
                    if opsi == '1':
                        pemain_1, pemain_2, username_P = com()
                        Hero_1, Hero_2 = bertarung(pemain_1, pemain_2, username_P)
                        run_com(Hero_1, Hero_2, pemain_1, pemain_2, username_P)                        
                    else:
                        break
                else:
                    print("Mohon pilih 1 atau 2")
    else:
        print("Mohon pilih antara 1, 2 atau 3")

