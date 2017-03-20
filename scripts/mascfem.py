import fuzzyplot
import imp
imp.reload(fuzzyplot)

from fuzzyplot import FuzzyPlot
import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats import rice

def set_axes(fuz):
  fuz.set_ylim(0,0.5);
  fuz.set_xlim(0,1.0)
  fuz.set_yticks([]); 
  fuz.set_ylabel('Number of people'); 

  fuz.set_xlabel('Behavior/Appearance')
  fuz.set_xlabel_side('More feminine', 'left')
  fuz.set_xlabel_side('More masculine', 'right')

  fuz.tight_layout(); 

def plot_fake():
  fuz = FuzzyPlot(1)
  fuz.pseudo_bar(0.0,0.4,0.1, color='r')
  fuz.pseudo_bar(1.0,0.4,0.1, color='b')

  np.random.seed(203)
  
  colors = plt.get_cmap('RdYlBu')
  
  idx = np.random.permutation(np.arange(50))
  pall = np.linspace(0.08,0.92,50)
  for j in range(50):
    i = idx[j]
    p = pall[i] # np.random.uniform(0.08,0.92)
    h = np.random.uniform(0.05,0.2)
    w = np.random.uniform(0.005,0.03)
    fuz.pseudo_bar(p,h,w,color=((50-i)/50., 0., i/50., 1.0)) #'m')

  fuz.set_title("How the 'woke' left sees gender")
  set_axes(fuz)

  fuz.arrow("'men'", (0.85,0.45), (0.95,0.4))
  fuz.arrow("'women'", (0.15,0.45), (0.05,0.4))

  fuz.arrow('lotsa different genders\nto describe how\neach person feels', (0.5,0.35), (0.5,0.2), size=16)
  fuz.arrow('', (0.52,0.34), (0.75,0.2))
  fuz.arrow('', (0.48,0.34), (0.25,0.2))

def plot_gend():
  x,xx = fuzzyplot.skewed_data('left')
  x,xy = fuzzyplot.skewed_data('right')
  
  fuz = FuzzyPlot(2)
  fuz.plot(x,xy, color='b');
  fuz.plot(x,xx, color='r');

  fuz.set_title('How biology sees gender')
  set_axes(fuz)

  fuz.arrow("XX\n('women')",(0.3,0.35),(0.2,0.4))
  fuz.arrow("XY\n('men')",(0.7,0.35), (0.8,0.4))



