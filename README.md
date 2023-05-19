# Backgammon - Phase 3 Project
# Racquel Glickman and Joshua Eichhorn

## Introduction

We built a CLI application to play Backgammon! Backgammon is a two-player game in which both players roll dice to try to maneuver their pieces around the board and score them. The first player to 15 wins!

In order to build our game, we set up 5 classes:

.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── game.py
    ├── board.py
    ├── player.py
    ├── column.py
    ├── move.py
    └── debug.py

The Game class initializes our game by calling the board to render and asking for user input to create players. 

The Board class initially creates 24 columns and sets up the pieces in the starting position. The Board class is also responsible for updating the rendering of the board and the location and color of the pieces. 

The Player class is responsible for keeping track of each player's name, color, score and direction in which they can move.

The Column class is responsible for keeping track of how many pieces are in each column after each turn, and whether the column is occupied by a specific player or not (i.e. whether there is more than one piece).

The Move class contains all of the logic for the game. Here, columns are updated with current numbers of pieces and occupying color after each turn. Each move is validated per the rules of the game, ensuring that a user is moving the amount of spaces corresponding to their die rolls and that each move is legal. User input is also validated to make sure that a user is only inputting what the game can understand. 

## Installation and Running the Game
In order to install all of the packages in our Pipfile, first enter pipenv install and then pipenv shell. Once inside the shell, to run the game, enter python lib/game.py. 

## Quick Rules of Backgammon

1. Players take turns rolling dice. On a player's turn, they enter an origin column to move from and then enter a valid destination column according to their die rolls. 
2. A piece can land on a column with its own color, a column with no color, or a column with only one piece of the opposite color. 
3. If a piece lands on a column with one piece of the opposite color, the opposite color's piece is put in jail.
4. The other player must leave jail before continuing to move their other pieces around the board on their turn. They leave jail by rolling a die roll that creates a valid destination from their starting zone (for red: columns 1-6, for white: columns 19-24). 
5. Once all of a player's pieces are in their endzone (for red: columns 19-24, for white: columns 1-6), they may use their die rolls to take pieces off of the board and score them. They do this by typing 'off'.
6. The first player to score all 15 of their pieces wins!

