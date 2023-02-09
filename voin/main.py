from voin import Voin
import random


voin_1 = Voin(hp=100)
voin_2 = Voin(hp=100)


def main():
    winner = 0
    while voin_1.hp >= 0 or voin_2.hp >= 0:
        print('Удар!')
        hit_voin = random.randint(1, 2)
        if hit_voin == 1:
            voin_2.hit()
            print('Атаковал воин №1')
            print('Остаток здоровья у воина 2 ' + str(voin_2.hp))
            if voin_2.hp == 0:
                winner = 1
                break
        else:
            voin_1.hit()
            print('Атаковал воин №2')
            print('Остаток здоровья у воина 1 ' + str(voin_1.hp))
            if voin_1.hp == 0:
                winner = 2
                break

    print('Бой окончен')
    print('Победу одержал ' + str(winner))

main()
