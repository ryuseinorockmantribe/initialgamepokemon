
# colours
import config

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (106, 229, 153)
YELLOW = (237, 208, 33)
RED = (251, 87, 60)

SCALE = 32

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640

BATTLE_HEALTH_BAR_WIDTH = 102

MAP_TILE_GRASS = "G"
MAP_TILE_WATER = "W"
MAP_TILE_ROAD = "R"
MAP_TILE_DOOR = "1"
MAP_TILE_DOORS = ["1", "2", "3", "4", "5", "6", "7", "8"]
MAP_TILE_LAB_FLOOR = "L"
MAP_TILE_LAB_WALL = "l"
MAP_TILE_ROOM_EXIT = "X"
MAP_TILE_BUILDING = "."

MONSTER_TYPES = ["G", "W", "S", "F"]

IMPASSIBLE = [MAP_TILE_WATER, MAP_TILE_LAB_WALL, MAP_TILE_BUILDING]

MAP_CONFIG = {
    "01" : {
        "start_position": [9, 29],
        "exits" : [
        {
            "map" : "02",
            "position" : [3, 0],
            "new_start_position": [1, 4],
        }],
        "buildings": [
            {
                "sprite": "04",
                "name": "Research Building",
                "position": [10, 2],
                "size" : [4, 5]
            },
            {
                "sprite": "05",
                "name": "Home",
                "position": [6, 26],
                "size" : [5, 3]
            }
        ],
    }
}