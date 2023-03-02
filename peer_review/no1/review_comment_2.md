# 再査読コメント
I checked the revised manuscript and author's response to reviewer's comments.
Although some points have improved, this paper has still very difficult problem to be acceptable for publication and is not revised enough based on the comments.
From this reason, the final judgement is "D" (reject).
I think this paper needs to be radically rewritten after reconsidered deeply in terms of originality and usability.
Detailed reasons and comments are as follows: 


# [major reasons]
## major reason1 (General)
The creativity is slightly improved according to reviewer's comment. 
Especially, the proposed PSO is changed to be added some SHADE's operators according to Reviewer A's comment and Reviewer B's major comment7.
And, the sentence about the originality of this paper is added to Section1 according to Reviewer B's major comment2.
However, I think the originality and creativity of this paper are still low according to the following points.
- Point1: Even if the above change, the proposed PSO is just a hybrid algorithm of the conventional PSO and many conventional operators as pointed out by Reviewer A. The creativity is not acceptable for publication of this journal.
- Point2: To my understanding, the objective of this paper may be not an new algorithm assuming versatile application environments but an effective algorithm to the path planning problem. In spite of Reviewer B's major comment2, there are no the essential difference between the proposed PSO and other algorithms.


## major reason2 (Section4)
Subsection 4.1 of the revised paper in page4 says the follwing two points as the effectiveness in the proposed PSO.
- Point1: "the CPSO algorithm adds dynamic inertia weights..."
- Point2: "The selection operation in genetic algorithm and the crossover and variation operation of SHADE are introduced..." 
However, it is still unclear whether their operators or ideas have the effectiveness for the path planning problem through numerical experiments.
While Reviewer B's major comment5 points out a necessary to combination of some ideas including the SHADE's operator, the experimental results in Section4 of the revised manuscript cannot show the necessary without comparing the LDIWM PSO in Subsection 3.2 and the original SHADE in Subsection 3.3.
So, the results should show the LDIWM PSO has superior to the original PSO if Point1 is correct, and the proposed PSO has superior to the original SHADE if Point2 is correct.
To supply no evidence supporting the usability of this paper is the mainly reason to be not acceptable for publication of this journal.


## major reason3 (General)
There are many insufficient explanations for the readers and this may cause them confused or misleading. I think there are too many points to be needed to rewrite or revise according to the following points.
- Point1: There is no explanation of the design variables in this revised paper while Reviewer B's major comment2 pointed out "Please clarify the optimization problem consisted of the objective function, the constraint condition, and the design variables". 
- Point2: There is no explanation of the important variables "pbest_i, gbest" of the PSO update rule in this revised paper while Reviewer A pointed out "Several important variables (pbest_i, gbest_i, x_i, y_i) are not mentioned. Explain them".
- Point3: There is no explanation of comparing algorithms in Section4, e.g., the CPSO (inferred from the context to be the proposed PSO) and FPSO in the revised paper. So, the readers cannot understand the significance or meaning of the experiment results.



# [minor comments]
## minor comment1
The author cannot reply enough to all major comments because the answer or response letter is too simple. The author should refer all sentence from the reviewer and reply to them point by point. 

## minor comment2
The author should use the appropriate symbols, e.g., "Iter" (iteration) in equation (8) and "g" (generation) in equation (9) are same meaning but not unified while Reviewer B's minor comment 1 pointed out "The symbols are different in each equation or section, but only meaning should be assinged to each symbol. Please unify them". 
