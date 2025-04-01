from utils.colors import ColorPalette

class NvBandwidthGraphConfig:
    TITLE_SIZE = 50
    X_AXIS = 'tests name'
    Y_AXIS = 'bandwidth (GB/s)'
    AXIS_LABEL_FONT_SIZE = 18
    LEGEND_FONT_SIZE = 16
    BAR_LABEL_FONT_SIZE = 16
    BAR_WIDTH = 0.35
    WIDTH = 30
    HEIGHT = 25
    COLOR_THEME = ColorPalette.COLORS_FOR_GRADIENT


class NvBandwidthCompareGraphConfig:
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
    COLOR_THEME = ColorPalette.COLORS_FOR_GRADIENT