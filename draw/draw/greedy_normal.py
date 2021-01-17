import PyGnuplot as gp 
import numpy as np 

gp.c('set term postscript eps size 9,8 color blacktext "Helvetica" 49')
gp.c("set output 'greedy_normal.eps'")
gp.c('set key left')
gp.c('set title "Comparision between FMTM-FSA and MTM-FSA";set xlabel "Number of Users";set ylabel "Total Maximum Lateness in hours"')
gp.c('set yrange [0:110000000]')
gp.c("set style line 2 lc rgb 'black' lt 1 lw 100")
#gp.c('set border 4')
gp.c("set style fill solid 1 border lt -1")
gp.c('set boxwidth 0.1')
gp.c("plot 'greedy_normal1.txt' using ($0):2:xtic(1) with boxes title 'FMTM-FSA' lc rgb '#fde725', \
	''using ($0+0.1):3 with boxes title 'MTM-FSA' lc rgb '#e56b5d'")