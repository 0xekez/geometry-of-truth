set terminal svg enhanced
set datafile separator tab

unset border
set border lc rgb "#000000"
set key textcolor rgb "#000000"

set xtics nomirror
set ytics nomirror

set xlabel "# Principal Components"
set ylabel "% Variance Captured"

plot filename using ($1 > 10 ? 1/0 : $1):2 with linespoints lc rgb "#000000" lt 6 notitle
