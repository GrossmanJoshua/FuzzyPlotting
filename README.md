# FuzzyPlotting
Plotting utils for generating fuzzy plots

# Usage

```python
import fuzzyplot

fuz = fuzzyplot.FuzzyPlot()

x,y = fuzzyplot.normal_data()

fuz.plot(x,y,color='r')

fuz.set_xlabel('height')
fuz.set_xlabel_side('shorter','left')
fuz.set_xlabel_side('taller','right')

fuz.set_ylabel('probability')
fuz.set_title('People')

fuz.arrow('Height', (0.5,0.5), (0.5,0.6))
```
 
