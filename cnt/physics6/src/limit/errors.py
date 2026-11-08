"""Выравнивание по фазе, метрики ошибок и аппроксимация сходимости в логарифмических координатах."""
import cmath
import math
import numpy as np
from .modes import minkowski_mode_mpmath

def phase_align(values, reference_ratio):
    """Удалите только глобальную фазу величины reference_ratio, не затрагивая её модуль."""
    if abs(reference_ratio) == 0:
        raise ZeroDivisionError("reference_ratio равно нулю.")
    phase = cmath.phase(reference_ratio)
    factor = cmath.exp(-1j*phase)
    return [v*factor for v in values], factor

def relative_error(phi, phi_ref):
    if abs(phi_ref) == 0:
        raise ZeroDivisionError("изначальная мода равно нулю")
    return abs(phi/phi_ref - 1.0)

def error_curve(mode_function, H_values, m, k, t_values, x=0.0, t_ref=0.0, **kwargs):
    """Возвращает максимальную относительную погрешность по набору значений `t_values` для каждого `H`.

    Глобальная фаза, зависящая от `H`, фиксируется путем совмещения фаз в точке `t_ref`.
    Амплитуда намеренно не подвергается перенормировке.
    В случае использования `mpmath` все отношения величин и погрешности вычисляются в рамках заданного контекста произвольной точности.
    """
    import mpmath as mp
    dps = int(kwargs.pop("dps", 50))
    results = []
    with mp.workdps(dps):
        phiM_ref = minkowski_mode_mpmath(m, k, t_ref, x)
        for H in H_values:
            phi_ref = mode_function(H, m, k, t_ref, x, **kwargs)
            ratio_ref = mp.mpc(phi_ref) / phiM_ref
            phase_factor = mp.e**(-1j*mp.arg(ratio_ref))
            errs = []
            for t in t_values:
                phi = mp.mpc(mode_function(H, m, k, t, x, **kwargs)) * phase_factor
                phiM = minkowski_mode_mpmath(m, k, t, x)
                errs.append(abs(phi/phiM - 1))
            results.append(float(max(errs)))
    return results

def estimate_order(H_values, errors, last_n=4):
    """Наклон прямой, полученный методом наименьших квадратов для зависимости $\log(\text{ошибка})$ от $\log(H)$, с использованием последних $n$ точек.

    Значения $H$ должны быть упорядочены по убыванию. Нулевые или нечисловые (бесконечные, NaN) значения ошибки исключаются.
    Полученный параметр $p$ носит описательный характер и не является доказательством наличия асимптотического режима.
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
