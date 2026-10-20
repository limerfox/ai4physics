# Часть 3: с. 9–13

[с. 9]
S1 =

a2x

2

2

6 2ty sinh(φ) y sinh(φ) − t cosh(φ) + 2t y + z −

8πf (t, x)

+ sinh(φ) t sinh(φ) − y cosh(φ) t2 + x2 + y2 + z2 − a−2 ,

S2 =

a2 2 2 2 2 2 2 2 −2 6 8ty cosh (φ) t + y − 4ty t + x + y − z − a +

32πf (t, x)

+ 2 sinh(φ) cosh(φ) z2 − x2 + a−2 2 − t2 + y2 2 + 4 x2z2 − t2y2 ,

S3 =

a2z 2 2 2 2 −2 6 − y sinh(φ) cosh(φ) 3t + x + y + z + a +

8πf (t, x)

+ t cosh2(φ) t2 + x2 + 3y2 + z2 + a−2 − 2t x2 + y2 .

(28)

These expressions reduce to those found in [4] in the limit φ = 0. Furthermore, in that paper it was shown that the ﬂux through the inﬁnitely distant surface is not zero, when the radiation achieves the surface after the appropriate time, i.e. there is an energy ﬂux emitted by the homogeneously accelerating charge which decouples from the source and can be measured by a very distant inertial observer in ﬂat space-time. Obviously the same is true for the case when φ = 0. But still let us be a bit more explicit and give some details.
Namely, let us show that the energy ﬂux, which follows from (28), through an inﬁnitely distant surface is not zero. To perform the integration over the distant surface, we choose the following parametrization:

t = r, x = r cos(α), y = r sin(α) cos(β), z = r sin(α) sin(β),

(29)

and take the limit ar → ∞. In this parametrization eq. (28) reduces to:

S1 =

a2 cos(α)

2

2

2

−2

2

6 sinh (φ) 2 + 2 sin (α) cos (β) − (ar) +

8πr f (r, α, β)

+ (ar)−2 − 4 sin(α) cos(β) sinh(φ) cosh(φ) + 2 sin2(α) ,

a2 −2 2 2 2 2

S2 =

2

6 2 sin(α) cos(β) (ar) + 2 sinh (φ) sin (α) cos (β) + 1 + 2 sin (α) +

16πr f (r, α, β)

+ sinh(φ) cosh(φ) (ar)−4 − 2(ar)−2 cos2(α) − sin2(α) sin2(β) − 8 sin2(α) cos2(β) ,

a2 sin(α) sin(β)

2

−2

2

2

S3 = 2

6 sinh (φ) (ar) + 2 sin (α) cos (β) + 2 −

8πr f (r, α, β)

− (ar)−2 + 4 sin(α) cos(β) sinh(φ) cosh(φ) + (ar)−2 + 2 sin2(α) ,

(30)

where

f (r, α, β) = − cosh(aθ) sin(α) cos(β) sinh(φ) + (1 − cosh(φ)) +

2

(31)

+ sin2(α) + (2ar)−1 − sinh(aθ) sin(α) cos(β) sinh(φ) + (1 − cosh(φ)) .

9

[с. 10]
Then the energy ﬂux through a solid angle dΩ is:

dI = S, n r2 =

a − 2 4 6 (ar) sin(α) cos(β) sinh(φ) cosh(φ)+

dΩ

16πf (r, α, β)

+ 2(ar)−2 1 + sinh2(φ) sin2(α) sin2(β) − cosh2(φ) cos2(α) +

(32)

+ 4 sin2(α) + sinh2(φ) sin2(α) cos2(β) + 1 − sin(α) cos(β) sinh(2φ) ,

where n = (cos(α), sin(α) cos(β), sin(α) sin(β)). In the large distance limit, ar → ∞, it reduces to:

dI a2 sin2(α) + sinh2(φ) sin2(α) cos2(β) + 1 − sin(α) cos(β) sinh(2φ) ≈ , (33)

dΩ

4πg(α, β)6

where

g(α, β) = − cosh(aθ) sin(α) cos(β) sinh(φ) + (1 − cosh(φ)) +

2

(34)

+ sin2(α) + sinh2(aθ) sin(α) cos(β) sinh(φ) + (1 − cosh(φ)) .

When φ = 0 the expression for the ﬂux that we ﬁnd here reduces to the one found in [4]. Note that the obtained expression is not zero. Thus, there is a ﬂux through a distant surface.
The expression (33) is always non-negative and, therefore, the total integrated ﬂux is non-zero.

5 Peculiar properties of the solution and other options
In this section we consider several peculiar properties of the solutions of the Maxwell’s equations which have been found above. Consider, e.g., the limit in which the acceleration, a, of the source of the radiation is taken to zero. Then the electromagnetic four-potential in the Rindler’s frame becomes a pure gauge:

lim ARµ (ρ → a−1e±τ , τ, y, z) = (coth(τ ), 0, 0, 0)

(35)

a→0

or

lim ARµ (τ → ±∞, ρ, y, z) = (±1, 0, 0, 0) .

(36)

a→0

Detailed calculations can be found in the appendix B. Therefore, in the absence of acceleration, the electric and magnetic ﬁelds are zero meanwhile the source seems to be still present, just does not accelerate.
Furthermore, in the appendix B we also show that in the Minkowski frame when a → 0 the electromagnetic four-potential is not a pure gauge only in one of the cases:

lim Aµ(x → a−1 cosh(aθ), t, y, z) = cosh(φ), 0,

sinh(φ)

,0 ,

a→0

θ − t cosh(φ) + y sinh(φ)

lim Aµ(t → ±a−1, x, y, z) = (0, 0, 0, 0) .

(37)

a→0

10

[с. 11]
The fact that the electric and magnetic ﬁelds are not zero only when x → a−1 cosh(aθ) will be explained below. For all other cases both magnetic and electric ﬁelds tend to zero when the source does not accelerate. Thus, we seem to have a paradox: for the world-line under consideration non-accelerating charge, a → 0, although being present, does not create even an electric ﬁeld.
The resolution of this apparent puzzle is as follows. In the limit a → 0, the world-line of the charge (6) is taken inﬁnitely far away along one of the spatial directions:

lim zα(θ) = (θ cosh φ, ∞, θ sinh φ, 0) .

(38)

a→0

Therefore, only in the limit when x → a−1 cosh(aθ) in the Minkowski frame the electromagnetic ﬁelds are non-zero.
To clarify the situation let us consider a bit diﬀerent world-line for which the position of the charged source does not get shifted inﬁnitely far away in the limit of zero acceleration:

zα(θ) = 1 sinh aθ cosh φ, 1 cosh(aθ) − 1 , 1 sinh aθ sinh φ, 0 . (39)

a

a

a

In such a case obviously

lim zα(θ) = θ cosh φ, 0, θ sinh φ, 0 .

(40)

a→0

However, this world-line does not fully (for all values of its proper time) lie in the Rindler’s region
that we consider. In fact, the condition for the world-line to ﬁt into the appropriate quadrant, |z0| ≤ z1, is fulﬁlled only when

cosh(φ) ≤ cosh(aθ) − 1 ≤ 1. (41) | sinh(aθ)|

Let us ﬁnd what electric and magnetic ﬁelds does the charge create in Minkowski frame if it moves along such a world-line as (39). The corresponding relation between the time of radiation and the time of the detection of the radiation in Minkowski frame is as follows:

x cosh(aθ) − t sinh(aθ) = x + a − t2 + x2 + y2 + z2 + 1 1 − cosh(aθ) +

2

a

(42)

+ sinh(aθ) t(cosh(φ) − 1) − y sinh(φ) .

Then, for this world-line we have that:

R − v, R = t − sinh aθ x + a−1 − sinh φ y. (43)

cosh aθ cosh φ

cosh φ

In such a case the four-potential looks like:

Aµ(t, x, y, z) = 1 cosh aθ cosh φ, − sinh aθ, − cosh aθ sinh φ, 0 (44) f (t, x, y, z)

11

[с. 12]
where

f (t, x, y, z) = t cosh(aθ) − x sinh(aθ) − a−1 sinh aθ+

+ cosh aθ t(cosh φ − 1) − y sinh φ .

(45)

Therefore, the electric and magnetic ﬁelds are

E1 = a 2f (t, x, y, z)3 2ty sinh(φ) − cosh(φ) t2 − x2 + y2 + z2 − 2a−1x ,

(ax + 1) y cosh(φ) − t sinh(φ)

E2 =

f (t, x, y, z)3 ,

z(ax + 1) cosh(φ)

E3 =

3,

(46)

f (t, x, y, z)

and

z(ax + 1) sinh(φ)

B1 =

3,

f (t, x, y, z)

az t cosh(φ) − y sinh(φ) B2 = − f (t, x, y, z)3 , B3 = a 2f (t, x, y, z)3 2ty cosh(φ) − sinh(φ) t2 + x2 + y2 − z2 + 2a−1x , (47)

In the case when φ = 0 these expressions reduce to:

E1 = − E2 = E3 =

4a t2 − x2 + y2 + z2 − 2a−1x 3,
2
2x + a(−t2 + x2 + y2 + z2) + 2a (1 − cosh(aθ)) − 4(x2 − t2) − 2a−1 sinh(aθ)
8ay (x + a−1) 3,
2
2x + a(−t2 + x2 + y2 + z2) + 2a (1 − cosh(aθ)) − 4(x2 − t2) − 2a−1 sinh(aθ)
8az(x + a−1) 3,
2
2x + a(−t2 + x2 + y2 + z2) + 2a (1 − cosh(aθ)) − 4(x2 − t2) − 2a−1 sinh(aθ) (48)

12

[с. 13]
and

B1 = 0, B2 = −
B3 =

3 8azt ,
2
2x + a(−t2 + x2 + y2 + z2) + 2a (1 − cosh(aθ)) − 4(x2 − t2) − 2a−1 sinh(aθ) 3 8ayt ,
2
2x + a(−t2 + x2 + y2 + z2) + 2a (1 − cosh(aθ)) − 4(x2 − t2) − 2a−1 sinh(aθ) (49)

Furthermore in the limits a → 0 and φ → 0 we have that the velocity of the charge is also vanishing

lim vi(θ) = lim sinh aθ , sinh φ , 0 = (0, 0, 0) . (50)

φ→0,a→0

φ→0,a→0 cosh aθ cosh φ cosh φ

As the result the expression for the electric ﬁeld reduces to its standard Coulomb form:

lim E = 3 R , t − θ = |R|. (51)

φ→0,a→0

(t − θ)

Meanwhile the magnetic ﬁeld is vanishing. As it should be, if φ is set to zero If we consider the limit of zero acceleration keeping φ = 0, then both electric and magnetic
ﬁelds will be non-zero

E = 3 (−x cosh(φ), t sinh(φ) − y cosh(φ), −z cosh(φ)), θ − t cosh(φ) + y sinh(φ)

(−z sinh(φ), 0, x sinh(φ)) (52)

B=

3.

θ − t cosh(φ) + y sinh(φ)

We think that these observations clarify the properties of the solutions of the Maxwell’s equations that we consider in this paper.

6 Conclusions and acknowledgments
Thus, we observe that a uniformly accelerating charge does create a radiation in the wave zone (i.e. as seen by a distant observer in Minkowski frame). At the same time in static zone corresponding to the co-moving Rindler’s frame the radiation is absent.
The question that remains to be considered is the number 4 among the questions formulated in the Introduction section.
This work was supported by the Ministry of Science and Higher Education of the Russian Federation (agreement no. 075–15–2022–287).

13

