from random import randint
import requests
from datetime import timedelta, datetime

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.type = self.get_type()
        self.HP = randint(200, 400)
        self.power = randint(30, 60)
        self.last_feed_time = datetime.now()
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/2.svg'


    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def get_type(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            try:    

                data = response.json()
                return (data['types'][randint(0,5)]['type']['name'])
            except Exception as e:
                return e
        else:
            return 'grass'



    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\n type:{self.type}\n здоровье: {self.HP}\n урон: {self.power}"


    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def atack(self, enemy):
        if isinstance(enemy, Wizard): 
            chance = randint(1, 5)
            if chance == 1:
                return "Покемон-Волшебник применил щит"
        if enemy.HP > self.power:
            enemy.HP -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n здоровье @{enemy.pokemon_trainer}\n теперь {enemy.HP}"
        elif enemy.HP <= 0: 
            enemy.HP = 0
            return f"Победа @{self.pokemon_trainer}\n ПОЗДРАВЛЬЯЕМ!!"
        elif self.HP <= 0:
            self.HP = 0
            return f"Поражение @{self.pokemon_trainer}\n Повезет в следующий раз"
        
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now() 
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.HP += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.HP}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"
        
class Wizard(Pokemon):
    def info(self):
        return f"У тебя Покемон-Волшебник \n" + super().info()

class Fighter(Pokemon):
    def atack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().atack(enemy)
        power -= super_power
        return result + f"Боец применил супер силу {super_power}"
    def info(self):
        return f"У тебя Покемон-Боец \n" + super().info()
    
if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(Wizard.info())
    print()
    print(Fighter.info())
    print()
    print(Fighter.attack(wizard))