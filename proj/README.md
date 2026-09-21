# Golomb Rulers Solver - Multiple Variants

## Overview

A comprehensive solver for Golomb Rulers (CSPLib Problem 006) with multiple constraint-based extensions.

**Standard Golomb Ruler:** All pairwise distances are distinct.

**Extensions:**
1. **Disjoint Golomb Rulers:** Two rulers with no common distances
2. **Prime Golomb Rulers:** All marks (except 0) are prime numbers
3. **Disjoint Prime Golomb Rulers:** Combines both constraints

## Installation

### Requirements
- Python 3.7+
- MiniZinc 2.10.1 (https://www.minizinc.org/)

### Setup Minizinc
```bash
# Install MiniZinc
brew install minizinc  # macOS

# Verify installation
minizinc --version
```

## Usage

```bash
python3 proj.py n
```

Where `n` is the number of marks.

## Output

The program outputs four variants for comparison:
- Standard Golomb
- Disjoint Rulers
- Prime Golomb
- Disjoint Prime Rulers

## References

- CSPLib Problem 006: https://www.csplib.org/Problems/prob006/
- MiniZinc: https://www.minizinc.org/
- Golomb Rulers: http://datagenetics.com/blog/february22013
