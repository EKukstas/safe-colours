# safe-colours
A module providing a set of colourblind-safe colours and colourmaps.

***

# Functionality
The module has three methods:
- `safeColours.distinct_named()` provides a dictionary of up to 13 different colours, all with unique names.
The available colour names are:
`navy`, `cyan`, `turquoise`, `green`, `olive`, `sandstone`, `coral`, `maroon`, `magenta`, `brown`, `skyblue`, `pink`, `blue`

- `safeColour.distinct_list(n_colours)` provides a list of length `n_colours` where the choices of colours maximise the contrast.

- `safeColour.colourmap(maptype, invert=False)` provides a choice of three colour maps. The `maptype` choices are: `diverging`, `heat`, `rainbow`. Setting `invert=True` reverses the colour sequence.