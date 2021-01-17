import PyGnuplot as gp 
import numpy as np 

gp.c('set term postscript eps size 10,6 color blacktext "Helvetica" 24')
gp.c("set output 'output1.eps'")
gp.c('set title "Comparision between FSAM-IComP and MFSAM-IComP(m>n)";set xlabel "Number of users";set ylabel "Number of allocations"')
gp.c('set yrange [0:510]')
gp.c('set xrange [0:520]')
gp.c("plot 'mfsam.txt' using 1:4 w lp lw 2 pt 3 t 'FSAM-IComP', \'' using 1:3 w lp lw 2 pt 5 t 'MFSAM-IComP'")


