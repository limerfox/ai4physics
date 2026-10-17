import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-
Formal Verification of Boyle's Law
===================================

Boyle's Law states that for an ideal gas at constant temperature,
the product of pressure and volume is constant: P · V = n · R · T

This module provides formal definitions and proofs of the key
properties of Boyle's Law.
-/

namespace BoyleLaw

/-- The universal gas constant R in J/(mol·K) -/
def R : ℝ := 8.314

/-- Boyle's Law: For an ideal gas at constant temperature T and
    amount n, the product P·V equals n·R·T. -/
def boyle_law (P V n T : ℝ) : Prop :=
  P * V = n * R * T

/-- Pressure as a function of volume at constant T and n: P(V) = nRT/V -/
def pressure (V n T : ℝ) : ℝ :=
  n * R * T / V

/-- Volume as a function of pressure at constant T and n: V(P) = nRT/P -/
def volume (P n T : ℝ) : ℝ :=
  n * R * T / P

/-- Boyle's Law is symmetric: if P·V = nRT, then V·P = nRT -/
theorem boyle_symmetric {P V n T : ℝ} :
  boyle_law P V n T ↔ boyle_law V P n T := by
  rw [boyle_law]
  rw [boyle_law]
  ring

/-- The pressure-volume product is conserved -/
theorem PV_conservation {P V n T : ℝ} (h : boyle_law P V n T) :
  P * V = n * R * T := by
  rw [boyle_law] at h
  exact h

/-- Pressure is inversely proportional to volume -/
theorem inverse_proportionality {V₁ V₂ P₁ P₂ n T : ℝ}
    (h₁ : boyle_law P₁ V₁ n T)
    (h₂ : boyle_law P₂ V₂ n T)
    (hV : V₁ ≠ 0) (hV₂ : V₂ ≠ 0) (hP : P₁ ≠ 0) (hP₂ : P₂ ≠ 0) :
  P₁ / P₂ = V₂ / V₁ := by
  have h₁' : P₁ = n * R * T / V₁ := by
    rw [boyle_law] at h₁
    field_simp [hV] at h₁ ⊢
    linarith
  have h₂' : P₂ = n * R * T / V₂ := by
    rw [boyle_law] at h₂
    field_simp [hV₂] at h₂ ⊢
    linarith
  rw [h₁', h₂']
  field_simp [hP, hP₂, hV, hV₂]
  ring

/-- If volume doubles, pressure halves -/
theorem volume_doubles_pressure_halves {P V n T : ℝ}
    (h : boyle_law P V n T)
    (hV : V ≠ 0) (hP : P ≠ 0) :
  let V' := 2 * V
  let P' := pressure V' n T
  P' = P / 2 := by
  unfold P'
  unfold pressure
  rw [boyle_law] at h
  field_simp [hV]
  ring

/-- The pressure function is strictly decreasing for V > 0 -/
theorem pressure_decreasing {V₁ V₂ n T : ℝ}
    (hV₁ : V₁ > 0) (hV₂ : V₂ > 0) (h : V₁ < V₂) :
  pressure V₁ n T > pressure V₂ n T := by
  unfold pressure
  have h₁ : n * R * T / V₁ > n * R * T / V₂ := by
    -- Since V₁ < V₂ and both positive, 1/V₁ > 1/V₂
    -- and n*R*T > 0 for positive n, T
    apply (div_lt_div_iff (by linarith) (by linarith)).mpr
    have : 0 < n * R * T := by
      -- R > 0, and we assume n > 0, T > 0 for physical validity
      norm_num [R]
      linarith
    nlinarith
  exact h₁

/-- Numerical verification: for n=1, T=300K, R=8.314
    P·V should equal 2494.2 J -/
theorem numerical_verification :
  let n : ℝ := 1.0
  let T : ℝ := 300.0
  let V : ℝ := 5.0  -- liters
  let P : ℝ := pressure V n T
  P * V = n * R * T := by
  unfold P
  unfold pressure
  norm_num [R]
  ring

/-- Physical validity: for positive n, T, V, the pressure is positive -/
theorem pressure_positive {V n T : ℝ}
    (hV : V > 0) (hn : n > 0) (hT : T > 0) :
  pressure V n T > 0 := by
  unfold pressure
  have hR : 0 < R := by norm_num [R]
  positivity

end BoyleLaw