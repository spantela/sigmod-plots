"""sigmod-plot.py: Plotting graphs based on Sigmod Standards."""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import datetime, time


# set some nicer defaults for matplotlib
from matplotlib import rcParams

#set total number of colors to use in rainbow style
colors = cm.rainbow(np.linspace(0,1, 10))

rcParams['axes.grid'] = False
rcParams['axes.facecolor'] = 'white'
rcParams['patch.edgecolor'] = 'none'

def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """
    Thank you CS109 for the great function:
    http://nbviewer.ipython.org/github/cs109/content/blob/master/HW3_solutions.ipynb
    Minimize chartjunk by stripping out unnecesary plot borders and axis ticks

    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)

    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')

    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()


def plot(filename, legend, title, savefigname):
  """
  Plot sample data set

  Args:
    filename: csv file of data
    legend: Legend for line
    title: Plot Title
    savefigname: Name of figure to save. Use PDF format for vectorization.
  """
  remove_border()

  data = np.genfromtxt(filename, names=True, delimiter=',')
  plt.plot(data['columna'], data['columnb'], linestyle='--', color=colors[0])
  plt.axis([0,9,0,9])

  # show the integers from 0 to 11-1 on the y axis
  plt.xticks(np.arange(0,11,1))
  plt.yticks(np.arange(0,11,1))

  # add axis labels
  plt.ylabel('Y Label', fontdict={'fontsize':22})
  plt.xlabel('X Label', fontdict={'fontsize':23})
  plt.tick_params(axis='x', labelsize=21, which='major', pad=15)
  plt.tick_params(axis='y', labelsize=21)

  # adjust position
  plt.subplots_adjust(bottom=0.16, left=0.10, right = 0.96, top = 0.744)

  # SIGMOD requires font 1 for the files
  plt.rc('ps', useafm=True)
  plt.rc('pdf', use14corefonts=True)
  plt.rc('text', usetex=True)

  # set plot title
  plt.title(title, fontdict={'fontsize':25})

  # set the legends
  plt.legend(legend, loc='best', frameon=False, prop={'size': 20})

  # you better use pdf for nice vectorization effects
  time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

  plt.savefig(savefigname + '-' + time_stamp + '.pdf')
  plt.show()


def main():
  plot('data.csv', ['My Line'], 'Title', 'plotname')

if __name__ == "__main__":
  main()