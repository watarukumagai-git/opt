TEEE No.3 Reviewer A

This paper constructs the optimization algorithm by combining with the PSO and Whale Optimization algorithm for production and transportation collaborative scheduling task in Intelligent Manufacturing Environment. Moreover, the optimization performance of this algorithm is verified by comparing to the others through numerical simulation. 

It provides an interesting data, but I think this paper has very difficult problem to be acceptable for publication in terms of originality, creativity, and readability. 

From this reason, the final judgement is "D" (reject). I think this paper needs to be radically rewritten after reconsidered deeply in terms of originality and usability. Detailed reasons and comments are as follows:

# [Major Reasons]
## major reason1 (General)
The readers cannot understand the creativity and originality although Chapter 1 describes the main innovations of this research work. Simply laying out previous relevant studies cannot explain the difference between them and this paper; especially, all sentences from "Then [5] explored..." in Chapter 1 to the end of Chapter 2. I believe there may be the following contributions: i) how to formulate the collaborative scheduling problem between production and transportation; ii) how to solve the problem using algorithm; and iii) how good the solution is, but cannot find the originality and creativity in anywhere. This is serious and fatal problem for pubilication. Examples are listed below:
- Most of the previous studies [17]-[26] and additional studies [29] proposes the collaborative scheduling problem between production and transportation. Therefore, I judge the problem formulation has no new idea.
- In general, the scheduling problem is formulated to a mixed-integer and continuous variable's linear programming problem (MILP). For example, the additional previous study [29] applies a MILP solver to it. But there is no discussion and difference between MILP solver and metaheuristic algorithm in the manuscript.
- The previous studies [20],[22,23] and additional studies [30]-[32] propose metaheuristic algorithm for scheduling problem. Especially, [30] costructs a hybrid of PSO and Whale Optimization and applies it. Moreover, the proposed algorithm has PSO, Whale Optimization, and Local Neighborhood Search steps, but is hybridized simply. Therefore, I judge the scheduling algorithm has also no new idea.

## major reason2 (General)
This paper cannot clarify and find the issues about collaborative scheduling manufacturing and transportation by citing literatures which are particularly relevant. Simply laying out previous studies is redundant and cannot explain the issue. Some referenced literatures in the current manuscript are not directly related to this paper's contribution. For example, I guess most of the literatures for Intelligent Manufacturing [3]-[8] are redundant and unnecessary. Moreover, there is no particularly related studies in the manuscript as major reason1 pointed out. Considering the publication level, it is diffucult to find the issues and their difference by organizing the previous studies in short.

## major reason3 (Chapter 2)
Some sentences has no evidence or fact. Examples is listed below:
- The end of Chapter 2 says "Furthermore, HPWL-IME has outperformed other techniques like SA, GA, CWOT, ACO, etc…," but there is no reference to this fact. If there is this paper’s originality in the proposed algorithm, the difference from conventional algorithms is important. 
- The end of Chapter 2 says "Furthermore, HPWL-IME … when used with other heuristics taken for comparison like DTCST, ELNSs, and HMOVNS with various performance metrics.", but the performance of HPWL-IME (the proposed algorithm) should be written in Chapter 5 because it is shown in numerical experiments of this paper for the first time.

## major reason4 (Chapter 3)
 I think the readers cannot understand the optimization problem which optimization variable, parameters, and objective and constraint functions because they are not written in an organized and current manner. This is serious and fatal for publication. The optimization problem and algorithm’s part of the current manuscript should be rewritten radically with learning the previous studies[22, 33], which are nicely written.
Moreover, the points raised are presented for future reference below:
- Chapter 3 can be separated into optimization problem’s formulation and optimization algorithm. So, the former is "Chapter 3: Collaborative Scheduling Problem" and the latter is "Chapter 4: Scheduling Algorithm".
- New Section 3.1 shows the whole of collaborative scheduling optimization problem.
- New Section 3.2 shows objective and constraint functions about the production.
- New Section 3.3 shows objective and constraint functions about the transportation.
- As problem representation, after the whole of mathematical formulas firstly is written with equation’s number, the explanation sentence about each formula should be done.
- Add the table defining the notations of that are used to describe the optimization problem.
- "minimize_[x] f_1(x) + f_2(x)" shows the objective function, f_1 shows the make-span time about production, f_2 shows the delivery time about transportation, "g(x)<=0" shows the constraints, x shows the optimization variables. More details about f_1, f_2, g, and x are given in later sections.
- Add more illustlations or figures for explanation about the variables to the manuscript.
- I think "t_{\mu,T}", "t_p", "t", and "t_ab" should be represented as different character because it avoids confusing the readers.
- The constraints meaning machine’s total capacity is "t_p \in \mu <= \alpha" but "\sum_{x=1}^{\mu} t_{p, x} <= \alpha" is correct. (page 4, right column)
- The constraints meaning transportation route’s total capacity is "\gamma \in T <= \beta" but "\sum_{q=1}^{d} \gamma_q <= \beta" is correct. (page 4, right column)
- Eq.(2) represents the both of objective function "minimize alpha" and constraints "such that \sum~". They should be separated to different equations.
- Eq.(2) represents "\sum..., y \in T and x \in \mu" but this is not written currently as Equality or Inequality constraints. Please revise it. I guess the authors want to write "minimize \sum ms...".
- I think "O_ab", "O_r", and "O_tp" should be represented as different character because there it avoids to confuse the readers.
- There is no explanation of Z_r,v in Eq.(4) and \phi in Eq.(5) of the manuscript.

## major reason5 (Section 3.4)
 It is important to describe and write the procedures or steps of the proposed algorithm because there is this paper’s originality in the proposed algorithm. There is suddenly Step7 and 8 in Section3.4. I guess they should be moved to below Step6 in Section 3.3, but cannot understand it correctly.

## major reason6 (Chapter 4)
 I guess the readers cannot understand the usability of this paper because the evaluation index’s definition is not written correctly. Please add exact definition and description about the evaluation index according to the following items: 
- What is ObjFn in Fig.4? I cannot understand "Figure4 diagram shows the number of objective functions…" as description for ObjFn. In general, the number of objective and constraint functions in the optimization problem are determined before solve it. I guess the objective functions are Eqs.(2) and (5) but ObjFn is the range of 100 – 400 in Fig.4. (Fig.4)
- I guess ARDI means the average of relative error about between observed (actual) and estimated make-span time, and "ARDI_S = 100*(1/N) \sum_[i=1]^N |(Est_i – Obj_i)/(Est_i)|, where N is the number of data, Est_i and Obj_i is the i-th estimated and observed make-span time (i=1,…,N)" may be correct. Moreover, it is more general called "mean absolute percentage error (MAPE) " or "mean absolute percentage deviation (MAPD)"[34] (Eq.7 and Fig.5).
- I guess the parameters is determined by [27], but I cannot understand which symbols are; e.g., actual and observed make-span are written in Eq.7.

## major reason7 (Chapter 4) 
Another reason I do not think the reader cannot understand the usability is the comparison in Chapter 4.
- As major reason 1 pointed out, the proposed algorithm should be compared to a MILP solver[29].
- There are many meta-heuristic algorithms including the hybridized algorithm of PSO and Whale Optimization[30]. The proposed algorithm should be also compared to simple PSO and Whale Optimization because it consists of them.
- Moreover, metaheuristic algorithm has adjustable hyperparameters but they must be determined by user. CMA-ES[35,36] and SHADE[37,38] have the function of adaptive and automatic adjusting its own hyperparameters. They known as novel algorithm and far superior to many algorithms in many benchmark problems or black-box functions. The fact is shown as several papers or the competition Black-Box Optimization Benchmarking held at top international conferences IEEE CEC and ACM GECCO[39]. If the authors think a difficulty to solve the scheduling problem, CMA-ES / SHADE based algorithms are also expected to show higher performance than the proposed algorithm in this case.

CMA-ESなどの有名なアルゴリズムと比較していない。協調スケジューリング問題は汎用ソルバで解ける。そのため協調スケジューリングの先行研究だけでなく、一般のメタヒューリスティクスと比較すべきだが、全くされておらず、その有用性が判断できない。


## major reason8 (Fig.7)
Fig.7 shows both of departure and transportation time in the results of each methods using 3D graph. However, the most of HPWL-IME’s bar is hidden by the others. The results should be shown as normal 2D-line plot which has the horizontal axis "departure time" and the vertical axis is "transportation time " (or velocity?) with different color’s line and marker corresponding methods. 

## major reason9 (Format)
The format of manuscript does not follow the author’s guidelines[40, 41]. Moreover, the authors do not review and consider them and the already published papers in this journal. Examples are listed below: 
- The author’s affiliation and correspondence should be written on the left column in page 1 with multi rows.
- Although there should be plenty of space around some parts for visiblity, it is too narrow in the current manuscript. The guideline says it needs "Double Space" between keywords and sentence (Chapter 1), space around chapter’s title, figure (table) and sentence, and figure (table) and its caption.
- Although Figs. 1, 2, and 4 are placed in the middle of column, the guideline says the position of figures, photographs and tables inserted should be at the tops and bottoms of columns. 
- The balance of the blanks in some itemizations is clearly different from the others. Unify them. 
- How to write the referenced literatures differs from the guideline. Is "published year" at the end?


# [Minor Comments]
Although the author does not have to revise everything, please refer to the following minor comments for improving the manuscript:
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
[29]: C. Celikbilek et al.: "Simulation and Mixed Integer Programming Optimization for Manufacturing and Transportation Scheduling", Proceedings of 25th Production and Operations Management Conference (2014)
[30]: V. Punyakum et al.: "Hybrid Particle Swarm and Whale Optimization Algorithm for Multi-Visit and Multi-Period Dynamic Workforce Scheduling and Routing Problems", Mathematics, No. 10 (19):3663 (2022) (https://doi.org/10.3390/math10193663)
[31]: F.Zhao et al.: "A cooperative whale optimization algorithm for energy-efficient scheduling of the distributed blocking flow-shop with sequence-dependent setup time", Computers & Industrial Engineering, No. 0360-8352, Vol. 178, page 109082 (2023) (10.1016/j.cie.2023.109082)
[32]∶ S. Aminzadegan et al.: "An integrated production and transportation scheduling problem with order acceptance and resource allocation decisions", Applied Soft Computing, Vol.112, No.107770, Elsevier (2021)
[33]: M. Babor et al.: "Modeling and optimization of bakery production scheduling to minimize makespan and oven idle time", Sci Rep Vol.13, No.235 (2023)(https://doi.org/10.1038/s41598-022-26866-9)
[34]: D. Myttenaere et.al.: "Mean absolute percentage error for regression models", Neurocomputing 2016 (2015) (arXiv:1605.02541)
[35]: 
[40]: "Author’s Guidelines for the Transactions of the Institute of Electrical Engineers of Japan" (https://www.iee.jp/wp-content/uploads/honbu/32-doc-kenq/guideline.pdf)
[41]: "Appendix 1: Sample of Paper and Technical Note" (https://www.iee.jp/wp-content/uploads/honbu/data-9014/ap01.pdf)
