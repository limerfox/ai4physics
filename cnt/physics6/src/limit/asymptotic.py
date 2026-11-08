"""Адиабатическое приближение (или приближение ВКБ) первого порядка по малому параметру $H$.

Это строго определенное приближение; оно не претендует на то,
чтобы воспроизвести полное равномерное разложение Дебая для функций Ханкеля высоких порядков.

Для фиксированного космологического времени $t$:
$\omega_H(t) = E_k - \frac{k^2 t}{E_k} H + O(H^2)$,
$\int_0^t \omega_H(s) \, ds = E_k t - \frac{k^2 t^2}{2 E_k} H + O(H^2)$.

Амплитуда включает множитель $a(t)^{-3/2}$ и главный адиабатический фактор.
"""
import cmath
import math

def wkb_first_order_mode(H, m, k, t, x=0.0):
    E = math.sqrt(m*m + k*k)
    omega = E - (k*k*t/E)*H
    if omega <= 0:
        raise ValueError("Частота в первом приближении ВКБ стала неположительной; уменьшите H или |t|.")
    phase_integral = E*t - (k*k*t*t/(2.0*E))*H
    amplitude = math.exp(-1.5*H*t) / math.sqrt(2.0*omega)
    return amplitude * cmath.exp(-1j*phase_integral + 1j*k*x)
