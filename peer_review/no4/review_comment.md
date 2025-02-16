This paper constructs the comprehensive scheduling problem in a flexible assembly job shop with AGV handling and proposes improved adaptive NSGA-II.
Moreover, it is verified that the optimization performance of this algorithm is superior to the others through numerical simulation. 
It provides an originality and creativity by careful comparison with previous studies, but I think it still needs extensive revisions to be acceptable for publication in terms of usability. 
From this reason, the judgement is "C" (Rereview after major revision). It should be revised according to following major comments and improved as necessary.

# [Major Comments]
## major comment 1 (General)
- Table 1 shows both of the optimization problem and algorithm of this paper differs from the existing papers. While this is recognized as originality, I guess the readers cannot understand the usefulness created by this feature.
解き方も、NSGA-IIの他に、可変近傍探索を導入するなど、違いがある


## major comment 2 (Figure 12)
- Even though Figure 12 shows the results of a search with 100 population size, why are only 7 solutions obtained by IA-NSGA-II (Red Marker) and 6 solutions obtained by INSGA-II (Blue Marker) shown?


# [Minor Comments]
Although the author does not have to revise everything, please refer to the following minor comments for improving the current manuscript:

## minor comment 1 (Section 4.1)
- "the original scheduling method proposed in the literature is referred to as "INSGA-II."", but the reference number of INSGA-II should be clearly written. Is the literature [23]?
- "The scheduling method proposed in the literature is referred to as "IGA."", but the reference number of IGA should be clearly written. Is the literature [27]?

## minor comment 2 (Section 4.1)
- In Section 4.1, the correspondence between the outline of each experiment, the instances, the comparison method, and the parameter settings is a bit vague and misleading. In my opinion, after a brief description of the three experiments in section 4, each information should be listed in correspondence with the experiment number. Or, it would be better to move them to the beginning of each section. For example, please refer to the following my draft: "Through numerical experiments, we verify the usability of the improved adaptive NSGA-II scheduling method (IA-NSGA-II) proposed in this paper. Experiments 1 and 2 deal with static scheduling problem, while Experiment 3 deals with dynamic scheduling problem. In Experiment 1, we select a test benchmark instance from the reference Wu et al. [22] and compare the results of IA-NSGA-II with the original scheduling method “INSGA-II” proposed in the literature [23]. In Experiment 2, we select a test benchmark instance from Wu et al. [27] in the context of FAJSP-AGV and compare the results of IA-NSGA-II with those of the scheduling method “IGA” and NSGA-II proposed in .... In Experiments 1 and 2, the solution was obtained independently for each instance to ensure reliability and consistency; Experiment 1 was run 10 times and Experiment 2 was run 20 times. In Experiment 3, three of the 20 scheduling results from Experiment 2 were randomly selected and the rescheduling method described in Section 3.4 was used. The common parameters for the algorithm in all experiments were set as follows: initial population size 100, number of genetic generations 100. The algorithm is implemented using the programming language MATLAB."
