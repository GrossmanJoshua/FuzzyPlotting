import matplotlib.pyplot as plt

plt.xkcd()

class FuzzyPlot:
  '''Uses plotting with an XKCD style to make concepts that
  are less than quantitative clear'''
  def __init__(self, *figargs, **figkw):
    self.fig = plt.figure(*figargs, **figkw)
    self.fig.clf()
    self.ax = self.fig.add_subplot(1,1,1)
    self.ax.set_axis_bgcolor('#fafafa')
    self.ax.set_xticks([])
    self.ax.set_yticks([])
   
  def set_xlabel_side(self, title, side, color='#555555', **annotateargs):
    '''Set the Xaxis to a range where the left side has
    one string and the right side has another. E.g.:
    
    .set_xlabel('size')
    .set_xlabel_side('smaller', 'left')
    .set_xlabel_side('larger', 'right')
    
    '''
    ax = self.ax
    trans = ax.get_xaxis_transform()
    a,b = ax.get_xlim()
    w=b-a
    if side == 'left':
      ax.annotate(title, (a,-0.02), (a + 0.1*w,-0.02),
        xycoords=trans, ha='left',va='center', annotation_clip=False, color=color,
        arrowprops=dict(arrowstyle='-|>',fc=color,ec=color),
        **annotateargs)
    elif side == 'right':
      ax.annotate(title, (b,-0.02), (a+0.9*w,-0.02),
        xycoords=trans, ha='right',va='center', annotation_clip=False, color=color,
        arrowprops=dict(arrowstyle='-|>',fc=color,ec=color),
        **annotateargs)
    else:
      raise ArgumentError("illegal side: {}".format(side))
      
  #def xaxis_ranges(self, title, left_range, right_range):
    #'''Set the Xaxis to a range where the left side has
    #one string and the right side has another. E.g.:
    
    #xaxis_ranges("Size", "Smaller", "Larger")
    
    #'''
    
    #ax = self.ax
    #c = '#555555'
    #ax.set_xlabel(title)
    #trans = ax.get_xaxis_transform()
    #a,b = ax.get_xlim()
    #w=b-a
    #ax.set_xticks([])
    #ax.annotate(left_range, (a,-0.02), (a + 0.1*w,-0.02),
      #xycoords=trans, ha='left',va='center', annotation_clip=False, color=c, arrowprops=dict(arrowstyle='-|>',fc=c,ec=c))
    #ax.annotate(right_range, (b,-0.02), (a+0.9*w,-0.02),
      #xycoords=trans, ha='right',va='center', annotation_clip=False, color=c, arrowprops=dict(arrowstyle='-|>',fc=c,ec=c))
  
  def arrow(self, text, startxy, endxy, size=24, **annkw):
    '''Draw an arrow with text at a given position. The
    text is drawn at `startxy` and the end of the arrow
    is at `endxy`.
    '''
    ax = self.ax
    if startxy[0] < endxy[0]:
      ha='right'
    elif startxy[0] > endxy[0]:
      ha='left'
    else:
      ha='center'
    ha='center'
    if startxy[1] < endxy[1]:
      va='top'
    elif startxy[1] > endxy[1]:
      va='bottom'
    else:
      va='center'
    ax.annotate(text, endxy, startxy, ha=ha,va=va,arrowprops=dict(arrowstyle='-|>',fc='k',ec='k'),size=size,**annkw)
  
  def pseudo_bar(self,x,h,w,*args,**kwargs):
    '''Draw a pseudo-bar with location centered at 'x'
    with height 'h' and width 'w'.
    '''
    ax = self.ax
    w *= 0.5
    ax.plot([x-w,x-w,x+w,x+w], [0,h,h,0], *args, **kwargs)

  def __getattr__(self, attr):
    return getattr(self.ax,attr)    

  def tight_layout(self):
    return self.fig.tight_layout()

  def close(self):
    plt.close(self.fig)

# -----------------------------------------------------------------------------
# Data generation
# -----------------------------------------------------------------------------

import numpy as np
from scipy.stats import rice, norm
def skewed_data(direction='left', amount='medium'):
  '''Generate data with a left or right skew.
  The amount can be:
  
  'low'    - A low amount of skew
  'medium' - A medium amount of skew
  'high'   - A high amount of skew
  '''
  x = np.linspace(0,1,1000)
  if amount == 'medium':
    y = rice.pdf((x+0.05)*5, 1.5)+0.025
  else:
    raise ArugmentError("illegal amount: {}".format(amount))
  
  # Flip
  if direction == 'right':
    y = y[::-1]
    
  return x,y

def normal_data(loc=0.0,scale=1.0):
  x = np.linspace(-3,3,1000)
  y = norm.pdf(x, loc=loc, scale=scale)
  x = np.linspace(0,1,1000)
  return x,y

  
  