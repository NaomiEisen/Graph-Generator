from utils.colors import ColorPalette

class DeviceAndHostGraphConfig:
    TITLE = 'memcpy (ce) between host and devices'
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
    

class D2DMemcpyCeGraphConfig:
    TITLE = 'memcpy (ce) device to device'
    TITLE_SIZE = 20

    X_AXIS = 'tests name'
    Y_AXIS = 'bandwidth (GB/s)'
    AXIS_LABEL_FONT_SIZE = 12

    LEGEND_FONT_SIZE = 12
    BAR_LABEL_FONT_SIZE = 12
    
    BAR_WIDTH = 0.25
    WIDTH = 16
    HEIGHT = 10

    COLOR_THEME = ColorPalette.BASIC_THEME