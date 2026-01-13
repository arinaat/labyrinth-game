EVENT_MODULO = 1
TRAP_ROOM_ID = "trap_room"
TRAP_DAMAGE = 30
MIN_HEALTH_TO_SURVIVE = 0

ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.', '10')
    },
    'trap_room': {
          'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
          'exits': {'west': 'entrance'},
          'items': ['rusty_key'],
          'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг')
    },
    'library': {
          'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
          'exits': {'east': 'hall', 'north': 'armory'},
          'items': ['ancient_book'],
          'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'резонанс')  
    },
        'armory': {
          'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
          'exits': {'south': 'library'},
          'items': ['sword', 'bronze_box'],
          'puzzle': None
    },
    "gallery": {
        "description": (
            "Узкая галерея со старыми фресками. Некоторые рисунки будто смотрят на вас."
        ),
        "exits": {"west": "hall", "north": "garden"},
        "items": ["note"],
        "puzzle": None,
    },
    "garden": {
        "description": (
            "Неожиданно — подземный сад. Тут влажно, пахнет травой. В центре — каменный стол."
        ),
        "exits": {"south": "gallery"},
        "items": [],
        "puzzle": ("На столе выгравировано: 2 + 3 = ? (введите цифрой)", "5"),
    },
    "crypt": {
        "description": (
            "Склеп с холодным воздухом. Слышно капание воды. На полу валяется старая монета."
        ),
        "exits": {"south": "trap_room"},
        "items": ["coin"],
        "puzzle": None,
    },
    "gate_room": {
        "description": (
            "Перед вами массивная дверь с символами. Дальше — сокровищница. "
            "Кажется, дверь реагирует на ваши действия."
        ),
        "exits": {"south": "hall", "north": "treasure_room"},
        "items": [],
        "puzzle": None,
    },
    "treasure_room": {
        "description": (
            "Комната, на столе большой сундук. Дверь защищена механизмом — нужен код."
        ),
        "exits": {"south": "gate_room"},
        "items": ["treasure_chest"],
        "puzzle": (
            "Дверь защищена кодом. Введите код (подсказка: 2*5 = ?)",
            "10",
        ),
    },
}