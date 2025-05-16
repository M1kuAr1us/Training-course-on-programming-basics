import random

def generate_loto_card():
    """Generates a lotto card in the form of a dictionary"""
    card = {}
    numbers = list(range(1, 91))
    for row in range(3):
        row_nums = random.sample(numbers, 5)
        row_nums.sort()
        row_dict = {i: '' for i in range(9)}
        columns = random.sample(range(9), 5)
        for col, num in zip(columns, row_nums):
            row_dict[col] = num
        card[row] = row_dict
    return card

def print_card(card):
    """Formatted lotto card output"""
    for row in card.values():
        line = ''
        for col in range(9):
            val = row[col]
            line += f'{val:>3}' if val != '' else '  -'
        print(line)
    print()

def mark_card(card, number):
    """Replaces the number with 0 if it is on the card"""
    for row in card.values():
        for col in row:
            if row[col] == number:
                row[col] = 0

def is_winner(card):
    """Checks if the card contains a string of five zeros"""
    for row in card.values():
        if list(row.values()).count(0) == 5:
            return True
    return False

def main():
    numbers_pool = list(range(1, 91))
    random.shuffle(numbers_pool)

    player1_card = generate_loto_card()
    player2_card = generate_loto_card()

    print("Player 1 card:")
    print_card(player1_card)

    print("Player 2's card:")
    print_card(player2_card)

    for number in numbers_pool:
        input(f"Number extracted: {number} (enter y to continue) ")

        mark_card(player1_card, number)
        mark_card(player2_card, number)

        print("\nUpdated player 1 card:")
        print_card(player1_card)

        print("Updated player 2 card:")
        print_card(player2_card)

        if is_winner(player1_card):
            print("Player 1 won!")
            break
        if is_winner(player2_card):
            print("Player 2 won!")
            break

if __name__ == "__main__":
    main()