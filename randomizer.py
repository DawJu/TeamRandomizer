import json
from random import randint
from typing import List


def load_char_list(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        char_list = json.load(file)
    return char_list


char_list = load_char_list('character_list.json')
total_char_count = len(char_list)
chars_to_roll = 8


def get_random_char_indices(total: int = total_char_count, n: int = chars_to_roll) -> List[int]:
    chars = []
    while len(chars) < n:
        char = randint(1, total)
        if char not in chars:
            chars.append(char)
    return chars


def get_char_names() -> List[str]:
    indices = get_random_char_indices()
    chars = []
    for i in indices:
        chars.append(char_list[i - 1])
    return chars


def make_teams() -> str:
    pool = get_char_names()
    half = int(chars_to_roll / 2)
    team1 = pool[0:half]
    team2 = pool[half:chars_to_roll]
    teams = f'Team 1: {team1}\nTeam 2: {team2}'
    return teams


if chars_to_roll <= total_char_count:
    while True:
        print(make_teams())
        user_input = input('[r] - Reroll\t')
        if user_input.lower() != 'r':
            break
