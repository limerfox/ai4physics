# Часть 4: с. 14–17

[с. 14]
A Appendix

In this appendix we study the radiation ﬂux in the Rindler’s frame in some peculiar situations. We observe that sometimes the ﬂux is not zero and even is negative.
Namely, we consider the behavior of the Poynting vector and the energy ﬂux in the case where ρ remains ﬁnite and y2 + z2 ∼ eτ are taken to inﬁnity. To observe somewhat anomalous behavior of the energy ﬂux, let us consider separately two cases when in the last limit y remains ﬁnite (recall that along this direction the charge is moving with constant velocity) and the the case when in the limit under consideration z remains ﬁnite.
In the ﬁrst case z2 ∼ eτ → ∞. Then the Poynting vector (20) in this limit takes the following form:

sinh2(φ) cosh(aθ) − sinh(aθ) cosh(φ) 4

S1R ≈ −

6,

πa2ρz4 sinh(aθ) − cosh(aθ) cosh(φ)

2 sinh2(φ) cosh(aθ) − sinh(aθ) cosh(φ) 4

S2R ≈

6×

πa3z6 sinh(aθ) − cosh(aθ) cosh(φ)

× ay + coth(φ) (cosh(aθ) − sinh(aθ) cosh(φ)) ,

2 sinh2(φ) cosh(aθ) − sinh(aθ) cosh(φ) 4

S3R ≈

6,

(53)

πa2z5 sinh(aθ) − cosh(aθ) cosh(φ)

and the energy ﬂux (|R| ∼ az2):

dI R

R

2 sinh2 (φ)

2

= S ,n R ∼

2 − az + o(z) ,

(54)

dΩ

aρz

where we used (21) to obtain these expressions. It can be seen that the ﬂux in this limit does not tend to zero at inﬁnity and even becomes negative for ﬁnite φ. Please note, however, that the resulting ﬂux is zero in the limit φ = 0. And what is even more important is that the ﬂux through the inﬁnity depends on the spatial coordinate ρ, which is never the case in standard situations. Perhaps that is the hint for the resolution of the puzzle: the notion of the large spatial distance limit in the Rindler’s frame is not that straightforward.
For completeness let us also consider the second case mentioned at the beginning of the ap-

14

[с. 15]
pendix. We see the same behavior of the energy ﬂux in this case y2 ∼ eτ → ∞:

sinh2(φ) cosh(aθ) − sinh(aθ) cosh(φ) 4

S1R = −

6,

πa2ρy4 sinh(aθ) − cosh(aθ) cosh(φ)

2 sinh2(φ) cosh(aθ) − sinh(aθ) cosh(φ) 4

S2R =

6,

πa2y5 sinh(aθ) − cosh(aθ) cosh(φ)

2z sinh2(φ) cosh(aθ) − sinh(aθ) cosh(φ) 4

S3R =

6,

(55)

πa2y6 sinh(aθ) − cosh(aθ) cosh(φ)

and the energy ﬂux is (|R| ∼ ay2):

dI R

R

2 sinh2 (φ)

2

= S ,n R ∼

2 − ay + o(y) .

(56)

dΩ

aρy

Thus, it has the same properties as the ﬂux of the ﬁrst case.

B Appendix

To obtain equation (35), consider the relation (11):

ρ(cosh(τ ) cosh(aθ) − sinh(τ ) sinh(aθ)) =

= a a−2 + ρ2 + y2 + z2 − sinh(aθ)(y sinh(φ) + ρ sinh(τ )(1 − cosh(φ))).

(57)

2

Using this relation, we can express ρ via other variables in the limit a → 0:

lim ρ = lim e±τ 1 ∓ θ cosh(φ) . (58)

a→0

a→0

a

Since θ is the proper time, then from the above limit we obtain that at a ﬁnite time τ the spatial position of the radiation observation point must be at inﬁnity.
Reversing the argument, the eq. (57) can be solved for τ . Then for a ﬁnite ρ the time of the radiation observation τ must tend to ±∞:

lim eτ = lim ρ−1 1 + θ cosh(φ) or lim eτ = 0.

(59)

a→0

a→0

a

a→0

15

[с. 16]
Thus, in the case (58), in the limit a → 0 the four-potential in the Rindler region (16) will tend to

lim AR0 (τ, y, z) = lim

ρ cosh(τ ) cosh(φ)

= coth(τ ),

a→0

a→0 ρ sinh(τ ) cosh(φ) − y sinh(φ)

lim A1R(τ, y, z) = lim y · sinh(φ) = 0,

a→0

a→0 ρ ρ sinh(τ ) cosh(φ) − y sinh(φ)

lim A2R(τ, y, z) = lim − sinh(φ) = 0,

a→0

a→0 ρ sinh(τ ) cosh(φ) − y sinh(φ)

lim AR3 (τ, y, z) = 0,

(60)

a→0

which agrees with (35). Such a four-potential is a pure gauge with α = ln(sinh(τ )). If we consider the other two cases (59), the four-potential will tend accordingly

lim ARµ (τ → − ln(aρ), ρ, y, z) = (1, 0, 0, 0) ,

(61)

a→0

or

lim ARµ (τ → −∞, ρ, y, z) = (−1, 0, 0, 0) .

(62)

a→0

The resulting four-potentials are also pure gauges. Let us consider also the behavior of a four-vector potential in the limit a → 0 in the Minkowski
coordinates. From the relation (10) we obtain the following limiting relation for the ﬁnite t:

lim x = lim 1 cosh(aθ) ± θ2 − 2θ(t cosh(φ) − y sinh(φ)) − (y2 + z2 − t2) ,

(63)

a→0

a→0 a

and the another relation for the ﬁnite x:

lim t = lim θ cosh(φ) ± 1 − x . (64)

a→0

a→0

a

Then the limiting values of the four-vector potential, when a → 0, in the Minkowski frame in the cases (63) and (64) are, correspondingly:

lim Aµ(x → a−1 cosh(aθ), t, y, z) = cosh(φ), 0,

sinh(φ)

,0 ,

a→0

θ − t cosh(φ) + y sinh(φ)

lim Aµ(t → ±a−1, x, y, z) = (0, 0, 0, 0) .

(65)

a→0

It can be seen that in the ﬁrst limit the four-vector is a pure gauge only when φ = 0.

References
[1] W. Pauli, Theory Relativity, Pergamon Press (1958).
[2] T. Fulton and F. Rohrlich, Annals of Physics 9, Issue 4, 499-517 (1960) doi.org/10.1016/00034916(60)90105-6.

16

[с. 17]
[3] R. Peierls, Surprises in Theoretical Physics, Princeton University Press (1979) doi.org/10.1515/9780691217888.
[4] D. Kalinov, Phys. Rev. D 92, no.8, 084048 (2015) doi:10.1103/PhysRevD.92.084048 [arXiv:1508.04281 [hep-th]].
[5] M. Born, Annalen Phys. 30, 840 (1909) doi.org/10.1002/andp.19093351102. [6] A. Liénard, L’éclairage électrique 16, No. 27-29, 5-14, 53-59, 106-112 (1898). [7] E. Wiechert, Archives Néerlandaises 5, 549-573 (1900) doi.org/10.1002/andp.19013090403. [8] E. T. Akhmedov, A. Roura and A. Sadofyev, Phys. Rev. D 82, 044035 (2010)
doi:10.1103/PhysRevD.82.044035 [arXiv:1006.3274 [gr-qc]]. [9] E. T. Akhmedov, P. V. Buividovich and D. A. Singleton, Phys. Atom. Nucl. 75, 525-529 (2012)
doi:10.1134/S1063778812040023 [arXiv:0905.2742 [gr-qc]].
17

