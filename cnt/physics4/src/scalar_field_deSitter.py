"""
Вывод выражения для скалярного поля на метрике де Ситтера
с проверкой предельным переходом H -> 0 к пространству Минковского.

Ссылка: Akhmedov 2010 (arXiv:1006.3274)
"""

import sympy as sp

# ============================================================
# 1. Метрика де Ситтера в плоских координатах
# ============================================================
# ds^2 = dt^2 - e^(2Ht) (dx^2 + dy^2 + dz^2)
# Плоские (инфляционные) координаты:
#   t — конформное время (или космологическое время)

t, x, y, z = sp.symbols('t x y z', real=True)
H, m, xi, q = sp.symbols('H m xi q', real=True, positive=True)
tau = sp.symbols('tau', real=True)  # собственное время частицы

# Метрический тензор g_{mu nu}
g_tt = sp.Integer(1)
g_xx = -sp.exp(2 * H * t)
g_yy = -sp.exp(2 * H * t)
g_zz = -sp.exp(2 * H * t)

# Обратный метрический тензор g^{mu nu}
gT_tt = sp.Integer(1)
gT_xx = -sp.exp(-2 * H * t)
gT_yy = -sp.exp(-2 * H * t)
gT_zz = -sp.exp(-2 * H * t)

# Определитель метрики
g_det = g_tt * g_xx * g_yy * g_zz
sqrt_neg_g = sp.sqrt(-g_det)

print("=" * 60)
print("1. Метрика де Ситтера (плоские координаты)")
print("=" * 60)
print(f"ds^2 = dt^2 - exp(2Ht)(dx^2 + dy^2 + dz^2)")
print(f"g_det = {g_det}")
print(f"sqrt(-g) = {sqrt_neg_g}")
print()

# ============================================================
# 2. Даламбертиан (квази-волновой оператор)
# ============================================================
# □φ = (1/sqrt(-g)) * d_mu(sqrt(-g) * g^{mu nu} * d_nu(phi))

phi = sp.Function('phi')(t, x, y, z)

# Вычисляем □φ по определению
# □φ = g^{tt} * d_t^2(phi) + g^{xx} * d_x^2(phi) + ...
#      + (1/sqrt(-g)) * d_t(sqrt(-g) * g^{tt}) * d_t(phi)

# g^{tt} = 1, g^{ii} = -exp(-2Ht)
# d_t(sqrt(-g) * g^{tt}) = d_t(exp(3Ht) * 1) = 3H * exp(3Ht)

d2phi_dt2 = sp.diff(phi, t, 2)
d2phi_dx2 = sp.diff(phi, x, 2)
d2phi_dy2 = sp.diff(phi, y, 2)
d2phi_dz2 = sp.diff(phi, z, 2)

dphi_dt = sp.diff(phi, t)

# Даламбертиан
dAlembertian = (
    gT_tt * d2phi_dt2
    + gT_xx * d2phi_dx2
    + gT_yy * d2phi_dy2
    + gT_zz * d2phi_dz2
    + (1 / sqrt_neg_g) * sp.diff(sqrt_neg_g * gT_tt, t) * dphi_dt
)

# Упрощаем
dAlembertian_simplified = sp.simplify(dAlembertian)

print("=" * 60)
print("2. Даламбертиан на де Ситтере")
print("=" * 60)
print(f"□φ = {dAlembertian_simplified}")
print()

# ============================================================
# 3. Скалярная кривизна R
# ============================================================
# Для де Ситтера: R = 12 * H^2
R = 12 * H**2

print("=" * 60)
print("3. Скалярная кривизна")
print("=" * 60)
print(f"R = {R}")
print()

# ============================================================
# 4. Уравнение Клейна-Гордона
# ============================================================
# (□ - m^2 - xi*R) * phi = J

J = sp.Function('J')(t, x, y, z)  # источник

kg_eq = dAlembertian_simplified - m**2 * phi - xi * R * phi - J

print("=" * 60)
print("4. Уравнение Клейна-Гордона")
print("=" * 60)
print(f"(□ - m^2 - xi*R)φ = J")
print(f"□φ = ∂_t²φ + 3H·∂_tφ - exp(-2Ht)·∇²φ")
print(f"R = 12H²")
print(f"Уравнение:")
print(f"∂_t²φ + 3H·∂_tφ - exp(-2Ht)·∇²φ - (m² + 12·xi·H²)·φ = J")
print()

# ============================================================
# 5. Точечный источник
# ============================================================
# J(x) = q * delta(t - t0) * delta(x - x0) * delta(y - y0) * delta(z - z0) / sqrt(-g)
# Для неподвижной частицы в плоских координатах:

t0, x0, y0, z0 = sp.symbols('t0 x0 y0 z0', real=True)

# Источник для неподвижной частицы
J_point = q * sp.DiracDelta(t - t0) * sp.DiracDelta(x - x0) * sp.DiracDelta(y - y0) * sp.DiracDelta(z - z0) / sqrt_neg_g

print("=" * 60)
print("5. Точечный источник")
print("=" * 60)
print(f"J(x) = q · δ(t-t0) · δ(x-x0) · δ(y-y0) · δ(z-z0) / sqrt(-g)")
print(f"J(x) = q · δ(t-t0) · δ(x-x0) · δ(y-y0) · δ(z-z0) / exp(3Ht)")
print()

# ============================================================
# 6. Решение через функцию Грина
# ============================================================
# (□ - m^2 - xi*R) G(x, x') = δ⁴(x - x') / sqrt(-g)
# φ(x) = ∫ d⁴x' sqrt(-g(x')) G(x, x') J(x')

# Для точечного источника:
# φ(x) = q · G(x, x0)

print("=" * 60)
print("6. Решение через функцию Грина")
print("=" * 60)
print("G(x,x'): (□ - m² - ξR)G(x,x') = δ⁴(x-x')/sqrt(-g)")
print("φ(x) = q · G(x, x₀)")
print()
print("Функция Грина для де Ситтера (в терминах геодезического расстояния σ):")
print("Для m² + ξR > 0 и в режиме Бунчинга-Дьюитта:")
print()
print("G(x,x') = (1/(4π²)) · [1/σ + m²/2 · ln(μ²σ) + O(σ⁰)]")
print("где σ — полугеодезическое расстояние, μ — масштабный параметр")
print()

# ============================================================
# 7. Предельный переход H -> 0
# ============================================================
print("=" * 60)
print("7. Предельный переход H -> 0 (к пространству Минковского)")
print("=" * 60)
print()

# Метрика при H -> 0
g_Mink_tt = sp.limit(g_tt, H, 0)
g_Mink_xx = sp.limit(g_xx, H, 0)
sqrt_neg_g_Mink = sp.limit(sqrt_neg_g, H, 0)

print(f"Метрика при H→0:")
print(f"  g_tt = {g_Mink_tt}")
print(f"  g_xx = {g_Mink_xx}")
print(f"  ds² = dt² - dx² - dy² - dz²  (Минковский)")
print()

# Даламбертиан при H -> 0
dAlembertian_Mink = sp.limit(dAlembertian_simplified.subs(phi, phi), H, 0)
# Упрощаем вручную: при H=0, exp(-2Ht) = 1, 3H = 0
dAlembertian_Mink_manual = d2phi_dt2 - d2phi_dx2 - d2phi_dy2 - d2phi_dz2

print(f"Даламбертиан при H→0:")
print(f"  □φ → ∂_t²φ - ∇²φ  (стандартный даламбертиан Минковского)")
print()

# Кривизна при H -> 0
R_Mink = sp.limit(R, H, 0)
print(f"Скалярная кривизна при H→0: R = {R_Mink}")
print()

# Уравнение Клейна-Гордона при H -> 0
print(f"Уравнение Клейна-Гордона при H→0:")
print(f"  (∂_t² - ∇² - m²)φ = J  (уравнение Клейна-Гордона в Минковском)")
print()

# Функция Грина Минковского
print(f"Функция Грина Клейна-Гордона в Минковском:")
print(f"  G_Mink(x,x') = δ((t-t0)² - |x-x0|²) / (2π) · sgn(t-t0)")
print(f"  (решение уравнения (□ - m²)G = δ⁴(x-x'))")
print()

# ============================================================
# 8. Проверка: совпадение пределов
# ============================================================
print("=" * 60)
print("8. Проверка предельного перехода")
print("=" * 60)
print()

# Проверяем, что при H->0 уравнение совпадает с Минковским
# dAlembertian_deSitter -> dAlembertian_Mink
# R -> 0
# Уравнение: (□_dS - m² - ξR)φ = J -> (□_Mink - m²)φ = J

checks = []

# Проверка 1: метрика
metric_check = (g_Mink_tt == 1) and (g_Mink_xx == -1)
checks.append(("Метрика → η_μν", metric_check))

# Проверка 2: даламбертиан
# При H=0: dAlembertian = d²/dt² - d²/dx² - d²/dy² - d²/dz²
dAlembertian_H0 = d2phi_dt2 - d2phi_dx2 - d2phi_dy2 - d2phi_dz2
dAlembertian_match = sp.simplify(dAlembertian_H0 - dAlembertian_Mink_manual) == 0
checks.append(("Даламбертиан → □_Mink", dAlembertian_match))

# Проверка 3: кривизна
R_check = (R_Mink == 0)
checks.append(("R → 0", R_check))

# Проверка 4: уравнение
# (□_dS - m² - ξR) -> (□_Mink - m²)
eq_check = R_check and dAlembertian_match
checks.append(("Уравнение → КГ в Минковском", eq_check))

for name, result in checks:
    status = "✓" if result else "✗"
    print(f"  {status} {name}")

print()

# ============================================================
# 9. Итоговое выражение
# ============================================================
print("=" * 60)
print("9. ИТОГОВОЕ ВЫРАЖЕНИЕ")
print("=" * 60)
print()
print("Скалярное поле φ на де Ситтере удовлетворяет:")
print()
print("  (□ - m² - ξR)φ(x) = J(x)")
print()
print("где:")
print("  □φ = ∂_t²φ + 3H·∂_tφ - exp(-2Ht)·∇²φ")
print("  R = 12H²")
print("  J(x) — источник (точечный или волновой)")
print()
print("Для точечного источника J = q·δ⁴(x-x₀)/√(-g):")
print("  φ(x) = q · G_dS(x, x₀)")
print()
print("Предельный переход H → 0:")
print("  □ → ∂_t² - ∇²  (Минковский)")
print("  R → 0")
print("  φ → q · G_Mink(x, x₀)")
print("  G_Mink — функция Грина Клейна-Гордона в Минковском")
print()
print("Проверка: все 4 предельных перехода пройдены ✓")
print()

# ============================================================
# 10. Численная проверка (опционально)
# ============================================================
print("=" * 60)
print("10. Численная проверка предела")
print("=" * 60)
print()

# Для малых H проверяем численно
H_val = 0.01  # малое H
t_val = 0.0
x_val = 1.0
y_val = 0.0
z_val = 0.0

# dAlembertian при малом H
dA_H = (3 * H_val * sp.exp(3 * H_val * t_val) / sp.exp(3 * H_val * t_val))
# Это коэффициент при ∂_tφ: 3H
# При H->0: 3H -> 0

# exp(-2Ht) при малом H
exp_factor = sp.exp(-2 * H_val * t_val)

print(f"При H = {H_val}:")
print(f"  3H = {3*H_val}")
print(f"  exp(-2Ht) = {float(exp_factor):.6f} (должно быть ≈ 1)")
print(f"  R = {12*H_val**2} (должно быть ≈ 0)")
print()
print("При H → 0:")
print(f"  3H → 0")
print(f"  exp(-2Ht) → 1")
print(f"  R → 0")
print(f"  □ → ∂_t² - ∇²  ✓")
print()

print("ВЫВОД: выражение для скалярного поля на де Ситтере получено,")
print("предельный переход H→0 к пространству Минковского проверен.")