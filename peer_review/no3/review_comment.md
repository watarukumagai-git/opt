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

## major comment4 (Fig.7)
Fig.7 shows both of departure time and transportation time in the results of each methods using 3D graph. However, the most of HPWL-IME’s bar is hidden by the others. The results should be shown as normal 2D-line plot which has the horizontal axis "departure time" and the vertical axis is "transportation time " (or velocity?) with different color’s line and marker corresponding methods. 


## major comment5 (General)
いくつかフォーマットに従っていない。
- p1のkeywordsとSection1の文章の空白が狭すぎる。
- p2右段の箇条書き内部の空白のバランスが、それ以外と明らかに違う。他の部分と揃えよ。
- 所属をtwo-columnで書くのは変。左段に寄せてtwo-rowsで書くべき。
- 3.1以降のタイトルの上下のスペースのバランスがおかしい。タイトルの上部は適切なスペースをとり、タイトルの下部は広げ過ぎないべきだ。
- Figure 3の周囲のスペースをとるべきだ。
- Section3.4で、Step7, 8が突然出てきた。本来、Section3.3 Step6の下に移動するのが正しいのでは？
- 文献の書き方がおかしい、年号は最後では？
- Eq.(6) has ",,," after where a, b=1, but "..." is correct.
- 図表はページの上下に寄せるべきだ。Fig.1, 2 and 4は守れていない。




# [Minor Comments]
## minor comment1 (Subsection 3.3.3)
The sentence "The goal is…" is twice in one paragraph and is difficult to read. For example, it should be "the goal is probably to reduce the overall makespan time considering both the process of production and transportation periods. Specifically, this is to identify T … ."

## minor comment2 (Section 3.4)
There are detailed miss. Please modify the following items so as for readers to understand:
- Is ":" needed behind Subsection 3.3.1, 3.3.2, and Section 3.4, 4.4, and 4.5’s title?
- "using an Enhanced Large Neighbourhood Search (ELNSs) approach is suggested with savings(s) technique." should be "using an Enhanced Large Neighbourhood Search with savings technique (ELNSs) approach is suggested." (p3, left column)
- "Lu et al. [23] Created a Hybridized Multi-verse Optimizer-Variable NS (HMOVNS)" should be "Lu et al. [23] created a Hybridized Multi-verse Optimizer-Variable NS (HMOVNS)." (p3, left column)
- There is no verb in the sentence "The lack of study…", so please add it appropriately. (p3, right column) 


## minor comment3 (Section 5)
Some terms of the current manuscript are not common in the optimization field.
Please modify them according to the following items: 
- In optimization field, the solution satisfying all constraint conditions should be called "infeasible" generally, not "viable". Please replace "viable" with "infeasible".
- In optimization field, the optimization  problem consists of "objective function" and "constraint conditions" (simply called constraints), not "restrictions". Please replace "restriction" with "constraint".
- What is "ObjFn" in Fig. 4's title? 
