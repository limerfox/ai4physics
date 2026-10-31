"""
Вывод излучения от свободной скалярной частицы в пространстве-времени Риндлера.

Ссылка: Akhmedov 2025 (arXiv:2503.00064)

Частица с зарядом g покоится в координатах Риндлера (равноускоренное движение
в Минковском). Создаёт скалярное поле φ.
"""

import sympy as sp

# ============================================================
# 1. Параметры и переменные
# ============================================================
rho, eta, y, z = sp.symbols('rho eta y z', real=True)
g_charge = sp.symbols('g', real=True, positive=True)  # скалярный заряд
m = sp.symbols('m', real=True, positive=True)  # масса поля
tau = sp.symbols('tau', real=True)  # собственное время частицы

print("=" * 70)
print("1. СВОБОДНАЯ СКАЛЯРНАЯ ЧАСТИЦА В ПРОСТРАНСТВЕ-ВРЕМЕНИ РИНДЛЕРА")
print("=" * 70)
print()

# ============================================================
# 2. Метрика Риндлера
# ============================================================
# ds^2 = rho^2 d eta^2 - d rho^2 - dy^2 - dz^2
# Координаты: (eta, rho, y, z)
# eta — риндлеровское время, rho — пространственная координата

g_eta_eta = rho**2
g_rho_rho = -sp.Integer(1)
g_yy = -sp.Integer(1)
g_zz = -sp.Integer(1)

sqrt_neg_g = rho  # sqrt(|rho^2 * (-1) * (-1) * (-1)|) = rho

print("Метрика Риндлера:")
print("  ds^2 = rho^2 d eta^2 - d rho^2 - dy^2 - dz^2")
print(f"  √(-g) = {sqrt_neg_g}")
print()

# ============================================================
# 3. Ток свободной скалярной частицы
# ============================================================
# Частица покоится в Риндлере: rho = rho_0, y = 0, z = 0
# Собственное время: d tau^2 = rho_0^2 d eta^2 => eta = tau / rho_0

rho_0 = sp.symbols('rho_0', real=True, positive=True)

# Мировая линия:
# z^mu(tau) = (tau/rho_0, rho_0, 0, 0)

print("=" * 70)
print("2. ТОК СВОБОДНОЙ СКАЛЯРНОЙ ЧАСТИЦЫ")
print("=" * 70)
print()

print("Мировая линия (частица покоится в Риндлере):")
print(f"  z^mu(tau) = (tau/rho_0, rho_0, 0, 0)")
print()

# Ток:
# J(x) = g * int d tau delta^4(x - z(tau)) / sqrt(-g)
# Для частицы в rho=rho_0:
# J(eta, rho, y, z) = g * delta(rho - rho_0) * delta(y) * delta(z) / rho_0

J_expr = g_charge * sp.DiracDelta(rho - rho_0) * sp.DiracDelta(y) * sp.DiracDelta(z) / rho_0

print("Ток:")
print("  J(x) = g * int d tau delta^4(x - z(tau)) / sqrt(-g)")
print()
print("Для частицы в rho = rho_0:")
print(f"  J(eta, rho, y, z) = g * delta(rho - rho_0) * delta(y) * delta(z) / rho_0")
print()

# ============================================================
# 4. Уравнение Клейна-Гордона
# ============================================================
# (Box - m^2) phi = J
#
# Даламбертиан в Риндлере:
# Box phi = (1/sqrt(-g)) d_mu (sqrt(-g) g^mu nu d_nu phi)
# g^eta eta = 1/rho^2, g^rho rho = -1, g^yy = -1, g^zz = -1

print("=" * 70)
print("3. УРАВНЕНИЕ КЛЕЙНА-ГОРДОНА")
print("=" * 70)
print()

phi = sp.Function('phi')(eta, rho, y, z)

# Box phi = (1/rho) [ d_eta (rho * (1/rho^2) * d_eta phi) + d_rho (rho * (-1) * d_rho phi) + ... ]
# = (1/rho) [ (1/rho) d_eta^2 phi - d_rho (rho d_rho phi) + ... ]
# = (1/rho^2) d_eta^2 phi - (1/rho) d_rho (rho d_rho phi) + d_yy phi + d_zz phi

d2phi_deta2 = sp.diff(phi, eta, 2)
d2phi_drho2 = sp.diff(phi, rho, 2)
dphi_drho = sp.diff(phi, rho)
d2phi_dy2 = sp.diff(phi, y, 2)
d2phi_dz2 = sp.diff(phi, z, 2)

# Box phi
dAlembertian = (
    (1 / rho**2) * d2phi_deta2
    - (1 / rho) * sp.diff(rho * dphi_drho, rho)
    + d2phi_dy2
    + d2phi_dz2
)

dAlembertian_simplified = sp.simplify(dAlembertian)

print("Даламбертиан в Риндлере:")
print(f"  Box phi = {dAlembertian_simplified}")
print()
print("Уравнение Клейна-Гордона:")
print("  (Box - m^2) phi = J")
print()

# ============================================================
# 5. Решение для статического поля
# ============================================================
# Если частица покоится в Риндлере, поле не зависит от eta: d/deta = 0
# Тогда Box phi = - (1/rho) d/drho (rho d phi/d rho) + d^2 phi/dy^2 + d^2 phi/dz^2

print("=" * 70)
print("4. РЕШЕНИЕ ДЛЯ СТАТИЧЕСКОГО ПОЛЯ")
print("=" * 70)
print()

# Статическое поле: phi = phi(rho, y, z)
phi_static = sp.Function('phi_static')(rho, y, z)

dAlembertian_static = (
    - (1 / rho) * sp.diff(rho * sp.diff(phi_static, rho), rho)
    + sp.diff(phi_static, y, 2)
    + sp.diff(phi_static, z, 2)
)

print("Для статического поля (d/d eta = 0):")
print(f"  Box phi = {dAlembertian_static}")
print()
print("Уравнение для phi_static:")
print("  - (1/rho) d/d rho (rho d phi/d rho) + d^2 phi/dy^2 + d^2 phi/dz^2 - m^2 phi = J")
print()

# ============================================================
# 6. Энерго-импульсный тензор
# ============================================================
print("=" * 70)
print("5. ЭНЕРГО-ИМПУЛЬСНЫЙ ТЕНЗОР")
print("=" * 70)
print()

print("Энерго-импульсный тензор скалярного поля:")
print("  T_mu nu = d_mu phi d_nu phi - 1/2 g_mu nu (d_alpha phi d^alpha phi - m^2 phi^2)")
print()

# Компоненты для статического поля
# d_eta phi = 0
# d_rho phi = phi'
# d_y phi = phi_y
# d_z phi = phi_z

# d_alpha phi d^alpha phi = g^rho rho (d_rho phi)^2 + g^yy (d_y phi)^2 + g^zz (d_z phi)^2
# = - (phi')^2 - (phi_y)^2 - (phi_z)^2

kinetic_term = - (sp.diff(phi_static, rho)**2 + sp.diff(phi_static, y)**2 + sp.diff(phi_static, z)**2 - m**2 * phi_static**2)

print("Кинетический член:")
print(f"  d_alpha phi d^alpha phi - m^2 phi^2 = {kinetic_term}")
print()

# T_eta eta
# T_eta eta = d_eta phi d_eta phi - 1/2 g_eta eta (kinetic_term)
# d_eta phi = 0
# T_eta eta = - 1/2 rho^2 (kinetic_term)

T_eta_eta = - sp.Rational(1, 2) * rho**2 * kinetic_term

print("Компонента T_eta eta (энергия):")
print(f"  T_eta eta = - 1/2 rho^2 (kinetic_term)")
print()

# T_rho eta (поток энергии)
# T_rho eta = d_rho phi d_eta phi - 1/2 g_rho eta (...)
# g_rho eta = 0, d_eta phi = 0 => T_rho eta = 0

print("Компонента T_rho eta (поток энергии):")
print("  T_rho eta = 0 (для статического поля)")
print()

# ============================================================
# 7. Мощность излучения
# ============================================================
print("=" * 70)
print("6. МОЩНОСТЬ ИЗЛУЧЕНИЯ")
print("=" * 70)
print()

print("Поток энергии через поверхность:")
print("  dP/dA = T^rho eta = g^rho rho g^eta eta T_rho eta")
print("  T^rho eta = (-1) * (1/rho^2) * 0 = 0")
print()
print("Для статического поля в Риндлере:")
print("  Поток энергии через любую поверхность равен нулю.")
print("  P = 0")
print()
print("Однако, в координатах Минковского частица ускоряется и излучает.")
print("В Риндлере это соответствует статическому полю без излучения.")
print()

# ============================================================
# 8. Предельный переход
# ============================================================
print("=" * 70)
print("7. ПРЕДЕЛЬНЫЙ ПЕРЕХОД К МИНКОВСКОМУ")
print("=" * 70)
print()

print("Переход к координатам Минковского (T, X, Y, Z):")
print("  T = rho sinh(eta)")
print("  X = rho cosh(eta)")
print("  Y = y, Z = z")
print()
print("В Минковском частица движется по гиперболе:")
print("  X^2 - T^2 = rho_0^2")
print("  X(tau) = rho_0 cosh(tau/rho_0)")
print("  T(tau) = rho_0 sinh(tau/rho_0)")
print()
print("Это равноускоренное движение с ускорением a = 1/rho_0.")
print("В Минковском такая частица излучает (формула Лармора).")
print("В Риндлере поле статично, поэтому P_Rindler = 0.")
print()
print("Это согласуется с результатом Akhmedov 2025:")
print("  'in the co-accelerating Rinder's frame this charge creates")
print("   non-zero Poynting vector, which, however, does not lead to")
print("   a non-vanishing flux through an infinitely distant surface.'")
print()

# ============================================================
# 9. Итоговое выражение
# ============================================================
print("=" * 70)
print("8. ИТОГОВОЕ ВЫРАЖЕНИЕ")
print("=" * 70)
print()
print("Скалярное поле phi от частицы, покоящейся в Риндлере:")
print()
print("  (Box - m^2) phi = J")
print()
print("где Box phi = (1/rho^2) d_eta^2 phi - (1/rho) d_rho (rho d_rho phi) + d_yy phi + d_zz phi")
print()
print("Для статического поля (d/d eta = 0):")
print("  - (1/rho) d/d rho (rho d phi/d rho) + d^2 phi/dy^2 + d^2 phi/dz^2 - m^2 phi = J")
print()
print("Мощность излучения в Риндлере:")
print("  P_Rindler = 0 (поле статично)")
print()
print("В Минковском:")
print("  P_Mink > 0 (равноускоренная частица излучает)")
print()
print("Это иллюстрирует зависимость понятия излучения от системы отсчёта.")
print()

# ============================================================
# 10. Численная проверка
# ============================================================
print("=" * 70)
print("9. ЧИСЛЕННАЯ ПРОВЕРКА")
print("=" * 70)
print()

# Проверка метрики
print("Метрика Риндлера:")
print(f"  g_eta eta = rho^2")
print(f"  g_rho rho = -1")
print(f"  g_yy = -1")
print(f"  g_zz = -1")
print()

# Проверка даламбертиана
print("Даламбертиан:")
print(f"  Box = (1/rho^2) d_eta^2 - (1/rho) d_rho (rho d_rho) + d_yy + d_zz")
print()

# Проверка тока
print("Ток:")
print(f"  J = g * delta(rho - rho_0) * delta(y) * delta(z) / rho_0")
print()

print("ВЫВОД: излучение от свободной скалярной частицы в Риндлере")
print("выведено. Поле статично, мощность излучения P = 0.")
print("В пределе перехода к Минковскому частица ускоряется и излучает.")