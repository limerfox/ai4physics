---
type: Результат
---
# Свободное электромагнитное поле в пространстве Риндлера

Свободное электромагнитное поле в пространстве-времени Риндлера.

## Метрика и уравнения Максвелла

Метрика Риндлера:
$$ds^2 = -a^2\xi^2 d\tau^2 + d\xi^2 + dy^2 + dz^2$$

Определитель: $g = -a^2\xi^2$, $\sqrt{-g} = a\xi$.

Уравнения Максвелла в искривлённом пространстве-времени:
$$\nabla_\mu F^{\mu\nu} = 0$$

В терминах потенциала в калибровке Лоренца ($\nabla_\mu A^\mu = 0$):
$$\Box A^\nu - R^\nu_{\ \mu}A^\mu = 0$$

Поскольку пространство Риндлера плоско ($R^\nu_{\ \mu} = 0$):
$$\Box A^\nu = 0$$

## Даламбиан в координатах Риндлера

$$\Box = \frac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,g^{\mu\nu}\partial_\nu) = -\frac{1}{a^2\xi^2}\partial_\tau^2 + \partial_\xi^2 + \frac{1}{\xi}\partial_\xi + \partial_y^2 + \partial_z^2$$

Уравнение для каждой компоненты:
$$-\frac{1}{a^2\xi^2}\partial_\tau^2 A^\nu + \partial_\xi^2 A^\nu + \frac{1}{\xi}\partial_\xi A^\nu + \partial_y^2 A^\nu + \partial_z^2 A^\nu = 0$$

## Разделение переменных

$$A^\nu(\tau,\xi,y,z) = e^{-i\omega\tau + ik_y y + ik_z z}\,R^\nu(\xi)$$

Радиальное уравнение (совпадает со скалярным случаем):
$$R^{\nu\prime\prime} + \frac{1}{\xi}R^{\nu\prime} + \left[\frac{\omega^2}{a^2\xi^2} - k_\perp^2\right]R^\nu = 0$$

где $k_\perp^2 = k_y^2 + k_z^2$.

Решение:
$$R^\nu(\xi) = C_1^\nu\,I_{i\omega/a}(k_\perp\xi) + C_2^\nu\,K_{i\omega/a}(k_\perp\xi)$$

Нормируемые решения: $K_{i\omega/a}(k_\perp\xi)$.

## Условие калибровки Лоренца

$$\nabla_\mu A^\mu = \frac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,A^\mu) = 0$$

В координатах Риндлера:
$$\partial_\tau A^\tau + \partial_\xi A^\xi + \partial_y A^y + \partial_z A^z = 0$$

Для мод:
$$-i\omega R^\tau + \frac{dR^\xi}{d\xi} + ik_y R^y + ik_z R^z = 0$$

Это условие связывает компоненты потенциала.

## Полное решение

$$A^\mu(\tau,\xi,\mathbf{x}_\perp) = \int_0^\infty d\omega\int\frac{d^2k_\perp}{(2\pi)^2}\,\frac{1}{\sqrt{2\omega}}\sum_{\lambda=1}^{2}\left[\varepsilon^\mu_{\lambda}(\omega,\mathbf{k}_\perp)\,a_{\omega,\mathbf{k}_\perp,\lambda}\,f_{\omega,\mathbf{k}_\perp,\lambda}(\tau,\xi,\mathbf{x}_\perp) + \text{c.c.}\right]$$

где моды:
$$f_{\omega,\mathbf{k}_\perp,\lambda}^\mu(\tau,\xi,\mathbf{x}_\perp) = \mathcal{N}\,e^{-i\omega\tau + i\mathbf{k}_\perp\cdot\mathbf{x}_\perp}\,K_{i\omega/a}(k_\perp\xi)\,\varepsilon^\mu_{\lambda}$$

$\varepsilon^\mu_\lambda$ — поляризационные векторы, удовлетворяющие условию калибровки.

## Тензор напряжённости

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

Компоненты электрического и магнитного полей в Риндлере:
$$E_\xi = F_{\xi\tau}, \quad E_y = F_{y\tau}, \quad E_z = F_{z\tau}$$
$$B_x = F_{yz}, \quad B_y = F_{z\xi}, \quad B_z = F_{\xi y}$$

## Связи
- тип: [[Результат]]
- применимоК: [[Поле]], [[ПространствоВремя]]
- хранитсяВ: [[notes/em_pole_rindler.md]]
- решает: [[Вывести выражение для свободного электромагнитного поля в пространстве Риндлера]]