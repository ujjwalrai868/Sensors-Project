
import numpy as np
from numpy import *
import Gnuplot

ranpam=genfromtxt('LP_Random_efficiency_loss.txt')
toam=genfromtxt('LP_Draw_efficiency_loss.txt')
toam2=genfromtxt('LP_d2_efficiency_loss.txt')
toam4=genfromtxt('LP_d4_efficiency_loss.txt')
toam8=genfromtxt('LP_d8_efficiency_loss.txt')
gp=Gnuplot.Gnuplot(persist = 1)
gp('set terminal x11 size 1000,1000 font "Times new roman" ')
gp('set tics font ",25"')
gp('set xlabel font",25"')
gp('set ylabel font",25"')
#gp('set key left top')
gp('set key at 295, 79900')
gp('set key spacing 3.0')
#gp('set key box width 1')
gp('set pointsize 1')
gp('set xlabel "Number of Agents"')
gp('set ylabel "Total Efficiency Loss" offset-2.5,0,0')
gp('set xrange [50:462]')	
gp('set yrange [0:80000]')
gp('set xtics 75')
gp('set ytics 16000')
plot1=Gnuplot.PlotItems.Data(ranpam, with_="lp lw 2.0 lc rgb '#00FFFF'", title="RanPAM")
plot2=Gnuplot.PlotItems.Data(toam, with_="lp lw 2.0 lc rgb '#FF00FF'", title="FSAM-IComP")
plot3=Gnuplot.PlotItems.Data(toam2, with_="lp lw 2.0 lc rgb '#008000'", title="FSAM-IComP L-var")
plot4=Gnuplot.PlotItems.Data(toam4, with_="lp lw 2.0 lc rgb '#FF0000'", title="FSAM-IComP M-var")
plot5=Gnuplot.PlotItems.Data(toam8, with_="lp lw 2.0 lc rgb '#0000FF'", title="FSAM-IComP S-var")
gp('set key font ",25"')
gp.plot(plot1,plot2,plot3,plot4,plot5)
epsFilename= 'LP_efficiency_loss.eps'
gp.hardcopy(epsFilename, terminal= 'postscript',color='rgb')
gp.reset()
