class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = ['food', food]
        self.clothing = ['clothing', clothing]
        self.entertain = ['entertainment', entertainment]

    def deposit(self, f, c, e):
        self.food[1] += f
        self.clothing[1] += c
        self.entertain[1] += e
        self.balance()

    def withdraw(self, category, amount):
        categories = [self.food, self.clothing, self.entertain]

        for i in categories:
            if i[0] == category:
                i[1] -= amount

        self.balance()

    def transfer(self, prev, next, amount):
        categories = [self.food, self.clothing, self.entertain]

        for i in categories:
            for j in categories:
                if i[0] == prev and j[0] == next:
                    i[1] -= amount
                    j[1] += amount

        self.balance()

    def balance(self):
        print(
            f'Your budget balance are \n Food: {self.food[1]} \n Clothing: {self.clothing[1]} \n Entertainment: {self.entertain[1]} ')


bud = Budget(300, 500, 200)
bud.deposit(500, 200, 300)
bud.withdraw('food', 200)
bud.transfer('food', 'entertainment', 300)
