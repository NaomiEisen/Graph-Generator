from utils.colors import ColorPalette


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