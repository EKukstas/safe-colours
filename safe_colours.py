class safeColours:

    """
    A module that provides colour-blind safe plotting colours.
    It can return either a dictionary of named colours, a list of a 
    chosen number of colours (1 to 12) with the largest contrast, or
    a colourmap to be used for colourbars and contour plots, etc.
    """

    # colour table in HTML hex format
    hexcols = ['#332288', '#88CCEE', '#44AA99', '#117733', '#999933', '#DDCC77', 
                '#CC6677', '#882255', '#AA4499', '#661100', '#6699CC', '#AA4466',
                '#4477AA']

    # a set of greysafe colours. Present for posterity but not used - effect is minimal.
    # Just use different line styles.
    greysafecols = ['#809BC8', '#FF6666', '#FFCC66', '#64C204']

    # array of lists of colour indices that maximise colour contrast
    xarr = [[12], 
            [12, 6], 
            [12, 6, 5], 
            [12, 6, 5, 3], 
            [0, 1, 3, 5, 6], 
            [0, 1, 3, 5, 6, 8], 
            [0, 1, 2, 3, 5, 6, 8], 
            [0, 1, 2, 3, 4, 5, 6, 8], 
            [0, 1, 2, 3, 4, 5, 6, 7, 8], 
            [0, 1, 2, 3, 4, 5, 9, 6, 7, 8], 
            [0, 10, 1, 2, 3, 4, 5, 9, 6, 7, 8], 
            [0, 10, 1, 2, 3, 4, 5, 9, 6, 11, 7, 8]]

    @classmethod
    def distinct_named(cls):
        """
        Give colours a name and return it as a dictionary.
        """
        cl = cls.hexcols

        outdict = {'navy':cl[0],\
                    'cyan':cl[1],\
                    'turquoise':cl[2],\
                    'green':cl[3],\
                    'olive':cl[4],\
                    'sandstone':cl[5],\
                    'coral':cl[6],\
                    'maroon':cl[7],\
                    'magenta':cl[8],\
                    'brown':cl[9],\
                    'skyblue':cl[10],\
                    'pink':cl[11],\
                    'blue':cl[12]}

        return outdict
    
    @classmethod
    def distinct_list(cls, nr):
        """
        Give a distinct list with highest contrast for nr number of colours.
        """

        # check if nr is in correct range
        if nr < 1 or nr > 12:
            print("wrong nr of distinct colours!")
            return

        # get list of indices
        lst = cls.xarr[nr-1]
        
        # generate colour list by stepping through indices and looking them up
        # in the colour table
        i_col = 0
        col = [0] * nr
        for idx in lst:
            col[i_col] = cls.hexcols[idx]
            i_col+=1
        return col


    # For making colourmaps.
    # Usage: cmap = safe_colours.colourmap('rainbow')
    @classmethod
    def colourmap(cls, maptype, invert=False):

        if maptype == 'diverging':
            # Deviation around zero colormap (blue--red)
            cols = []
            for x in np.linspace(0, 1, 256):
	            rcol = 0.237 - 2.13*x + 26.92*x**2 - 65.5*x**3 + 63.5*x**4 - 22.36*x**5
	            gcol = ((0.572 + 1.524*x - 1.811*x**2)/(1 - 0.291*x + 0.1574*x**2))**2
	            bcol = 1/(1.579 - 4.03*x + 12.92*x**2 - 31.4*x**3 + 48.6*x**4 - 23.36*x**5)
	            cols.append((rcol, gcol, bcol))

            if invert==True:
                cols = cols[::-1]

            return plt.get_cmap(matplotlib.colors.LinearSegmentedColormap.from_list("PaulT_plusmin", cols))

        elif maptype == 'heat':
            # Linear colormap (white--red)
            cols = []
            for x in np.linspace(0,1, 256):
	            rcol = (1 - 0.392*(1 + erf((x - 0.869)/ 0.255)))
	            gcol = (1.021 - 0.456*(1 + erf((x - 0.527)/ 0.376)))
	            bcol = (1 - 0.493*(1 + erf((x - 0.272)/ 0.309)))
	            cols.append((rcol, gcol, bcol))

            if invert==True:
                cols = cols[::-1]

            return plt.get_cmap(matplotlib.colors.LinearSegmentedColormap.from_list("PaulT_linear", cols))

        elif maptype == 'rainbow':
            # Linear colormap (rainbow)
            cols = []
            for x in np.linspace(0,1, 254):
	            rcol = (0.472-0.567*x+4.05*x**2)/(1.+8.72*x-19.17*x**2+14.1*x**3)
	            gcol = 0.108932-1.22635*x+27.284*x**2-98.577*x**3+163.3*x**4-131.395*x**5+40.634*x**6
	            bcol = 1./(1.97+3.54*x-68.5*x**2+243*x**3-297*x**4+125*x**5)
	            cols.append((rcol, gcol, bcol))

            if invert==True:
                cols = cols[::-1]

            return plt.get_cmap(matplotlib.colors.LinearSegmentedColormap.from_list("PaulT_rainbow", cols))

        else:
            raise KeyError('Please pick a valid colourmap, options are "diverging", "heat" or "rainbow"')

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from scipy.special import erf