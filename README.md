# BENIGN

**Constructive Benignity for Nonconvex Optimization**

A Grand Challenge Labs research programme.

## Programme question

Can a semantic optimization problem be compiled into a representation,
geometry, composition structure, and discrete dynamics whose nonconvexity is
quantitatively benign?

The working principle is:

> Preserve the residual; engineer the landscape.

BENIGN does not begin from the claim that nonconvexity is generically benign.
It studies when benign structure can be constructed deliberately, quantified,
composed, and preserved under actual numerical dynamics.

## Initial research wedge

The programme begins with **quantitative compositional benignity**.

Given independently understood optimization presentations, determine whether
landscape reserves, interface gains, and discrete dynamical margins can be
propagated through their composition without becoming vacuous.

The first interface unit test is restricted to positive normal curvature:

\[
\chi =
\left\|A^{-1/2} C B^{-1/2}\right\|_2,
\]

where \(A,B\succ0\) are normal Hessian blocks near local minima and \(C\) is
their cross-coupling.

The elementary two-block condition \(\chi < 1\) is only the instrumentation
unit test. It is not a saddle-sector certificate. The research target is a
nonlinear, quotient-aware, error-controlled matrix-free compositional
certificate that also accounts for critical-point displacement and, separately,
for signed/inertia stability in strict-saddle sectors.

## Programme status

**EXPLORATORY / FALSIFICATION-GATED**

No general constructive-benignity calculus is presently claimed.

The programme survives as a standalone GCL programme only if the first
theorem-and-bench tranche establishes a genuinely nontrivial composition rule
and a practical certificate that predicts controlled failures.

See:

- `docs/PROGRAMME_CHARTER.md`
- `docs/NOVELTY_AND_FALSIFICATION_GATE.md`
- `docs/WORK_PACKAGES.md`
- `experiments/README.md`
