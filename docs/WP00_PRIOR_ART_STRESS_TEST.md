# BENIGN-WP00 Prior-Art Stress Test

Status: `NOVELTY_WEDGE_SURVIVES_ONLY_IN_STRONG_FORM__G1_NOT_YET_PASSED`

This note records the first serious attempt to kill the BENIGN composition thesis before implementation.

## 1. Result

The weak form of the proposed BENIGN theorem is not novel enough.

A theorem saying only that sufficiently weak coupling preserves a nearby critical point and preserves Hessian inertia can be assembled from classical or established ingredients:

1. quantitative implicit/inverse-function or Newton-Kantorovich arguments for persistence and displacement of nondegenerate zeros;
2. Morse-Bott normal nondegeneracy after quotienting exact gauge directions;
3. Weyl/spectral-gap perturbation or Schur-complement/Haynsworth inertia arguments;
4. block diagonal dominance / H-matrix / small-gain conditions for multi-block nonsingularity;
5. structured-singular-value (`mu`) theory when the admissible coupling/uncertainty structure is known;
6. existing a priori and a posteriori Krylov/Lanczos error bounds for matrix-free spectral quantities.

BENIGN must therefore not claim novelty for any of those components or for their immediate juxtaposition.

## 2. Prior-art boundary sharpened

### 2.1 Representation and parametrization

Levin, Kileel, and Boumal develop a general framework for how smooth parametrizations affect local minima and first-/second-order stationary points, including quotienting symmetries, low-rank factorizations, and Burer-Monteiro-style lifts.

Reference:

- E. Levin, J. Kileel, N. Boumal, *The effect of smooth parametrizations on nonconvex optimization landscapes*, Mathematical Programming 209 (2025), 63-111. DOI: 10.1007/s10107-024-02058-3.

Consequence for BENIGN: transformation-of-landscape claims require a contribution beyond general lift/parametrization theory.

### 2.2 Morse-Bott normal geometry

The Morse-Bott lemma already supplies the local normal form around a nondegenerate critical submanifold. Exact symmetry directions therefore belong in the tangent/gauge sector, with nondegeneracy assessed on the normal bundle.

Reference:

- A. Banyaga, D. Hurtubise, *A proof of the Morse-Bott Lemma*, Expositiones Mathematicae 22 (2004), 365-373. DOI: 10.1016/S0723-0869(04)80014-8.

Consequence for BENIGN: using a normal Hessian instead of the raw Hessian is necessary but not itself novel.

### 2.3 Critical-point continuation and displacement

Quantitative implicit-function theorems provide explicit neighborhoods and parameter ranges in which zeros persist uniquely. Such theorems already support the basic operation "small coupling moves the critical point by a controlled amount."

A recent explicit Banach-space formulation appears in the appendix of:

- *Mean field coupled dynamical systems: Bifurcations and phase transitions*, Advances in Mathematics (2025). DOI: 10.1016/j.aim.2025.110115.

Consequence for BENIGN: a displacement bound derived only from invertibility plus derivative variation is insufficient for G1.

### 2.4 Block inertia and Schur complements

Haynsworth-type inertia additivity and generalized Schur complements already characterize the inertia of Hermitian block matrices under broad hypotheses. Recent work extends generalized-Schur-complement inertia statements using Moore-Penrose inverses and bounded operators.

References:

- J. H. Maddocks, *Restricted quadratic forms, inertia theorems, and the Schur complement*, Linear Algebra and its Applications 108 (1988), 1-36. DOI: 10.1016/0024-3795(88)90177-2.
- T. Sano, *Moore-Penrose inverse, generalized Schur complement and inertia*, Acta Scientiarum Mathematicarum (2026). DOI: 10.1007/s44146-026-00231-y.

Consequence for BENIGN: a two-block signed-inertia result obtained directly by Schur complement is not a standalone contribution.

### 2.5 Block dominance and network small gain

Norm-based multi-block conditions are old. Block diagonal dominance gives nonsingularity conditions, and H-matrix/comparison-matrix theory packages these conditions through nonnegative comparison matrices. Nonlinear small-gain theory goes considerably further, constructing global/interconnected stability statements from subsystem gains; network versions use a gain operator or gain matrix and a spectral/small-gain condition.

References:

- C. Echeverria, J. Liesen, R. Nabben, *Block diagonal dominance of matrices revisited: Bounds for the norms of inverses and eigenvalue inclusion sets*, Linear Algebra and its Applications 553 (2018), 365-383. DOI: 10.1016/j.laa.2018.04.025.
- S. N. Dashkovskiy, B. S. Rueffer, F. R. Wirth, *Small Gain Theorems for Large Scale Systems and Construction of ISS Lyapunov Functions*, SIAM Journal on Control and Optimization 48 (2010). DOI: 10.1137/090746483.

Consequence for BENIGN: a condition of the form `rho(G) < 1` for a matrix of local block gains is not novel by itself.

### 2.6 Structured singular value

Robust-control `mu` theory already asks for the smallest structured perturbation that destroys a stability/nonsingularity property and refines unstructured small-gain bounds.

Representative reference:

- W. M. Haddad, V.-S. Chellaboina, D. S. Bernstein, *An implicit small gain condition and an upper bound for the real structured singular value*, Systems & Control Letters 29 (1997), 197-205. DOI: 10.1016/S0167-6911(96)00069-2.

Consequence for BENIGN: an "exact structured coupling radius" that is merely a static `mu` calculation is not sufficient novelty.

### 2.7 Matrix-free certification

Lanczos/Krylov methods already have rigorous error analyses, including explicit extremal-eigenvalue error estimates and a posteriori bounds for related matrix-function calculations.

References:

- T. Chen, *Uniform Error Estimates for the Lanczos Method*, SIAM Journal on Matrix Analysis and Applications (2021). DOI: 10.1137/20M1331470.
- T. Chen, A. Greenbaum, C. Musco, C. Musco, *Error Bounds for Lanczos-Based Matrix Function Approximation*, SIAM Journal on Matrix Analysis and Applications (2022). DOI: 10.1137/21M1427784.

Consequence for BENIGN: "matrix-free" is an implementation requirement. Novelty requires how certified local numerical intervals are propagated through the BENIGN contract, not the existence of Lanczos bounds.

## 3. What has been killed

The following candidate claims are rejected as BENIGN novelty claims:

- "small coupling preserves a nondegenerate critical point";
- "small Hessian perturbations preserve strict-saddle inertia";
- "a positive two-block Hessian remains positive when `chi < 1`";
- "a block gain matrix with spectral radius below one gives a nonsingular interconnection";
- "structured perturbation radii are better than raw operator norms";
- "Krylov methods can estimate extremal spectral quantities without materializing the Hessian".

These remain reusable machinery.

## 4. Strong-form BENIGN target

The surviving candidate is a **contract-level theorem** that certifies the optimization critical structure of a coupled system without assembling or globally diagonalizing that system.

Each module exposes only a local contract containing some subset of:

- an exact semantic/quotient chart;
- a normal critical object;
- an inverse-normal-Hessian action or certified approximation to it;
- a local normal spectral/inertia margin;
- a Hessian-variation bound on a declared tube;
- a boundary forcing bound caused by coupling;
- structured cross-block derivative gains;
- certified numerical intervals for estimated quantities.

A successful composition theorem must consume those local contracts and return all of the following:

1. **existence and localization:** a coupled quotient critical object exists in a certified product tube;
2. **displacement:** a componentwise bound on how far it moves from the uncoupled product critical object;
3. **inertia:** the normal Hessian at the actual displaced object has a certified inertia or strict-saddle/minimum classification;
4. **composition:** the certificate is obtained from local/interface data and remains non-vacuous for a sparse two-/three-module graph;
5. **numerical soundness:** interval/error uncertainty from matrix-free estimation is included in the reserve calculation;
6. **semantic soundness:** gauge directions are excluded by an exact quotient/normal construction rather than numerically thresholded away.

The theorem must not require construction of the full coupled Hessian as an intermediate object. That requirement is now central: otherwise the result is merely a repackaging of global perturbation theory.

## 5. Candidate mathematical form

Let the uncoupled quotient problem have blocks `q_i^*` with invertible normal Hessians `H_i`. Let coupling produce a gradient forcing vector `b` and block derivative gains `G(r)` on a product tube of radii `r`.

The first candidate fixed-point/displacement contract is componentwise:

```text
r >= b + G(r) r + n(r),
```

where `n(r)` is a certified nonlinear remainder bound. A weighted small-gain condition may be used internally to prove the self-map/contraction property, but this is reused machinery rather than the novelty claim.

The second contract is an inertia reserve evaluated over the same tube and at the resulting displaced critical object. Positive-normal-curvature sectors may use curvature normalization. Indefinite sectors must use signed/inertia-safe machinery; they must not reuse `A^{-1/2}` notation when `A` is indefinite.

The potential BENIGN contribution is the **joint closure of displacement, quotient-normal inertia, structured sparse composition, and certified numerical uncertainty into one local-contract theorem**.

## 6. Required counterexample

Before theorem development, construct a three-block nonlinear example in which all of the following are true:

1. raw cross-block norm is identical for two systems;
2. component Hessian spectra at the uncoupled critical objects are identical;
3. one composition preserves the intended critical classification while the other loses it after displacement;
4. a displacement-aware structured contract distinguishes the cases;
5. a global unstructured norm/Weyl bound is either inconclusive or materially more conservative.

If such a counterexample cannot be constructed, the proposed strong-form contract is unlikely to add enough information to justify BENIGN as a separate programme.

## 7. WP00 disposition

`G1 = OPEN`

`G2 = OPEN`

`G3 = OPEN`

`G4 = OPEN`

`G5 = OPEN`

The novelty wedge has survived the first stress test only in the strong form above. The weak composition theorem has been killed.

No programme promotion is authorized by this note.