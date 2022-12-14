import character
import trivia
import black_jack_func
import tictac
import noir_items

interactions_essential = {
    'Jeremy': {
        'game_offer': 'PLAYER: Hey, Jeremy. Do you know who stole the gerbil?\nJEREMY: I do! I will tell you if you beat me at Tic-Tac-Toe.\n\tWould you like to play Tic-Tac-Toe?(y/n): ',
        'conclusion': 'JEREMY: Congratulations! I saw Lucy open the cage but I don\'t know why.'},
    'Ms. Frizzle': {
        'game_offer': 'PLAYER: Hello Mrs. Frizzle. Could I have a hall pass?\nMRS. FRIZZLE: Sure. I will write you one if you pass this quiz I wrote.\nWould you like to try it out?(y/n): ',
        'conclusion': 'Congratulations! Here\'s your hall pass.'},
    'Red McGuffin': {
        'game_offer': 'PLAYER: Hi Red, you\'re on the Gerbil Crew right? Do you know who else access to the gerbil cage?\nRED McGUFFIN: Yup. But I\'ll only tell you if you beat me at blackjack. Wanna play?(y/n): ',
        'conclusion': 'That was a good hand. Here\'s a list of the rest of the people on the crew. They all have keys to the cage.'},
    'Ned Beasley': {
        'game_offer': 'PLAYER: Hey Ned, I need some information about a missing classroom pet. Have you seen anything that might help? NED BEASLEY: Hmmm... Yeah I do think I did see something this morning. How about you answer some questions I\'ve got and if you answer most of them I\'ll help you out?? (y/n): ',
        'conclusion': 'Nice, dude! So look, this morning I did someone lurking around the classroom before 8:30. Looked like a girl but I couldn\'t really tell. That\'s all I got'}
}

interactions_nonessential = {
    'Adam Jacobs': 'PLAYER: Hi Adam, do you know who took the gerbil?\nADAM: Uh, no?',
    'Bryce Balin': 'PLAYER: Hi Bryce, do you know who took the gerbil?\nADAM: Uh, no?',
    'Becky Barnett': 'PLAYER: Hi Becky, do you know who took the gerbil?\nADAM: Uh, no?',
    'Jered Kropholler': 'PLAYER: Hi Jered, do you know who took the gerbil?\nADAM: Uh, no?',
    'Tanner Laramie': 'PLAYER: Hi Tanner, do you know who took the gerbil?\nADAM: Uh, no?',
    'Jessica Nathenson': 'PLAYER: Hi Jessica, do you know who took the gerbil?\nADAM: Uh, no?',
    'Judy Wrench': 'PLAYER: Hi Judy, do you know who took the gerbil?\nADAM: Uh, no?',
    'Lucy Zastophil': 'You walk over to Lucy Zastophil and see that she is wearing a tie-dyed shirt which has the word ???PETA??? on the front.\nPLAYER: Hello, Lucy. Did you take the gerbil?\nLUCY: Fur is murder you facist.\nPLAYER: So the quickest way out of here is the way I came right?\nYou leave'
}

character_list = {'ms_frizzle': character.NpcEssential(
    'Ms. Frizzle',
    'Middle aged science teacher',
    interactions_essential,
    mini_game=trivia.trivia_game,
    gameparam='science',
),

    'ned_beasley': character.NpcEssential(
        'Ned Beasley',
        'Resident comic-book expert',
        interactions_essential,
        mini_game=trivia.trivia_game,
        gameparam='comics',
    ),

    'jeremy': character.NpcEssential(
        'Jeremy',
        'Tic-Tac-Toe Student',
        interactions_essential,
        mini_game=tictac.TicTacToe,
        gameparam='player'
    ),

    'red_mcguffin': character.NpcEssential(
        'Red McGuffin',
        'blackjack student Student',
        interactions_essential,
        mini_game=black_jack_func.black_jack,
        gameparam='player'
    ),
    'adam_jacobs': character.NpcNonEssential(
        'Adam Jacobs',
        'description',
        interactions_nonessential
    ),
    'bryce_balin': character.NpcNonEssential(
        'Bryce Balin',
        'description',
        interactions_nonessential
    ),
    'becky_barnett': character.NpcNonEssential(
        'Becky Barnett',
        'description',
        interactions_nonessential
    ),
    'jered_kropholler': character.NpcNonEssential(
        'Jered Kropholler',
        'description',
        interactions_nonessential
    ),
    'tanner_laramie': character.NpcNonEssential(
        'Tanner Laramie',
        'description',
        interactions_nonessential
    ),
    'jessica_nathenson': character.NpcNonEssential(
        'Jessica Nathenson',
        'description',
        interactions_nonessential
    ),
    'judy_wrench': character.NpcNonEssential(
        'Judy Wrench',
        'description',
        interactions_nonessential
    ),
    'lucy_zastophil': character.NpcNonEssential(
        'Lucy Zastophil',
        'description',
        interactions_nonessential
    ),
}
clues = {
    'red_clue': noir_items.Item(
        'Team List',
        'A list of the members of the animal team',
        False,
        False,
        'The animal cage is locked so only animal team members would have access to the cage',
        5
    ),
    'frizz_clue': noir_items.Item(
        "Ms Frizzle ultimate clue",
        "Bad student kid thing is allergic yo",
        False,
        False,
        "not bad dude", 5)
}
character_list['red_mcguffin'].inventory.append(clues['red_clue'])
character_list['ms_frizzle'].inventory.append(clues['frizz_clue'])
