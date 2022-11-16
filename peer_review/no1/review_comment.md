# レビューコメント
## 総括コメント
- 本論文は、改良したPSOを提案し、UAVの3次元経路計画問題に適用している。
提案手法は、GAの操作や慣性パラメータの調整など、様々なアイディアを組み込んだPSOである。
そして、3次元環境モデルを構築し、障害物や経路長に基づく適合度関数を設計している。
数値実験を通じて、提案手法で経路計画問題を解き、他の手法と比較して、計算効率や得た経路の質が優れていることを確認している。
- 一方、現原稿は、本論文の動機・目的、新規性・有用性の論述などにおいて、大幅な修正と追記が必要だと感じた。
この理由から、本論文は、独創性・新規性・有用性のそれぞれで不足していると判断し、照会後判定とした。
下記の照会事項およびコメントへの回答と、必要に応じた原稿修正を要求する。
  - C判定：照会後判定？

## 照会事項1 (p1, Chapter1)
- 現原稿は、本論文の動機・目的が不明瞭である。
先行研究[2]-[13]は、改良したアルゴリズムをUAVの3次元経路問題に適用しているのみに留まっていると推測される。
また、本論文はこれらの先行研究と同じカテゴリに属していると推測する。
それにも関わらず、先行研究における研究課題や、それを踏まえた研究動機が現原稿には明記されていない。
以上を踏まえ、先行研究と比較しながら、本論文が着目しているUAVの3次元経路問題における研究課題や動機を明記すべきである。

## 照会事項2 (General)
- 現原稿は、本論文の独創性・新規性の主張が不明瞭である。
先行研究と比べて本論文の新しい点として、問題の定式化、適用したアルゴリズム、得た経路のどこにあるのかが明記されていない。
しかしながら、私が見る限り、独創性・新規性は、UAVの3次元経路問題における多峰性を克服するために提案したアルゴリズムに存在すると推測される。
もしこの推測が正しいなら、この問題を解くために本論文が提案したアルゴリズムが、先行研究のアルゴリズムと本質的に異なる点を提示することが必要である。
以上を踏まえ、先行研究と比較しながら、本論文の独創性・新規性を明記すべきである。


## 照会事項3 (p3, Chapter3)
- 提案手法は、様々なアイディアから構成されているが、現原稿では、本論文の提案手法における各アイディアに関する有用性の論述が不明瞭である。
もし著者らがUAVの3次元経路問題を解く難しさが多峰性にあると問題視するならば、提案手法の各アイディアの有効性を示す必要がある。
しかしながら、現原稿では、数値実験を通じて各アイディアの有効性について示されていない。
例えば、各アイディア単体を付加したアルゴリズム（dynamic weightだけを加えたPSO, 交叉・突然変異のみを工夫したGAなど）の探索性能との比較を通じて、この問題においてこれらのアイディアを組み合わせる必要性を示すべきである。


## 照会事項4 (p4, Chapter4)
- 現原稿では、提案手法の探索性能が古いGAやPSOよりも優れていることを示しているが、本論文の提案手法の比較手法が適切であることは非常に疑問である。
- メタヒューリスティクスの分野では、多峰性関数を含めた多くのベンチマーク問題において、CMA-ES[1,2]やSHADE[3,4]、あるいはその改良手法の探索性能は、PSOやGAよりもはるかに優れていることが一般的に知られている。
- この事実は、CECやGECCOなどのトップカンファレンスで開催されるコンペティション[5]など、様々な文献を通じて示されている。
もし著者らがUAVの3次元経路問題を解く難しさが多峰性にあると問題視するならば、CMA-ESやSHADEベースのアルゴリズムはこの問題においても高速かつ良好な探索性能を示すことが十分期待されるだろう。
- これらの事実を踏まえると、本論文は、提案手法の比較手法が、CMA-ESやSHADEベースのアルゴリズムではなく、古いGAやPSOのみで十分である理由、あるいは、CMA-ESやSHADEベースのアルゴリズムのいずれかの探索性能と、この問題において直接比較する必要がある。以上を踏まえ、適切な文献を追加で引用すると共に、適切な比較手法を選定すべきである。

- [1]: CMAES、[2]: multistart CMAES、[3]: SHADE、[4]: LSHADE、[5]: BBOB


## 照会事項5 (p2, Chapter2)
- equations(1)-(4)は、3次元環境モデルとスプライン曲線による経路生成を表す。
- しかしながら、現原稿では、上記のモデルに基づく経路計画のための最適化問題に関わる数式が式(7),(9)など定義が散らばっており、最終的な最適化問題が不明である。
- 査読者は、基本的に目的関数$f: \mathbb{R}^N \rightarrow \mathbb{R}$はUAVの経路長、最適化変数$q \in \mathbb{R}^N$は、3次元空間内経路のスプライン曲線中の各セグメント座標だと推測している。
- よって、査読者が推測した下記例のように、目的関数、制約条件、最適化変数を数式で明示的せよ。
~~~~~~~~~~~~
minimize 
f(q) = ρ√(Σ_[i=1,n-1] (x_{i+1}-x_i)^2+(y_{i+1}-y_i)^2+(z_{i+1}-z_i)^2)
subj.to 
zmin<z_i<zmax; i=1,…,n
ρ = k, Lmin(q)<Ld; 1, otherwise
q = [x_1, x_2, … , x_n, y_1, y_2, … , y_n, z_1, z_2, … , z_n]
ただし、nはセグメント数、Nはthe dimension of search spaceでN = 3nで与えられる。
~~~~~~~~~~~~
- また、もし経路の始点(x_1,y_1,z_1)と終点(x_n,y_n,z_n)が計算前に与えられるなら、(x_1,y_1,z_1,x_n,y_n,z_n)がパラメータに固定されるという制約条件を最適化問題に追加すべきだ。



## 照会事項6 (p3, Chapter3)
- 最適化問題の制約条件は、高さの上下限制約（式(13)）だけ記載されている。
- しかし、査読者は、x方向y方向の上下限制約も必要なように思うが、実際はどうなのか？もし他にも制約条件があるなら、全ての条件を示せ。
- さらに、制約対処法が記載されていないため、それを示せ。
- 例えば、探索過程で解を更新したとき、上下限制約を逸脱するときに、上下限制約内に収めるなど。


## 照会事項7 (General)
- 現原稿は、静的かつ非常に簡易的な3D環境下における経路計画問題に対して、本論文の提案手法の計算効率・探索性能が古いGAやPSOよりも優れていることを主張しているが、応用問題での状況や適用可能性が明記されていない。
- 例えば、文献[6]には、「UAVのガイダンスシステム開発においては、オペレータの介入無しで操作イベントを解決することが注目されている。例えば、脅威の検出、ミッションや環境設定の変更に伴う軌道の再計画などが挙げられる。」という記述がある。
- 文献[7]、[8]のレビューでも、動的かつ複雑な環境を想定したUAVの研究も見られる。
- このように、最新かつ網羅的なレビュー論文などを引用して、UAV経路計画に関する研究課題を取り上げると同時に、それに合致した数値実験を実施したり、その状況における適用可能性について言及することは、読者にとって非常に有益である。 
- したがって、本論文の提案手法は、動的かつ複雑な環境にも適用可能でかつ高い効果が期待されるのか、あるいは、今後の課題としてそのような問題への拡張を考えているなど、より応用に近い問題に対する著者らの考えを新原稿に示しなさい。

- [6]: Present state and future prospect of autonomous control technology for industrial drones
- [7]: A literature review of UAV 3D path planning
- [8]: A Review on Viewpoints and Path-planning for UAV-based 3D Reconstruction



## コメント1 (General)
- 現原稿の数式における文字が統一されておらず、読者を混乱させる恐れがある。
- 査読者が読んだ範囲でも、下記の多くの点が統一されていない。
- 読者が本論文を読んで再現できるように、これらの表現を修正・工夫してください。

- アルゴリズム中のイテレーションカウンター：Iter（式(10)） , t（式(5),(6)）, or i-th generation（式(11),(12)）
- 3D環境モデル内のUAVの座標と最適化変数：式(1),(2),(5),(6),(7)
- 確率P：式(3),(11),(12), or 表1（including p and P）
- x_i：ランドスケープ内のピーク番号i(式(2)) or 個体位置（式(5),(6)）
- x_ij, z_j：最適化変数
- f：3D環境モデルの係数（式(1)）、障害物のバリア係数（式(8)）、適合度（式(11),(12)）
- k：拡大係数（式(9)）、GAの染色体数（表1）


## コメント2 (p4, Chapter4)
- 現原稿の数値実験における一部の条件が不明である。
- ピーク数(4.1は7個、4.2は10個)
- 紹介事項5と関連するが、現原稿の数値実験では、経路を構成する最適化変数の数が明記されていない。
- メタヒューリスティクスのアルゴリズムの探索ダイナミクスは、最適化変数の個数との関連性が強いため、原稿に明記すべきである。


## コメント3 (p5, Figure6)
- Figure6は、障害物のランドスケープがランダムに変更するにも関わらず、提案手法がPSOとGAよりも安定して良い性能を示すと解釈できる。
これは、一般的なメタヒューリスティクスの探索性能とランダム性の関係を言及している。
このとき、各試行の性能をそのまま記載するよりも、性能の統計分布(平均値/標準偏差/最大値/最小値)を比較可能なbox-and-whisker plotとエラーバー(横軸が手法、縦軸が性能の各統計量)で表現するほうが良い。


## コメント4 (p2, 式(8))
査読者は、式(8)を、UAVと障害物が近過ぎるのを避けるためのペナルティ関数だと解釈している。
LminはUAVの座標位置とピーク位置の最短距離だが、具体的な計算は何か？
査読者は、全セグメント上におけるUAVの位置と全ピーク位置を毎回計算した後、その最短距離をLminとしていると判断した。
このとき、Lminの計算量はセグメント数やピーク数と関連が強いと推測する。
さらに、机上シミュレーションでは、開始地点、終着地点、各物体位置を静的な状態で正確に把握していることが前提だが、実応用では、Lminを含めてこれらの計算はどうするのか？(リアルタイムで物体位置を認識するのか、机上シミュレーションと同様に、事前に全ての物体位置を把握しておくのか)
本論文におけるLminの具体的な計算方法、あるいは、実応用でのLminの考え方について述べよ。

## コメント5 (p2, chapter3)
3章は提案PSOのアルゴリズムを記述する章だが、3.3節、3.6節は最適化問題と制約条件の内容である。
これらは、PSOアルゴリズムの工夫ではなく、最適化問題の記述であるため、「2.3 optimization problem for path planning」などのように節を追加するのが良いと思った。


# English
------------------------------------------
Reviewer A

- This paper proposed an improved particle swarm optimization (PSO) and applied in three-dimensional path planning of UAV. 
- The proposed method is the PSO algorithm introduced to the following several ideas: improved operations (crossover/mutation/selection) in real-coded genetic algorithm (GA) and inertia weight parameter tuning. 
- Moreover, the paper built a three-dimensional environment model for the problem and constructed a fitness function based on obstacles and path lengths.
- Finally, it is verified that the obtained path of the proposed method is superior to that of conventional PSO and GA by solving the problem through numerical simulations.
- It provides an interesting observation and data, but I think it still needs a considerable and major revision to be acceptable for publication in terms of originality or usability.
- From this reason, the judgement is "C" (major revision).
- It should be revised according to following major comments and improved as necessary.


# [major comments]
## major comment1 (General)
- What is the main purpose or motivation of this paper?
- I guess the existing studies [2]-[13] or this paper only apply an improved algorithm in 3D path planning of UAV and belong to the same category. 
- Nevertheless, there are no research subject and motivation of this category in the current manuscript.
- If the authors think the subject is for PSO to be trapped into a local minima in the path planning, the existing studies [2]-[13] may have solved it to some extent.
- Overall, please describe and clarify the research subject for 3D path planning of UAV or motivation of this paper comparing to the existing studies.


## major comment2 (General)
- What is the originality of this paper?
- There is no contention about the originality in the current manuscript; for example, problem formulation, applied algorithm, or gained path. 
- To my understanding, the main originality may be the proposed PSO to overcome a multimodality of the objective function in the path planning.
- If the above understanding is correct, this paper should point out the essential difference between the proposed PSO and other algorithms in existing studies.
- Overall, please describe and clarify the originality of this paper comparing to existing studies.


## major comment3 (General)
- The references are very selective from the viewpoint of algorithm for path planning and not enough assuming situation/applicability to real case.
- To show the research widely subjects about UAV path planning citing some exhaustive review papers, experiment suitable numerical simulation, and explain applicability for them is beneficial for the readers.
- For example, the review paper [21] says "Currently, there is growing interest in increasing vehicle autonomy by developing guidance systems that are able to tackle several operational events without operator intervention."
- Increasing researches for assuming dynamic and more complicated environment are written in the review papers [22,23].
- Overall, describe and clarify the author's opinion for real case; for example, whether or not the proposed PSO is applicable and effective to dynamic and complicated environment, or the future work is extension to such problems.

- [21]: K Nonami: "Present state and future prospect of autonomous control technology for industrial drones", IEEJ Transactions on Electrical and Electronic Engineering, Vol. 15, No. 1, pp. 6-11 (2020)
- [22]: L. Yang et al. : "A literature review of UAV 3D path planning", Proceeding of the 11th World Congress on Intelligent Control and Automation, pp. 2376-2381 (2014)
- [23]: M. Maboudi et al. : "A Review on Viewpoints and Path-planning for UAV-based 3D Reconstruction", https://doi.org/10.48550/arXiv.2205.03716, (2022)



## major comment4 (p2, Chapter2)
- The formulas constituting the optimization problem for path planning are written in disparate parts of the current manuscript such as equations (7) and (9), and the problem to be dealt with finally is unclear.
- To my understanding, the objective function $f: \mathbb{R}^N \rightarrow \mathbb{R}$ is the path length of UAV, the constraint condition is the lower/upper limit of path's height, and the design variable $q \in \mathbb{R}^N$ is the each segment position at the spline curve, basically.
- Moreover, if the start position (x_1, y_1, z_1) and goal position (x_n, y_n, z_n) are given before calculation, constraint conditions that variables (x_1, y_1, z_1, x_n, y_n, z_n) are fixed to the start or goal position should be added to the problem. 
- Please clarify the optimization problem consisted of the objective function, the constraint condition, and the design variables such as the following example:
[the following formulations written by LaTeX style]
~~~~~~~~~~~~
minimize_{q\in \mathbb{R}^N} 
f(q) = \rho \sqrt{\sum_[i=1,n-1] (x_{i+1}-x_i)^2+(y_{i+1}-y_i)^2+(z_{i+1}-z_i)^2}
subj.to z_{min} \le z_i \le z_{max}; i=1,…,n
q = [x_1, x_2,... , x_n, y_1, y_2,... , y_n, z_1, z_2,... , z_n]
, where $n$ is a number of segments, $N$ is the dimension of the search space and determined by $N=3n$, 
and $\rho$ is the barrier coefficient. If $L_{min}<L_d$, $\rho=k$; otherwise, $\rho=1$. 
~~~~~~~~~~~~


## major comment5 (p3, Chapter3)
- The proposed PSO consists on the several ideas.
- If the authors think a difficulty to solve the path planning is the multimodality, an effectiveness of each idea should be shown.
- However, there is no numerical simulation's result to support usability of their ideas in the manuscript.
- Please show a necessary to combination of their ideas for the path planning comparing to algorithms with only each idea; for example, PSO with inertia weight parameter tuning and GA with improved operations (crossover/mutation/selection).


## major comment6 (p3, Chapter3)
- The upper/lower limit of height is formulated by equation (13) as the constraint condition.
- However, there is no an explanation of constraint handling technique; for example, search points outside the limit are projected to the nearest neighbor limit at each solution update.
- Please write the constraint handling technique used in algorithm section.
- And, is there no an upper / lower limit of the x and y-axes?
- If there are other constraints, show all of them.


## major comment7 (p4, Chapter4)
- The current manuscript shows the performance of the proposed PSO is superior to the classic GA and PSO in the path planning, but comparing them is questionable.
- In metaheuristic algorithm's field, CMA-ES[24,25] / SHADE[26,27] are known as novel algorithm and far superior to the classic GA and PSO in many benchmark problems including multimodality function.
- The fact is shown as several papers or the competition Black-Box Optimization Benchmarking held at top international conferences IEEE CEC and ACM GECCO[28].
- If the authors think a difficulty to solve the path planning is the multimodality, CMA-ES / SHADE based algorithms are also expected to show high performance in the path planning.
- Based on the fact, this paper should provide a reason why just comparing to the classic GA and PSO is enough, or compare the performance / feature of the proposed PSO and either CMA-ES / SHADE based algorithms.
- Overall, please check whether compared methods are appropriate to support usability of the proposed PSO, and provide an additional simulation results / the above references as needed.

- [24]: N. Hansen et. al: "Impacts of Invariance in Search: When CMA-ES and PSO Face Ill-Conditioned and Non-Separable Problems", Journal of Applied Soft Computing, pp. 5755-5769 (2011)
- [25]: N. Hansen: "Benchmarking a BI-population CMA-ES on the BBOB-2009 function testbed", Workshop Proceedings of the GECCO Genetic and Evolutionary Computation Conference, pp. 2389–2396 (2009)
- [26]: R. Tanabe and A. Fukunaga: "Success-History Based Parameter Adaptation for Differential Evolution," Proceedings of the 2013 IEEE Congress on Evolutionary Computation, pp. 71-78 (2013)
- [27]: R. Tanabe and A. Fukunaga: “Improving the Search Performance of SHADE Using Linear Population Size Reduction,” Proceedings of the 2014 IEEE Congress on Evolutionary Computation, pp. 1658-1665 (2014)
- [28]: The Black-box Optimization Benchmarking (BBOB) Workshop, http://numbbo.github.io/workshops/index.html


# [minor comments]
## minor comment1 (General)
- The symbols are different in each equation or section, but only one meaning should be assigned to each symbol.
- Please unify (at least) the following symbols in order for the readers to understand and reproduce.
  - Iteration counter in algorithm: "Iter" in equation (10), "t" in equations (5) and (6), or "i-th generation" in equations (11) and (12)
  - UAV coordinate position in 3D environment model and design variable: "x, y, and z" in equations (1), (2), (3), and (7); "x_ij" in equations (5), (6)
  - Probability and vertex: "P_i" in equation (3), "p" in section 3.4, "P_c, P_m" in equations (11), (12), Table 1 (including lowercase or uppercase letter)
  - Constants in 3D environment model, the barrier coefficient, and fitness: "f" in equations (1) and (8); and "f_ibest and f_iave" in equations (11), (12)
  - multiple of expansion and chromosome length in GA: "k" in equation (9) and Table 1


## minor comment2 (p2, equation (8))
- I understand equation (8) occurs a penalty effect to avoid for UAV and obstacle being too close.
- Lmin is the shortest distance between UAV coordinate position and peak position in 3D environment, but how is it calculated?
- To my understanding, after all distances between UAV positions on each path segment and peaks are calculated during search process, Lmin may be the shortest distance of them.
- If the above understanding is correct, the amount of calculation is high dependence on the number of segments and peaks.
- Moreover, the numerical simulation assumes the static environment (start, destination, and obstacle position) is known, but how is Lmin calculation in practical application?
- Please add how to calculate Lmin in numerical simulation of this paper and show the author's opinion about Lmin in practical application.


## minor comment3 (p2, chapter3)
- Chapter 3 shows the proposed PSO's algorithm, but 3.3 and 3.6 sections show the optimization problem's formulation.
- Therefore, I think it is better to add a new section; for example, "2.3 optimization problem for path planning".


## minor comment4 (p4, Chapter4)
- There is no an explanation of the following conditions in numerical simulation. Please clarify them.
  - The number of peaks (7 peaks in section 4.1 and 10 peaks in section 4.2 to my understanding)
  - The dimension of the search space


## minor comment5 (p5, Figure6)
- Figure 6 shows the performance of the proposed PSO is more stable and superior to the classic GA and PSO in the path planning although the landscape of obstacles changes randomly.
- In general, the result means the relationship between the randomness and performance of metaheuristic algorithm.
- In this case, the box-and-whisker plot comparing statistical distribution of performance (average/standard deviation/max/min) and error bar (the x-axis label is each algorithm and the y-axis label is each statistic) are better than the current figure in Figure 6.

------------------------------------------
