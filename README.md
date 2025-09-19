# Airport Mapper Game ✈️🗺️
This interactive Python game challenges players to match airport codes to their correct geographic locations on a map. Built using Pygame, it features 123 airport codes and delivers 5-question rounds with real-time scoring and feedback.

Gameplay:
- Each round presents 5 airport codes.
- Players click on the map to identify the correct city for each code.
- Accuracy is measured by proximity (±6 pixels) to the correct coordinates.
- Incorrect guesses are listed at the end of each round.

Tech Stack:
- Python 3.10+
- Pygame (UI and event handling)
- Pandas (answer validation)
- CSV (data persistence)

Installation:
-Create a folder "testMapGame"
-Change directory to the folder: cd ...\testMapGame
-Clone repo: git clone https://github.com/kamarkseit/map-game1-airport-codes.git
-Open Anaconda Prompt
-Create an environment: conda create -n mapgame-env python=3.10
-Activate it: conda activate mapgame-env
-Change directory: cd ...\testMapGame
-Install dependencies: pip install -r requirements.txt
-Run the game: python MapGame_v2.py

Architecture Notes:
- `main.py`: Game loop, event handling, scoring logic
- `game_dictionary()`: Loads airport codes and map tiles
- `draw_bg()`, `draw_gamer_airports()`, `draw_text()`: UI rendering
- `helper_box()`: Displays hints or instructions
- `gamer_answers.csv`: Stores player responses
- `correct_answers.csv`: Stores ground truth coordinates

Scoring Logic:
- Player clicks are compared to correct coordinates.
- If within ±6 pixels on both axes, the answer is marked correct.
- Score is displayed dynamically during gameplay.
