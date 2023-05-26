# review_comment
- This paper studied empirically resampling strategies in noisy evolutionary multi-objective optimization assuming uncertainties in design variables and proposed the concept of bad point, which is able to illustrate how noise affects the performance of different MOEAs.
- It provides an intereting observation and data, and the focus of the paper is well phrased.
- But I think it still needs a considerable and minor revision to be improved.
- The judgement of overall quality assessment is "4" (Original; Accept).
- Please revise it according to following major comments as necessary and I hope minor comments will be useful in future research.

## [major comments]
### major comment1 (General)
- Letter and Size in the figures 1 and 2 are too small.
- Please write and illustrate them bigger.

### major comment2 (Section III-E)
- Maybe I made a mistake, I cannot find when to perform the resampling in the optimization algorithm.
- Please write clearly the resampling timing.


## [minor comments]
### minor comment1 (Section II-B)
- The existing noisy multi-objective optimization algorithm can be roughly categorized under five categories [23].
- My understanding, they are roughly divided into two categories "candidate generation" and "evaluation and selection" according to evolutionary algorithm's search structure, and subdivided into five categories in detail.
- The former category "candidate generation" (assuming x) includes (1) resampling and (2)implicit averaging. 
- The latter category "evaluation and selection" (assuming f(x))  includes (3) robust selection, (4) specialized search strategies, and (5) alternative fitness estimation methods.
- In this paper,  assuming uncertainties in design variables

### minor comment2 (Section III-E; Equation(2))
- Equation (2) is to simply modify x to the upper or lower boundary if x is outside the boundary by adding noise.
- But, the modification range is limited if general constraints are imposed.
- As the conclusion shows considering constraints is future task, I think this task is very important and recommend it.

### minor comment3 (Supplementaly material)
- The title of supplementaly material should be added clearly in the manuscript, e.g., the top of it like the main manusript.
- Also, figure' names in the Appendix A should be "Fig. AXX" to be distingushed from figures in the main manuscript.
