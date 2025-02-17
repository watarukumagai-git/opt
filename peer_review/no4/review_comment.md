This paper constructs the comprehensive scheduling problem in a flexible assembly job shop with AGV handling and proposes improved adaptive NSGA-II.
Moreover, it is verified that the optimization performance of this algorithm is superior to the others through numerical simulation. 
It provides an originality and creativity by careful comparison with previous studies, but I think it still needs extensive revisions to be acceptable for publication in terms of usability. 
From this reason, the judgement is "C" (Rereview after major revision). It should be revised according to following major comments and improved as necessary.

# [Major Comments]
## major comment 1 (Title)
- Table 1 shows both of the optimization problem and algorithm of this paper differs from the existing papers. Based on Table 1, the originality is in the contribution of this paper is both of the optimization problem and algorithm, but I feel the title is algorithm's proposal. Please correct the title to an appropriate name: for instances, "Multi-objective comprehensive scheduling problem of flexible assembly job shop problem with AGVs and NSGA-II based optimization algorithm".

## major comment 2 (Page3, Equations (1), (2), and (5))
- This paper proposes the three-objective optimization problem as the FAJSP-AGVs but Equations (1), (2), and (5) show minimization problems independent of each other. Please rewrite these as follows: "minimize (Cmax, Et, Tv)...(1)", "a. Makespan: Cmax = max(...)...(2)", "b. Total machine energy consumption: Et = Epro + Est...(3)", and "c. Total AGV working time: Tv= ...(6)".

## major comment 3 (Table 2)
- Table 2 shows the symbolic description of model parameters and the FAJSP-AGVs should be formulated to the mixed-integer linear programming problem (MILP). But I guess the reader cannot distinguish between the decision variables and fixed parameters in the FAJSP-AGVs. Therefore, please add a description of decision variables under Eqution (12) as follows: "The FAJSP-AGVs is formulated to the mixed-integer linear programming problem (MILP). The integer variables $X_{i,j,k}, Y^k_{i,j,p,q}, V_{i,j,v}, and Z_{i,j,p,q,v} \in {0, 1}$; and the continuous variables $S_{i,j}, S_{p,q,k}, S_{i,j,k} \in \mathbb{R}$ are mixed. Number of the integer variables is ~ and number of the continuous variables is ~."

## major comment 4 (Chapter 3)
- One of the contributions of this paper is the proposal of an algorithm. While the ideas are described from Subsections 3.1 to 3.3, the reader cannot understand an overall proposed NSGA-II. Please show flowchart or steps of the proposed NSGA-II in Chapter 3. 

## major comment 5 (Chapter 4)
- Chapter 4 shows the usability of the proposed NSGA-II (IA-NSGA-II) by comparing it with the results of INSGA-II and IGA, but I guess the reader cannot understand the usability created by this feature. While this paper says "In this paper, the genetic operator is improved with the same purpose and further improved for the problem of local optimum.", it does not prove the effect of avoid the population falling into local optimum by comparing with/without elements. Without this, it is difficult to understand how it is a meaningful idea. Therefore, please add additional comparison results shown below:
  - Crossover and mutation probability are fixed to a certain value in the proposed NSGA-II to verify the effect of adaptive crossover and mutation probability in 3.2.3.
  - The Variable neighborhood search (VNS) is excluded from the proposed NSGA-II to verify the effect of VNS in 3.3.


# [Minor Comments]
Although the author does not have to revise everything, please refer to the following minor comments for improving the current manuscript:

## minor comment 1 (Section 4.1)
- "the original scheduling method proposed in the literature is referred to as "INSGA-II."", but the reference number of INSGA-II should be clearly written. Is it the literature [23]?
- "The scheduling method proposed in the literature is referred to as "IGA."", but the reference number of IGA should be clearly written. Is it the literature [27]?

## minor comment 2 (Section 4.1)
- In Section 4.1, the correspondence between the outline of each experiment, the instances, the comparison method, and the parameter settings is a bit vague and misleading. In my opinion, after a brief description of the three experiments in section 4, each information should be listed in correspondence with the experiment number. Or, it would be better to move them to the beginning of each section. For example, please refer to the following my draft: "Through numerical experiments, we verify the usability of the improved adaptive NSGA-II scheduling method (IA-NSGA-II) proposed in this paper. Experiments 1 and 2 deal with static scheduling problem, while Experiment 3 deals with dynamic scheduling problem. In Experiment 1, we select a test benchmark instance from the reference Wu et al. [22] and compare the results of IA-NSGA-II with the original scheduling method “INSGA-II” proposed in the literature [23]. In Experiment 2, we select a test benchmark instance from Wu et al. [27] in the context of FAJSP-AGV and compare the results of IA-NSGA-II with those of the scheduling method “IGA” and NSGA-II proposed in .... In Experiments 1 and 2, the solution was obtained independently for each instance to ensure reliability and consistency; Experiment 1 was run 10 times and Experiment 2 was run 20 times. In Experiment 3, three of the 20 scheduling results from Experiment 2 were randomly selected and the rescheduling method described in Section 3.4 was used. The common parameters for the algorithm in all experiments were set as follows: initial population size 100, number of genetic generations 100. The algorithm is implemented using the programming language MATLAB."

## minor comment 3 (Figure 12)
- Even though Figure 12 shows the results of a search with 100 population size, why are only 7 solutions obtained by IA-NSGA-II (Red Marker) and 6 solutions obtained by INSGA-II (Blue Marker) shown? Please add a description of Figure 12.

## minor comment 4 (Chapter 4)
- This paper improves some genetic operations in NSGA-II, but I guess the reason for the room for improvement in results may lie in GA or non-dominated sorting. There are multi-objective optimization methods: for instances, decomposition-based method (MOEA/D) or differential evolution (DE). Especially, MOEA/D-DE[28] combining MOEA/D and DE is known as the best multi-objective optimization method. In the future, the authors should compare a wide range of methods, including such state-of-the-art methods, to find an efficient way to solve the FAJSP-AGVs.


# [Additional Literature]
[28] H.Li and Q. Zhang: "Multiobjective optimization problems with complicated Pareto sets, MOEA/D and NSGA-II", IEEE Transactions on Evolutionary Computation, Vol.13, No.2, pp.284-302 (2008)
