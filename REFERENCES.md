# References

Sources below support the mathematics, rather than the guide's teaching order. Original examples and the habitat map are attributed separately in [Attribution](ATTRIBUTION.md).

## How to use this bibliography

The [core lessons](README.md#take-the-tour) are the plain-language entry route. These references let you check a claim or continue studying. Most source texts assume more mathematics than the guide.

| If you want to continue with… | An accessible next source, relative to this list | More technical directions |
|---|---|---|
| Rates, totals, and space | OpenStax's worked textbook sections | Differential equations, forms, and manifolds |
| Differences and approximation | Kleitman's beginner notes | Numerical analysis and error estimates |
| Logic | The Open Logic Project's *forall x* | Proof theory and type theory |
| Programs | The combinator-card and System F tracks, then Lynn and Bornholt | Bracket abstraction; Girard's *Proofs and Types*; Coquand–Huet |
| Program guarantees and memory | The credit and separate-cell tracks, then Aldrich's notes | Dijkstra's predicate transformers; Reynolds's separation logic |
| Data | *Database System Concepts*, query-language chapter | Safety and expressive power |
| Communication and actions | The everyday track examples, followed by the linked tutorials | Original process and action papers |
| Chance and cause | MIT's introductory probability course | Stochastic integration and Pearl's do-calculus |
| New directions and boundaries | The tensor and exterior tracks, then Peeters and Sjamaar | Tensor fields, differential forms, and manifolds |
| Complex numbers and operators | MIT's 18.04 notes and Higham's matrix-function introduction | Contour integration, residues, and operator calculi |
| Memory and resource use | The fractional and linear-logic tracks | Mainardi–Gorenflo's fractional operators; Pfenning's proof rules |
| Observation and knowledge | The card and crate tracks, then Open Logic and Pawlak | Dynamic epistemic models, rough approximations, and behavioral equivalence |
| Measurements and interventions | The measurement-calculus and do-calculus tracks | Danos–Kashefi–Panangaden's patterns; Pearl's identification rules |

“Introductory” in a university source can still mean demanding for a new reader. The small examples in this guide are not a substitute for all that background.

## Classical calculus and analysis

- Strang, Gilbert; Herman, Edwin “Jed.” *Calculus Volume 1*. OpenStax, 2016. Modern instructional treatment:
  - [§3.1, Defining the Derivative](https://openstax.org/books/calculus-volume-1/pages/3-1-defining-the-derivative)
  - [§5.3, The Fundamental Theorem of Calculus](https://openstax.org/books/calculus-volume-1/pages/5-3-the-fundamental-theorem-of-calculus)
- Strang, Gilbert; Herman, Edwin “Jed.” *Calculus Volume 2*. OpenStax, 2016. [§4.1, Basics of Differential Equations](https://openstax.org/books/calculus-volume-2/pages/4-1-basics-of-differential-equations).
- Strang, Gilbert; Herman, Edwin “Jed.” *Calculus Volume 3*. OpenStax, 2016. [§6.7, Stokes' Theorem](https://openstax.org/books/calculus-volume-3/pages/6-7-stokes-theorem), for the vector-calculus setting.
- Spivak, Michael. *Calculus on Manifolds*. W. A. Benjamin, 1965. Differential forms and the general Stokes theorem.

These support modern formulations, not historical priority claims.

## Discrete and numerical methods

- Stanley, Richard P. [*Enumerative Combinatorics*, Volume 1, second edition](https://math.mit.edu/~rstan/ec/ec1.pdf), author-hosted text, §1.9. Difference tables, the forward-difference operator, and the shift operator. This is an advanced source; the [tile track](tracks/change/finite-difference-calculus.md) starts with a small construction.
- Demanet, Laurent. [MIT 18.336 notes, spring 2011](https://math.mit.edu/icg/resources/teaching/18.336-spring2011/notes-18.336.pdf), Chapter 1. Finite-difference methods and their operator notation. These notes divide a first difference by the grid spacing; our sequence track writes that division separately.
- Kleitman, Daniel J. *Calculus for Beginners and Artists*, MIT, [Chapter 9: Numerical Differentiation](https://math.mit.edu/~djk/calculus_beginners/chapter09/contents.html), especially [§9.1](https://math.mit.edu/~djk/calculus_beginners/chapter09/section01.html). Difference quotients and the effect of limited numerical precision.
- Demanet, Laurent. [MIT 18.330 numerical analysis notes, draft April 25, 2014](https://math.mit.edu/icg/resources/teaching/18.330/18.330-Apr-2014.pdf), Chapter 2, “Integrals as sums and derivatives as differences.” Trapezoidal sums, finite differences, and error orders.
- Strang, Gilbert; Herman, Edwin “Jed.” *Calculus Volume 2*, OpenStax, [§3.6, Numerical Integration](https://openstax.org/books/calculus-volume-2/pages/3-6-numerical-integration). Trapezoidal approximation and error bounds.

The finite-sum cancellation and product identities are shown directly in the [finite-difference track](tracks/change/finite-difference-calculus.md). The [numerical track](tracks/change/numerical-calculus.md) separates approximation error from measurement error and checks its estimates against a known curve.

## Differential equations and initial values

- Strang, Gilbert; Herman, Edwin “Jed.” *Calculus Volume 2*, OpenStax: [§4.1, Basics of Differential Equations](https://openstax.org/books/calculus-volume-2/pages/4-1-basics-of-differential-equations); [§4.2, Direction Fields and Numerical Methods](https://openstax.org/books/calculus-volume-2/pages/4-2-direction-fields-and-numerical-methods); [§4.3, Separable Equations](https://openstax.org/books/calculus-volume-2/pages/4-3-separable-equations); [§4.5, First-Order Linear Equations](https://openstax.org/books/calculus-volume-2/pages/4-5-first-order-linear-equations). Initial values, Euler's method, Newton's cooling model, and solution methods.

The [tank track](tracks/change/differential-equations.md) specifies a controlled drain proportional to the water amount. It is an idealized feedback rule, not a claim about every hole in a tank. Its Euler step-size condition follows by subtracting the equilibrium from the displayed recurrence.

## Operational calculus and Laplace transforms

- Mattuck, Arthur; Miller, Haynes; Orloff, Jeremy; Lewis, John. MIT 18.03SC, *Differential Equations*, 2011. [Laplace Transform: Solving Initial Value Problems](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/laplace-transform-solving-initial-value-problems/), with readings on [derivatives](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/22aba4126352ce0f76930d858d8dffa5_MIT18_03SCF11_s29_1text.pdf), [inversion](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/93bc4d1fe9fadd1b4e78b90566cdc1e7_MIT18_03SCF11_s29_2text.pdf), [initial-value examples](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/30364347a6539066d841ffd90fece5b6_MIT18_03SCF11_s29_3text.pdf), and a [transform table](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/a85bae85be861b27bcbb0e5332483df2_MIT18_03SCF11_laptable29.pdf).
- Strang, Gilbert. [*Differential Equations and Linear Algebra* materials](https://math.mit.edu/~gs/dela/), including Laplace-transform explanations.

The [operational-calculus track](tracks/operators/operational-calculus.md) introduces one Laplace-transform route through this wider subject. Its smooth example uses the ordinary initial value; MIT's generalized-signal convention uses a left-hand initial value at zero. The distinction matters when impulses or jumps occur.

## Complex analysis and residue calculus

- MIT. [18.04, *Complex Analysis with Applications*, course notes](https://math.mit.edu/~dunkel/Teach/18.04_2019S/notes/1804_Main.pdf). Complex multiplication, complex derivatives (§4.5), contour integration, Laurent series, and the residue theorem.
- Cheng, Hung. [*Lecture 2: Complex Analysis*](https://math.mit.edu/classes/18.305/WWW_2004_HungCheng/second1.pdf), MIT 18.305, 2004. Complex integration and the Cauchy residue theorem.

## Calculus of variations

- Strang, Gilbert. “Calculus of Variations,” §7.2, course reading in *Mathematical Methods for Engineers II*, MIT OpenCourseWare (2006).\
  https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/e94c05947ed036cd6ad0150102087062_am72.pdf

- Encyclopedia of Mathematics. “Variational calculus.”\
  https://encyclopediaofmath.org/wiki/Variational_calculus
- Encyclopedia of Mathematics. “Variation.”\
  https://encyclopediaofmath.org/wiki/Variation
- Gel'fand, I. M.; Fomin, S. V. *Calculus of Variations*. Prentice-Hall, 1963.

## Stochastic calculus

- Encyclopedia of Mathematics. “Stochastic integral.”\
  https://encyclopediaofmath.org/wiki/Stochastic_integral
- Karatzas, Ioannis; Shreve, Steven E. *Brownian Motion and Stochastic Calculus*. Springer, 1988.

- Varadhan, S. R. S. [Notes on stochastic integration](https://math.nyu.edu/~varadhan/fall06/fall06.3.pdf), NYU, 2006. Itô integration and comparison with Stratonovich.
- Kunze, Markus. [*An Introduction to Malliavin Calculus*](https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.020/kunze/malliavin/Malliavin_skript.pdf), University of Ulm lecture notes, 2013. Advanced reading for the map's Malliavin entry.

## Probability and causal inference

- Tsitsiklis, John; Jaillet, Patrick. [*Introduction to Probability*](https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/pages/part-i-the-fundamentals/), MIT OpenCourseWare, 2018. Course using Bertsekas and Tsitsiklis, *Introduction to Probability*, 2nd ed. (2008), with author-supplied summary material.
- Pearl, Judea. [*The Do-Calculus Revisited*](https://ftp.cs.ucla.edu/pub/stat_ser/r402.pdf), 2012. Causal-effect identification and the role of graphical assumptions. This is technical reading, not a beginner exercise book.
- Pearl, Judea. [“Causal Diagrams for Empirical Research”](https://ftp.cs.ucla.edu/pub/stat_ser/R218-B.pdf), *Biometrika*, 1995. See §3.1 for the back-door criterion and adjustment formula. The [do-calculus track](tracks/observation/do-calculus.md) supplies an original numerical example.

## Geometry and field calculi

- Peeters, Kasper. [*Introduction to Tensor Calculus*](https://www.maths.dur.ac.uk/users/kasper.peeters/pdf/tensor_en.pdf), Durham University lecture notes. Tensor components, transformation rules, and derivatives.
- Tong, David. [*General Relativity*, §2](https://www.davidtong.org/teaching/general-relativity/grhtml/S2). §2.3 develops tensors and tensor fields; §2.4 develops differential forms and Stokes' theorem. This is advanced reading.
- Sjamaar, Reyer. [*Manifolds and Differential Forms*](https://pi.math.cornell.edu/~sjamaar/manifolds/manifold.pdf), revised 2017. Chapters 2, 5, and 9 explain forms, boundaries, and Stokes' theorem in Euclidean space and on manifolds.
- Ricci-Curbastro, Gregorio; Levi-Civita, Tullio. Foundational work on the absolute differential calculus / tensor calculus, 1900.
- Strang, Gilbert; Herman, Edwin “Jed.” *Calculus Volume 3*, OpenStax. [§4.6, Directional Derivatives and the Gradient](https://openstax.org/books/calculus-volume-3/pages/4-6-directional-derivatives-and-the-gradient), [§6.1, Vector Fields](https://openstax.org/books/calculus-volume-3/pages/6-1-vector-fields), and [§6.7, Stokes' Theorem](https://openstax.org/books/calculus-volume-3/pages/6-7-stokes-theorem).
- Spivak, Michael. *Calculus on Manifolds*. W. A. Benjamin, 1965. An advanced treatment of differential forms, integration, and Stokes' theorem.

Tensor, Ricci, and exterior methods overlap within differential geometry. This grouping is not a claim that the names identify disjoint subjects.

## Operators and fractional extensions

- Higham, Nicholas J. [“What Is a Matrix Function?”](https://nhigham.com/2020/06/09/what-is-a-matrix-function/), June 9, 2020. Definitions of matrix functions and their distinction from entrywise evaluation.
- Higham, Nicholas J. [“Functions of Matrices”](https://eprints.maths.manchester.ac.uk/2109/), in *Handbook of Linear Algebra*, CRC Press, 2014. Matrix functions provide an entry to functional-calculus ideas.
- Mainardi, Francesco; Gorenflo, Rudolf. [“Time-fractional derivatives in relaxation processes: a tutorial survey”](https://arxiv.org/abs/0801.4914). *Fractional Calculus and Applied Analysis* 10(3):269–308, 2007; arXiv version 2008. §1 gives Riemann–Liouville and Caputo definitions; later sections treat relaxation and viscoelasticity.
- Gorenflo, Rudolf; Mainardi, Francesco. [“Fractional Calculus: Integral and Differential Equations of Fractional Order”](https://arxiv.org/abs/0805.3823), arXiv version 2008 of their earlier book chapter. Fractional integration, differentiation, and differential equations.
- Strang, Gilbert. [*Differential Equations and Linear Algebra* materials](https://math.mit.edu/~gs/dela/), especially Fourier and Laplace transforms; see also his [“Nice Functions”](https://math.mit.edu/~gs/dela/nice_functions.pdf) for a concrete transform calculation.
- Mainardi, Francesco. [*An Introduction to Fractional Calculus*](https://www.dam.brown.edu/fractional_calculus/home.htm), Brown University short course, with [lecture materials](https://www.dam.brown.edu/fractional_calculus/lecture.htm). These develop specific fractional integral and derivative definitions.

## Logic and formal reasoning

- Open Logic Project. [*forall x*, natural deduction](https://forallx.openlogicproject.org/bookml/Ch16.html), and [proof-systems overview](https://builds.openlogicproject.org/content/first-order-logic/proof-systems/proof-systems.pdf). Modern explanations of logical languages and proof presentations.
- Girard, Jean-Yves. [*Proofs and Types*](https://www.paultaylor.eu/stable/Proofs+Types.html), translated with appendices by Paul Taylor and Yves Lafont. Cambridge University Press, 1989; corrected reprint 1990. Natural deduction, sequent calculus, Curry–Howard correspondence, System F, and linear logic. Graduate-level source.

- Frege, Gottlob. *Begriffsschrift*, 1879 — foundational predicate-logic lineage.
- Gentzen, Gerhard. Foundational work on natural deduction and sequent calculi, 1934–35.
- Stanford Encyclopedia of Philosophy. “Classical Logic.”

## Linear logic and resources

- Girard, Jean-Yves. “Linear Logic.” *Theoretical Computer Science* 50(1):1–101, 1987. DOI: 10.1016/0304-3975(87)90045-4.
- Pfenning, Frank. [*Linear Logic*](https://www.cs.cmu.edu/~fp/courses/15816-f01/handouts/linear.pdf), lecture notes, draft January 26, 2002. Linear hypotheses, simultaneous conjunction, linear implication, and unrestricted resources. The notes emphasize intuitionistic linear logic.

The token-stall example uses a small resource interpretation. It does not define all of linear logic, and linear and affine assumptions have different discard rules.

## Program logic and correctness

- Aldrich, Jonathan. [*Axiomatic Semantics and Hoare-style Verification*](https://www.cs.cmu.edu/~aldrich/courses/17-355-19sp/notes/notes11-hoare-logic.pdf), Carnegie Mellon University, 2019. Program contracts, inference rules, weakest preconditions, and loop proofs, especially §§2.1–2.2.
- Dijkstra, Edsger W. [EWD472: “Guarded commands, non-determinacy and formal derivation of programs”](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD472.html). Predicate transformers and program derivation.
- Reynolds, John C. [“Separation Logic: A Logic for Shared Mutable Data Structures”](https://www.cs.cmu.edu/~jcr/seplogic.pdf), 2002. Extending program logic with assertions about separate parts of storage and local reasoning.

The [Hoare-logic track](tracks/proof/hoare-logic.md) distinguishes partial-correctness triples from Dijkstra's termination-sensitive wp. The [separation-logic track](tracks/proof/separation-logic.md) uses Reynolds's classical exact-heap assertions and the frame rule, including its condition on modified variables.

## Process algebra and concurrency

- Milner, Robin. *A Calculus of Communicating Systems*. Springer LNCS 92, 1980.
- Hoare, C. A. R. [*Communicating Sequential Processes*](https://www.cs.ox.ac.uk/ucs/hoarebook.pdf), Prentice Hall, 1985. Author-hosted book; communication, deadlock, and process behavior.
- Hoare, C. A. R. “Communicating Sequential Processes.” *Communications of the ACM* 21(8), 1978.
- Bergstra, J. A.; Klop, J. W. “Process Algebra for Synchronous Communication.” *Information and Control* 60, 1984.
- Bergstra, J. A.; Klop, J. W. [*Algebra of Communicating Processes*](https://ir.cwi.nl/pub/1778/1778D.pdf), CWI-hosted author survey. §§1–2 introduce sequential, alternative, and parallel composition, communication functions, and encapsulation.
- van Glabbeek, Rob. [*Comparative Concurrency Semantics*, COMP3152/9152 course notes](https://cgi.cse.unsw.edu.au/~rvg/3152/notes.html), UNSW, 2012. CCS operational semantics, CSP synchronization, and the comparison of CCS/CSP/ACP on May 8.

The [coordination track](tracks/interaction/ccs-csp-acp.md) specifies which events must synchronize. Its CCS handoff becomes an internal tau step; its CSP handoff is initially visible. Any comparison of their traces must account for that choice.

## Locations and cryptographic processes

- Cardelli, Luca; Gordon, Andrew D. [*Mobile Ambients*](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/fossacs98.pdf), FoSSaCS 1998, LNCS 1378, pp. 140–155. §2 gives ambient nesting and the in, out, and open rules. A later journal version appeared in *Theoretical Computer Science* 240(1), 2000, pp. 177–213.
- Abadi, Martín; Gordon, Andrew D. [*A Calculus for Cryptographic Protocols: The Spi Calculus*](https://andrewdgordon.github.io/papers/ic99spi.pdf), *Information and Computation* 148(1), 1999, pp. 1–70. §§3–4 give symbolic cryptography, replay examples and repairs, and operational rules; later sections develop behavioral proof methods.

The [locations and messages track](tracks/interaction/ambient-and-spi-calculi.md) uses original bag, printer, and ticket stories. A basic ambient move depends on capability and nesting. The printer's one-use challenge check is an explicit protocol condition, not an automatic effect of encryption or a complete real-world security proof.

## Data and relations

- Silberschatz, Abraham; Korth, Henry F.; Sudarshan, S. *Database System Concepts*, [Chapter 27: Formal Relational Query Languages](https://www.db-book.com/online-chapters-dir/27.pdf). §§27.1–27.2 treat tuple/domain relational calculus, quantifiers, empty groups, and safety; §27.3 compares their expressive power with relational algebra.

- Codd, E. F. “A Relational Model of Data for Large Shared Data Banks.” *Communications of the ACM* 13(6), 1970.

The [tuple track](tracks/data/tuple-relational-calculus.md) queries whole records; the [domain track](tracks/data/domain-relational-calculus.md) queries field values and changes an existential question into a universal one. Both use finite, complete tables for the exercise and classical set semantics. Their particular bounded queries remain unchanged when unused possible values are added to the surrounding domains.

## λ-calculus

- Pfenning, Frank. “The λ-Calculus,” Lecture 1, *Types and Programming Languages*, Carnegie Mellon University, August 26, 2025. §§2–5 give syntax, binding, and reduction rules.\
  https://www.cs.cmu.edu/~fp/courses/15814-f25/lectures/01-lambda.pdf

- Church, Alonzo. Foundational papers on λ-definability and effective calculability.
- Stanford Encyclopedia of Philosophy. “The Lambda Calculus.” Substantive revision 2023.\
  https://plato.stanford.edu/entries/lambda-calculus/

## Combinatory logic

- Lynn, Ben. [*Combinatory Logic*](https://theory.stanford.edu/~blynn/lambda/cl.html), author-hosted Stanford exposition. S/K reduction, bracket abstraction, and translation from lambda expressions; includes an interactive evaluator.
- Diller, Antoni. [*Bracket abstraction algorithms*](https://www.cantab.net/users/antoni.diller/brackets/intro.html), author-hosted exposition and demonstrations. Combinator reductions, the identity $I=SKK$, and several abstraction algorithms.

The [rule-card track](tracks/computation/combinatory-logic.md) works through standard identities using original everyday stand-ins. Translation preserves a specified computational relationship, not necessarily expression size or step count.

## System F and parametric polymorphism

- Girard, Jean-Yves. [*Proofs and Types*, full text](https://www.paultaylor.eu/stable/prot.pdf), translated with appendices by Paul Taylor and Yves Lafont, 1989, corrected reprint 1990. Chapter 11 defines System F and data encodings; Chapter 14 proves strong normalization. See the [book's hosting page](https://www.paultaylor.eu/stable/Proofs+Types.html).
- Bornholt, James. [*Lecture 8: Polymorphism and System F*](https://www.cs.utexas.edu/~bornholt/courses/cs345h-24sp/lectures/8-system-f/), University of Texas at Austin, 2024. A twice-application recipe motivates explicit type abstraction and type application.
- Pfenning, Frank. [*Parametric Polymorphism*](https://www.cs.cmu.edu/afs/cs/Web/People/fp/courses/15814-f18/lectures/11-polymorphism.pdf), Carnegie Mellon University lecture notes, October 9, 2018. Quantification over types, typing restrictions, and the Girard/Reynolds origins.

The [System F track](tracks/types/system-f.md) uses familiar data types to teach the recipe; it separates those teaching conveniences from the pure calculus and its termination theorem.

## Proof calculi

- The [Open Logic proof-systems overview](https://builds.openlogicproject.org/content/first-order-logic/proof-systems/proof-systems.pdf) and Girard's [*Proofs and Types*](https://www.paultaylor.eu/stable/Proofs+Types.html) supply modern, directly accessible treatments. See also the logic section above.

- Gentzen, Gerhard. Foundational work on natural deduction and sequent calculi, 1934–35.
- Stanford Encyclopedia of Philosophy. “Natural Deduction Systems in Logic.” Revised 2026.\
  https://plato.stanford.edu/entries/natural-deduction/
- Stanford Encyclopedia of Philosophy. “Proof Theory.”\
  https://plato.stanford.edu/entries/proof-theory/

## Calculus of Constructions

- Rocq documentation, [core language](https://rocq-prover.org/doc/master/refman/language/core/index.html). The Calculus of Inductive Constructions in the proof assistant formerly called Coq.

- Coquand, Thierry; Huet, Gérard. “The Calculus of Constructions.” *Information and Computation* 76(2–3):95–120, 1988. DOI: 10.1016/0890-5401(88)90005-3.

## π-calculus

- Milner, Robin; Parrow, Joachim; Walker, David. “A Calculus of Mobile Processes, I.” *Information and Computation* 100(1):1–40, 1992. DOI: 10.1016/0890-5401(92)90008-4.
- Milner, Robin; Parrow, Joachim; Walker, David. “A Calculus of Mobile Processes, II.” *Information and Computation* 100(1):41–77, 1992. DOI: 10.1016/0890-5401(92)90009-5.
- Milner, Robin. “The Polyadic π-Calculus: A Tutorial.” LFCS report ECS-LFCS-91-180, 1991; later published in *Logic and Algebra of Specification*.\
  https://www.lfcs.inf.ed.ac.uk/reports/91/ECS-LFCS-91-180/

## ρ-calculus and reflective process calculi

- Lybech, Stian. “Encodability and Separation for a Reflective Higher-Order Calculus.” arXiv:2209.02356, 2022.
- Lybech, Stian. “The Reflective Higher-Order Calculus: Encodability, Typability and Separation.” *Information and Computation* 297 (2024), 105138. DOI: 10.1016/j.ic.2024.105138.
- Meredith, Lucius Gregory; Stay, Michael. “Name-Free Combinators for Concurrency.” arXiv:1703.07054, 2017.
- Meredith, L. G.; Radestock, Matthias. “A Reflective Higher-order Calculus.” *Electronic Notes in Theoretical Computer Science* 141(5):49–67, 2005. DOI: 10.1016/j.entcs.2005.05.016.\
  https://www.sciencedirect.com/science/article/pii/S1571066105051893

## Situation, event, and fluent calculi

- McCarthy, John; Hayes, Patrick J. “Some Philosophical Problems from the Standpoint of Artificial Intelligence.” In *Machine Intelligence 4*, 1969.
- Stanford Encyclopedia of Philosophy. “Logic-Based Artificial Intelligence.”\
  https://plato.stanford.edu/entries/logic-ai/
- Kowalski, Robert; Sergot, Marek. “A Logic-based Calculus of Events.” *New Generation Computing* 4:67–95, 1986. Listed on [Kowalski's publications page](https://www.doc.ic.ac.uk/~rak/).
- Thielscher, Michael. “From Situation Calculus to Fluent Calculus: State Update Axioms as a Solution to the Inferential Frame Problem.” *Artificial Intelligence* 111(1–2):277–299, 1999.\
  https://www.cse.unsw.edu.au/~mit/Papers/AIJ99.pdf
- McCarthy, John. “Actions and Other Events in Situation Calculus.”\
  https://www-formal.stanford.edu/jmc/sitcalc.pdf

## Calculus of indications

- Kauffman, Louis H. *Laws of Form: An Exploration in Mathematics and Foundations*. Author-hosted exposition, including calling and crossing diagrams.\
  https://homepages.math.uic.edu/~kauffman/Laws.pdf

- Spencer-Brown, G. *Laws of Form*. London: Allen & Unwin, 1969. ISBN 0-04-510028-4.

## Epistemic and dynamic epistemic logic

- Open Logic Project. [*Public Announcement Logic*](https://builds.openlogicproject.org/content/applied-modal-logic/epistemic-logic/public-announcement-logic-lang.pdf). A short introduction to the language of truthful public announcements.
- Baltag, Alexandru; Moss, Lawrence S.; Solecki, Sławomir. [*The Logic of Public Announcements, Common Knowledge, and Private Suspicions*](https://ir.cwi.nl/pub/4497/04497D.pdf). CWI report SEN-R9922, 1999, following their TARK 1998 paper. Models, epistemic actions, semantics, and proof systems.
- Charrier, T.; Herzig, A.; Lorini, E.; Maffre, F.; Schwarzentruber, F. [“Building Epistemic Logic from Observations and Public Announcements”](https://cdn.aaai.org/ocs/12899/12899-57552-1-PB.pdf), 2016. Observation-based knowledge and changes to information and visibility.

## Rough sets and limited distinctions

- Pawlak, Zdzisław. [“Rough Sets”](https://link.springer.com/article/10.1007/BF01001956). *International Journal of Computer & Information Sciences* 11:341–356, 1982. DOI: 10.1007/BF01001956. Approximate set operations based on available distinctions.
- Pawlak, Zdzisław. [“Rough Set Theory and Its Applications to Data Analysis”](https://www.tandfonline.com/doi/abs/10.1080/019697298125470). *Cybernetics and Systems* 29(7), 1998. DOI: 10.1080/019697298125470. Lower and upper approximations and their uses in data analysis.

## Observational equivalence and bisimulation

- Sangiorgi, Davide. [*An Introduction to Bisimulation and Coinduction*](https://www.cs.unibo.it/~sangio/DOC_public/corsoFL.pdf), author-hosted notes. Labelled transition systems, traces, bisimulation, and proof techniques. See also his [book and reading materials](https://www.cs.unibo.it/~sangio/IntroBook.html).
- Milner, Robin; Sangiorgi, Davide. [“Barbed Bisimulation”](https://www.research.ed.ac.uk/en/publications/barbed-bisimulation/), ICALP 1992. Behavioral comparison based on reductions and observable capabilities.

The machine example uses strong bisimulation on an explicit labelled transition system. Barbed, weak, testing, and trace equivalences make different comparison choices.

## Measurement-based quantum computation

- Danos, Vincent; Kashefi, Elham; Panangaden, Prakash. [*The Measurement Calculus*](https://arxiv.org/abs/0704.1263). *Journal of the ACM* 54(2), 2007. The [full text](https://arxiv.org/html/0704.1263v1), §§2–3, gives commands, dependencies, and the two-qubit Hadamard pattern; §5 gives the rewrite calculus.
- Nielsen, Michael A. [*Cluster-state Quantum Computation*](https://arxiv.org/abs/quant-ph/0504097), 2005 preprint. A review of computation with entangled resources, measurements, and classical control.

## Relational quantum mechanics

- Rovelli, Carlo. [“Relational Quantum Mechanics”](https://arxiv.org/abs/quant-ph/9609002), 1996. A physical interpretation in which quantum descriptions concern relations between systems. The field map includes it as neighboring reading.

## Distinction graphs

- Goertzel, Ben. “Distinction Graphs and Graphtropy: A Formalized Phenomenological Layer Underlying Classical and Quantum Entropy, Observational Semantics and Cognitive Computation.” arXiv:1902.00741, 2019.\
  https://arxiv.org/abs/1902.00741

## Fuzzy Calculus / bounded observer geometry

Primary sources for Tiffany's use of the name Fuzzy Calculus. The track follows their specific definitions and theorem assumptions.

- Tiffany III, Paul Carver. *Principia Symbolica*, especially Book IV bounded-observer, observer-kernel, derivation, and curvature constructions.\
  https://paultiffany.github.io/Principia-Symbolica/
  - Book IV source labels: `definition:bk4_bounded_observer`, `definition:bk4_observer_kernel_convolution_map`, `theorem:bk4_fuzzy_fundamental` in [src/book4.tex](https://github.com/PaulTiffany/Principia-Symbolica/blob/main/src/book4.tex). Structured records and proof links are in the [canonical atlas](https://paultiffany.github.io/Principia-Symbolica/principia_atlas.json).
- Tiffany III, Paul Carver. *The Hypothesis Surface: An Operational Epistemology for Autonomous Research*, AGI-26 supplementary materials. The Figure 2 companion contains a reduced curve-local Fuzzy Fundamental Theorem of Calculus and Observer-Relative Stokes with bulk and boundary residues.\
  https://paultiffany.github.io/hypothesis-surface-agi26/
  - [Figure 2 companion source](https://github.com/PaulTiffany/hypothesis-surface-agi26/blob/master/supplementary/fig2_companion_fftc.tex): curve-local FFTC and Observer-Relative Stokes, with their own hypotheses.


## Bibliography discipline

A reference supports only the relation it actually establishes.

For example:

- a historical statement needs historical evidence;
- an encoding statement needs the encoding theorem;
- a separation claim needs its criteria;
- a structural analogy may be ours, but must be labeled as such.

[Home](README.md) · [Field map](PANTHEON.md) · [Attribution](ATTRIBUTION.md)
