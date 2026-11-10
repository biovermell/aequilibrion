"""
Tests for the metrology module from experimental analysis
"""

# 0. PREAMBLE
import math

from logic.experimental import metrology


# 1. UNCERTAINTY
# 1.1. STANDARD COMBINED UNCERTAINTY
def test_std_combined_u():
    result = metrology.std_combined_u({"u_mass": 5.0, "u_volume": 8.0})
    assert result == math.sqrt(89)


# 1.2. STANDARD RELATIVE UNCERTAINTY
# 1.3. EXPANDED UNCERTAINTY
# 1.4. EXPANDED RELATIVE UNCERTAINTY


# 2. EXPRESSION OF RESULTS

# 3. CLAIMS ADJUSTMENT
