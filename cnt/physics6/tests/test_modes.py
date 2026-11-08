import math
from src.limit.modes import minkowski_mode_mpmath, desitter_mode_mpmath
from src.limit.asymptotic import wkb_first_order_mode

def test_minkowski_mode_normalization():
    m, k = 2.0, 3.0
    value = minkowski_mode_mpmath(m, k, 0.0, 0.0)
    assert math.isclose(abs(value), 1.0/math.sqrt(2.0*math.sqrt(m*m+k*k)),
                        rel_tol=1e-13)

def test_wkb_has_minkowski_limit_at_fixed_time():
    m, k, t = 1.0, 1.5, 0.2
    errors = []
    for H in (1e-2, 5e-3, 2.5e-3):
        got = wkb_first_order_mode(H, m, k, t)
        ref = minkowski_mode_mpmath(m, k, t)
        errors.append(abs(got/ref - 1))
    assert errors[2] < errors[0]

def test_exact_mode_is_finite_for_moderate_parameters():
    value = desitter_mode_mpmath(0.05, 1.0, 1.0, 0.1, dps=60)
    assert math.isfinite(value.real)
    assert math.isfinite(value.imag)
