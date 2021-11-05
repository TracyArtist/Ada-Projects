#!/bin/python3
import pydoc
#
# Complete the 'sales_summary' function below.
#

def sales_summary(packs_purchased, dice_purchased, board_games_purchased):
    """
    Parameters:
      packs_purchased: How many packs of trading cards each customer purchased.
      dice_purchased: How many sets of dice were each customer purchased.
      board_games_purchased: How many board games each customer purchased.
    """
    print("Welcome to the Ada's Game Emporium Sales Tracker!\n")

    packs_price = 4.25
    large_packs_price = 125.00
    dice_price = 11.00
    board_games_price = 50.00

    packs_total = []
    dice_total = []
    board_games_total = []
    total_spent = []

    for i in range(len(packs_purchased)):
        packs_purchased_rev = 0
        if (packs_purchased[i] >= 36):
            bulk_pack_num = int(packs_purchased[i] / 36)
            a = 125 * bulk_pack_num
            b = (packs_purchased[i] - (36 * bulk_pack_num)) * packs_price
            packs_purchased_rev = a + b
        else:
            packs_purchased_rev = packs_price * packs_purchased[i]

        packs_total.append(packs_purchased_rev)
        dice_total.append(dice_price * dice_purchased[i])
        board_games_total.append(board_games_price * board_games_purchased[i])
        total_spent.append(
            packs_purchased_rev + dice_price * dice_purchased[i] + board_games_price * board_games_purchased[i])
    # print(total_spent)
    format_string = "{0:.2f}"
    for i in range(len(packs_purchased)):
        print(f"Customer {i + 1} spent ${format_string.format(total_spent[i])}")
        print(f">>> ${format_string.format(packs_total[i])} for trading card packs")
        print(f">>> ${format_string.format(dice_total[i])} for dice sets")
        print(f">>> ${format_string.format(board_games_total[i])} for board games\n")

    # how to code the combinded total of each?
    total_customer_expense = 0
    dice_plus_board_games = 0
    most_profitable_customer = 0
    most_profitable_customer_num = -1
    for i in range(len(packs_purchased)):
        total_customer_expense += packs_total[i] + dice_total[i] + board_games_total[i]
        dice_plus_board_games += dice_total[i] + board_games_total[i]
    for i in range(len(packs_purchased)):
        current_customer_expense = packs_total[i] + dice_total[i] + board_games_total[i]
        if (most_profitable_customer <= current_customer_expense):
            most_profitable_customer_num = i + 1
            most_profitable_customer = current_customer_expense

    print(f"Combined all customers paid ${format_string.format(total_customer_expense)} total")
    print(f"Non-trading card products (dice + board games) were ${format_string.format(dice_plus_board_games)} total\n")

    print(f"${format_string.format(most_profitable_customer)} was the most paid by any single customer")
    print(f"The customer(s) that paid the most were: #{most_profitable_customer_num}")


def bootstrap():