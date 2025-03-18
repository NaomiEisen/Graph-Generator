from globals import ColorPalette

class DeviceAndHostGraphConfig:
    TITLE = 'memcpy between host and devices'
    X_AXIS = 'tests name'
    Y_AXIS = 'bandwidth (GB/s)'
    AXIS_LABEL_FONT_SIZE = 18
    TITLE_SIZE = 20

    COLOR_THEME = ColorPalette.COLOR_BAR_THEME
    BAR_WIDTH = 0.1
    WIDTH = 30
    HEIGHT = 12

class D2DMemcpyCeGraphConfig:
    TITLE = 'memcpy between host and devices'
    X_AXIS = 'tests name'
    Y_AXIS = 'bandwidth (GB/s)'
    AXIS_LABEL_FONT_SIZE = 12
    TITLE_SIZE = 14
    COLOR_THEME = ColorPalette.BASIC_THEME
    BAR_WIDTH = 0.25
    WIDTH = 16
    HEIGHT = 10