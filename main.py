import random
import math


class Game:
    scores = {}
    options = ['!exit', '!rating']
    win_points = {'Win': 100, 'Draw': 50}

    def __init__(self):
        self.RPS = {}
        self.name = input('Enter your name: ')
        print(f'Hello {self.name}')
        if self.name not in self.scores:
            self.scores[self.name] = 0
        self.check_score()

    def rules(self, user_input):
        output = {}
        items = list(user_input.split(','))
        if len(items) == 1:
            return {'rock': ['paper'], 'paper': ['scissors'], 'scissors': ['rock']}
        double_items = items + items
        half_items = math.ceil(len(items) / 2)
        for i in range(len(items)):
            output[items[i]] = double_items[i + 1:i + half_items:1]
        return output

    def check_score(self):
        with open('rating.txt') as rating:
            for lines in rating.readlines():
                self.scores[lines.split()[0]] = int(lines.split()[1])

    def process(self):
        self.RPS = self.rules(input())
        print("Okay, let's start")
        random.seed()
        while True:
            hand = input()
            cpu_hand = random.choice(list(self.RPS.keys()))
            if hand not in self.RPS.keys() and hand not in self.options:
                print('Invalid input')
            elif hand == '!rating':
                print(f'Your score: {self.scores[self.name]}')
            elif hand == '!exit':
                print('Bye!')
                return
            elif hand == cpu_hand:
                print(f'There is a draw ({hand})')
                self.scores[self.name] += self.win_points['Draw']
            elif hand in self.RPS.get(cpu_hand):
                print(f'Well done. Computer chose {cpu_hand} and failed')
                self.scores[self.name] += self.win_points['Win']
            elif hand not in self.RPS.get(cpu_hand):
                print(f'Sorry, but computer chose {cpu_hand}')


game = Game()
game.process()
