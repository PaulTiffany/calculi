# References

Sources below support the mathematics, rather than the guide's teaching order. Original examples and the habitat map are attributed separately in [Attribution](ATTRIBUTION.md).

## How to use this bibliography

The [core lessons](README.md#take-the-tour) are the plain-language entry route. These references let you check a claim or continue studying. Most source texts assume more mathematics than the guide.

| If you want to continue with… | An accessible next source, relative to this list | More technical directions |
|---|---|---|
| Rates, totals, and space | OpenStax's worked textbook sections | Differential equations, forms, and manifolds |
| Differences and approximation | Kleitman's beginner notes | Numerical analysis and error estimates |
| Logic | The Open Logic Project's *forall x* | Proof theory and type theory |
| Programs | Pfenning's lambda lecture and CMU's program-logic notes | Dijkstra, Coquand–Huet, Reynolds |
| Data | *Database System Concepts*, query-language chapter | Safety and expressive power |
| Communication and actions | The everyday track examples, followed by the linked tutorials | Original process and action papers |
| Chance and cause | MIT's introductory probability course | Stochastic integration and Pearl's do-calculus |

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

- Kleitman, Daniel J. *Calculus for Beginners and Artists*, MIT, [Chapter 9: Numerical Differentiation](https://math.mit.edu/~djk/calculus_beginners/chapter09/contents.html).
- MIT, 18.330. [Numerical analysis notes, April 2014](https://math.mit.edu/icg/resources/teaching/18.330/18.330-Apr-2014.pdf). Derivatives as differences, integrals as sums, and numerical methods.

The finite-sum cancellation identity in lesson 3 is also shown directly; it needs no claim about historical priority.

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

## Geometry and field calculi

- Ricci-Curbastro, Gregorio; Levi-Civita, Tullio. Foundational work on the absolute differential calculus / tensor calculus, 1900.
- Strang, Gilbert; Herman, Edwin “Jed.” *Calculus Volume 3*, OpenStax. [§4.6, Directional Derivatives and the Gradient](https://openstax.org/books/calculus-volume-3/pages/4-6-directional-derivatives-and-the-gradient), [§6.1, Vector Fields](https://openstax.org/books/calculus-volume-3/pages/6-1-vector-fields), and [§6.7, Stokes' Theorem](https://openstax.org/books/calculus-volume-3/pages/6-7-stokes-theorem).
- Spivak, Michael. *Calculus on Manifolds*. W. A. Benjamin, 1965. An advanced treatment of differential forms, integration, and Stokes' theorem.

Tensor, Ricci, and exterior methods overlap within differential geometry. This grouping is not a claim that the names identify disjoint subjects.

## Operators and fractional extensions

- Higham, Nicholas J. [“Functions of Matrices”](https://eprints.maths.manchester.ac.uk/2109/), in *Handbook of Linear Algebra*, CRC Press, 2014. Matrix functions provide an entry to functional-calculus ideas.
- Strang, Gilbert. [*Differential Equations and Linear Algebra* materials](https://math.mit.edu/~gs/dela/), especially Fourier and Laplace transforms; see also his [“Nice Functions”](https://math.mit.edu/~gs/dela/nice_functions.pdf) for a concrete transform calculation.
- Mainardi, Francesco. [*An Introduction to Fractional Calculus*](https://www.dam.brown.edu/fractional_calculus/home.htm), Brown University short course, with [lecture materials](https://www.dam.brown.edu/fractional_calculus/lecture.htm). These develop specific fractional integral and derivative definitions.

## Logic and formal reasoning

- Open Logic Project. [*forall x*, natural deduction](https://forallx.openlogicproject.org/bookml/Ch16.html), and [proof-systems overview](https://builds.openlogicproject.org/content/first-order-logic/proof-systems/proof-systems.pdf). Modern explanations of logical languages and proof presentations.
- Girard, Jean-Yves. [*Proofs and Types*](https://www.paultaylor.eu/stable/Proofs+Types.html), translated with appendices by Paul Taylor and Yves Lafont. Cambridge University Press, 1989; corrected reprint 1990. Natural deduction, sequent calculus, Curry–Howard correspondence, System F, and linear logic. Graduate-level source.

- Frege, Gottlob. *Begriffsschrift*, 1879 — foundational predicate-logic lineage.
- Gentzen, Gerhard. Foundational work on natural deduction and sequent calculi, 1934–35.
- Stanford Encyclopedia of Philosophy. “Classical Logic.”

## Program logic and correctness

- Carnegie Mellon University, course 17-355. [Notes on Hoare logic](https://www.cs.cmu.edu/~aldrich/courses/17-355-19sp/notes/notes11-hoare-logic.pdf), 2019. Program contracts, inference rules, weakest preconditions, and partial correctness.
- Dijkstra, Edsger W. [EWD472: “Guarded commands, non-determinacy and formal derivation of programs”](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD472.html). Predicate transformers and program derivation.
- Reynolds, John C. [“Separation Logic: A Logic for Shared Mutable Data Structures”](https://www.cs.cmu.edu/~jcr/seplogic.pdf), 2002. Extending program logic with assertions about separate parts of storage and local reasoning.

## Process algebra and concurrency

- Milner, Robin. *A Calculus of Communicating Systems*. Springer LNCS 92, 1980.
- Hoare, C. A. R. [*Communicating Sequential Processes*](https://www.cs.ox.ac.uk/ucs/hoarebook.pdf), Prentice Hall, 1985. Author-hosted book; communication, deadlock, and process behavior.
- Hoare, C. A. R. “Communicating Sequential Processes.” *Communications of the ACM* 21(8), 1978.
- Bergstra, J. A.; Klop, J. W. “Process Algebra for Synchronous Communication.” *Information and Control* 60, 1984.
- Cardelli, Luca; Gordon, Andrew D. “Mobile Ambients.” 1998.
- Abadi, Martín; Gordon, Andrew D. “A Calculus for Cryptographic Protocols: The Spi Calculus.” *Information and Computation* 148(1), 1999.

## Data and relations

- Silberschatz, Abraham; Korth, Henry F.; Sudarshan, S. *Database System Concepts*, [Chapter 27: Formal Relational Query Languages](https://www.db-book.com/online-chapters-dir/27.pdf). Author-hosted treatment of relational algebra, tuple/domain relational calculus, safety, and expressive power.

- Codd, E. F. “A Relational Model of Data for Large Shared Data Banks.” *Communications of the ACM* 13(6), 1970.

## λ-calculus

- Pfenning, Frank. “The λ-Calculus,” Lecture 1, *Types and Programming Languages*, Carnegie Mellon University, August 26, 2025. §§2–5 give syntax, binding, and reduction rules.\
  https://www.cs.cmu.edu/~fp/courses/15814-f25/lectures/01-lambda.pdf

- Church, Alonzo. Foundational papers on λ-definability and effective calculability.
- Stanford Encyclopedia of Philosophy. “The Lambda Calculus.” Substantive revision 2023.\
  https://plato.stanford.edu/entries/lambda-calculus/

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

## Distinction graphs

- Goertzel, Ben. “Distinction Graphs and Graphtropy: A Formalized Phenomenological Layer Underlying Classical and Quantum Entropy, Observational Semantics and Cognitive Computation.” arXiv:1902.00741, 2019.\
  https://arxiv.org/abs/1902.00741

## Fuzzy Calculus / bounded observer geometry

This heading refers specifically to Tiffany's framework. These sources establish its definitions and claims; they do not make it the standard meaning of “fuzzy” across mathematics.

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
