# Часть 1: с. 1–4

[с. 1]
arXiv:2503.00064v1 [physics.class-ph] 27 Feb 2025

Once more about radiation from uniformly accelerating charge
E. T. Akhmedov1,2 and M. N. Milovanova1
1Institutskii per, 9, Moscow Institute of Physics and Technology, 141700, Dolgoprudny, Russia
2Academician Kurchatov Square, 1, NRC ”Kurchatov Institute”, 123182, Moscow, Russia
March 4, 2025
Abstract
We consider an electric charge uniformly accelerating along x direction and moving with constant velocity along y direction. We show that in the co-accelerating along x direction Rinder’s frame this charge creates non-zero Poynting vector, which, however, does not lead to a non-vanishing ﬂux through an inﬁnitely distant surface. Furthermore, we show that in the laboratory Minkowski frame such a charge creates a stress energy ﬂux that does not vanish at inﬁnity. We interpret these observations as that while the Rindler’s frame corresponds to the static zone around the charge, the Minkowski frame does contain the wave zone. We give detailed calculations and explanations concluding that uniformly accelerating charge does radiate.
1 Introduction
The issue of radiation from a uniformly accelerating charge has been extensively discussed in the literature (see, e.g., [1], [2], [3]). However, it remains noteworthy that there is no universally accepted consensus on this matter among experts.
The problem is complex due to its high symmetry and unusual nature: eternally accelerating charges do not occur in nature, and the answer to the question may, in principle, depend on the initial conditions and the precise deﬁnition of classical radiation. To place the issue in a broader context, it is important to note that it is closely related to the following series of problems1:
1. Does a charge ﬁxed in a gravitational ﬁeld produce radiation? (According to the equivalence principle, such a charge is equivalent to a uniformly accelerating charge in Minkowski spacetime.) If radiation is produced, would it be observed by a remote observer ﬁxed in the gravitational ﬁeld? Furthermore, if radiation is produced, would it be detected by a remote observer who is free-falling within the gravitational ﬁeld?
1At least some of these questions are interconnected through coordinate transformations between Rindler and Minkowski reference frames.
1

[с. 2]
2. Does a charge in free fall within a homogeneous gravitational ﬁeld emit radiation? (According to the equivalence principle, such a charge is equivalent to a charge in inertial motion within Minkowski spacetime.) If radiation is emitted, would it be observed by a co-falling remote observer? Furthermore, if radiation is emitted, would it be detected by a remote observer ﬁxed in the gravitational ﬁeld? Now consider a charge in inertial motion within Minkowski spacetime: does such a charge emit radiation in an accelerating reference frame?
3. Does a charge in free fall within an expanding Universe emit radiation as observed from another free-falling reference frame within the same Universe2?
4. What are the answers to the above questions if, instead of point-like sources of radiation, one considers, for example, scalar waves as the sources3? If radiation is produced by a wave as a source, while no radiation arises from a point-like source, what is the explanation for this apparent paradox?
While some of these questions may have straightforward answers, others require a more thorough examination. In this paper, we present our analysis of the situation.
We will now outline several key facts, some of which are straightforward, while others are more complex:
• Radiation is not merely a non-zero ﬂux of the Poynting vector; it is a ﬂux that does not vanish at inﬁnity.
• The radiation friction force can only be deﬁned after an averaging procedure and cannot be deﬁned for a trajectory that lacks ﬁnite spatial support [3]. Therefore, the absence of radiation friction force does not necessarily imply the absence of radiation.
• The intensity of radiation, deﬁned as the integral over a distant surface of the scalar product of the Poynting vector and the unit area vector, is not Lorentz invariant. The Lorentz invariant quantity is the power associated with the energy loss of the radiation source. This power, being independent of the reference frame, does not depend on the observer. If the power of energy loss is nonzero, radiation must be present.
• For a uniformly accelerating charge, the energy loss power is proportional to the square of the four-acceleration and, therefore, is nonzero.
• In the paper [4], it is demonstrated that the intensity of radiation from a uniformly accelerating charge in Minkowski space is nonzero at inﬁnity. Furthermore, [4] shows that, in Rindler coordinates, both the magnetic ﬁeld and, consequently, the Poynting vector vanish.
• The electromagnetic ﬁeld surrounding an accelerating charge forms two distinct regions: a close, static zone and a distant radiation zone. The static zone exists near the source, at distances shorter than the so-called radiation creation length, which is the characteristic distance the source must travel to produce radiation. In contrast, the radiation zone extends over distances much greater than the radiation creation length.
2The answer to this question for point-like sources of radiation is provided in [8]. 3Question No. 3 regarding the use of waves as sources of radiation for scalar ﬁelds was addressed in [9].
2

[с. 3]
• For a uniformly accelerating charge with acceleration a, the radiation creation length (and the characteristic wavelength of the radiation) is 1/a, assuming the speed of light is set to unity, c = 1. The Rindler coordinates cannot be extended beyond a distance of 1/a from the charge in the direction of radiation.
The situation considered in [4] is quite restrictive. To explore a more general case, this paper examines a charge that not only undergoes uniform acceleration along the ﬁrst direction but also moves with constant velocity along the second spatial direction. This approach allows us to observe that, in a less restrictive scenario, the magnetic ﬁeld in the co-accelerating frame is nonzero. Consequently, we ﬁnd that the Poynting vector is nonzero in the co-moving frame. However, this Poynting vector does not correspond to any radiation. These observations lead us to classify the co-moving reference frame as being within the static zone. In contrast, radiation is present beyond the Rindler frame, in the wave zone.

2 Set up of the problem
We look for solutions of the Maxwell equations

√1 ∂µ(√−gF µν) = 4πjν. (1) −g

in two diﬀerent reference frames of ﬂat space-time — the Minkowski metric:

ds2 = dt2 − dx2 − dy2 − dz2

(2)

and the Rindler one:

ds2 = ρ2dτ 2 − dρ2 − dy2 − dz2.

(3)

The relation between these coordinate systems is as follows:

t = ρ sinh(τ ), x = ρ cosh(τ ), y = y, z = z.

(4)

We use the Lorenz gauge:

∂µAµ = gµν Γµν η Aη.

(5)

In the Maxwell equation we consider the source, jµ, created by a particle that is uniformly accelerating. Namely, we assume that the source is moving with constant 4-acceleration aµaµ = −a2
along the world-line parameterized as follows:

α

1

1

1

d2zµ

z (θ) = sinh(aθ) cosh(φ), cosh(aθ), sinh(aθ) sinh(φ), 0 , aµ = 2

(6)

a

a

a

dθ

where θ — its proper time. Such a world-line is obtained from the standard one

α

1

1

z¯ (θ) = sinh(aθ), cosh(aθ), 0, 0 ,

(7)

a

a

3

[с. 4]
by boosting the later along the y axis with the rapidity φ. That is, we consider the source that is accelerating along the x axis and moving with constant velocity along the y one.

3 The solution in Rindler’s frame
The easiest way to ﬁnd the electromagnetic four-potential is to use the expressions for the LiénardWiechert potentials in Minkowski space-time for a charge moving along a given world-line [6, 7]:
Aµ(t, x) = (1, −v) , where R = t − trad, (8) R − v, R

in our case trad = z0(θ, φ) and R = x − z(θ, φ). The relation between R and t establishes that the proper time of the moment of radiation
and the time of the detection of the radiation are connected by the light-like world-line and the three-speed of the source v(θ, φ) = dz(θ, φ)/dz0(θ, φ) is equal to:

v(θ, φ) = tanh(aθ) , tanh(φ), 0 . (9) cosh(φ)

Squaring the relation between R and t and substituting into it the world-line of the source (6), we ﬁnd the relation between the event of the detection of the radiation and the event of its radiation

− t2 + x2 + y2 + z2 + a21 − 2ya sinh(aθ) sinh(φ) =

= 2x cosh(aθ) − 2t sinh(aθ) cosh(φ), (10)

a

a

and in the Rindler region

1 + ρ2 + y2 + z2 = a2 = 2 ρ cosh(τ ) cosh(aθ) + y sinh(aθ) sinh(φ) − ρ sinh(τ ) sinh(aθ) cosh(φ) , (11)
a
which we will use below. Then let us write the denominator of the right hand side of eq.(8) in Minkowski coordinates:

R − v, R = t − tanh(aθ) x − tanh(φ)y, (12) cosh(φ)

and in Rindler ones R − v, R = ρ sinh(τ ) − ρ cosh(τ ) tanh(aθ) − tanh(φ)y, (13) cosh(φ)

where we have used the relation between trad and R from (8). These relations will be also used below.
We want to ﬁnd and compare the expressions for the Lienard-Wiechert potentials and electro-

4

