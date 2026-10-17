"""
Numerical Experiment: Boyle's Law Verification
P * V = n * R * T (ideal gas law at constant T)

This script simulates pressure-volume measurements for an ideal gas
and verifies the inverse relationship P ∝ 1/V.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Constants
n = 1.0  # moles
R = 8.314  # J/(mol·K) - universal gas constant
T = 300.0  # K - constant temperature

# Volume range (in liters, converted to m³ for calculations)
V_liters = np.linspace(1.0, 10.0, 50)
V_m3 = V_liters / 1000.0  # convert to m³

# Calculate pressure using ideal gas law: P = nRT/V
P_pascals = n * R * T / V_m3
P_atm = P_pascals / 101325.0  # convert to atmospheres

# Verify Boyle's Law: P * V should be constant
PV_product = P_pascals * V_m3
PV_constant = n * R * T

# Calculate relative error
relative_error = np.abs(PV_product - PV_constant) / PV_constant

# Statistical verification
mean_PV = np.mean(PV_product)
std_PV = np.std(PV_product)
cv_PV = std_PV / mean_PV  # coefficient of variation

print("=" * 60)
print("BOYLE'S LAW NUMERICAL EXPERIMENT")
print("=" * 60)
print(f"Temperature: T = {T} K")
print(f"Amount of gas: n = {n} mol")
print(f"Gas constant: R = {R} J/(mol·K)")
print("-" * 60)
print(f"Expected P·V constant: {PV_constant:.4f} J")
print(f"Mean P·V product: {mean_PV:.4f} J")
print(f"Std deviation: {std_PV:.6f} J")
print(f"Coefficient of variation: {cv_PV:.6f}")
print(f"Maximum relative error: {np.max(relative_error) * 100:.6f}%")
print("-" * 60)
print(f"Number of data points: {len(V_liters)}")
print(f"Volume range: {V_liters[0]:.1f} - {V_liters[-1]:.1f} L")
print(f"Pressure range: {P_atm[0]:.4f} - {P_atm[-1]:.4f} atm")
print("=" * 60)

# Save data
np.savez('boyle_data.npz', 
         volume=V_liters, 
         pressure=P_atm, 
         PV_product=PV_product)

# Create figures
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Figure 1: P vs V (hyperbola)
axes[0, 0].plot(V_liters, P_atm, 'b-', linewidth=2, label='P = nRT/V')
axes[0, 0].set_xlabel('Volume (L)', fontsize=12)
axes[0, 0].set_ylabel('Pressure (atm)', fontsize=12)
axes[0, 0].set_title('Boyle\'s Law: P vs V', fontsize=14, fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].legend()

# Figure 2: P vs 1/V (linear)
axes[0, 1].plot(1/V_liters, P_atm, 'r-', linewidth=2)
axes[0, 1].set_xlabel('1/Volume (L⁻¹)', fontsize=12)
axes[0, 1].set_ylabel('Pressure (atm)', fontsize=12)
axes[0, 1].set_title('Linear Verification: P ∝ 1/V', fontsize=14, fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

# Figure 3: P·V product (should be constant)
axes[1, 0].plot(V_liters, PV_product, 'g-', linewidth=2, label='P·V product')
axes[1, 0].axhline(y=PV_constant, color='r', linestyle='--', linewidth=1.5, 
                    label=f'Expected: {PV_constant:.2f} J')
axes[1, 0].set_xlabel('Volume (L)', fontsize=12)
axes[1, 0].set_ylabel('P·V Product (J)', fontsize=12)
axes[1, 0].set_title('Conservation of P·V Product', fontsize=14, fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].legend()

# Figure 4: Relative error
axes[1, 1].plot(V_liters, relative_error * 100, 'm-', linewidth=2)
axes[1, 1].set_xlabel('Volume (L)', fontsize=12)
axes[1, 1].set_ylabel('Relative Error (%)', fontsize=12)
axes[1, 1].set_title('Numerical Precision of P·V = const', fontsize=14, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('boyle_results.png', dpi=150, bbox_inches='tight')
plt.savefig('boyle_results.pdf', bbox_inches='tight')

print("\nFigures saved: boyle_results.png, boyle_results.pdf")
print("Data saved: boyle_data.npz")
print("Experiment completed successfully.")