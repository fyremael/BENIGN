# BENIGN Falsification Bench

The benchmark sequence is deliberately small and analytically anchored.

## Stage 0 — Exact two-block unit test

Use

\[
L_\alpha(x,y)
=
\frac12x^\top A x
+
\frac12y^\top B y
+
\alpha x^\top C y,
\]

with \(A,B\succ0\).

The exact transition is

\[
|\alpha|
\left\|
A^{-1/2}CB^{-1/2}
\right\|_2
=
1.
\]

Requirements:

- compute the exact transition;
- estimate it matrix-free;
- compare raw \(\|C\|\) against normalized interface gain;
- deliberately vary component curvature scales;
- verify that the normalized quantity predicts the invariant transition.

This is the instrumentation unit test, not a research result by itself.

## Stage 1 — Nonlinear local perturbation

Add controlled nonlinear terms with known local critical structure.

Track:

- gradient reserve;
- negative-curvature reserve;
- positive normal-curvature reserve;
- curvature variation radius.

Requirement: the derived reserve must bound the observed qualitative transition
without becoming vacuous.

## Stage 2 — Quotient/factorized problem

Use an exact semantic map such as

\[
X=UV^\top
\]

or

\[
X=YY^\top.
\]

Compare:

- raw parameter Hessian diagnostics;
- gauge-aware normal/quotient diagnostics;
- semantic reconstruction error.

Requirement: show a concrete case where gauge zero modes obscure the useful
geometry in raw coordinates.

## Stage 3 — Manifold presentation

Use a sphere- or Stiefel-constrained regression/PCA problem.

Compare semantically matched presentations such as:

- intrinsic manifold optimization;
- Euclidean penalty formulation;
- normalized/retracted parameterization.

Requirement: identify which observed changes are conditioning effects and which,
if any, alter admissible critical structure.

## Stage 4 — Discrete dynamics separation

Hold the local objective fixed.

Compare gradient descent against at least one momentum/accelerated
optimizer-state map.

Measure:

\[
\rho(J)
\]

and

\[
G_T=\max_{0\le k\le T}\|J^k\|.
\]

Requirement: demonstrate comparable landscape structure with materially
different transient dynamics.

## Mandatory baselines

Every relevant stage must include:

- semantic error;
- ordinary condition number;
- raw Hessian extremal spectrum;
- raw coupling norm;
- normalized interface quantity;
- optimizer-state spectral radius where applicable;
- finite-horizon amplification where applicable.

## Programme rule

No transformer or large neural-network experiment can substitute for failure on
Stages 0–4.
