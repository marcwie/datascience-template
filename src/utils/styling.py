import string


def hide_and_move_axis(axis, hide=['right', 'top'], move=3):
    """
    Hide spines of an axis and move the remaining visible one's outward.
    """
    for position in ['left', 'right', 'bottom', 'top']:

        if position in hide:
            axis.spines[position].set_visible(False)
        else:
            axis.spines[position].set_position(('outward', move))

    if 'left' in hide and 'right' not in hide:
        axis.yaxis.tick_right()
        axis.yaxis.set_label_position('right')

    if 'left' not in hide and 'right' in hide:
        axis.yaxis.tick_left()
        axis.yaxis.set_label_position('left')

    if 'left' not in hide and 'right' not in hide:
        pass
        #axis.yaxis.set_label_position('both')

    if 'left' in hide and 'right' in hide:
        axis.set_yticks([])


def add_label(axarr, pos, size=20, offset=0.075):
    """
    Adds sequential labels to a set of matplotlib axes.

    Uses upper case labels, i.e., 'A', 'B', ...

    Args:
        axarr (np.array):
            Array containing all matplolib axes
        pos (list of strings):
            Position of the desired labels. Must be the same length as the number of axes.
            Valid values: ['upper left', 'upper right', 'lower left', 'lower right']
        size (int, optional):
            Text size. Defaults to 20.
        offset (float, optional):
            The offset from the boundary of the axes at which the label is displayed.
            Must be between 0 and 1. Defaults to 0.075.
    """
    for i, ax in enumerate(axarr.flatten()):
        label = string.ascii_uppercase[i]

        if pos[i].split(' ')[0] == 'upper':
            y = 1 - offset
        else:
            y = offset

        if pos[i].split(' ')[1] == 'left':
            x = offset
        else:
            x = 1 - offset

        ax.text(x, y, label, horizontalalignment='center', verticalalignment='center',
                transform = ax.transAxes, size=size)