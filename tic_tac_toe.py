import wikipediaapi


def game_setup():
    print("Welcome to a game of Tic-Tac-Toe!")
    num_players = int(input("How many players are going to play?"))
    rule_display = input("Would you like to see the rules? Y/N")

    return num_players, rule_display


def fetch_ruleset_from_wiki():
    wiki_wiki = wikipediaapi.Wikipedia('en')
    wiki_summary = wiki_wiki.page('Tic-Tac-Toe').summary
    
    return wiki_summary


def display_grid(grid):
    print(f"{grid[0][0]} | {grid[0][1]} | {grid[0][2]}")
    print("----------")
    print(f"{grid[1][0]} | {grid[1][1]} | {grid[1][2]}")
    print("----------")
    print(f"{grid[2][0]} | {grid[2][1]} | {grid[2][2]}")


def player_picks_spot(current_player, turn, grid):
    if turn % 2 == 1:
        current_val = 'X'
    else:
        current_val = 'O'

    player_selection = int(input(f"{current_player} you are {current_val}'s.  Please choose the number on the grid that you would like to place an {current_val}:"))
    sub_val = ''
    for sub_grid in grid:
        try:
            sub_val = sub_grid.index(player_selection)
            sub_grid[:] = [current_val if x == player_selection else x for x in sub_grid]
        except ValueError:
            pass

    if sub_val == '':
        print("I don't think you made a valid selection. Try again.")
        player_picks_spot(current_player, turn, grid)


def check_for_win_condition(current_player, grid):
    for sub_grid in grid:
        if len(set(sub_grid)) == 1:
            print("Winner, winner.  Chicken dinner!")
            return current_player

def game_turn(grid, current_player, turn):
    display_grid(grid)
    player_picks_spot(current_player, turn, grid)
    winner = check_for_win_condition(current_player, grid)
    if winner:
        return winner


def we_have_a_winner(grid, winner, players):
    print(f"{winner} wins!")

    for k, v in players.items():
        print(f"{v['name']} has {v['score']} wins.")

    play_again = input("Would you like to play again? Y/N")

    if play_again:
        if play_again.lower() == 'y':
            if len(players.keys()) == 2:
                two_player_game(players)


def two_player_game(players={}):
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    turn = 1
    current_player = ''

    if players:
        if turn % 2 == 1:
            current_player = next(iter(players))
        else:
            current_player = next(next(iter(players)))
    else:
        player_one = input("Player One: what is your name?")
        player_two = input("Player Two: what is your name?")

        players[player_one] = {'name': player_one, 'score': 0}
        players[player_two] = {'name': player_two, 'score': 0}

    while turn <= 9:
        if turn % 2 == 1:
            if not current_player:
                current_player = players[player_one]['name']
        else:
            if not current_player:
                current_player = players[player_two]['name']

        winner = game_turn(grid, current_player, turn)
        if winner:
            players[current_player]['score'] += 1
            we_have_a_winner(grid, winner, players)
            break

        turn += 1


def init_game(player_qty, show_rule):
    if show_rule:
        if show_rule.lower() == 'y':
            ruleset = fetch_ruleset_from_wiki()
            if ruleset:
                print(f"Here are the rules for Tic-Tac-Toe according to Wikipedia:\n{ruleset}")
    
    if player_qty == 2:
        two_player_game()
            

def main():
    num_players, rule_display = game_setup()
    init_game(num_players, rule_display)


if __name__ == '__main__':
    main()