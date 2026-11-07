"""Mode functions for a minimally coupled massive scalar in 4D de Sitter.

Convention:
 ds^2 = dt^2 - exp(2 H t) d x^2,
 eta = -exp(-Ht)/H,
 nu^2 = 9/4 - m^2/H^2.

The Bunch-Davies mode is
 u_k(eta) = (sqrt(pi)/2) H (-eta)^(3/2)
            exp[i pi (nu/2 + 1/4)] H^{(1)}_nu(-k eta).
The overall H-dependent phase is not physically relevant for the
phase-aligned comparison; the implementation keeps this convention.
"""
import cmath
import math
import mpmath as mp

def minkowski_mode(m: float, k: float, t: float, x: float = 0.0):
    E = math.sqrt(m*m + k*k)
    return cmath.exp(-1j*E*t + 1j*k*x) / math.sqrt(2.0*E)

def desitter_mode_mpmath(H, m, k, t, x=0.0, dps=80):
    with mp.workdps(dps):
        Hm, mm, km, tm, xm = map(mp.mpf, (H, m, k, t, x))
        eta = -mp.e**(-Hm*tm) / Hm
        z = -km*eta
        nu = mp.sqrt(mp.mpf(9)/4 - (mm/Hm)**2)
        phase = mp.e**(1j*mp.pi*(nu/2 + mp.mpf(1)/4))
        value = (mp.sqrt(mp.pi)/2) * Hm * (-eta)**mp.mpf("1.5") * phase * mp.hankel1(nu, z)
        return value * mp.e**(1j*km*xm)

def desitter_mode_float64(H, m, k, t, x=0.0):
    """Low-precision comparator rounded to Python complex (binary64).

    SciPy's standard Hankel ufunc does not accept the purely imaginary
    order nu that occurs in the small-H massive-field regime. Therefore
    this implementation evaluates the special function at 17 decimal
    digits with mpmath and rounds the result to Python complex/binary64.
    It is a practical low-precision proxy, not a native binary64 Hankel
    implementation; the README documents this limitation explicitly.
    """
    value = desitter_mode_mpmath(H, m, k, t, x, dps=17)
    return complex(value)
