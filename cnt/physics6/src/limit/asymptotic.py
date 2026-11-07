"""First-order small-H adiabatic/WKB approximation.

This is an explicitly defined approximation, not a claim to implement
the full uniform Debye expansion of a large-order Hankel function.

For fixed cosmic time t:
 omega_H(t) = E_k - (k^2 t/E_k) H + O(H^2),
 integral_0^t omega_H(s) ds = E_k t - (k^2 t^2/(2 E_k)) H + O(H^2).

The amplitude includes a(t)^(-3/2) and the leading adiabatic factor.
"""
import cmath
import math

def wkb_first_order_mode(H, m, k, t, x=0.0):
    E = math.sqrt(m*m + k*k)
    omega = E - (k*k*t/E)*H
    if omega <= 0:
        raise ValueError("First-order WKB frequency became non-positive; reduce H or |t|.")
    phase_integral = E*t - (k*k*t*t/(2.0*E))*H
    amplitude = math.exp(-1.5*H*t) / math.sqrt(2.0*omega)
    return amplitude * cmath.exp(-1j*phase_integral + 1j*k*x)
