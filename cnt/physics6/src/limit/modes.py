"""Функции мод для минимально связанного массивного скалярного поля в 4-мерном пространстве де Ситтера.

Принятые обозначения:
ds^2 = dt^2 - exp(2 H t) d x^2,
eta = -exp(-Ht)/H,
nu^2 = 9/4 - m^2/H^2.

Мода Банча-Дэвиса имеет вид:
u_k(eta) = (sqrt(pi)/2) H (-eta)^(3/2) exp[i pi (nu/2 + 1/4)] H^{(1)}_nu(-k eta).
Общий фазовый множитель, зависящий от H, не имеет физического значения при сравнении величин с согласованными фазами; в данной реализации используется именно это соглашение.
"""
import cmath
import math
import mpmath as mp

# def minkowski_mode(m: float, k: float, t: float, x: float = 0.0):
#     E = math.sqrt(m*m + k*k)
#     return cmath.exp(-1j*E*t + 1j*k*x) / math.sqrt(2.0*E)

def minkowski_mode_mpmath(m: float, k: float, t: float, x: float = 0.0):
    E = mp.sqrt(m*m+k*k)
    # Верное выражение:
    # phiM = mp.e**(-1j*E*t + 1j*k*x) / mp.sqrt(2*E)

    # Выражение с ошибкой:
    phiM = mp.e**(-1j*E*t + 1j*k*x) / mp.sqrt(E)
    return phiM

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
    """
    Реализация с пониженной точностью, приводящая результат к типу Python complex (binary64). 

    Стандартная универсальная функция (ufunc) для вычисления функций Ханкеля в библиотеке SciPy
    не поддерживает чисто мнимые значения порядка $\nu$, которые возникают в режиме малых $H$
    для массивных полей. В связи с этим данная реализация вычисляет специальную функцию
    с точностью до 17 десятичных знаков с помощью библиотеки mpmath, а затем округляет результат
    до типа Python complex (binary64). Это лишь практический суррогат с пониженной точностью,
    а не полноценная реализация функций Ханкеля для формата binary64.
    """
    value = desitter_mode_mpmath(H, m, k, t, x, dps=17)
    return complex(value)
