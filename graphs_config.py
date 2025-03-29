from utils.colors import ColorPalette

class ComparisonGraphConfig:
    TITLE_SIZE = 50
    TITLE = 'opt xml vs original xml'
    BAR_WIDTH = 0.35
    Y_AXIS = 'bandwidth (GB/s)'
    X_AXIS = "GPU's"
    AXIS_LABEL_FONT_SIZE = 18
    BAR_LABEL_FONT_SIZE = 16
    COLOR_THEME = ColorPalette.COLOR_THEME_OPT_VS_ORG


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
    COLOR_THEME = ColorPalette.COLOR_THEME_OPT_VS_ORG


class GpuBandwidthGraphConfig:
    TITLE_SIZE = 50
    TITLE = 'bandwidthTest'
    X_AXIS = 'Transfer Size (Bytes)'
    Y_AXIS = 'Bandwidth(GB/s)'
    AXIS_LABEL_FONT_SIZE = 30
    LEGEND_FONT_SIZE = 20
    WIDTH = 30
    HEIGHT = 18
    Y_NBINS = 20
    COLOR_THEME = ColorPalette.DARK_COLOR_THEME_MINI
