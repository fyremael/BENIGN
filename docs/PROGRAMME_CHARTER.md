# BENIGN Programme Charter

## 1. Name

**BENIGN — Constructive Benignity for Nonconvex Optimization**

BENIGN is a name, not a forced acronym.

## 2. Research thesis

Many optimization difficulties are not invariant under semantically equivalent
presentations.

For a suitable class of structured problems, it may be possible to engineer
the representation, quotient geometry, metric, composition interfaces, and
discrete optimizer dynamics so that nuisance nonconvexity is eliminated or
converted into controlled gauge freedom while the remaining intrinsic
nonconvexity has robust quantitative structure.

The programme seeks a calculus only if such transformation and composition
rules can be made mathematically explicit and experimentally predictive.

## 3. Optimization presentation

The initial formal object is an optimization presentation

\[
\mathscr P =
(\Theta,\mathcal Z,\pi,G,L,g,\Phi_h,\mathcal I),
\]

with:

- \(\Theta\): computational parameter/state space;
- \(\mathcal Z\): semantic object space;
- \(\pi:\Theta\to\mathcal Z\): semantic realization map;
- \(G\): exact gauge/symmetry action contained in fibers of \(\pi\);
- \(L\): represented objective;
- \(g\): metric/preconditioner;
- \(\Phi_h\): actual discrete optimizer map, including optimizer state;
- \(\mathcal I\): composition/interface structure.

The semantic object is \(\pi(\theta)\), not the coordinate vector \(\theta\).

For the first tranche, semantic equivalence must be exact or possess an explicit
error bound. Vague equivalence of "capability" is not admissible evidence.

## 4. Landscape certificate

The initial landscape certificate is built from normal/quotient margins such as

\[
\mathfrak B_L=(\eta,\gamma,\mu,r),
\]

where, in appropriate regions,

\[
\|\operatorname{grad} L\|\ge\eta,
\]

\[
\lambda_{\min}(H_\perp)\le-\gamma,
\]

and near the semantic solution manifold

\[
H_\perp\succeq\mu I.
\]

Gauge directions are not to be misclassified as pathological zero curvature.

The exact certificate may change during WP01–WP03. These symbols are programme
scaffolding, not a frozen theorem statement.

## 5. Dynamical certificate

Landscape structure alone is insufficient.

For the implemented optimizer-state map

\[
z_{t+1}=\Phi_h(z_t),
\]

BENIGN separately studies the Jacobian

\[
J=D\Phi_h
\]

and finite-horizon amplification

\[
G_T=\max_{0\le k\le T}\|J^k\|.
\]

Spectral-radius stability does not by itself exclude large transient growth in
nonnormal systems.

The programme therefore treats landscape benignity and dynamical benignity as
distinct proof obligations.

## 6. Composition target

The first composition unit test is restricted to a positive-normal-curvature
sector. For two components near local minima, let \(A\succ0\) and \(B\succ0\)
be their normal Hessian blocks and let \(C\) be the cross block. Define

\[
\chi =
\left\|A^{-1/2}CB^{-1/2}\right\|_2.
\]

The condition \(\chi<1\) for positive block curvature follows from standard
linear algebra and is not itself a BENIGN novelty claim.

This quantity must not be silently extended to indefinite saddle blocks. In a
strict-saddle sector, BENIGN requires a separate signed/inertia-stability
formulation that preserves the relevant negative direction while controlling
coupling to positive and gauge directions.

A second issue is equally important: nonlinear coupling generally moves the
critical point. A compositional theorem therefore cannot inspect only the block
Hessian at an uncoupled stationary point. It must first establish persistence or
continuation of a nearby critical object under coupling, with an explicit bound
on its displacement, and then certify the normal/quotient Hessian at that
displaced critical object.

The research target is therefore a law of the schematic form

\[
\mathfrak B_{\mathrm{coupled}}
\succeq
F(
  \mathfrak B_1,
  \mathfrak B_2,
  \mathcal C,
  \delta,
  \varepsilon
),
\]

where \(\mathcal C\) denotes the appropriate curvature-normalized coupling
object, \(\delta\) controls nonlinear curvature variation and critical-point
displacement, and \(\varepsilon\) is a certified numerical-estimation error.

A useful law must:

1. go beyond restating local Schur-complement positivity;
2. include existence/continuation and displacement of the coupled critical
   object when coupling changes the stationarity equations;
3. distinguish positive-curvature and strict-saddle sectors rather than using
   an SPD normalization outside its domain;
4. admit matrix-free estimation with explicit error bounds;
5. remain non-vacuous under at least small multi-block composition;
6. predict a qualitative transition in controlled experiments.

Near a decision boundary, a point estimate is not a certificate. Matrix-free
inverse-curvature and spectral approximations must carry an error bound or
interval sharp enough to determine whether the available reserve has actually
been exhausted.

## 7. Transformation classes

BENIGN distinguishes at least four classes.

### Conditioning transformations

Smooth invertible reparameterizations preserve the inertia of the Hessian
bilinear form at a critical point by congruence. Metric and preconditioner
changes can substantially alter operator spectra and trajectories while leaving
the underlying stationary set unchanged when the objective itself is fixed.
These effects must not be confused with topology-changing presentations.

### Gauge removal

Quotienting and gauge fixing remove semantically redundant directions.

### Topology-changing presentations

Noninjective lifts, factorization, overparameterization, manifold restriction,
normalization, and objective shaping may alter critical structure and require
separate semantic-preservation proofs.

### Numerical/dynamical transformations

Splitting, retractions, momentum, reversibility, step size, and integrator
choice alter implemented dynamics even when the continuous objective is fixed.

## 8. Relationship to existing GCL work

BENIGN is upstream of individual implementation programmes.

Candidate transfer targets and instruments include:

- MODULUS: metric and dynamics construction;
- BoundaryContract: interface-gain instrumentation;
- CPS: optimizer-state dynamical diagnostics;
- SPINDLE: splitting and discretization;
- nGPT / RSSD: representation and manifold test cases;
- SPLICE: coupling and noncommutativity diagnostics;
- Neural Krylov methods: matrix-free inverse-curvature actions.

These programmes are not BENIGN's conceptual parent.

## 9. Initial nonclaims

BENIGN does not presently claim:

- a general calculus for arbitrary nonconvex optimization;
- that deep-learning landscapes are globally benign;
- that strict-saddle theory adequately describes transformer-scale systems;
- that benign continuous landscapes imply benign discrete optimization;
- that \(\chi\) alone is a novel result or a valid saddle-sector certificate;
- that semantic equivalence is solved for arbitrary learned systems;
- that a transformer-scale experiment constitutes programme validation.

## 10. Programme disposition

Initial disposition:

`EXPLORATORY__FALSIFICATION_GATED`

The programme earns independent continuation only by satisfying the gate in
`NOVELTY_AND_FALSIFICATION_GATE.md`.
