import numpy as np
import matplotlib.patches as mpatches

from utils.set_users_args import get_color_by_version
from data_structures.test_verion import TestVersion
from utils.colors import ColorPalette

# Create gradient effect
def gradient_bars(bars, test_version = TestVersion.V1):
    grad = np.linspace(0, 1, 256).reshape(-1, 1)

    start_color = ColorPalette.COLORS_FOR_GRADIENT[get_color_by_version(test_version)]['start']
    end_color = ColorPalette.COLORS_FOR_GRADIENT[get_color_by_version(test_version)]['end']

    # Convert hex colors to RGB
    start_rgb = np.array([int(start_color[i:i + 2], 16) for i in (1, 3, 5)]) / 255
    end_rgb = np.array([int(end_color[i:i + 2], 16) for i in (1, 3, 5)]) / 255

    # Create gradient transition
    gradient_rgb = np.outer(grad, end_rgb - start_rgb) + start_rgb

    ax = bars[0].axes
    lim = ax.get_xlim() + ax.get_ylim()

    for bar in bars:
        bar.set_zorder(1)
        bar.set_facecolor("none")
        x, y = bar.get_xy()
        w, h = bar.get_width(), bar.get_height()

        ax.imshow(gradient_rgb.reshape(256, 1, 3), extent=[x, x + w, y, y + h], aspect="auto", zorder=0)

    ax.axis(lim)

# update legend to have the same colors as the bars
def update_legends_colorscheme(fig, graph_config):
    fig.legend(handles=[
        mpatches.Patch(color=ColorPalette.COLORS_FOR_GRADIENT[get_color_by_version(TestVersion.V1)]['start'],
                       label=graph_config.V1_LEGEND),
        mpatches.Patch(color=ColorPalette.COLORS_FOR_GRADIENT[get_color_by_version(TestVersion.V2)]['start'],
                       label=graph_config.V2_LEGEND)
    ])