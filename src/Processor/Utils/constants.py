

TAG_CLASS_NAMES = {0: 'CircleLine', 1: 'Leaf', 2: 'Note1', 3: 'Unknown', 4: 'DD', 5: 'Peace', 6: 'Question', 7: 'Pillars', 8: 'HH', 9: 'Ampersand', 10: 'PP', 11: 'Hash', 12: 'Power', 13: 'Ankh', 14: 'TT', 15: 'Trident', 16: 'Asterisk', 17: '4', 18: 'Lines3', 19: '1', 20: '0', 21: '3', 22: 'Plane', 23: '5', 24: 'CircleHalf', 25: '7', 26: 'Sun', 27: '8', 28: 'Omega', 29: 'ArrowHollow', 30: 'AA', 31: 'Note2', 32: 'Radioactive', 33: 'EE', 34: 'UU', 35: '6', 36: 'Plant', 37: 'GG', 38: 'XX', 39: 'ZZ', 40: 'Necklace', 41: 'Umbrella', 42: 'Triangle', 43: 'Dot', 44: 'a', 45: 'Heart', 46: 'e', 47: 'RR', 48: 'KK', 49: 'h', 50: 'Queen', 51: 'Tadpole', 52: 'n', 53: 'MM', 54: '2', 55: 'r', 56: 'ArrowLine', 57: 'y', 58: 'Scissors', 59: 'CircleCross'}

TAG_CLASS_NAMES = {50: 'Queen', 3: 'Unknown'}

TREATMENT_CLASS_NAMES = {}
CONTROL_CLASS_NAMES = {}
NIGHT_HOURS = [19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6]

unknown_class_num = None
queen_class_num = None
for tag_class in TAG_CLASS_NAMES.keys():
    if TAG_CLASS_NAMES[tag_class] == 'Unknown':
        unknown_class_num = tag_class
    if TAG_CLASS_NAMES[tag_class] == 'Queen':
        queen_class_num = tag_class

FPS = 20
NUM_FRAMES_IN_VIDEO = FPS * 60 * 60
TAG_DIAMETER = 30
HALF_TAG_DIAMETER = int(TAG_DIAMETER / 2)
DOUBLE_TAG_DIAMETER = int(TAG_DIAMETER * 2)
PERIMETER_RADIUS = int(TAG_DIAMETER * 6)
MIN_NUM_SECONDS_SPENT_IN_AREA = 10
SECONDS_IN_45_MINS = 2700

MAX_FRAME_GAP_BETWEEN_PATHS = 1 * FPS
MAX_FRAME_GAP_BETWEEN_VIDEOS = 3 * FPS

UNKNOWN_CLASS = unknown_class_num
QUEEN_CLASS = queen_class_num
MIXED_CLASS = 'mixed'
GAP_CLASS = 'gap'

NUM_GROUP_CLASSIFICATIONS = 40
MIN_NUM_CLASSIFIED_GROUP = 10
NUM_GROUPS_IN_SECTION = 5
CLASS_CONF_THRESH = 0.6
NUM_UNKNOWNS_IN_PATH_THRESHOLD = 3

NUM_X_CELLS = 80
NUM_Y_CELLS = 40
X_BINS = 3840/NUM_X_CELLS
Y_BINS = 2160/NUM_Y_CELLS