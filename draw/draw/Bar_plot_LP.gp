set terminal postscript eps enhanced "Helvetica" 600
set grid y
set term post color
set style data histogram
set style histogram cluster gap 3
set style fill solid border -1
set boxwidth 1 
set xtics rotate by 0 font "Helvetica, 600"
set ylabel 'Number of Best Allocation'
set key autotitle columnheader
set key left
set key font "20"
set key spacing "1.0"
set term post size 140,120
#set term eps size 800,400
set xlabel 'Number of Users'
set yrange[0:3000]

set output 'Best Allocation_LP.eps'
#set title "Number of Best allocation for patients with Patients requesting"
plot [-0.5:] [0:] 'LP_d2_best_allocation.txt' using 2:xticlabels(1) linecolor rgb "#0000FF", \
		  'LP_d4_best_allocation.txt' using 2:xticlabels(1) lc rgb "green", \
		  'LP_d8_best_allocation.txt' using 2:xticlabels(1) lc rgb "#4B0082", \
		  'LP_Draw_best_allocation.txt' using 2:xticlabels(1) lc rgb "#FF1493",\
		  'LP_Random_best_allocation.txt' using 2:xticlabels(1) lc rgb "red"

