import random

characters = {
    'Пират': {
        'здоровье': 100,
        'атака': 10,
        'инвентарь': [],
    },
    'Военные': {
        'максимальное здоровье': 50,
        'здоровье': 50,
        'атака': 8,
        'инвентарь': [],
    },
}

events = {
    1: "Вы нашли сундук с сокровищами!",
    2: "Вас атаковали военные. Бой начался!",
    3: "Вы нашли зелье здоровья!",
}

def show_event(event_id):
    print(events[event_id])

def boy():
    pirat = characters['Пират']
    voenniy = characters['Военные']
    voenniy ['здоровье'] = voenniy ['максимальное здоровье']
    while pirat['здоровье'] > 0 and voenniy['здоровье'] > 0:
        pirat_damage = random.randint(1, pirat['атака'])
        voenniy_damage = random.randint(1, voenniy['атака'])
        
        print(f"Вы нанесли {pirat_damage} урона военному.")
        voenniy['здоровье'] -= pirat_damage
        
        print(f"Военные нанесли вам {voenniy_damage} урона.")
        pirat['здоровье'] -= voenniy_damage
        
        print(f"Ваше здоровье: {pirat['здоровье']}, Здоровье военных: {voenniy['здоровье']}\n")
    
    if pirat['здоровье'] <= 0:
        print("Вы проиграли! Игра окончена.")
    else:
        print("Вы победили военных!")

def use_health_potion():
    pirat = characters['Пират']
    if 'зелье здоровья' in pirat['инвентарь']:
        pirat['здоровье'] += 20 
        pirat['инвентарь'].remove('зелье здоровья')
        print("Вы использовали зелье здоровья и восстановили здоровье.")
    else:
        print("У вас нет зелья здоровья.")

def check_game_over():
    pirat = characters['Пират']
    if pirat['здоровье'] <= 0:
        print("Вы проиграли! Игра окончена.")
        return True
    elif 'сокровища' in pirat['инвентарь']:
        print("Поздравляем! Вы нашли сокровища и победили военных. Игра окончена.")
        return True
    else:
        return False

def use_inventory_item():
    pirat = characters['Пират']
    if len(pirat['инвентарь']) == 0:
        print("У вас нет предметов в инвентаре.")
    else:
        print("Ваш инвентарь:")
        for i, item in enumerate(pirat['инвентарь'], start=1):
            print(f"{i}. {item}")
        
        choice = input("Выберите предмет для использования (введите номер): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(pirat['инвентарь']):
                item_to_use = pirat['инвентарь'][choice - 1]
                if item_to_use == 'зелье здоровья':
                    use_health_potion()
                else:
                    print(f"Вы использовали предмет: {item_to_use}")
                    pirat['инвентарь'].remove(item_to_use)
            else:
                print("Некорректный выбор.")
        except ValueError:
            print("Введите число.")

def start_game():
    print("Добро пожаловать в игру 'Сокровища пиратов'")
    print("Вы - Пират, и ваша цель - победить военных и найти сокровища.\n")
    
    while True:
        choice = input("Выберите действие:\n1. Идти дальше\n2. Проверить инвентарь\n3. Использовать предмет из инвентаря\n4. Выйти из игры\n")
        
        if choice == '1':
            event_id = random.randint(1, 3)
            
            if event_id == 2:
                boy()
            elif event_id == 1:
                characters['Пират']['инвентарь'].append('сокровища')
            elif event_id == 3:
                characters['Пират']['инвентарь'].append('зелье здоровья')
                print("Вы нашли зелье здоровья!")
        elif choice == '2':
            inventory = ', '.join(characters['Пират']['инвентарь'])
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