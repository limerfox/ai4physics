# Часть 2: с. 5–8

[с. 5]
magnetic ﬁelds in the Rindler and Minkowski coordinate frames. They are related by the coordinate transformation from (4) as components of the four-vector potential and the electromagnetic tensor, respectively.
Before writing out the expression for the four-potential in the Rindler’s frame, let us use the remaining gauge freedom to simplify it. The Lorenz gauge ﬁxing condition (5) in this frame is as follows:

AR gµν ∂µARν = 1 ρ ,

(14)

where gµν is the inverse Rindler metric and we have introduced the index R just to stress that these expressions are attributed to the Rindler’s frame, to distinguish them from those in the Minkowski frame (without an index). Then the scalar function α(τ, ρ, y, z) performing the remaining gauge freedom, i.e. the gauge transformation Aµ − ∂µα that does not change the gauge condition, must solve
gµν∂µ∂ν α = ∂1α . (15) ρ

This equation has such a solution as α = C · ln(ρ) with an arbitrary constant C. Let us use such

a

remaining

gauge

transformation

over

the

ﬁrst

component

of

the

four-potential,

AR
1

=

AR
1

−

ρ−1,

to change its expression. Then the electromagnetic four-potential in Rindler coordinates takes the

following form:

ρ cosh(τ − aθ) + cosh(τ ) cosh(aθ) cosh(φ) − 1

A0R =

f (τ, ρ, y, z, θ) ,

A1R = yρ · cosh(aθ) sinh(φ) f (τ, ρ, y, z, θ) ,

A2R = −cosh(aθ) sinh(φ) f (τ, ρ, y, z, θ) ,

A3R = 0.

(16)

To simplify these expressions, we introduce the following function:

f (τ, ρ, y, z, θ) = ρ sinh(τ − aθ) − cosh(aθ) y sinh(φ) + ρ sinh(τ ) 1 − cosh(φ) . (17)

Note

that

in

the

Rindler

frame

AR
0

has

a

diﬀerent

dimensionality

from

AR.

That

is

because

while

ρ, y, z have dimension of length, the time coordinate τ is dimensionless. For the same reason, the

electric ﬁeld, ER, also has a diﬀerent dimensionality from the magnetic one, BR.

5

[с. 6]
The corresponding electric and magnetic ﬁelds in the Rindler frame are as follows:

aρ 2yρ sinh(τ ) sinh(φ) − cosh(φ) − ρ2 + y2 + z2 + a−2

E1R =

2f (τ, ρ, y, z, θ)3

,

aρ sinh(τ ) sinh(φ) ρ2 − y2 + z2 + a−2 − 2ρy cosh(φ) E2R = − 2f (τ, ρ, y, z, θ)3 ,

aρz ρ cosh(φ) + y sinh(τ ) sinh(φ) E3R = f (τ, ρ, y, z, θ)3 . (18)

and

B1R = f (τ, ρ, y, z, θ)3 aρz cosh(τ ) sinh(φ) ,

B2R = f (τ, ρ, y, z, θ)3 ayz cosh(τ ) sinh(φ) ,

R a (−ρ2 − y2 + z2 + a−2) cosh(τ ) sinh(φ)

B3 =

3

.

(19)

2f (τ, ρ, y, z, θ)

Then the corresponding Poynting vector is:

R a2ρ cosh(τ ) sinh(φ)

2

2

2

−2

S1 =

6 − 2ρy cosh(φ) ρ + z + y − a −

16πf (τ, ρ, y, z)

− sinh(τ ) sinh(φ) − ρ4 + y4 + z4 + 2y2z2 + 2a−2 z2 − y2 + a−4 ,

R a2ρ cosh(τ ) sinh(φ)

2

2

2

−2

S2 =

6 2ρy sinh(τ ) sinh(φ) ρ + y + z − a +

16πf (τ, ρ, y, z)

+ cosh(φ) ρ4 − y4 + z4 + 2ρ2z2 + 2a−2 z2 − ρ2 + a−4 ,

R a2ρz cosh(τ ) sinh(φ) 2 2 2 −2

S3 =

6 ρ + y + z + a ρ sinh(τ ) sinh(φ) − y cosh(φ) . (20)

8πf (τ, ρ, y, z)

When we return to the situation that was considered in [4], φ = 0, we reproduce the results of that paper. In the case φ = 0 the magnetic ﬁeld and Poynting vector in the Rindler’s frame are zero. Meanwhile in our situation these quantities are not zero and the question of the presence or the absence of the radiation in the Rindler’s frame demands a careful consideration.
To answer the last question we have to ﬁnd the behavior of the intensity of the radiation (stressenergy ﬂux) within Rindler’s region but far away from the source. Using the relation between trad and R from (8) the distance from the source R 2, can be written in Rindler’s coordinates as:

R 2 = ρ sinh(τ ) − a−1 sinh(aθ) cosh(φ) 2.

In has to be taken to inﬁnity in units of acceleration. Essentially our goal is to single out in (20) the last function of τ, ρ, y, z in the limit R 2 → ∞. But there are diﬀerent ways to go far away

6

[с. 7]
from the source of radiation within the Rindler’s wedge. Let us examine them separately. To fulﬁll the relation (11) in the limit R 2 → ∞, the Rindler’s time τ should also be taken to
inﬁnity, which can be expected on general grounds. Let us take the large distance limit in such a way that ρ ∼ ekτ , k ∈ [0, 1]. Note that k cannot be greater than 1, since then the relation (11) will not be satisﬁed. Then there are several ways in which the spatial coordinates tend to inﬁnity:
1. If k = 1, then y, z can be taken to be of the order of ρ in the limit in question, or they can be taken to remain ﬁnite, i.e. will not tend to inﬁnity;
2. If k < 1, then we should assume that y2 + z2 ∼ e(k+1)τ to fulﬁll (11). In any case the term y sinh(aθ) sinh(φ) on the right hand side of (11) is much smaller than all the other terms. Therefore, we can drop this term oﬀ. In all, we consider such a limit, in which:

eτ

ρ2 + y2 + z2

cosh(τ ) ≈ sinh(τ ) ≈ ≈ −1

.

(21)

2 2a ρ (cosh(aθ) − sinh(aθ) cosh(φ))

Substituting these expressions into (20) gives the approximate expression for the components of the Poynting vector at large spatial distances within the Rindler’s wedge:

a−2 sinh2(φ) cosh(aθ) − sinh(aθ) cosh(φ) 4 S1R ≈ 4 6 ×
πρ ρ2 + y2 + z2 sinh(aθ) − cosh(aθ) cosh(φ)

× − 4a−1ρ2y coth(φ) cosh(aθ) − sinh(aθ) cosh(φ) + ρ4 − y2 + z2 2 ,

2a−2y sinh2(φ) cosh(aθ) − sinh(aθ) cosh(φ) 4 S2R ≈ 3 6 ,
π ρ2 + y2 + z2 sinh(aθ) − cosh(aθ) cosh(φ)

2a−2z sinh2(φ) cosh(aθ) − sinh(aθ) cosh(φ) 4

S3R ≈ 3

6,

(22)

π ρ2 + y2 + z2 sinh(aθ) − cosh(aθ) cosh(φ)

as follows from (21) in the limit under consideration ρ2 + y2 + z2 → ∞ in units of the acceleration 1/a. This then leads to the following expression for the energy ﬂux through a solid angle dΩ at long distance from the source (within the Rindler’s wedge):

dIR = SR, n dΩ

2

sinh2 (φ)

R∼

2×

2ρ ρ2 + y2 + z2

× ρ4 − (y2 + z2)2 − 4ρa−1(ρy − (y2 + z2))(cosh(aθ) − sinh(aθ) cosh(φ)) .

(23)

This expression is vanishing for the both ways to take the large spatial distance limit, which have been described above, except k = 0. In the latter case the ﬂux in the inﬁnity is not zero in some directions and even sometimes is negative. We give technical details in the appendix A. Please note that the resulting ﬂux is zero in the limit φ = 0. And what is even more important is that the ﬂux through the inﬁnity depends on the spatial coordinate ρ, which is never the case in standard situations. Perhaps that is the hint for the resolution of the puzzle: the notion of the large spatial

7

[с. 8]
distance limit in the Rindler’s frame is not that straightforward.

4 The solution in Minkowski frame
Let us now consider the situation in the Minkowski frame. We can either directly calculate the electromagnetic ﬁelds from (8) or transform back to the Minkowski frame the ﬁelds found above in Rindler’s frame. As an independent check both ways we obtain the same answer.
Using eq. (10) and eq. (4) to express t and x via Rindler’s coordinates, we obtain
cosh(τ − aθ) = = 2ρ a2 a 1 + ρ2 + y2 + z2 − 2 sinh(aθ) a y sinh(φ) + ρ sinh(τ ) 1 − cosh(φ) (24)
In the following expressions this relationship will be implied wherever there the functions cosh(τ − aθ) and sinh(τ − aθ) are present. Then, making the change of the coordinates to the Minkowskian coordinates in (17) we obtain the functions:

f (t, x) = − cosh(aθ) y sinh(φ) + t(1 − cosh(φ) +
+ 1 4 t2 − x2 + a a−2 − t2 + x2 + y2 + z2 − 2 sinh(aθ) y sinh(φ) + t 1 − cosh(φ) 2, 2 (25)

where we have used (24) to express out sinh(τ − aθ). Then, the electric and magnetic ﬁelds in the Minkowski frame can be written as follows:

E1 = − a

cosh(φ) a−2 + t2 − x2 + y2 + z2 − 2yt sinh(φ) ,

2f (t, x)3

ax y cosh(φ) − t sinh(φ)

E2 =

f (t, x)3 ,

axz cosh(φ)

E3 =

3.

(26)

f (t, x)

and

axz sinh(φ)

B1 =

3,

f (t, x)

az y sinh(φ) − t cosh(φ)

B2 =

f (t, x)3 ,

B3 = a 2f (t, x)3 sinh(φ) a−2 − t2 − x2 − y2 + z2 + 2yt cosh(φ) . (27)

And the resulting Poynting vector is:

8

