WIDTH = 960
HEIGHT = 640
FPS = 60
TILESIZE = 32

HEALTH_BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
FONT = "assets/font/PressStart2P-Regular.ttf"
FONT_SIZE = 18

WATER_COLOUR = "#D6F9FC"
MENU_BG_COLOUR = "#48769f"
BG_COLOUR = "#222222"
BORDER_COLOUR = "#111111"
TEXT_COLOUR = "#EEEEEE"
HEALTH_COLOUR = "green"


snowball = {
    "cooldown" : 100,
    "damage" : 10,
    "graphic" : "assets/snowball.png"
}

enemy = {
    "health" : 100,
    "damage" : 20,
    "attack_sound" : "assets/music/mixkit-impact-of-a-blow-2150.wav",
    "image" : "assets/snowman1.png",
    "speed" : 1,
    "resistance" : 3,
    "attack_radius" : 50,
    "notice_radius" : 280
}