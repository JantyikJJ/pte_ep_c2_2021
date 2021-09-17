import random

map_size = 3
win_count = 3


tto = []
for ind in range(map_size * map_size):
    tto.append(0)


def int_to_char(n):
    if n == 0:
        return " "
    elif n == 1:
        return "*"
    else:
        return "0"


def print_map():
    for i in range(len(tto)):
        print("| " + int_to_char(tto[i]), end=" ")
        if (i + 1) % map_size == 0:
            if i < map_size * map_size - map_size:
                print("|\n|---|---|---|")
            else:
                print("|")
    print()


def get_input(text, acceptable):
    answer = input(text)
    if answer in acceptable:
        return answer
    return get_input(text, acceptable)


def gen_acceptable(n):
    acceptable = []
    for i in range(n):
        for j in range(n):
            acceptable.append(f"{i + 1} {j + 1}")
    return acceptable


def check_move(x, y, char):
    i = x - 1
    j = y - 1
    if tto[i * map_size + j] != 0:
        return False
    else:
        tto[i * map_size + j] = char
        return True


def make_user_move():
    acceptable = gen_acceptable(map_size)
    success = False

    while not success:
        answer = get_input("Hova szeretné rakni a jelét? (sor oszlop) pl.: 1 3: ", acceptable)
        nums = answer.split(' ')
        success = check_move(int(nums[0]), int(nums[1]), 2)
        if not success:
            print("Rossz lépés!")


def get_winner():
    # diagonal check
    for i in range(map_size - win_count + 1):
        for j in range(map_size - win_count + 1):
            if tto[i * map_size + j] == 0:
                continue
            count = 0
            for k in range(win_count):
                if tto[(i + k) * map_size + (j + k)] == tto[i * map_size + j]:
                    count += 1
                else:
                    break
            if win_count == count:
                return tto[i * map_size + j]

            count = 0
            for k in range(win_count - 1, 0):
                print(k)
                if tto[(i + (win_count - 1 - k)) * map_size + (j + k)] == tto[i * map_size + j]:
                    count += 1
                else:
                    break
            if win_count == count:
                return tto[i * map_size + j]

    # vertical + horizontal check
    for i in range(map_size):
        for j in range((map_size - win_count) + 1):
            if tto[i * map_size + j] == 0:
                continue
            # horizontal check
            count = 0
            for k in range(win_count):
                if tto[i * map_size + j + k] == tto[i * map_size + j]:
                    count += 1
                else:
                    break
            if win_count == count:
                return tto[i * map_size + j]

            # vertical check
            count = 0
            for k in range(win_count):
                if tto[(k + j) * map_size + i] == tto[j * map_size + i]:
                    count += 1
                else:
                    break
            if win_count == count:
                return tto[j * map_size + i]


    return 0


def is_playable():
    for i in range(map_size * map_size):
        if tto[i] == 0:
            return True
    return False


def make_pc_move():
    success = False

    while not success:
        x = random.randint(1, map_size)
        y = random.randint(1, map_size)
        success = check_move(x, y, 1)


pc_move = get_input("Kezdeni szeretne? (i/n): ", ["i", "n"]) == 'n'
in_game = True
winner = 0

while in_game:
    if pc_move:
        make_pc_move()
    else:
        make_user_move()

    pc_move = not pc_move

    print_map()
    winner = get_winner()
    in_game = winner == 0

    if in_game and not is_playable():
        in_game = False

if winner == 0:
    print("Senki se nyert!")
elif winner == 1:
    print("Gép nyert!")
elif winner == 2:
    print("Játékos nyert!")

