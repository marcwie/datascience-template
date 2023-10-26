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
