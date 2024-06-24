from game_logic import * 



game = Game("")
print(game.welcome_message)
if game.secret_word == "":
    game.word_list_file_path = game.open_filemanager()
    print(game.word_list_file_path)
    game.secret_word = game.choose_word(file_path=game.word_list_file_path)
while True:
    print("- - - - - - - - - - - - - - -")
    game.get_user_input(input("Enter a letter: "))
    print(game.show_hidden_word())
    player_won = game.chack_for_win()
    if player_won == True:
       game.win_prompep()
    if game.tryies == 0:
        game.lose_prompep()