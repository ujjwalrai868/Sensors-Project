import numpy as np
from numpy import *
import Gnuplot

ranpam=genfromtxt('EP_Random_efficiency_loss.txt')
toam=genfromtxt('EP_Draw_efficiency_loss.txt')
toam2=genfromtxt('EP_d2_efficiency_loss.txt')
toam4=genfromtxt('EP_d4_efficiency_loss.txt')
toam8=genfromtxt('EP_d8_efficiency_loss.txt')
gp=Gnuplot.Gnuplot(persist = 1)
gp('set terminal x11 size 1000,1000 font "Times new roman" ')
gp('set tics font ",18"')
gp('set xlabel font",25"')
gp('set ylabel font",25"')
#gp('set key left top')
gp('set key at 3350, 71500')
gp('set key spacing 1.0')
#gp('set key box width 1')
gp('set pointsize 1')
gp('set xlabel "Number of Users"')
gp('set ylabel "Total Efficiency Loss"')
gp('set xrange [700:5000]')	
gp('set yrange [0:72000]')
gp('set xtics 1000')
gp('set ytics 8000')
gp('set ytics ("8000" 8000 ,"16,000" 16000, "24,000" 24000, "32,000" 32000, "40,000" 40000, "48,000" 48000, "56,000" 56000, "64,000" 64000, "72,000" 72000)')
plot1=Gnuplot.PlotItems.Data(ranpam, with_="lp lw 2.0 lc rgb '#00FFFF'", title="RM-FSA")
plot2=Gnuplot.PlotItems.Data(toam, with_="lp lw 2.0 lc rgb '#FF00FF'", title="TM-FSA")
plot3=Gnuplot.PlotItems.Data(toam2, with_="lp lw 2.0 lc rgb '#008000'", title="TM-FSA-L-var")
plot4=Gnuplot.PlotItems.Data(toam4, with_="lp lw 2.0 lc rgb '#FF0000'", title="TM-FSA-M-var")
plot5=Gnuplot.PlotItems.Data(toam8, with_="lp lw 2.0 lc rgb '#0000FF'", title="TM-FSA-S-var")
gp('set key font ",25"')
gp.plot(plot1,plot2,plot3,plot4,plot5)
epsFilename= 'EP_efficiency_loss.eps'
gp.hardcopy(epsFilename, terminal= 'postscript',color='rgb')
gp.reset()