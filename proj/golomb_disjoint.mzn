%-----------------------------------------------------------------------------%
% Disjoint Golomb Rulers
%-----------------------------------------------------------------------------%

include "globals.mzn";

int: m;
int: n = 2*m*m;

array[1..m] of var 0..n: mark1;
array[1..m] of var 0..n: mark2;

array[1..(m*(m-1)) div 2] of var 0..n: diff1 =
    [ mark1[j] - mark1[i] | i in 1..m, j in i+1..m];

array[1..(m*(m-1)) div 2] of var 0..n: diff2 =
    [ mark2[j] - mark2[i] | i in 1..m, j in i+1..m];

constraint mark1[1] = 0;
constraint forall ( i in 1..m-1 ) ( mark1[i] < mark1[i+1] );
constraint alldifferent(diff1);

constraint mark2[1] = 0;
constraint forall ( i in 1..m-1 ) ( mark2[i] < mark2[i+1] );
constraint alldifferent(diff2);

% Disjoint: no common distances
constraint forall (i, j in 1..(m*(m-1)) div 2) (
    diff1[i] = 0 \/ diff2[j] = 0 \/ diff1[i] != diff2[j]
);

constraint diff1[1] < diff1[(m*(m-1)) div 2];
constraint diff2[1] < diff2[(m*(m-1)) div 2];

solve minimize (mark1[m] + mark2[m]);

output [
    "ruler1: ", show(mark1), "\n",
    "ruler2: ", show(mark2), "\n"
];

%-----------------------------------------------------------------------------%
