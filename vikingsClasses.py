from random import choice


# Soldier
class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
    
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health = self.health - damage



# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return 'Odin Owns You All!'



# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'



# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
        return None

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        return None
    
    def vikingAttack(self):
        saxon = choice(self.saxonArmy)
        viking = choice(self.vikingArmy)
        ataque = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        else:
            pass
        return ataque

    def saxonAttack(self):
        viking = choice(self.vikingArmy)
        saxon = choice(self.saxonArmy)
        ataque = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        else:
            pass
        return ataque
    
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"  
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."    
        else:
            return "Vikings and Saxons are still in the thick of battle."