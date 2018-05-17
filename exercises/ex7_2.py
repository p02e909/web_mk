#!/usr/bin/env python3

'''
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

'''
import random

class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def __str__(self):
        return "%s: %s damage" % (self.name, self.damage)

sword = Weapon(name = 'sword', damage = 500)
katana = Weapon(name = 'katana', damage = 700)
Weapons = [katana, sword]

class Fighter():
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP
        self.Weapon = random.choice(Weapons)

    def __str__(self):
        return "%s - %s: %d HP" % (self.name, self.Weapon, self.HP)
        # print(self.name, ' ', self.Weapon,' :', self.HP, ' HP')

    def attack(self, oppoiment):
        oppoiment.HP = oppoiment.HP - self.Weapon.damage

def solve(player1, player2):
    '''Trả về tuple tên người thắng cuộc và lượng máu còn lại'''
    result = None

    print(player1)
    print(player2)
    while True:
        player = random.choice([player1, player2])       
        #danh nhau
        if player is player1:
            print(player.name, 'attack')
            player.attack(player2)
            print(player1.name, ' :', player1.HP, ' HP')   
            print(player2.name, ' :', player2.HP, ' HP', '\n')        
            # player2.HP = player2.HP - player1.Weapon
            if player2.HP <= 0:
                break            
        else:
            print(player.name, 'attack')
            player.attack(player1)
            print(player1.name, ' :', player1.HP, ' HP')
            print(player2.name, ' :', player2.HP, ' HP', '\n')
            # player1.HP = player1.HP - player2.Weapon      
            if player1.HP <= 0:
                break                  
    if player1.HP > 0:
        result = (player1.name, player1.HP)
    else:
        result = (player2.name, player2.HP)
    return result


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter(name = 'Garnet', HP = 10000)
    player2 = Fighter(name = 'Violet', HP = 10000)
    print(solve(player1, player2))


if __name__ == "__main__":
    main()
