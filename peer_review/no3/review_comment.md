TEEE No.3 Reviewer A

This paper constructs the optimization algorithm by combining with the PSO and Whale Optimization algorithm for production and transportation collaborative scheduling task in Intelligent Manufacturing Environment. Moreover, it is verified that the optimization performance of this algorithm is superior to the others through numerical simulation. 

It provides an interesting data, but I think it still needs extensive revisions to be acceptable for publication in terms of originality, creativity, and readability. 

From this reason, the judgement is "C" (Rereview after major revision). It should be revised according to following major comments and improved as necessary.


# [Major Comments]
## major comment1 (General)
I think the readers cannot understand the originality, creativity, and usability of this paper although Section1 of the current manuscript describes the main innovations of this research work.
Simply laying out previous relevant studies cannot explain the difference between them and this paper; especially, all sentences from "Then [5] explored..." to the end of Section1 and Section2.
I believe there may be the following contributions: 1) how to formulate the collaborative scheduling problem between production and transportation; 2) how to solve the problem using algorithm; and 3) how good the solution is.
Please revise so that which parts are the same or different between them is clear based on the above perspectives (formulation, solver, and result). 

## major comment2 (General)
As major comment1, いくつかの引用されている先行研究は直接的に関係がなく、不要だと思う。
例えば、

## major comment3 (Chapter 2)
The end of Chapter 2 says "Furthermore, HPWL-IME has outperformed other techniques like SA, GA, CWOT, ACO, etc…," but there is no reference to this fact. If there is this paper’s originality in the proposed algorithm, the difference from conventional algorithms is important. To show this, please cite references or add the results using them in Chapter 4.

## major comment4 (Chapter 2)
The end of Chapter 2 says "Furthermore, HPWL-IME … when used with other heuristics taken for comparison like DTCST, ELNSs, and HMOVNS with various performance metrics.", but the performance of HPWL-IME (the proposed algorithm) should be written in Chapter 5 because it is shown in numerical experiments of this paper for the first time. Instead, please clarify the structural difference about how to solve the collaborative scheduling problem in Chapter 2.

## major comment5 (Chapter 3)
 I think the readers cannot understand the optimization problem which optimization variable, parameters, objective and constraint functions. Please revise it considering my idea below:
- Chapter 3 can be separated into optimization formulation and algorithm. So, the former is "Chapter 3: Collaborative Scheduling Problem" and the latter is "Chapter 4: Scheduling Algorithm".
- Section 3.1 shows the whole of collaborative scheduling optimization problem. "minimize_[x] f_1(x) + f_2(x)" shows the objective function, f_1 shows make-span time about production, f_2 shows delivery time about transportation, "g(x)<=0" shows constraints, x shows optimization variables. More details about f_1, f_2, g, and x are given in later sections.
- Section 3.2 shows objective and constraint functions about the production. 
- Section 3.3 shows objective and constraint functions about the transportation. 

## major comment6 (Section 3.4)
 It is important to describe and write the procedures or steps of the proposed algorithm because there is this paper’s originality in the proposed algorithm. Please rewrite correctly them as the following items:
- There is suddenly Step7 and 8 in Section3.4. I think they should be moved to below Step6 in Section 3.3. 

## major comment7 (Chapter 4)
 I cannot the usability of this paper. Please revise the manuscript according to the following items: 
- The evaluation index’s definition is not written correctly. Please add exact definition and description about the evaluation index.
- What is ObjFn in Fig.4? I cannot understand "Figure4 diagram shows the number of objective functions…" as description for ObjFn. In general, the number of objective and constraint functions in the optimization problem are determined before solve it. I guess the objective functions are Eqs.(2) and (5) but ObjFn is the range of 100 – 400 in Fig.4. (Fig.4)
  - I guess ARDI means the average of relative error about between observed (actual) and estimated make-span time, and "ARDI_S = 100*(1/N) \sum_[i=1]^N |(Est_i – Obj_i)/(Est_i)|, where N is the number of data, Est_i and Obj_i is the i-th estimated and observed make-span time (i=1,…,N)" may be correct. Moreover, it is more general called "mean absolute percentage error (MAPE) " or "mean absolute percentage deviation (MAPD)"[31] (Eq.7 and Fig.5).
  - I guess the parameters is determined by [27], but I cannot understand which symbols are; e.g., actual and observed make-span are written in Eq.7.

## major comment8 (Fig.7)
Fig.7 shows both of departure and transportation time in the results of each methods using 3D graph. However, the most of HPWL-IME’s bar is hidden by the others. The results should be shown as normal 2D-line plot which has the horizontal axis "departure time" and the vertical axis is "transportation time " (or velocity?) with different color’s line and marker corresponding methods. 

## major comment9 (Format)
The format of manuscript does not follow the author’s guidelines[29, 30]. Review and consider them and the already published papers in this journal. The following items should be modified according to them for publication: 
- The author’s affiliation and correspondence should be written on the left column in page 1 with multi rows.
- Although there should be plenty of space around some parts for visiblity, it is too narrow in the current manuscript. The guideline says it needs "Double Space" between keywords and sentence (Chapter 1), space around chapter’s title, figure (table) and sentence, and figure (table) and its caption.
- Although Figs. 1, 2, and 4 are placed in the middle of column, the guideline says the position of figures, photographs and tables inserted should be at the tops and bottoms of columns. 
- The balance of the blanks in some itemizations is clearly different from the others. Please unify them. 
- How to write the referenced literatures differs from the guideline. Is "published year" at the end?



# [Minor Comments]

## minor comment1 (Subsection 3.3.3)
The sentence "The goal is…" is twice in one paragraph and is difficult to read. For example, it should be "the goal is probably to reduce the overall makespan time considering both the process of production and transportation periods. Specifically, this is to identify T …."

## minor comment2 (Section 3)
There are many misstatements in the current manuscript. Please modify the following items so as for readers to understand:
- Is ":" needed behind Subsection 3.3.1, 3.3.2, and Section 3.4, 4.4, and 4.5’s title?
- In Eq.(6), I think "where a, b=1 ,,, C" is unnecessary because a = 0,…,C and b = 1,…,C+1 are still defined in the sum part.
- "Variable Neighbourhood Search" should be "Variable Neighborhood Search". (page 2, right column)
- What is "DT"? Is DT an abbreviation for Digital Twins? (page 3, left column)
- "using an Enhanced Large Neighborhood Search (ELNSs) approach is suggested with savings(s) technique." should be "using an Enhanced Large Neighborhood Search with savings technique (ELNSs) approach is suggested." (page 3, left column)
- "Lu et al. [23] Created a Hybridized Multi-verse Optimizer-Variable NS (HMOVNS)" should be "Lu et al. [23] created a Hybridized Multi-verse Optimizer-Variable NS (HMOVNS)." (page 3, left column)
- There is no verb in the sentence "The lack of study…", so please add it appropriately. (page 3, right column) 

## minor comment3 (Chapter 5)
Some terms of the current manuscript are not common in the optimization field.
Please modify them according to the following items: 
- In optimization field, the solution satisfying all constraint conditions should be called "infeasible" generally, not "viable". Please replace "viable" with "infeasible".
- In optimization field, the optimization problem consists of "objective function" and "constraint conditions" (simply called constraints), not "restrictions". Please replace "restriction" with "constraint".

# [Additional References]
[29]: "Author’s Guidelines for the Transactions of the Institute of Electrical Engineers of Japan" (https://www.iee.jp/wp-content/uploads/honbu/32-doc-kenq/guideline.pdf)
[30]: "Appendix 1: Sample of Paper and Technical Note" (https://www.iee.jp/wp-content/uploads/honbu/data-9014/ap01.pdf)
[31]: de Myttenaere et.al.: "Mean absolute percentage error for regression models", Neurocomputing 2016 (2015) (arXiv:1605.02541)
