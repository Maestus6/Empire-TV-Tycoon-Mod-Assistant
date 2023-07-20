import numpy as np 

def setHeaderAndPages():
    pages = np.arange(1, 5, 50) #entry (start, stop), lines between each entry 
    headers = {'Accept-Language': 'en-US,en;q=0.8'} # the default language is mandarin
