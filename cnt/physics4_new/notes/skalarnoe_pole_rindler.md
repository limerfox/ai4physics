---
type: Результат
---
# Свободное скалярное поле в пространстве Риндлера

Свободное скалярное поле φ массы m в пространстве-времени Риндлера.

## Метрика и координаты Риндлера

Пространство-время Риндлера — это часть пространства Минковского, покрываемая координатами, связанными с инерциальными (T, X, Y, Z) преобразованием:

$$T = \xi\sinh(a\tau), \quad X = \xi\cosh(a\tau), \quad Y = y, \quad Z = z$$

где $a$ — параметр ускорения, $\xi > 0$ покрывает правый клин ($X > |T|$).

Метрика в координатах Риндлера:
$$ds^2 = -a^2\xi^2 d\tau^2 + d\xi^2 + dy^2 + dz^2$$

Определитель: $g = -a^2\xi^2$, $\sqrt{-g} = a\xi$.

Обратная метрика:
$$g^{\tau\tau} = -\frac{1}{a^2\xi^2}, \quad g^{\xi\xi} = 1, \quad g^{yy} = 1, \quad g^{zz} = 1$$

## Уравнение Клейна-Гордона

$$\frac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,g^{\mu\nu}\partial_\nu\phi) - m^2\phi = 0$$

Подстановка метрики:
$$-\frac{1}{a^2\xi^2}\partial_\tau^2\phi + \partial_\xi^2\phi + \frac{1}{\xi}\partial_\xi\phi + \partial_y^2\phi + \partial_z^2\phi - m^2\phi = 0$$

## Разделение переменных

Ищем решение в виде:
$$\phi(\tau,\xi,y,z) = e^{-i\omega\tau + ik_y y + ik_z z}\,R(\xi)$$

Обозначим $k_\perp^2 = k_y^2 + k_z^2$ и $\kappa = \sqrt{k_\perp^2 + m^2}$.

Уравнение для радиальной части:
$$R'' + \frac{1}{\xi}R' + \left[\frac{\omega^2}{a^2\xi^2} - \kappa^2\right]R = 0$$

## Решение через функции Бесселя

Сделаем замену $z = \kappa\xi$:
$$\frac{d^2R}{dz^2} + \frac{1}{z}\frac{dR}{dz} + \left[\frac{\omega^2}{a^2z^2} - 1\right]R = 0$$

Это модифицированное уравнение Бесселя с мнимым порядком $\nu = i\omega/a$.

Общее решение:
$$R(\xi) = C_1\,I_{i\omega/a}(\kappa\xi) + C_2\,K_{i\omega/a}(\kappa\xi)$$

где $I_\nu$ и $K_\nu$ — модифицированные функции Бесселя первого и второго рода.

Для нормируемых решений в клине Риндлера ($\xi \to \infty$) выбираем $K_{i\omega/a}$, так как $I_{i\omega/a}$ растёт экспоненциально.

## Полное решение

$$\phi(\tau,\xi,\mathbf{x}_\perp) = \int_0^\infty d\omega \int \frac{d^2k_\perp}{(2\pi)^2}\,\frac{1}{\sqrt{2\omega}}\left[a_{\omega,\mathbf{k}_\perp}\,f_{\omega,\mathbf{k}_\perp}(\tau,\xi,\mathbf{x}_\perp) + a_{\omega,\mathbf{k}_\perp}^\dagger\,f_{\omega,\mathbf{k}_\perp}^*(\tau,\xi,\mathbf{x}_\perp)\right]$$

где моды:
$$f_{\omega,\mathbf{k}_\perp}(\tau,\xi,\mathbf{x}_\perp) = \mathcal{N}\,e^{-i\omega\tau + i\mathbf{k}_\perp\cdot\mathbf{x}_\perp}\,K_{i\omega/a}(\kappa\xi)$$

$\mathcal{N}$ — нормировочная константа, определяемая из условия ортонормировки по скалярному произведению Клейна-Гордона.

## Скалярное произведение Клейна-Гордона

На поверхности постоянного $\tau$:
$$(\phi_1,\phi_2) = i\int_0^\infty d\xi\int d^2x_\perp\,\sqrt{-g}\,n^\mu(\phi_1^*\partial_\mu\phi_2 - \phi_2\partial_\mu\phi_1^*)$$

где $n^\mu = (1/(a\xi), 0, 0, 0)$ — единичный нормальный вектор.

## Связи
- тип: [[Результат]]
- применимоК: [[Поле]], [[ПространствоВремя]]
- хранитсяВ: [[notes/skalarnoe_pole_rindler.md]]
- решает: [[Вывести выражение для свободного скалярного поля в пространстве Риндлера]]