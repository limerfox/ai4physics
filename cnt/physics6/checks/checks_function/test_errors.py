import math
from src.limit.errors import estimate_order

def test_estimate_order_recovers_known_power():
    hs = [1e-1, 1e-2, 1e-3, 1e-4]
    es = [h**2 for h in hs]
    p, residual = estimate_order(hs, es, last_n=4)
    assert abs(p-2.0) < 1e-12
    assert residual < 1e-12
