from random import randint
from typing import List
from character_list import char_list


total_char_count = len(char_list)
chars_to_roll = 8


def get_random_char_indices(total: int = total_char_count, n: int = chars_to_roll) -> List:
    chars = []
    while len(chars) < n:
        char = randint(1, total)
        if char not in chars:
            chars.append(char)
    return chars


def get_char_names() -> List:
    indices = get_random_char_indices()
    chars = []
    for i in indices:
        chars.append(char_list[i-1])
    return chars


def make_teams() -> str:
    pool = get_char_names()
    half: int = int(chars_to_roll / 2)
    team1 = pool[0:half]
    team2 = pool[half:chars_to_roll]
    teams = f'Team 1: {team1}\nTeam 2: {team2}'
    return teams


print(make_teams())
input('Press Enter to exit...')
