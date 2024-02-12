import pygame
import time
import random
from abc import ABC, abstractclassmethod

def Audio(path_audio):
    pygame.mixer.init()
    pygame.mixer.music.load(path_audio)
    pygame.mixer.music.play()

class Hero(ABC):
    def __init__(self, build):
        self._build = build
        self._health = 0
        self._power = 0
        self._magic = 0
        self._armor = 0
        self._mana = 0

    def build(self):
        if self._build == "Blade of Despair":
            self._power += 200
        elif self._build == "Guardian Helmet":
            self._health += 5000
        elif self._build == "Antique Cuirass":
            self._armor += 500
        elif self._build == "Enchanted Talisman":
            self._mana += 3000
    
    def getName(self):
        return self._name

    def getBuild(self):
        return self._build

    def getHealth(self):
        return self._health
    
    def getPower(self):
        return self._power

    def getMagic(self):
        return self._magic

    def getArmor(self):    
        return self._armor

    def getMana(self):
        return self._mana


    def setName(self):
        self._name = name
        
    def setBuild(self):
        self._build = build

    def setHealth(self):
        self._health = health
    
    def setPower(self):
        self._power = power

    def setMagic(self):
        self._magic = magic

    def setArmor(self):
        self._armor = armor

    def setMana(self):
        self._mana = mana
        

    @abstractclassmethod
    def skill_1(self, target):
        pass
    
    @abstractclassmethod
    def skill_2(self, target):
        pass

    @abstractclassmethod
    def Ulti(self):
        pass



class Layla(Hero):
    def __init__(self, build):
        super().__init__(build)
        self._name = "Layla"
        self._health = 4500
        self._power = 3000
        self._magic = 0
        self._armor = 100
        self._mana = 400

    def skill_1(self, target):
        if target._armor > 0:
            target._armor -= self._power * (50/100)
            target._health -= self._power * (20/100)
        else:
            target._health -= self._power * (50/100)
        self._mana -= 50
        print("Layla : Bull's eye!")
        Audio("Audio\Layla\Audio181-skill01.ogg")
        time.sleep(1)
	
    def skill_2(self, target):
        if target._armor > 0:
            target._armor -= self._power * (25/100)
            target._health -= self._power * (10/100)
        else:
            target._health -= self._power * (25/100)
            
        self._mana -= 20
        self._power += 10
        print("Layla : Target locked!")
        Audio("Audio\Layla\Audio181-skill02.ogg")
        time.sleep(1)

    def Ulti(self, target):
        target._health -= self._power
        self._mana -= 100
        print("Layla : Time to shine!")
        Audio("Audio\Layla\Audio181-ult01.ogg.ogx")
        time.sleep(1)

class Miya(Hero):
    def __init__(self, build):
        super().__init__(build)
        self._name = "Miya"
        self._health = 5000
        self._power = 2500
        self._magic = 0
        self._armor = 150
        self._mana = 400
		
    def skill_1(self, target):
        if target._armor > 0:
            target._armor -= self._power * (20/100)
            target._health -= self._power * (10/100)
        else:
            target._health -= self._power * (20/100)
        
        self._mana -= 50
        self._power += 15
        self._health += 15
        print("Miya : Watch your back")
        Audio("Audio\Miya\Audio011-v2-attack01.ogg.ogx")
        time.sleep(1)

		
    def skill_2(self, target):
        if target._armor > 0:
            target._armor -= self._power * (25/100)
            target._health -= self._power * (10/100)
        else:
            target._health -= self._power * (25/100)
        self._mana -= 20
        print("Miya : You can't run from my arrow")
        Audio("Audio\Miya\Audio011-v2-attack02.ogg.ogx")
        time.sleep(2)

		
    def Ulti(self, target):
        self._power += 200
        self._armor += 30
        self._mana -= 70
        print("Miya : May the moon forever shine upon us!")
        Audio("Audio\Miya\Audio011-v2-ult01.ogg.ogx")
        time.sleep(2)
	
class Fanny(Hero):
    def __init__(self, build):
        super().__init__(build)
        self._name = "Fanny"
        self._health = 6000
        self._power = 500
        self._magic = 0	
        self._armor = 30
        self._mana = 100
        self._kabel = 0

    def skill_1(self, target):
        if target._armor > 0:
            target._armor -= self._power * (25/100)
            target._health -= self._power * (10/100)
        else:
            target._health -= self._power * (25/100)
        self._mana -= 20
        print("Fanny : Where are you looking? I am here")
        Audio("Audio\Fanny\Fanny.new.skill01.ogg.ogx")
        time.sleep(2)

    def skill_2(self, target):
        kabel = int(self._mana // 10)
        if kabel <=0 :
            kabel = 0
        self._kabel += kabel
        print(f"Wow, kamu terbang sebanyak {kabel} kabel")
        if target._armor > 0:
            target._armor -= self._power * (10/100)
            target._health -= self._power * (5/100)
        else:
            target._health -= self._power * (10/100)
        self._mana -= (10 * kabel)
        self._health += (30 * kabel)
        print("Fanny : Ah, darn it! I went a bit too far")
        Audio("Audio\Fanny\Fanny.new.skill02.ogg.ogx")
        time.sleep(3)

    def Ulti(self, target):
        target._health -= self._power * self._kabel
        self._mana -= 100
        print("Fanny : Fully exposed!")
        Audio("Audio\Fanny\Fanny.new.ult.ogg.ogx")
        time.sleep(2)
		
class Yin(Hero):
    def __init__(self, build):
        super().__init__(build)
        self._name = "Yin"
        self._health = 8000
        self._power = 2000
        self._magic = 0
        self._armor = 100
        self._mana = 0
		
    def skill_1(self, target):
        if target._armor > 0:
            target._armor -= self._power * (50/100)
            target._health -= self._power * (25/100)
        else:
            target._health -= self._power * (50/100)
        self._health += 20
        print("Yin : I will protect the good in people around me")
        Audio("Audio\Yin\Yin.move02.ogg.ogx")
        time.sleep(2)

		
    def skill_2(self, target):
        if target._armor > 0:
            target._armor -= self._power * (20/100)
            target._health -= self._power * (10/100)
        else:
            target._health -= self._power * (20/100)
        self._armor += 20
        print("Yin : I'd rather lose than stop fighting")
        Audio("Audio\Yin\Yin.move03.ogg.ogx")
        time.sleep(2)

		
    def Ulti(self, target):
        print("Yin memasuki mode Tsukuna")
        print("Yin : My turn now!")
        Audio("Audio\Yin\Yin.ult02.ogg.ogx")
        time.sleep(2)
        if target._armor > 0:
            target._armor -= self._power * (50/100)
            target._health -= self._power * (25/100)
        else:
            target._health -= self._power * (50/100)
        self._health += 20
        print("Yin : 許可なく見上げるな。不愉快だ")
        Audio("Audio\Yin\Audio1134-move15.ogg.ogx")
        time.sleep(3)

        if target._armor > 0:
            target._armor -= self._power * (20/100)
            target._health -= self._power * (10/100)
        else:
            target._health -= self._power * (20/100)
        self._armor += 20
        print("Yin : さてと、晴れて自由の身だ")
        Audio("Audio\Yin\Audio1134-move14.ogg.ogx")
        time.sleep(3)
        
class Uranus(Hero):
    def __init__(self, build):
        super().__init__(build)
        self._name = "Uranus"
        self._health = 12000
        self._power = 1000
        self._magic = 250
        self._armor = 1000
        self._mana = 300
		
    def skill_1(self, target):
        if target._armor > 0:
            target._armor -= self._power * (50/100)
            target._armor -= self._magic * (50/100)
            target._health -= self._power * (40/100)
            target._health -= self._magic * (40/100)
        else:
            target._health -= self._power * (40/100)
            target._health -= self._magic * (40/100)
        self._health += 100
        self._mana -= 30
        print("Uranus : [snarls]")
        Audio("Audio\\Uranus\\Uranus.skill.ogg.ogx")
        time.sleep(1)


    def skill_2(self, target):
        self._armor += 100
        self._mana -= 50
        print("Uranus : [roars] Leave now... intruders!")
        Audio("Audio\\Uranus\\Uranus.move07.ogg.ogx")
        time.sleep(5)


    def Ulti(self, target):
        
        self._health += 2000
        self._mana -= 100
        print("Uranus : [laughs]")
        Audio("Audio\\Uranus\\Uranus.ult.ogg.ogx")
        time.sleep(3)

class Belerick(Hero):
    def __init__(self, build):
        super().__init__(build)
        self._name = "Belerick"
        self._health = 10000
        self._power = 1000
        self._magic = 50
        self._armor = 500
        self._mana = 500
		
    def skill_1(self, target):
        if target._armor > 0:
            target._armor -= self._power * (50/100)
            target._armor -= self._magic * (30/100)
            target._health -= self._power * (50/100)
            target._health -= self._magic * (30/100)
        else:
            target._health -= self._power * (70/100)
            target._health -= self._magic * (70/100)
        
        self._mana -= 40
        target._power -= 20
        target._mana -= 20
        print("Belerick : In death, I shall be reborn")
        Audio("Audio\Belerick\Belerick.new.move02.ogg.ogx")
        time.sleep(4)

		
    def skill_2(self, target):
        if target._armor > 0:
            target._armor -= self._power * (40/100)
            target._health -= self._power * (20/100)
        else:
            target._health -= self._power * (40/100)
        self._health += 100
        self._mana -= 50
        print("Belerick : All lives, are precious")
        Audio("Audio\Belerick\Belerick.new.move03.ogg.ogx")
        time.sleep(3)
		
    def Ulti(self, target):
        target._power -= 20
        target._mana -= 20
        self._health += 200
        self._mana -= 70
        print("Belerick : Bloom, against the wind!")
        Audio("Audio\Belerick\Belerick.new.ult.ogg.ogx")
        time.sleep(3)

			
class Sun(Hero):
    def __init__(self, build):
        super().__init__(build)
        self._name = "Sun"
        self._health = 8500
        self._power = 1000
        self._magic = 0
        self._armor = 350
        self._mana = 200
		
    def skill_1(self, target):
        self._mana -= 20
        self._power += 300
        print("Sun : Every mistake could be a lesson")
        Audio("Audio\Sun\Sun.move06.ogg.ogx")
        time.sleep(2)

	
    def skill_2(self, target):
        if target._armor > 0:
            target._armor -= self._power * (40/100)
            target._health -= self._power * (20/100)
        else:
            target._health -= self._power * (40/100)
        self._mana -= 20
        print("Sun : Take this!")
        Audio("Audio\Sun\Sun.move07.ogg.ogx")
        time.sleep(1)

		
    def Ulti(self, target):
        self._mana -= 100
        self._power *= 3
        print("Sun : Go, boys!")
        Audio("Audio\Sun\Sun.ult.ogg.ogx")
        time.sleep(1)

	
class Martis(Hero):
    def __init__(self, build):
        super().__init__(build)
        self._name = "Martis"
        self._health = 9000
        self._power = 3000
        self._magic = 0
        self._armor = 500
        self._mana = 0
	
    def skill_1(self, target):
        if target._armor > 0:
            target._armor -= self._power * (50/100)
            target._health -= self._power * (25/100)
        else:
            target._health -= self._power * (50/100)
        print("Martis : I'll show you what fighting really is")
        Audio("Audio\Martis\Martis.move01.ogg.ogx")
        time.sleep(5)
			
    def skill_2(self, target):
        if target._armor > 0:
            target._armor -= self._power * (20/100)
            target._health -= self._power * (10/100)
        else:
            target._health -= self._power * (20/100)
        self._armor += 30
        self._health += 10
        print("Martis : Feel my wrath!")
        Audio("Audio\Martis\Martis.move07.ogg.ogx")
        time.sleep(2)
		
    def Ulti(self, target):
        target._power -= target._power/4
        self._power += target._power
        print("Martis : Ashura!")
        Audio("Audio\Martis\Martis.ult00.ogg.ogx")
        time.sleep(1)
		
class Estes(Hero):
    def __init__(self, build):
        super().__init__(build)
        self._name = "Estes"
        self._health = 6000
        self._power = 0
        self._magic = 500
        self._armor = 300
        self._mana = 3000
        
    def skill_1(self, target):
        self._health += 200
        self._mana -= 10
        print("Estes : Love others as love yourself")
        Audio("Audio\Estes\Estes.move01.ogg.ogx")
        time.sleep(3)

    def skill_2(self, target):
        target._health -= self._magic * 2
        print("Estes : Darkness is the right hand of the Light")
        Audio("Audio\Estes\Estes.move06.ogg.ogx")
        time.sleep(2)

    def Ulti(self, target):
        self._health += 2000
        self._mana -= 100
        print("Estes : May the Holy Light be with you!")
        Audio("Audio\Estes\Estes.ult.ogg.ogx")
        time.sleep(2)

class Gord(Hero):
    def __init__(self, build):
        super().__init__(build)
        self._name = "Gord"
        self._health = 6000
        self._power = 0
        self._magic = 2000
        self._armor = 300
        self._mana = 300
	
    def skill_1(self, target):
        if target._armor > 0:
            target._armor -= self._magic * (50/100)
            target._health -= self._magic * (25/100)
        else:
            target._health -= self._magic * (50/100)
        self._mana -= 20
        print("Gord : Imagination is the driving force of the energy")
        Audio("Audio\Gord\Gord.move05.ogg.ogx")
        time.sleep(3)

    def skill_2(self, target):
        if target._armor > 0:
            target._armor -= self._magic * (50/100)
            target._health -= self._magic * (25/100)
        else:
            target._health -= self._magic * (50/100)
        self._mana -= 20
        print("Gord : I'm not a monster, I'm a demon!")
        Audio("Audio\Gord\Gord.move06.ogg.ogx")
        time.sleep(3)

    def Ulti(self, target):
        target._health -= 1000
        print("Gord : Bear my wrath!")
        Audio("Audio\Gord\Gord.ult.ogg.ogx")
        time.sleep(2)