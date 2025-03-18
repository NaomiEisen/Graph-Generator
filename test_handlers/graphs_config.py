from colors import ColorPalette

class DeviceAndHostGraphConfig:
    TITLE = 'memcpy between host and devices'
    TITLE_SIZE = 20

    X_AXIS = 'tests name'
    Y_AXIS = 'bandwidth (GB/s)'
    AXIS_LABEL_FONT_SIZE = 18

    BAR_WIDTH = 0.1
    WIDTH = 30
    HEIGHT = 12

    COLOR_THEME = ColorPalette.COLOR_BAR_THEME
    

class D2DMemcpyCeGraphConfig:
    TITLE = 'memcpy between host and devices'
    TITLE_SIZE = 14

    X_AXIS = 'tests name'
    Y_AXIS = 'bandwidth (GB/s)'
    AXIS_LABEL_FONT_SIZE = 12
    
    BAR_WIDTH = 0.25
    WIDTH = 16
    HEIGHT = 10

    COLOR_THEME = ColorPalette.BASIC_THEME