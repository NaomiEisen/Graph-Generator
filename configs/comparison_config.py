from utils.colors import ColorPalette

OUTPUT_FOLDER = 'all_reduce_graph'

class ComparisonGraphConfig:
    TITLE_SIZE = 50
    TITLE = 'opt xml vs original xml'

    V1_LEGEND = 'opt xml'
    V2_LEGEND = 'original xml'

    BAR_WIDTH = 0.35
    Y_AXIS = 'bandwidth (GB/s)'
    X_AXIS = "GPU's"
    AXIS_LABEL_FONT_SIZE = 18
    BAR_LABEL_FONT_SIZE = 16
    COLOR_THEME = ColorPalette.COLOR_THEME_COMPARISON