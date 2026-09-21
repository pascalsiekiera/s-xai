#!/usr/bin/env python3
"""
Golomb Rulers Solver - Multiple Extensions
"""

import subprocess
import sys

def run_minizinc(model_file, m):
    """Run MiniZinc"""
    dzn_content = f"m = {m};"
    with open("temp.dzn", "w") as f:
        f.write(dzn_content)
    
    result = subprocess.run(
        ["minizinc", "-a", model_file, "temp.dzn"],
        capture_output=True,
        text=True,
        timeout=120
    )
    return result.stdout

def parse_marks(output, key):
    """Extract marks"""
    for line in output.split("\n"):
        if line.startswith(f"{key}:"):
            marks_str = line.replace(f"{key}:", "").strip()
            try:
                return eval(marks_str)
            except:
                pass
    return None

def get_distances(marks):
    """Get all distances"""
    distances = []
    for i in range(len(marks)):
        for j in range(i+1, len(marks)):
            distances.append(marks[j] - marks[i])
    return sorted(distances)

def main(m=4):
    # Optimal Ruler
    print("Optimal Ruler:")
    optimal_output = run_minizinc("golomb_regular.mzn", m)
    optimal = parse_marks(optimal_output, "marks")
    
    if optimal:
        dist = get_distances(optimal)
        print(f"{optimal}")
        print(f"Distances: {dist}")
    else:
        print("Not Solvable")
    
    print()
    
    # Disjoint Rulers
    print("Disjoint Rulers:")
    disjoint_output = run_minizinc("golomb_disjoint.mzn", m)
    ruler1 = parse_marks(disjoint_output, "ruler1")
    ruler2 = parse_marks(disjoint_output, "ruler2")
    
    if ruler1 and ruler2:
        dist1 = get_distances(ruler1)
        dist2 = get_distances(ruler2)
        
        print(f"Ruler 1: {ruler1}")
        print(f"Distances: {dist1}")
        print()
        print(f"Ruler 2: {ruler2}")
        print(f"Distances: {dist2}")
    else:
        print("Not Solvable")
    
    print()
    
    # Prime Golomb Ruler
    print("Prime Golomb Ruler:")
    prime_output = run_minizinc("golomb_prime.mzn", m)
    prime = parse_marks(prime_output, "marks")
    
    if prime:
        dist = get_distances(prime)
        print(f"{prime}")
        print(f"Distances: {dist}")
    else:
        print("Not Solvable")
    
    print()
    
    # Disjoint Prime Rulers
    print("Disjoint Prime Rulers:")
    prime_disjoint_output = run_minizinc("golomb_disjoint_prime.mzn", m)
    p_ruler1 = parse_marks(prime_disjoint_output, "ruler1")
    p_ruler2 = parse_marks(prime_disjoint_output, "ruler2")
    
    if p_ruler1 and p_ruler2:
        p_dist1 = get_distances(p_ruler1)
        p_dist2 = get_distances(p_ruler2)
        
        print(f"Ruler 1: {p_ruler1}")
        print(f"Distances: {p_dist1}")
        print()
        print(f"Ruler 2: {p_ruler2}")
        print(f"Distances: {p_dist2}")
    else:
        print("Not Solvable")

if __name__ == "__main__":
    m = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    main(m)
