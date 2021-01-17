import PyGnuplot as gp 
import numpy as np 

gp.c('set term postscript eps size 9,8 color blacktext "Helvetica" 50')
gp.c("set output 'output6.eps'")
gp.c('set key left')
gp.c('set title "";set xlabel "Number of Users";set ylabel "Number of Best Allocations"')
gp.c('set yrange [0:5200]')
gp.c("set style line 2 lc rgb 'black' lt 1 lw 100")
gp.c('set style fill solid 1 border lt -1')
gp.c('set boxwidth 0.1')
gp.c("plot 'partdraw2.txt' using ($0):3:xtic(1) with boxes title 'TM-FSA' lc rgb '#FF1493', \
	''using ($0+0.1):4 with boxes title 'MTM-FSA' lc rgb '#6A5ACD'")
