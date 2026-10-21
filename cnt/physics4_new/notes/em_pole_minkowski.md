---
type: Результат
---
# Свободное электромагнитное поле в пространстве Минковского

Свободное электромагнитное поле в плоском пространстве-времени Минковского.

## Лагранжиан и уравнения Максвелла

Лагранжиан электромагнитного поля:
$$\mathcal{L} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu}$$

где тензор напряжённости:
$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

Уравнения Максвелла (без источников):
$$\partial_\mu F^{\mu\nu} = 0$$

В терминах потенциала:
$$\Box A^\nu - \partial^\nu(\partial_\mu A^\mu) = 0$$

## Калибровка Лоренца

Выбираем калибровку Лоренца:
$$\partial_\mu A^\mu = 0$$

Тогда уравнения упрощаются:
$$\Box A^\nu = 0$$

Каждая компонента $A^\mu$ удовлетворяет волновому уравнению.

## Разложение по модам

Положительные частотные моды:
$$A^\mu(x) = \int \frac{d^3k}{(2\pi)^3}\,\frac{1}{\sqrt{2\omega_{\mathbf{k}}}}\,\sum_{\lambda=1}^{2}\left[\varepsilon^\mu_{\lambda}(\mathbf{k})\,a_{\mathbf{k},\lambda}\,e^{-i\omega_{\mathbf{k}}t + i\mathbf{k}\cdot\mathbf{x}} + \varepsilon^{*\mu}_{\lambda}(\mathbf{k})\,a_{\mathbf{k},\lambda}^\dagger\,e^{+i\omega_{\mathbf{k}}t - i\mathbf{k}\cdot\mathbf{x}}\right]$$

где $\omega_{\mathbf{k}} = |\mathbf{k}|$ (безмассовое поле).

## Поляризации

Для фотона с импульсом $\mathbf{k}$ выбираем два поперечных поляризационных вектора $\varepsilon^\mu_\lambda(\mathbf{k})$:

Условия:
1. $k_\mu \varepsilon^\mu_\lambda = 0$ (условие Лоренца)
2. $\varepsilon_\lambda \cdot \varepsilon^*_{\lambda'} = -\delta_{\lambda\lambda'}$ (нормировка)
3. $\varepsilon^0_\lambda = 0$ в калибровке Кулона

Для импульса вдоль оси $z$: $\mathbf{k} = (0,0,k)$:
$$\varepsilon^\mu_1 = (0,1,0,0), \quad \varepsilon^\mu_2 = (0,0,1,0)$$

## Тензор напряжённости

$$F_{\mu\nu}(x) = \int \frac{d^3k}{(2\pi)^3}\,\frac{1}{\sqrt{2\omega_{\mathbf{k}}}}\,\sum_{\lambda=1}^{2}\left[-i(k_\mu\varepsilon_{\nu\lambda} - k_\nu\varepsilon_{\mu\lambda})\,a_{\mathbf{k},\lambda}\,e^{-i\omega t + i\mathbf{k}\cdot\mathbf{x}} + \text{c.c.}\right]$$

## Электрическое и магнитное поля

$$\mathbf{E} = -\nabla A^0 - \partial_t\mathbf{A}, \quad \mathbf{B} = \nabla\times\mathbf{A}$$

В калибровке Кулона ($A^0 = 0$):
$$\mathbf{E} = -\partial_t\mathbf{A}, \quad \mathbf{B} = \nabla\times\mathbf{A}$$

## Энергия

$$E = \int d^3x\,\frac{1}{2}(\mathbf{E}^2 + \mathbf{B}^2) = \int \frac{d^3k}{(2\pi)^3}\,\omega_{\mathbf{k}}\,\sum_{\lambda=1}^{2}a_{\mathbf{k},\lambda}^\dagger a_{\mathbf{k},\lambda}$$

## Связи
- тип: [[Результат]]
- применимоК: [[Поле]], [[ПространствоВремя]]
- хранитсяВ: [[notes/em_pole_minkowski.md]]
- решает: [[Вывести выражение для свободного электромагнитного поля в пространстве Минковского]]