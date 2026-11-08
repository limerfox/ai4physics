import Mathlib.Analysis.Calculus.Deriv.Basic

/-!
# Rindler Geodesic Equations (G1)

From the Rindler metric `ds² = -ρ² dτ² + dρ²` (ρ > 0), derive:
1. `E = ρ² · τ̇` (conserved energy from cyclic coordinate τ)
2. `ρ̇² = E²/ρ² - 1` (from timelike normalization)

The derivation:
- τ is cyclic → ∂L/∂τ̇ = -ρ² τ̇ = -E → E = ρ² τ̇
- Timelike normalization: -ρ² τ̇² + ρ̇² = -1
- Substitute τ̇ = E/ρ²: -E²/ρ² + ρ̇² = -1 → ρ̇² = E²/ρ² - 1
-/

open Real

/-- G1: Given the conserved energy `E = ρ² · τ̇` and the timelike
    normalization `-ρ² · τ̇² + ρ̇² = -1`, derive `ρ̇² = E²/ρ² - 1`. -/
theorem rindler_geodesic_equations
    (ρ τ E ρ' τ' : ℝ)
    (hρ_pos : 0 < ρ)
    (hE : E = ρ ^ 2 * τ')
    (hnorm : -ρ ^ 2 * τ' ^ 2 + ρ' ^ 2 = -1) :
    ρ' ^ 2 = E ^ 2 / ρ ^ 2 - 1 := by
  have hρ_ne_zero : ρ ≠ 0 := by linarith
  -- From hE: τ' = E / ρ²
  have h_tau_deriv : τ' = E / ρ ^ 2 := by
    field_simp [hρ_ne_zero] at hE ⊢
    ring_nf at hE ⊢
    linarith
  -- Substitute into hnorm
  rw [h_tau_deriv] at hnorm
  field_simp [hρ_ne_zero] at hnorm ⊢
  ring_nf at hnorm ⊢
  linarith