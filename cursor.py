"""
Scatter plots are highlighted point-by-point.
=============================================
... as opposed to lines with a ``"."`` style, which have the same appearance,
but are highlighted as a whole.
"""

import numpy as np
import matplotlib.pyplot as plt
import mplcursors

x, y, z = np.random.random((3, 10))
fig, axs = plt.subplots(3)
fig.suptitle("Highlighting affects individual points\n"
             "only in scatter plots (top two axes)")
axs[0].scatter(x, y, c=z, s=100 * np.random.random(10))
axs[1].scatter(x, y)
axs[2].plot(x, y,'o')
mplcursors.cursor(highlight = True)
plt.show()

"""
Annotate on hover
=================
When *hover* is set to ``True``, annotations are displayed when the mouse
hovers over the artist, without the need for clicking.
"""

import matplotlib.pyplot as plt
import numpy as np
import mplcursors
np.random.seed(42)

fig, ax = plt.subplots()
ax.plot(*np.random.random((2, 26)))
ax.set_title("Mouse over a point")

mplcursors.cursor(hover=True)

plt.show()
