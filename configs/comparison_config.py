from utils.colors import ColorPalette

OUTPUT_FOLDER = 'all_reduce_graph'

class ComparisonGraphConfig:
    TITLE_SIZE = 50
    TITLE = 'updated xml vs original xml'

    V1_LEGEND = 'original xml'
    V2_LEGEND = 'updated xml'

    BAR_WIDTH = 0.35
    Y_AXIS = 'bandwidth (GB/s)'
    X_AXIS = "GPU's"
    AXIS_LABEL_FONT_SIZE = 18
    BAR_LABEL_FONT_SIZE = 12

    OUTPUT_FILE_PREFIX = 'org-xml-vs-upd-xml_'
    COLOR_THEME = ColorPalette.COLOR_THEME_COMPARISON