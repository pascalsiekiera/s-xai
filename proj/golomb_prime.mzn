%-----------------------------------------------------------------------------%
% Prime Golomb Rulers
% Only prime numbers allowed as mark positions
%-----------------------------------------------------------------------------%

include "globals.mzn";

int: m;
int: n = m*m;

% Prime numbers up to n
set of int: primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293};
array[1..m] of var (0..n): mark;

array[1..(m*(m-1)) div 2] of var 0..n: differences =
    [ mark[j] - mark[i] | i in 1..m, j in i+1..m];

% First mark is always 0
constraint mark[1] = 0;

% All other marks must be prime
constraint forall ( i in 2..m ) (
    mark[i] in primes
);

% Standard Golomb: marks increasing
constraint forall ( i in 1..m-1 ) ( mark[i] < mark[i+1] );

% All distances distinct
constraint alldifferent(differences);

constraint differences[1] < differences[(m*(m-1)) div 2];

solve :: int_search(mark, input_order, indomain, complete)
    minimize mark[m];

output [
    "marks: ", show(mark), "\n",
    "differences: ", show(differences), "\n"
];

%-----------------------------------------------------------------------------%
