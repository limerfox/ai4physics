"""Phase alignment, error metrics, and log-log convergence fits."""
import cmath
import math
import numpy as np
from .modes import minkowski_mode

def phase_align(values, reference_ratio):
    """Remove only the global phase of reference_ratio, not its magnitude."""
    if abs(reference_ratio) == 0:
        raise ZeroDivisionError("Reference mode ratio is zero.")
    phase = cmath.phase(reference_ratio)
    factor = cmath.exp(-1j*phase)
    return [v*factor for v in values], factor

def relative_error(phi, phi_ref):
    if abs(phi_ref) == 0:
        raise ZeroDivisionError("Reference mode is zero.")
    return abs(phi/phi_ref - 1.0)

def error_curve(mode_function, H_values, m, k, t_values, x=0.0, t_ref=0.0, **kwargs):
    """Return max relative error over t_values for each H.

    The H-dependent global phase is fixed by aligning the phase at t_ref.
    The amplitude is deliberately not renormalized. For mpmath, all ratios
    and errors are evaluated inside the requested arbitrary-precision context.
    """
    import mpmath as mp
    dps = int(kwargs.pop("dps", 50))
    results = []
    with mp.workdps(dps):
        phiM_ref = mp.e**(-1j*mp.sqrt(m*m+k*k)*t_ref + 1j*k*x) / mp.sqrt(2*mp.sqrt(m*m+k*k))
        for H in H_values:
            phi_ref = mode_function(H, m, k, t_ref, x, **kwargs)
            ratio_ref = mp.mpc(phi_ref) / phiM_ref
            phase_factor = mp.e**(-1j*mp.arg(ratio_ref))
            errs = []
            for t in t_values:
                phi = mp.mpc(mode_function(H, m, k, t, x, **kwargs)) * phase_factor
                E = mp.sqrt(m*m+k*k)
                phiM = mp.e**(-1j*E*t + 1j*k*x) / mp.sqrt(2*E)
                errs.append(abs(phi/phiM - 1))
            results.append(float(max(errs)))
    return results

def estimate_order(H_values, errors, last_n=4):
    """Least-squares slope of log(error) vs log(H), using the last n points.

    H_values must be ordered from large to small. Zero/non-finite errors
    are excluded. The returned p is descriptive, not a proof of an
    asymptotic regime; inspect the log-log plot and fit residuals.
    """
    pairs = [(float(h), float(e)) for h, e in zip(H_values, errors)
             if h > 0 and e > 0 and math.isfinite(h) and math.isfinite(e)]
    pairs = pairs[-last_n:]
    if len(pairs) < 2:
        return float("nan"), float("nan")
    x = np.log([p[0] for p in pairs])
    y = np.log([p[1] for p in pairs])
    p, intercept = np.polyfit(x, y, 1)
    residual = float(np.sqrt(np.mean((y - (p*x + intercept))**2)))
    return float(p), residual
