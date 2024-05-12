TEEE No.3 Reviewer A

This paper constructs the optimization algorithm by combining with the PSO and Whale Optimization algorithm for production and transportation collaborative scheduling task in Intelligent Manufacturing Environment. Moreover, it is verified that the optimization performance of this algorithm is superior to the others through numerical simulation. 

It provides an interesting data, but I think this paper has very difficult problem to be acceptable for publication in terms of originality, creativity, and readability. 

From this reason, the final judgement is "D" (reject). I think this paper needs to be radically rewritten after reconsidered deeply in terms of originality and usability. Detailed reasons and comments are as follows:

# [Major Reasons]
## major reason1 (General)
The readers cannot understand them although Chapter 1 describes the main innovations of this research work. Simply laying out previous relevant studies cannot explain the difference between them and this paper; especially, all sentences from "Then [5] explored..." in Chapter 1 to the end of Chapter 2. I believe there may be the following contributions: i) how to formulate the collaborative scheduling problem between production and transportation; ii) how to solve the problem using algorithm; and iii) how good the solution is, but cannot find the originality and creativity in anywhere. This is serious and fatal problem for pubilication. Examples are listed below:
- Most of [17]-[26] proposes the collaborative scheduling problem between production and transportation. 
- 

## major reason2 (General)
This paper cannot clarify and find the issues about collaborative scheduling manufacturing and transportation by citing literatures which are particularly relevant. Simply laying out previous studies is redundant and cannot explain the issue. Some referenced literatures in the current manuscript are not directly related to this paper's contribution. Example, I guess most of the literatures for Intelligent Manufacturing [3]-[8] are redundant and unnecessary. Considering the publication level, it is diffucult to find the issues and their difference by organizing the previous studies in short.

## major reason3 (Chapter 2)
Some sentences has no evidence or fact. Examples is listed below:
- The end of Chapter 2 says "Furthermore, HPWL-IME has outperformed other techniques like SA, GA, CWOT, ACO, etc…," but there is no reference to this fact. If there is this paper’s originality in the proposed algorithm, the difference from conventional algorithms is important. 
- The end of Chapter 2 says "Furthermore, HPWL-IME … when used with other heuristics taken for comparison like DTCST, ELNSs, and HMOVNS with various performance metrics.", but the performance of HPWL-IME (the proposed algorithm) should be written in Chapter 5 because it is shown in numerical experiments of this paper for the first time.

## major comment4 (Chapter 3)
 I think the readers cannot understand the optimization problem which optimization variable, parameters, and objective and constraint functions because they are not written in an organized and current manner. This is serious and fatal for publication. The optimization problem and algorithm’s part of the current manuscript should be rewritten radically with learning the previous studies[22, 29], which are nicely written.
Moreover, the points raised are presented for future reference below:
- Chapter 3 can be separated into optimization problem’s formulation and optimization algorithm. So, the former is "Chapter 3: Collaborative Scheduling Problem" and the latter is "Chapter 4: Scheduling Algorithm".
- Section 3.1 shows the whole of collaborative scheduling optimization problem. "minimize_[x] f_1(x) + f_2(x)" shows the objective function, f_1 shows the make-span time about production, f_2 shows the delivery time about transportation, "g(x)<=0" shows the constraints, x shows the optimization variables. More details about f_1, f_2, g, and x are given in later sections.
- As problem representation, after the whole of mathematical formulas firstly is written with equation’s number, the explanation sentence about each formula should be done.
- To add more illustlations or figures for explanation about the variables to the manuscript is better.
- Section 3.2 shows objective and constraint functions about the production. 
- I think the notation of the processing time is "t_p", but "\tau_x" meaning processing time each machine is better than before because there are many notation’s types of "t" in the manuscript.
- The constraints meaning machine’s total capacity is "t_p \in \mu <= \alpha" but "\sum_{x=1}^{\mu} t_{p, x} <= \alpha" is correct. (page 4, right column)
- The constraints meaning transportation route’s total capacity is "\gamma \in T <= \beta" but "\sum_{q=1}^{d} \gamma_q <= \beta" is correct. (page 4, right column)
- Eq.(2) represents the both of objective function "minimize alpha" and constraints "such that \sum~". They should be separated to different equations.
- Eq.(2) represents "\sum~, y \in T and x \in \mu" but this is not written currently as Equality or Inequality constraints. Please revise it. I guess the authors want to write "minimize \sum ms~".
- Section 3.3 shows objective and constraint functions about the transportation. 
- Please add the table defining the notations of that are used to describe the optimization problem.


## major comment6 (Section 3.4)
 It is important to describe and write the procedures or steps of the proposed algorithm because there is this paper’s originality in the proposed algorithm. Please rewrite correctly them as the following items:
- There is suddenly Step7 and 8 in Section3.4. I think they should be moved to below Step6 in Section 3.3. 

## major comment7 (Chapter 4)
 I guess the readers cannot understand the usability of this paper because the evaluation index’s definition is not written correctly. Please add exact definition and description about the evaluation index according to the following items: 
- What is ObjFn in Fig.4? I cannot understand "Figure4 diagram shows the number of objective functions…" as description for ObjFn. In general, the number of objective and constraint functions in the optimization problem are determined before solve it. I guess the objective functions are Eqs.(2) and (5) but ObjFn is the range of 100 – 400 in Fig.4. (Fig.4)
- I guess ARDI means the average of relative error about between observed (actual) and estimated make-span time, and "ARDI_S = 100*(1/N) \sum_[i=1]^N |(Est_i – Obj_i)/(Est_i)|, where N is the number of data, Est_i and Obj_i is the i-th estimated and observed make-span time (i=1,…,N)" may be correct. Moreover, it is more general called "mean absolute percentage error (MAPE) " or "mean absolute percentage deviation (MAPD)"[31] (Eq.7 and Fig.5).
- I guess the parameters is determined by [27], but I cannot understand which symbols are; e.g., actual and observed make-span are written in Eq.7.

## major comment8 (Chapter 4) 
Another reason I do not think the reader cannot understand the usability is the comparison in Chapter 4. 
- Comparison is not correctly. 

## major comment9 (Fig.7)
Fig.7 shows both of departure and transportation time in the results of each methods using 3D graph. However, the most of HPWL-IME’s bar is hidden by the others. The results should be shown as normal 2D-line plot which has the horizontal axis "departure time" and the vertical axis is "transportation time " (or velocity?) with different color’s line and marker corresponding methods. 

## major comment10 (Format)
The format of manuscript does not follow the author’s guidelines[29, 30]. Review and consider them and the already published papers in this journal. The following items should be modified according to them for publication: 
- The author’s affiliation and correspondence should be written on the left column in page 1 with multi rows.
- Although there should be plenty of space around some parts for visiblity, it is too narrow in the current manuscript. The guideline says it needs "Double Space" between keywords and sentence (Chapter 1), space around chapter’s title, figure (table) and sentence, and figure (table) and its caption.
- Although Figs. 1, 2, and 4 are placed in the middle of column, the guideline says the position of figures, photographs and tables inserted should be at the tops and bottoms of columns. 
- The balance of the blanks in some itemizations is clearly different from the others. Please unify them. 
- How to write the referenced literatures differs from the guideline. Is "published year" at the end?


# [Minor Comments]
Although the author does not have to revise everything, please refer to the following minor comments for improving the current manuscript:
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
[29]: Babor, M., Paquet-Durand, O., Kohlus, R. et al.: "Modeling and optimization of bakery production scheduling to minimize makespan and oven idle time", Sci Rep Vol. 13, No. 235 (2023). (https://doi.org/10.1038/s41598-022-26866-9)
[30]: Punyakum V et al.: "Hybrid Particle Swarm and Whale Optimization Algorithm for Multi-Visit and Multi-Period Dynamic Workforce Scheduling and Routing Problems", Mathematics, No. 10 (19):3663 (2022) (https://doi.org/10.3390/math10193663)
[31]: F.Zhao et al.: "A cooperative whale optimization algorithm for energy-efficient scheduling of the distributed blocking flow-shop with sequence-dependent setup time", Computers & Industrial Engineering, No. 0360-8352, Vol. 178, page 109082 (2023) (10.1016/j.cie.2023.109082)
[32]: "Author’s Guidelines for the Transactions of the Institute of Electrical Engineers of Japan" (https://www.iee.jp/wp-content/uploads/honbu/32-doc-kenq/guideline.pdf)
[33]: "Appendix 1: Sample of Paper and Technical Note" (https://www.iee.jp/wp-content/uploads/honbu/data-9014/ap01.pdf)
[34]: de Myttenaere et.al.: "Mean absolute percentage error for regression models", Neurocomputing 2016 (2015) (arXiv:1605.02541)
