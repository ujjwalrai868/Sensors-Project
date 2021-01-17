import numpy as np
from numpy import *
import Gnuplot

ranpam=genfromtxt('GP_Random_efficiency_loss.txt')
toam=genfromtxt('GP_Draw_efficiency_loss.txt')
toam2=genfromtxt('GP_d2_efficiency_loss.txt')
toam4=genfromtxt('GP_d4_efficiency_loss.txt')
toam8=genfromtxt('GP_d8_efficiency_loss.txt')
gp=Gnuplot.Gnuplot(persist = 1)
gp('set terminal x11 size 1000,1000 font "Times new roman" ')
gp('set tics font ",25"')
gp('set xlabel font",25"')
gp('set ylabel font",25"')
#gp('set key left top')
gp('set key at 335, 5550')
gp('set key spacing 1.0')
#gp('set key box width 1')
gp('set pointsize 1')
gp('set xlabel "Number of Users"')
gp('set ylabel "Total Efficiency Loss" offset-2.5,0,0')
gp('set xrange [70:480]')	
gp('set yrange [0:5600]')
gp('set xtics 80')
gp('set ytics 800')
plot1=Gnuplot.PlotItems.Data(ranpam, with_="lp lw 2.0 lc rgb '#00FFFF'", title="RanAlgo")
plot2=Gnuplot.PlotItems.Data(toam, with_="lp lw 2.0 lc rgb '#FF00FF'", title="FSAM-IComP")
plot3=Gnuplot.PlotItems.Data(toam2, with_="lp lw 2.0 lc rgb '#008000'", title="FSAM-IComP L-var")
plot4=Gnuplot.PlotItems.Data(toam4, with_="lp lw 2.0 lc rgb '#FF0000'", title="FSAM-IComP M-var")
plot5=Gnuplot.PlotItems.Data(toam8, with_="lp lw 2.0 lc rgb '#0000FF'", title="FSAM-IComP S-var")
gp('set key font ",25"')
gp.plot(plot1,plot2,plot3,plot4,plot5)
epsFilename= 'GP_efficiency_loss.eps'
gp.hardcopy(epsFilename, terminal= 'postscript',color='rgb')
gp.reset()
