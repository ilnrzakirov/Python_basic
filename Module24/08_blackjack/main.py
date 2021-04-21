import random

all_card = ["T", "K", "D", "V", 10, 9, 8, 7, 6, 5, 4, 3, 2]


class Card:

    def __init__(self):
        self.card = random.choice(all_card)

    def info(self):
        print(self.card, end=" ")

    def card_return(self):
        return self.card


class Player:

    def __init__(self, name):
        self.name = name
        self.player_card = []

    def points(self):
        total_point = 0
        for card in self.player_card:
            card = card.card_return()
            if card == "K" or card == "D" or card == "V":
                total_point += 10
            elif card == "T":
                if total_point < 21:
                    total_point += 11
                else:
                    total_point += 1
            else:
                total_point += int(card)
        return total_point

    def my_card(self, card):
        if isinstance(card, Card):
            self.player_card.append(card)

    def info_my_card(self):
        for card in self.player_card:
            card.info()


user_1 = Player("user_1")
computer = Player("computer")

for card in range(2):
    card_for_user = Card()
    card_for_computer = Card()
    user_1.my_card(card_for_user)
    computer.my_card(card_for_computer)

while True:
    print("Ваши карты: ", end=" ")
    user_1.info_my_card()
    answer = input("\nХотите взять еще карту?: ").lower()
    if answer == "да":
        card_for_user = Card()
        user_1.my_card(card_for_user)
    elif answer == "нет":
        user1_points = user_1.points()
        computer_points = computer.points()
        if user1_points > 21:
            print("{} проиграл так как собрал больше 21".format(user_1.name))
            break
        if user1_points > computer_points:
            print("Победил {} с общим количеством очков {} против очков компьютера {}".format(
                user_1.name, user1_points, computer_points))
            break
        elif computer_points > user1_points:
            print("Победил компьютер с общим количеством очков {} против твоего {}".format(
                computer_points, user1_points))
            break
        else:
            print("Ничья")
            break

# зачёт!
