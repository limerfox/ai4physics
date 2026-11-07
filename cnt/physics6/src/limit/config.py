from dataclasses import dataclass
from typing import Tuple

DEFAULT_H_VALUES = (1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5)
DEFAULT_M_VALUES = (0.5, 1.0, 2.0, 4.0)
DEFAULT_K_VALUES = (0.5, 1.0, 2.0, 4.0)
DEFAULT_T_VALUES = (-0.5, -0.25, 0.0, 0.25, 0.5)

# @dataclass(frozen=True)
# class RunConfig:
#     H: float
#     m: float
#     k: float
#     t_values: Tuple[float, ...] = DEFAULT_T_VALUES
#     x: float = 0.0
#     t_ref: float = 0.0
#     method: str = "mpmath"
#     dps: int = 80

#     def validate(self):
#         if self.H <= 0:
#             raise ValueError("H must be positive.")
#         if self.m <= 0:
#             raise ValueError("m must be positive.")
#         if self.k <= 0:
#             raise ValueError("k must be positive for this implementation.")
#         if not self.t_values:
#             raise ValueError("t_values must not be empty.")
#         if self.dps < 30:
#             raise ValueError("Use at least 30 decimal digits for mpmath.")
#         if self.method not in {"float64", "mpmath", "asymptotic"}:
#             raise ValueError(f"Unknown method: {self.method}")
