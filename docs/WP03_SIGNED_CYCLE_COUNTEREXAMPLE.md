# BENIGN-WP03 Signed-Cycle Counterexample

Status: `G3_ANALYTIC_WITNESS_FOUND__HOLONOMY_ITSELF_IS_PRIOR_ART`

This note constructs the first three-block counterexample required by `WP00_PRIOR_ART_STRESS_TEST.md`.

The result is deliberately split into two statements:

1. **positive result for BENIGN:** norm-only local contracts lose decisive information even in a three-scalar-block optimization problem;
2. **novelty restriction:** the missing information is a signed/gain-graph switching invariant, so cycle sign / holonomy is reused mathematics, not a BENIGN novelty claim.

## 1. Family

Let

\[
V_\sigma(x_1,x_2,x_3)
=
\sum_{i=1}^3
\left(
\frac12x_i^2+
\frac14x_i^4
\right)
+h\sum_{i=1}^3x_i
+c\left(
\sigma_{12}x_1x_2+
\sigma_{23}x_2x_3+
\sigma_{31}x_3x_1
\right),
\]

with

\[
c=0.6,
\qquad
h=0.01,
\qquad
\sigma_{ij}\in\{+1,-1\}.
\]

The uncoupled module is

\[
f_i(x_i)=\frac12x_i^2+\frac14x_i^4,
\]

with critical object `x_i = 0` and local Hessian `H_i=1`.

The common linear term `h sum_i x_i` is treated as boundary forcing. It ensures that the actual coupled critical object is displaced from the uncoupled product critical object.

## 2. Two compositions with identical norm-only local data

Compare

### Composition A: balanced triangle

\[
(\sigma_{12},\sigma_{23},\sigma_{31})=(+1,+1,+1).
\]

Its signed cross-block matrix is

\[
K_A
=
c
\begin{pmatrix}
0&1&1\\
1&0&1\\
1&1&0
\end{pmatrix}.
\]

### Composition B: unbalanced triangle

\[
(\sigma_{12},\sigma_{23},\sigma_{31})=(+1,+1,-1).
\]

Its signed cross-block matrix is

\[
K_B
=
c
\begin{pmatrix}
0&1&-1\\
1&0&1\\
-1&1&0
\end{pmatrix}.
\]

Both systems expose exactly the same data to an edge-norm-only contract:

- every uncoupled normal Hessian is `1`;
- every edge coupling has magnitude `0.6`;
- `|K_A| = |K_B|` entrywise;
- `||K_A||_2 = ||K_B||_2 = 1.2`;
- the absolute gain matrix has spectral radius `1.2` in both cases.

Thus a raw unstructured Weyl bound gives only

\[
\lambda_{\min}(I+K_\sigma)
\ge 1-1.2=-0.2,
\]

which is inconclusive for both systems. Likewise, an absolute small-gain test based only on the `0.6` edge gains fails for both because its gain-matrix spectral radius exceeds one.

## 3. The actual reference spectra differ

For Composition A,

\[
\operatorname{spec}(I+K_A)
=\{0.4,0.4,2.2\}.
\]

For Composition B,

\[
\operatorname{spec}(I+K_B)
=\{-0.2,1.6,1.6\}.
\]

The norm-only contracts therefore identify the two interfaces while their signed assembled normal Hessians have different inertia.

## 4. Displacement is real, not ignored

The actual critical objects are not the origin because `h != 0`.

### 4.1 Balanced composition

Symmetry gives `x_1=x_2=x_3=a`, where

\[
a^3+2.2a+0.01=0.
\]

The derivative `3a^2+2.2` is strictly positive, so this equation has exactly one real root. Numerically,

\[
a=-0.004545411858\ldots
\]

and therefore

\[
x_A^*=(-0.004545411858\ldots)^3.
\]

More importantly, for every `x`,

\[
\nabla^2V_A(x)
=
I+K_A+3\,\operatorname{diag}(x_1^2,x_2^2,x_3^2)
\succeq 0.4I.
\]

Hence Composition A is globally strongly convex and its displaced critical object is its unique global minimum.

At the critical object the Hessian eigenvalues are approximately

\[
(0.400061982307,
 0.400061982307,
 2.200061982307).
\]

### 4.2 Unbalanced composition

By the `x_1=x_3` symmetry set `x_1=x_3=a` and `x_2=b`. The stationarity equations reduce to

\[
F_1(a,b)=a^3+0.4a+0.6b+0.01=0,
\]

\[
F_2(a,b)=b^3+b+1.2a+0.01=0.
\]

Write

\[
M=
\begin{pmatrix}
0.4&0.6\\
1.2&1
\end{pmatrix},
\qquad
M^{-1}
=
\begin{pmatrix}
-3.125&1.875\\
3.75&-1.25
\end{pmatrix}.
\]

The fixed-point map

\[
T(a,b)
=-M^{-1}
\begin{pmatrix}
0.01+a^3\\
0.01+b^3
\end{pmatrix}
\]

maps the rectangle

\[
R=[0,0.02]\times[-0.04,-0.01]
\]

strictly into itself. Indeed,

\[
T_1(R)\subset[0.012501875,0.012645],
\]

and

\[
T_2(R)\subset[-0.02511,-0.02500125].
\]

On `R`, the infinity-norm Lipschitz constant of `T` is bounded by

\[
\max(0.01275,0.0105)=0.01275<1.
\]

Banach's fixed-point theorem therefore gives a unique stationary point in `R`.

Numerically,

\[
x_B^*
=(0.012535547570\ldots,
 -0.025026981439\ldots,
 0.012535547570\ldots).
\]

At this point the Hessian eigenvalues are approximately

\[
(-0.199059614850,
  1.600471419859,
  1.601410084109).
\]

The stationary point is therefore a strict saddle.

The saddle classification can also be certified without trusting those decimal eigenvalues. On `R`,

\[
0\preceq
D(x)=3\operatorname{diag}(x_1^2,x_2^2,x_3^2)
\preceq 0.0048I.
\]

The unperturbed signed Hessian has eigenvalues `-0.2, 1.6, 1.6`. Hence the unique negative eigenvalue can move upward by at most `0.0048`, remaining below `-0.1952`, while the two positive eigenvalues remain positive. Thus the stationary point in `R` has inertia `(2+,1-)` throughout the certified tube.

## 5. What information did the norm-only contract discard?

Define the cycle sign

\[
\tau
=
\sigma_{12}\sigma_{23}\sigma_{31}.
\]

For Composition A, `tau=+1`; for Composition B, `tau=-1`.

Under local sign-coordinate changes

\[
x_i\mapsto s_i x_i,
\qquad s_i\in\{+1,-1\},
\]

edge signs transform as

\[
\sigma_{ij}\mapsto s_i\sigma_{ij}s_j,
\]

but the product around the cycle is unchanged.

Thus `tau` is invariant under the local gauge action. Taking absolute edge norms destroys exactly this invariant.

For higher-dimensional normal spaces, the analogous transformation is

\[
K_{ij}\mapsto Q_i^*K_{ij}Q_j
\]

under local orthogonal/unitary changes of frame. Products around closed walks transform by conjugation. Conjugacy invariants of those products are therefore candidate interface data that survive local gauge.

## 6. Novelty boundary: cycle holonomy is not ours

Signed-graph switching theory already establishes that cycle signs are invariant under switching, and that balance/unbalance is characterized by those cycle signs. Gain-graph theory generalizes this: switching equivalence of connected gain graphs is characterized by closed-walk gains up to simultaneous conjugacy, and unitary representations produce Hermitian block adjacency operators whose spectra are switching invariant.

Relevant prior art includes:

- signed-graph balance and switching equivalence: Harary's balance theory and its modern spectral formulations;
- M. Cavaleri, A. Donno, *On cospectrality of gain graphs*, Special Matrices 10 (2022), DOI `10.1515/spma-2022-0169`;
- T. Gao, J. Brodzki, S. Mukherjee, *The Geometry of Synchronization Problems and Learning Group Actions*, which interprets synchronization through flat bundles, gauge equivalence, and holonomy;
- recent twisted-Laplacian work showing directly that cycle holonomy can govern dynamical stability transitions in frustrated synchronization systems.

Therefore BENIGN must **not** claim discovery of cycle sign, switching invariance, gain-graph holonomy, or holonomy-controlled spectral effects.

## 7. What the example does establish for BENIGN

This example satisfies the intended G3 diagnostic-separation requirement at the analytic level:

1. raw cross-block operator norm is identical;
2. uncoupled component Hessian spectra are identical;
3. both systems have the same absolute gain graph;
4. one composition has a displaced minimum while the other has a displaced strict saddle;
5. raw unstructured norm/Weyl and absolute small-gain tests are inconclusive for both;
6. a structure-aware contract retaining the gauge-invariant cycle class distinguishes them;
7. a certified displacement tube then propagates the reference signed inertia to the actual displaced critical object.

This is evidence that a useful BENIGN contract cannot in general collapse interfaces to scalar edge norms.

## 8. Updated theorem target

The emerging object is not merely a gain matrix. It is a **gauge-covariant interface network**.

A candidate BENIGN module contract should expose local normal operators and interface maps only up to admissible local frame/gauge changes. The composition layer may then use gauge-invariant closed-walk information together with local displacement and curvature reserves.

The target is therefore strengthened to:

> Given local quotient-normal contracts and a sparse gauge-covariant interface graph, certify existence/localization and normal inertia of the actual coupled critical object using local/interface data, including the relevant switching/holonomy class and numerical uncertainty, without materializing the full coupled Hessian.

The holonomy/switching component is prior art. The unresolved BENIGN question is whether it can be combined with nonlinear critical-object displacement, normal-inertia reserve, sparse contract composition, and certified matrix-free numerics into a useful optimization theorem.

## 9. Disposition

`G3 = ANALYTIC_WITNESS_FOUND__FORMAL_CONTRACT_NOT_YET_PROVED`

`G1 = OPEN`

`G2 = OPEN`

`G4 = OPEN`

`G5 = OPEN`

The next obligation is to formulate a gauge-covariant three-block contract that reproduces the classifications above without assembling the full `3 x 3` Hessian as the certification step, and then determine whether that formulation is genuinely stronger than existing gain-graph spectral theory plus classical perturbation bounds.