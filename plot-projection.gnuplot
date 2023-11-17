# usage: gnuplot -e "filename='hmm.csv'" plot-projection.gnuplot

set terminal svg enhanced
set datafile separator tab

unset border
set border lc rgb "#000000"
set key textcolor rgb "#000000"

set xtics nomirror format ""
set ytics nomirror format ""

p(x) = (x<5?x:(x==5?12:(x==6?13:(x==7?8:(x==8?10:11)))))

plot filename using 1:2:(p($3)) with points pointtype variable lc rgb "#000000" notitle
