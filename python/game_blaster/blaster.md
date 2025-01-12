# Blaster Game Description

This is a simple blaster game built using Pygame. The game features two players who can move around the screen, shoot projectiles, and collect perks. The objective is to win 5 rounds by reducing the opponent's health to zero. Each player starts with 100 health points, and each hit from a projectile reduces the player's health by 5 points. When a player's health reaches zero, the opponent wins the round. The first player to win 5 rounds is declared the overall winner.

## Game Features

1. **Players**:
   - Player One: Moves using W, A, S, D keys and shoots using the F key.
   - Player Two: Moves using arrow keys and shoots using the / key.
   - Players cannot move outside the game window boundaries.
   - Players are represented by the `player.png` image (104x58).
   - Players rotate in the direction of movement and shoot in the direction they are facing.

2. **Background**:
   - The game background is represented by the `grass.jpeg` image.

3. **Walls**:
   - A small wall is placed on the screen that players cannot pass through but can go around.
   - The wall is represented by a dark black rectangle with 60% opacity.
   - The wall size is 400x50.

4. **Projectiles**:
   - Players can shoot projectiles in the direction they are facing.
   - There is a 0.5-second delay between shots to make the shooting more realistic.
   - Projectile fires from the gun barrel of the players.

5. **Perks**:
   - Randomly appear on the screen.
   - Types of perks: `randomPotion` (decreases opponent player's health by 50), `increaseFireRate` (increases the perk owner's fire rate), `freeze` (freezes the opponent).
   - Perks are valid for 5 seconds after being collected.

6. **Game Loop**:
   - Handles events, updates player positions, handles shooting, checks collisions, detects winners, handles perks, and updates the screen.

7. **Winning Sound**:
   - Plays `winning.mp3` when a player wins the game.

## How to Run

1. Ensure you have Python and Pygame installed.
2. Run the `blaster.py` file to start the game.

```sh
python blaster.py
```

## Controls

- Player One:
  - Move: W, A, S, D
  - Shoot: F
- Player Two:
  - Move: Arrow Keys
  - Shoot: /

### How to Collect Perks

- Green circles appear randomly on the screen as perks.
- Move your player over the perk to collect it.
- Perks are valid for 5 seconds after being collected.

## Code Structure and Functionality

- `blaster.py`: Contains the main game loop and handles user input and game updates in this one file.

### Variables

- `WIDTH`, `HEIGHT`: Dimensions of the game window.
- `win`: The game window surface.
- `shoot_sound`, `winning_sound`: Sound effects for shooting and winning.
- `background`: The game background image.
- `player1_image`, `player2_image`: Images representing the players.
- `player1_pos`, `player2_pos`: Positions of player 1 and player 2.
- `player1_health`, `player2_health`: Health of player 1 and player 2.
- `player1_score`, `player2_score`: Scores of player 1 and player 2.
- `projectiles`: List of active projectiles.
- `perks`: List of active perks.
- `current_perk`: The currently active perk.
- `perk_start_time`: The time when the current perk was collected.
- `start_time`: The time when the game started.
- `fire_rate_multiplier`: Multiplier for the fire rate.
- `freeze_player`: Indicates which player is frozen.
- `last_shot_time_p1`, `last_shot_time_p2`: The last time player 1 and player 2 shot a projectile.
- `shot_delay`: Delay between shots.
- `wall_pos`, `wall_size`, `wall_color`: Position, size, and color of the wall.
- `player1_direction`, `player2_direction`: Directions player 1 and player 2 are facing.

### Functions

- `main()`: The main game loop.
- `handle_movement(keys)`: Handles player movement based on keyboard input.
- `is_colliding_with_wall(player_pos, direction)`: Checks if a player is colliding with the wall.
- `is_projectile_colliding_with_wall(projectile_pos, direction)`: Checks if a projectile is colliding with the wall.
- `handle_shooting(keys)`: Handles shooting projectiles based on keyboard input.
- `update_projectiles()`: Updates the positions of projectiles and checks for collisions.
- `check_collisions()`: Checks for collisions between projectiles and players.
- `spawn_perks()`: Spawns perks randomly on the screen.
- `handle_perks()`: Handles the collection and effects of perks.
- `apply_perk(perk, player)`: Applies the effect of a collected perk to a player.
- `draw_window()`: Draws the game elements on the screen.
- `get_rotation_angle(direction)`: Gets the rotation angle for a player image based on the direction.
- `display_status()`: Displays the status of players and the game.
- `check_winner()`: Checks for round winners and updates scores.
- `display_winner(message)`: Displays the winner message and ends the game.
- `reset_round()`: Resets the game variables for a new round.
