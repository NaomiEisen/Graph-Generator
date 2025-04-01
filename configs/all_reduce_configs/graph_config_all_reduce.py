from utils.colors import ColorPalette


class AllReduceGraphConfig:
    TITLE_SIZE = 50
    TITLE = 'All Reduce Test'

    X_AXIS = ''
    Y_AXIS = ['usec', 'GB/sec']
    SUB_PLOT_TITLE = ['Latency', 'Bandwidth']

    AXIS_LABEL_FONT_SIZE = 30
    LEGEND_FONT_SIZE = 20
    COLOR_THEME = ColorPalette.DARK_COLOR_BAR_THEME

class AllReduceCompareGraphConfig:
    TITLE_SIZE = 50
    TITLE = 'Comparing all reduce tests'

    FILE_NAME= 'all_reduce_compare'

    V1_LEGEND = 'original xml'
    V2_LEGEND = 'updated xml'

    X_AXIS = ''
    Y_AXIS = ['usec', 'GB/sec']
    SUB_PLOT_TITLE = ['Latency', 'Bandwidth']
    AXIS_LABEL_FONT_SIZE = 30
    LEGEND_FONT_SIZE = 20
    COLOR_THEME = ColorPalette.DARK_COLOR_BAR_THEME
