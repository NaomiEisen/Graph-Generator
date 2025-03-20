from utils.colors import ColorPalette

class NvBandwidthGraphConfig:
    TITLE_SIZE = 30

    X_AXIS = 'tests name'
    Y_AXIS = 'bandwidth (GB/s)'
    AXIS_LABEL_FONT_SIZE = 18

    LEGEND_FONT_SIZE = 12
    BAR_LABEL_FONT_SIZE = 12

    BAR_WIDTH = 0.1
    WIDTH = 30
    HEIGHT = 15

    COLOR_THEME = ColorPalette.DARK_COLOR_BAR_THEME1


class GpuBandwidthGraphConfig:
    TITLE_SIZE = 50
    TITLE = 'bandwidthTest'

    X_AXIS = 'Transfer Size (Bytes)'
    Y_AXIS = 'Bandwidth(GB/s)'
    AXIS_LABEL_FONT_SIZE = 18

    LEGEND_FONT_SIZE = 20

    WIDTH = 30
    HEIGHT = 18

    Y_NBINS = 20

    COLOR_THEME = ColorPalette.DARK_COLOR_BAR_THEME1
