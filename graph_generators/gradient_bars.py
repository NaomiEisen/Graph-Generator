import numpy as np

from utils.colors import ColorPalette


def gradient_bars(bars, type = 0):
    grad = np.linspace(0, 1, 256).reshape(-1, 1)

    start_color = ColorPalette.COLOR_THEME_OPT_VS_ORG[type]['start']
    end_color = ColorPalette.COLOR_THEME_OPT_VS_ORG[type]['end']

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