import random

characters = {
    'Герой': {
        'здоровье': 100,
        'атака': 10,
        'инвентарь': [],
    },
    'Злодей': {
        'здоровье': 50,
        'атака': 8,
        'инвентарь': ['дубинка', 'меч'],
    },
}

events = {
    1: "Вы нашли сундук с сокровищами!",
    2: "Вас атаковал злодей. Бой начался!",
    3: "Вы нашли камень силы!",
}

def show_event(event_id):
    print(events[event_id])

def boi():
    geroy = characters['Герой']
    zlodey = characters['Злодей']
    
    while geroy['здоровье'] > 0 and zlodey['здоровье'] > 0:
        geroy_damage = random.randint(1, geroy['атака'])
        zlodey_damage = random.randint(1, zlodey['атака'])
        
        print(f"Вы нанесли {geroy_damage} урона злодею.")
        zlodey['здоровье'] -= geroy_damage
        
        print(f"Злодей нанес вам {zlodey_damage} урона.")
        geroy['здоровье'] -= zlodey_damage
        
        print(f"Ваше здоровье: {geroy['здоровье']}, Здоровье злодея: {zlodey['здоровье']}\n")
    
    if geroy['здоровье'] <= 0:
        print("Вы проиграли! Игра окончена.")
    else:
        print("Вы победили злодея!")

def start_game():
    print("Добро пожаловать в игру 'Сокровища Злодея'")
    print("Вы - герой, и ваша цель - победить злодея и найти сокровища. Главное сокровище, это камень силы.\n")
    
    while True:
        choice = input("Выберите действие:\n1. Начать поиск\n2. Проверить инвентарь\n3. Выход из игры\n")
        
        if choice == '1':
            event_id = random.randint(1, 3)
            show_event(event_id)
            
            if event_id == 2:
                boi()
            elif event_id == 1:
                characters['Герой']['инвентарь'].append('сокровища')
            elif event_id == 3:
                print("Вы вышли из игры.")
                break
        elif choice == '2':
            inventory = ', '.join(characters['Герой']['инвентарь'])
            print(f"Ваш инвентарь: {inventory}\n")
        elif choice == '3':
            print("Вы вышли из игры.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.\n")

if __name__ == "__main__":
    start_game()