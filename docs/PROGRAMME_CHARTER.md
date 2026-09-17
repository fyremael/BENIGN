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

For two local components with normal Hessian blocks \(A,B\) and cross block
\(C\), define

\[
\chi =
\left\|A^{-1/2}CB^{-1/2}\right\|_2.
\]

The condition \(\chi<1\) for positive block curvature follows from standard
linear algebra and is not itself a BENIGN novelty claim.

The research target is instead a law of the form

\[
\mathfrak B_{\mathrm{coupled}}
\succeq
F(
  \mathfrak B_1,
  \mathfrak B_2,
  \chi,
  \delta
),
\]

where \(\delta\) controls nonlinear curvature variation, quotient effects, or
other certified defects.

A useful law must:

1. go beyond restating local Schur-complement positivity;
2. admit matrix-free estimation;
3. remain non-vacuous under at least small multi-block composition;
4. predict a qualitative transition in controlled experiments.

## 7. Transformation classes

BENIGN distinguishes at least four classes.

### Conditioning transformations

Smooth invertible reparameterizations and metric/preconditioner changes may
dramatically change conditioning and trajectories while preserving local
critical-point inertia.

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
- that \(\chi\) alone is a novel result;
- that semantic equivalence is solved for arbitrary learned systems;
- that a transformer-scale experiment constitutes programme validation.

## 10. Programme disposition

Initial disposition:

`EXPLORATORY__FALSIFICATION_GATED`

The programme earns independent continuation only by satisfying the gate in
`NOVELTY_AND_FALSIFICATION_GATE.md`.
