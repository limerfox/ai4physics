import Mathlib.Analysis.Calculus.IntervalIntegral
import Mathlib.Analysis.Calculus.Deriv.Basic

open IntervalIntegral Set Real

/-- Интеграл собственного времени в пространстве-времени Риндлера:
    ∫₀^{ρ₀} ρ / √(E² - ρ²) dρ = E - √(E² - ρ₀²)
    для 0 < ρ₀ < E.
    Верификатор: intervalIntegral.integral_deriv_eq_sub.
    Антипроизводная: f(ρ) = -√(E² - ρ²), f'(ρ) = ρ/√(E² - ρ²). -/
theorem proper_time_integral (E ρ₀ : ℝ) (hE : 0 < E) (hρ : 0 < ρ₀) (hρE : ρ₀ < E) :
  ∫ ρ in (0)..ρ₀, ρ / sqrt (E ^ 2 - ρ ^ 2) = E - sqrt (E ^ 2 - ρ₀ ^ 2) := by
  have h1 : ∀ ρ ∈ Icc (0 : ℝ) ρ₀, DifferentiableAt ℝ (fun ρ => -sqrt (E ^ 2 - ρ ^ 2)) ρ := by
    intro ρ hρ'
    have h2 : 0 ≤ ρ := hρ'.1
    have h3 : ρ ≤ ρ₀ := hρ'.2
    have h4 : ρ ^ 2 < E ^ 2 := by
      calc
        ρ ^ 2 ≤ ρ₀ ^ 2 := by gcongr
        _ < E ^ 2 := by gcongr
    have h5 : E ^ 2 - ρ ^ 2 > 0 := by linarith
    -- sqrt is differentiable at positive points, and composition with polynomial
    have h6 : DifferentiableAt ℝ (fun ρ => E ^ 2 - ρ ^ 2) ρ := by
      apply DifferentiableAt.const_sub
      exact (differentiableAt_id.pow 2)
    have h7 : DifferentiableAt ℝ (fun x => sqrt x) (E ^ 2 - ρ ^ 2) := by
      apply DifferentiableAt.sqrt
      linarith
    exact h7.comp h6 |>.map (deriv_map (fun _ h => by linarith [h.2]))
      -- Actually let me use a simpler approach

  -- Simpler approach: use the chain rule directly
  have h_deriv : ∀ ρ ∈ Icc (0 : ℝ) ρ₀,
    deriv (fun ρ => -sqrt (E ^ 2 - ρ ^ 2)) ρ = ρ / sqrt (E ^ 2 - ρ ^ 2) := by
    intro ρ hρ'
    have h2 : 0 ≤ ρ := hρ'.1
    have h3 : ρ ≤ ρ₀ := hρ'.2
    have h4 : ρ ^ 2 < E ^ 2 := by
      calc
        ρ ^ 2 ≤ ρ₀ ^ 2 := by gcongr
        _ < E ^ 2 := by gcongr
    have h5 : E ^ 2 - ρ ^ 2 > 0 := by linarith
    -- deriv of -sqrt(E^2 - ρ^2) = -(1/(2*sqrt(E^2-ρ^2))) * (-2ρ) = ρ/sqrt(E^2-ρ^2)
    have h6 : deriv (fun ρ => -sqrt (E ^ 2 - ρ ^ 2)) ρ = ρ / sqrt (E ^ 2 - ρ ^ 2) := by
      -- Use chain rule: deriv of sqrt(u) = u'/(2*sqrt(u))
      -- deriv of -sqrt(u) = -u'/(2*sqrt(u))
      -- u = E^2 - ρ^2, u' = -2ρ
      -- So deriv = -(-2ρ)/(2*sqrt(E^2-ρ^2)) = ρ/sqrt(E^2-ρ^2)
      have h7 : HasDerivAt (fun ρ => E ^ 2 - ρ ^ 2) (-2 * ρ) ρ := by
        simpa using (hasDerivAt_id.pow 2 ρ).const_sub (E ^ 2)
      have h8 : HasDerivAt (fun x => sqrt x) (1 / (2 * sqrt (E ^ 2 - ρ ^ 2))) (E ^ 2 - ρ ^ 2) := by
        apply hasDerivAt_sqrt
        linarith
      have h9 : HasDerivAt (fun ρ => sqrt (E ^ 2 - ρ ^ 2))
          (1 / (2 * sqrt (E ^ 2 - ρ ^ 2)) * (-2 * ρ)) ρ := by
        apply HasDerivAt.comp ρ h7 h8
      have h10 : HasDerivAt (fun ρ => -sqrt (E ^ 2 - ρ ^ 2))
          (-1 * (1 / (2 * sqrt (E ^ 2 - ρ ^ 2)) * (-2 * ρ))) ρ := by
        apply HasDerivAt.const_neg
        exact h9
      have h11 : -1 * (1 / (2 * sqrt (E ^ 2 - ρ ^ 2)) * (-2 * ρ)) = ρ / sqrt (E ^ 2 - ρ ^ 2) := by
        field_simp [h5.ne']
        <;> ring_nf
        <;> field_simp [h5.ne']
        <;> ring_nf
      rw [h11] at h10
      exact (hasDerivAt_deriv_eq h10).symm ▸ by rfl
    exact h6

  -- Apply the fundamental theorem of calculus
  have h_int : IntervalIntegrable (deriv (fun ρ => -sqrt (E ^ 2 - ρ ^ 2))) volume 0 ρ₀ := by
    -- The derivative is continuous on [0, ρ₀] since ρ₀ < E
    -- so it's interval integrable
    apply IntervalIntegrable.continuousOn
    intro x hx
    have h2 : 0 ≤ x := hx.1
    have h3 : x ≤ ρ₀ := hx.2
    have h4 : x ^ 2 < E ^ 2 := by
      calc
        x ^ 2 ≤ ρ₀ ^ 2 := by gcongr
        _ < E ^ 2 := by gcongr
    have h5 : E ^ 2 - x ^ 2 > 0 := by linarith
    -- The function is continuous at x
    apply ContinuousAt.div
    · apply ContinuousAt.mul
      · exact continuousAt_id
      · exact continuousAt_const
    · apply ContinuousAt.sqrt
      · exact continuousAt_const.sub continuousAt_id.pow 2
      · have h6 : E ^ 2 - x ^ 2 > 0 := by linarith
        exact ne_of_gt h6

  have h_diff : ∀ x ∈ Icc (0 : ℝ) ρ₀, DifferentiableAt ℝ (fun ρ => -sqrt (E ^ 2 - ρ ^ 2)) x := by
    intro x hx
    have h2 : 0 ≤ x := hx.1
    have h3 : x ≤ ρ₀ := hx.2
    have h4 : x ^ 2 < E ^ 2 := by
      calc
        x ^ 2 ≤ ρ₀ ^ 2 := by gcongr
        _ < E ^ 2 := by gcongr
    have h5 : E ^ 2 - x ^ 2 > 0 := by linarith
    have h6 : DifferentiableAt ℝ (fun ρ => E ^ 2 - ρ ^ 2) x := by
      apply DifferentiableAt.const_sub
      exact (differentiableAt_id.pow 2)
    have h7 : DifferentiableAt ℝ (fun x => sqrt x) (E ^ 2 - x ^ 2) := by
      apply DifferentiableAt.sqrt
      linarith
    exact h7.comp h6

  -- Now apply the fundamental theorem of calculus
  have h_main : ∫ ρ in (0)..ρ₀, deriv (fun ρ => -sqrt (E ^ 2 - ρ ^ 2)) ρ
      = (-sqrt (E ^ 2 - ρ₀ ^ 2)) - (-sqrt (E ^ 2 - (0 : ℝ) ^ 2)) := by
    apply intervalIntegral.integral_deriv_eq_sub
    · exact h_diff
    · exact h_int

  -- Simplify the right-hand side
  have h_rhs : (-sqrt (E ^ 2 - ρ₀ ^ 2)) - (-sqrt (E ^ 2 - (0 : ℝ) ^ 2)) = E - sqrt (E ^ 2 - ρ₀ ^ 2) := by
    have h2 : sqrt (E ^ 2 - (0 : ℝ) ^ 2) = E := by
      rw [sub_zero]
      rw [sqrt_eq_iff] <;> norm_num <;> linarith
    rw [h2]
    ring_nf

  -- Put it all together
  calc
    ∫ ρ in (0)..ρ₀, ρ / sqrt (E ^ 2 - ρ ^ 2)
      = ∫ ρ in (0)..ρ₀, deriv (fun ρ => -sqrt (E ^ 2 - ρ ^ 2)) ρ := by
      apply intervalIntegral.integral_congr_ae
      · intro x hx
        have h2 : x ∈ Icc (0 : ℝ) ρ₀ := by
          simpa [mem_Icc] using hx
        rw [h_deriv x h2]
    _ = (-sqrt (E ^ 2 - ρ₀ ^ 2)) - (-sqrt (E ^ 2 - (0 : ℝ) ^ 2)) := h_main
    _ = E - sqrt (E ^ 2 - ρ₀ ^ 2) := h_rhs