#!/usr/bin/env python3
"""Deterministic BENIGN three-block signed-cycle witness.

This is a falsification/diagnostic fixture, not evidence of a new theorem.
It verifies the analytic example in docs/WP03_SIGNED_CYCLE_COUNTEREXAMPLE.md.

Dependency: numpy
"""

from __future__ import annotations

import json

import numpy as np


C = 0.6
H = 0.01
TOL = 1.0e-12


def coupling_matrix(signs: tuple[int, int, int]) -> np.ndarray:
    s12, s23, s31 = signs
    return C * np.array(
        [
            [0.0, s12, s31],
            [s12, 0.0, s23],
            [s31, s23, 0.0],
        ],
        dtype=np.float64,
    )


def gradient(x: np.ndarray, signs: tuple[int, int, int]) -> np.ndarray:
    return x + x**3 + H + coupling_matrix(signs) @ x


def hessian(x: np.ndarray, signs: tuple[int, int, int]) -> np.ndarray:
    return np.eye(3) + coupling_matrix(signs) + np.diag(3.0 * x**2)


def newton(signs: tuple[int, int, int]) -> np.ndarray:
    x = np.zeros(3, dtype=np.float64)
    for _ in range(32):
        g = gradient(x, signs)
        dx = np.linalg.solve(hessian(x, signs), -g)
        x = x + dx
        if np.linalg.norm(dx, ord=np.inf) < 1.0e-15:
            break
    residual = float(np.linalg.norm(gradient(x, signs), ord=np.inf))
    if residual >= TOL:
        raise AssertionError(f"stationarity residual too large: {residual}")
    return x


def summarize(name: str, signs: tuple[int, int, int]) -> dict[str, object]:
    K = coupling_matrix(signs)
    x_star = newton(signs)
    evals = np.linalg.eigvalsh(hessian(x_star, signs))
    return {
        "name": name,
        "signs": list(signs),
        "cycle_sign": int(np.prod(signs)),
        "raw_coupling_norm_2": float(np.linalg.norm(K, ord=2)),
        "reference_hessian_eigenvalues": np.linalg.eigvalsh(np.eye(3) + K).tolist(),
        "critical_point": x_star.tolist(),
        "gradient_residual_inf": float(np.linalg.norm(gradient(x_star, signs), ord=np.inf)),
        "critical_hessian_eigenvalues": evals.tolist(),
        "negative_eigenvalue_count": int(np.sum(evals < 0.0)),
    }


def main() -> None:
    balanced_signs = (1, 1, 1)
    unbalanced_signs = (1, 1, -1)

    K_bal = coupling_matrix(balanced_signs)
    K_unbal = coupling_matrix(unbalanced_signs)

    # Norm-only interface contracts see the same graph.
    np.testing.assert_allclose(np.abs(K_bal), np.abs(K_unbal), atol=0.0, rtol=0.0)
    np.testing.assert_allclose(
        np.linalg.norm(K_bal, ord=2),
        np.linalg.norm(K_unbal, ord=2),
        atol=1.0e-14,
        rtol=0.0,
    )
    assert np.linalg.norm(K_bal, ord=2) > 1.0

    balanced = summarize("balanced", balanced_signs)
    unbalanced = summarize("unbalanced", unbalanced_signs)

    # The actual displaced critical objects have different inertia.
    assert balanced["negative_eigenvalue_count"] == 0
    assert unbalanced["negative_eigenvalue_count"] == 1

    # The cycle switching class distinguishes the pair.
    assert balanced["cycle_sign"] == 1
    assert unbalanced["cycle_sign"] == -1

    payload = {
        "c": C,
        "h": H,
        "uncoupled_component_hessian": 1.0,
        "absolute_gain_matrix_spectral_radius": 1.2,
        "unstructured_weyl_lower_bound": -0.2,
        "balanced": balanced,
        "unbalanced": unbalanced,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
