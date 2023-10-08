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
    3: "Вы нашли зелье здоровья!",
}

def show_event(event_id):
    print(events[event_id])

def battle():
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

def use_health_potion():
    geroy = characters['Герой']
    if 'зелье здоровья' in geroy['инвентарь']:
        geroy['здоровье'] += 20 
        geroy['инвентарь'].remove('зелье здоровья')
        print("Вы использовали зелье здоровья и восстановили здоровье.")
    else:
        print("У вас нет зелья здоровья.")

def check_game_over():
    geroy = characters['Герой']
    if geroy['здоровье'] <= 0:
        print("Вы проиграли! Игра окончена.")
        return True
    elif 'сокровища' in geroy['инвентарь']:
        print("Поздравляем! Вы нашли сокровища и победили злодея. Игра окончена.")
        return True
    else:
        return False

def use_inventory_item():
    geroy = characters['Герой']
    if len(geroy['инвентарь']) == 0:
        print("У вас нет предметов в инвентаре.")
    else:
        print("Ваш инвентарь:")
        for i, item in enumerate(geroy['инвентарь'], start=1):
            print(f"{i}. {item}")
        
        choice = input("Выберите предмет для использования (введите номер): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(geroy['инвентарь']):
                item_to_use = geroy['инвентарь'][choice - 1]
                if item_to_use == 'зелье здоровья':
                    use_health_potion()
                else:
                    print(f"Вы использовали предмет: {item_to_use}")
                    geroy['инвентарь'].remove(item_to_use)
            else:
                print("Некорректный выбор.")
        except ValueError:
            print("Введите число.")

def start_game():
    print("Добро пожаловать в текстовую игру-новеллу!")
    print("Вы - герой, и ваша цель - победить злодея и найти сокровища.\n")
    
    while True:
        choice = input("Выберите действие:\n1. Идти дальше\n2. Проверить инвентарь\n3. Использовать предмет из инвентаря\n4. Выйти из игры\n")
        
        if choice == '1':
            event_id = random.randint(1, 3)
            show_event(event_id)
            
            if event_id == 2:
                battle()
            elif event_id == 1:
                characters['Герой']['инвентарь'].append('сокровища')
            elif event_id == 3:
                characters['Герой']['инвентарь'].append('зелье здоровья')
                print("Вы нашли зелье здоровья!")
        elif choice == '2':
            inventory = ', '.join(characters['Герой']['инвентарь'])
            print(f"Ваш инвентарь: {inventory}\n")
        elif choice == '3':
            use_inventory_item()
        elif choice == '4':
            print("Вы вышли из игры.")
            break
        
        if check_game_over():
            break

if __name__ == "__main__":
    start_game()