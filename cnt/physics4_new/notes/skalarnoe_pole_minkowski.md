---
type: Результат
---
# Свободное скалярное поле в пространстве Минковского

Свободное скалярное поле φ массы m в плоском пространстве-времени Минковского.

## Метрика и уравнение движения

Метрика Минковского в декартовых координатах:
$$ds^2 = -dt^2 + dx^2 + dy^2 + dz^2 = \eta_{\mu\nu}dx^\mu dx^\nu$$

где $\eta_{\mu\nu} = \text{diag}(-1, +1, +1, +1)$.

Даламбиан:
$$\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu = -\partial_t^2 + \nabla^2$$

Уравнение Клейна-Гордона для свободного поля:
$$(\Box + m^2)\phi = 0 \quad\Rightarrow\quad \ddot{\phi} - \nabla^2\phi + m^2\phi = 0$$

## Разложение по модам

Ищем решение в виде разложения по плоским волнам:
$$\phi(t,\mathbf{x}) = \int \frac{d^3k}{(2\pi)^3}\, \tilde{\phi}(t,\mathbf{k})\, e^{i\mathbf{k}\cdot\mathbf{x}}$$

Подстановка в уравнение Клейна-Гордона даёт для каждой моды:
$$\ddot{\tilde{\phi}}(\mathbf{k}) + (\mathbf{k}^2 + m^2)\,\tilde{\phi}(\mathbf{k}) = 0$$

Обозначим $\omega_{\mathbf{k}} = \sqrt{\mathbf{k}^2 + m^2}$. Решение:
$$\tilde{\phi}(\mathbf{k},t) = \frac{1}{\sqrt{2\omega_{\mathbf{k}}}}\left(a_{\mathbf{k}}\,e^{-i\omega_{\mathbf{k}}t} + a_{-\mathbf{k}}^\dagger\,e^{+i\omega_{\mathbf{k}}t}\right)$$

## Полное решение

$$\phi(t,\mathbf{x}) = \int \frac{d^3k}{(2\pi)^3}\,\frac{1}{\sqrt{2\omega_{\mathbf{k}}}}\left[a_{\mathbf{k}}\,e^{-i\omega_{\mathbf{k}}t + i\mathbf{k}\cdot\mathbf{x}} + a_{\mathbf{k}}^\dagger\,e^{+i\omega_{\mathbf{k}}t - i\mathbf{k}\cdot\mathbf{x}}\right]$$

где $a_{\mathbf{k}}$ и $a_{\mathbf{k}}^\dagger$ — операторы уничтожения и рождения (при квантовании).

## Нормировка мод

Ортонормированные положительные частотные моды:
$$u_{\mathbf{k}}(t,\mathbf{x}) = \frac{1}{(2\pi)^{3/2}\sqrt{2\omega_{\mathbf{k}}}}\,e^{-i\omega_{\mathbf{k}}t + i\mathbf{k}\cdot\mathbf{x}}$$

Скалярное произведение Клейна-Гордона:
$$(u_{\mathbf{k}}, u_{\mathbf{k}'}) = \delta^{(3)}(\mathbf{k} - \mathbf{k}')$$

## Лагранжиан и энергия

Лагранжиан:
$$\mathcal{L} = -\frac{1}{2}\eta^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi - \frac{1}{2}m^2\phi^2 = \frac{1}{2}\dot{\phi}^2 - \frac{1}{2}(\nabla\phi)^2 - \frac{1}{2}m^2\phi^2$$

Тензор энергии-импульса:
$$T_{\mu\nu} = \partial_\mu\phi\,\partial_\nu\phi - \eta_{\mu\nu}\mathcal{L}$$

Энергия:
$$E = \int d^3x\,T_{00} = \int d^3x\,\left[\frac{1}{2}\dot{\phi}^2 + \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2}m^2\phi^2\right]$$

## Связи
- тип: [[Результат]]
- применимоК: [[Поле]], [[ПространствоВремя]]
- хранитсяВ: [[notes/skalarnoe_pole_minkowski.md]]
- решает: [[Вывести выражение для свободного скалярного поля в пространстве Минковского]]