"""
Covers uncertainty, expression of results and claims adjustment
"""

# 0. PREAMBLE
import math


# 1. UNCERTAINTY
# 1.1. STANDARD COMBINED UNCERTAINTY
def std_combined_u(uncertainties: dict) -> float:
    """Calculates combined uncertainty for a mathematical model with only addition and susbstraction"""
    return math.sqrt(sum(u**2 for u in uncertainties.values()))


# 1.2. STANDARD RELATIVE UNCERTAINTY
# 1.3. EXPANDED UNCERTAINTY
# 1.4. EXPANDED RELATIVE UNCERTAINTY


# 2. EXPRESSION OF RESULTS

# 3. CLAIMS ADJUSTMENT
