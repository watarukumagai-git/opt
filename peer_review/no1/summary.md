# Summary
## Abstruct
- The traditional particle swarm optimization algorithm is fast and efficient, but it is easy to fall into a local optimum.
An improved PSO algorithm is proposed and applied in 3D path planning of UAV to solve the problem. 
Improvement methods are described as follows: combining PSO algorithm with genetic algorithm (GA), setting dynamic inertia weight, adding sigmoid function to improve the crossover and mutation probability of genetic algorithm, and changing the selection method. 
Simulation results show that the route results solved by the improved PSO algorithm are better, which is 10% higher than that of PSO, and 58.3% better than that of GA.
- 古典的なPSOは高速かつ効率的だが、局所解に陥りやすい。本論文は、改良したPSOを提案し、UAV（ドローン）の3次元経路計画問題に適用している。改良手法は下記のように説明できる：PSOにGAを組み合わせた、dynamic inertia weightを設定した、シグモイド関数をGAの交叉・突然変異の確率に追加した、選択方法を変更した。数値実験結果を通じて、改良したPSOが導出した経路結果は、従来のPSOよりも10%優れており、GAよりも58.3%優れていることを確認した。


## 1章：導入
- At present, as robots enter our lives, boring, repetitive work is transformed into more unmanned and intelligent work using machines instead. 
Among them, the development of UAV-related technology has brought great convenience to our lives, such as the use of UAV for plant protection operations, logistics and distribution. 
Due to the short flight duration of UAV, path planning is one of the key issues in the automatic control of UAVs.
- 現在、我々の生活・余暇・反復作業にロボットが介入するなどは、機械を代理で使うことで、より実施する人が不要かつ賢くなるように、変革している。
これらの間で、UAV関連の技術開発は生活により改善をもたらした、例えば、工場保全業務、ロジスティクス、流通などでのUAVの使用である。
UAVの短い飛行間隔のため、経路計画はUAVの自律制御化において重要な課題の一つである。
- Path planning algorithms suitable for UAVs can be divided into two categories, one is the global path planning algorithm in the continuous domain, and the other is the local path planning algorithm in the continuous domain (1). 
Threedimensional path planning belongs to global path planning, which can be optimized by using traditional algorithms or swarm intelligence. 
- UAVに適した経路問題アルゴリズムは、二つのカテゴリーに大別できる：連続空間でのグローバル経路計画とローカル経路計画。3次元経路計画はグローバル経路計画に属しており、古典的な手法か群知能アルゴリズムによって最適化できる。
  - Qiang Bian and others (2) used greedy search, adaptive processing of search direction and other methods to improve the A* algorithm for path planning.
improved some of the defects of the PSO algorithm and improved its search ability. 
  - Wang Yihu and others (3) introduced the chemotaxis and migration operations of the bacterial foraging algorithm (BFO) into the PSO algorithm, which effectively improved some of the defects of the PSO algorithm and improved its search ability.
  - Wang Zhihui and others (4) proposed the moth to flame algorithm, which introduced a dynamic adjustment strategy, and constantly generated new individuals to avoid falling into local optimum and enhance population diversity.
  - Sun and others (5) proposed a high-performance bacterial foraging genetic particle swarm hybrid algorithm to improve the computing speed and the availability of the method.
  - Kong (6) introduced the artificial potential field method and added random pheromones to improve the ant colony algorithm to improve the problem of slow convergence and the tendency to fall into local optima.
  - Xie and Kong (7) proposed a high performance bacterial foraging-genetic-particle swarm hybrid algorithm to address the shortcomings of the particle swarm algorithm, improving the computational speed and capability of the algorithm and further enhancing the usability of the method.
  - Pan (8) designed a step-based A* algorithm that not only guarantees path planning but also optimises search time.
  - Particle swarm optimization algorithm is easy to fall into local optimization in the later stage, so Fu and Hu (9) mixed particle swarm optimization with longicorn beetle beard algorithm (BAS) to obtain the more reasonable path and the higher search-efficiency.
  - Chengyang Lu and others (10) introduced the A* idea on the basis of RRT, which enables RRT to be targeted in the search and improves the path quality.
  - Manh Duong Phung and Quang Phuc Ha (11) proposed a particle swarm optimization algorithm based on spherical vector (SPSO), which transforms the path planning problem into an optimization problem with UAV feasibility and safe operation requirements and constraints. 
  - Through the corresponding relationship between the particle position and the UAV speed, turning angle and pitch angle, the SPSO algorithm is used to find the optimal path. 
  - B. Abhishek (12) et al. proposed a particle swarm optimization algorithm based on harmony search algorithm, which performs exploratory search and utilization search at the same time.
  - In order to solve the problem of UAV path planning under unknown threats, Jong-Jin Shin and Hyochoong Bang (13) proposed an improved particle swarm optimization algorithm consisting of preprocessing steps, multi-swarm PSO algorithm and postprocessing steps.
  - [2]は、貪欲法やadaptive processing of search directionなどの手法を使い、経路計画のためのA*アルゴリズムを改善している。
  - [3]は、bacterial foraging algorithm（BFO）の走化性と移民操作を導入したPSOを提案し、PSOよりも探索性能が改善することを示した。
  - [4]は、the moth-flame algorithm（飛んで火にいる夏の虫）に動的な調整戦略を導入し、局所解収束の回避と個体の多様性の改善をするために、候補生成を変更した。
  - [5]は、high performance bacterial foraging-genetic-particle swarm hybrid algorithmを提案し、計算速度と利便性を改善した。
  - [6]は、ポテンシャル場アルゴリズムにランダム現象を導入し、収束性の遅さと局所解に陥る傾向を有するACOを改善した。
  - [7]は、high performance bacterial foraging-genetic-particle swarm hybrid algorithmを提案し、PSOの欠点を克服し、計算速度と手法の有効性を改善した。
  - [8]は、経路計画の保証だけでなく探索時間も最適化する、stepベースA*アルゴリズムを設計した。
  - [9]は、PSOが探索終盤で局所解に収束するため、PSOとlongicorn beetle beard algorithm (BAS)を組み合わせた方法を提案、探索効率を改善しながら、より合理的な経路を入手できることを確認した。
  - [10]は、A*アルゴリズムのアイディアをRRTの基礎に導入し、RRTの目標探索を可能にし、経路の品質を改善した。
  - [11]は、PSO　based on spherical vector(SPSO)を提案し、経路計画問題をUAVの実行可能性と安全運転の必要性と制約条件を有する問題に変換した。
  - [12]は、PSO based on harmony search algorithmを提案し、探索の有効性と多様な探索を同時に実現した。
  - [13]は、未知の脅威が前提のUAVの経路計画問題を解くために、前処理に改善したPSOを適用し、後処理にmulti-swarm PSOを適用した方法を提案した。
- The paper designs a hybrid particle swarm optimization algorithm to solve the 3-dimensional path planning problem of UAV. 
Build a 3D environment model, and constructing a fitness function based on obstacles and path lengths. 
At the same time, the inertia weights of the particle swarm algorithm are improved. 
The selection operation of Genetic Algorithm (GA) is introduced, and the crossover and mutation probability models are improved. 
Finally, the proposed algorithm is simulated by MATLAB to verify the effectiveness.
- 本論文は、UAVの3次元経路計画問題を解くハイブリッドPSOを設計する。3次元環境モデル、障害と経路長に基づき適合度関数を構築する。同時に、PSOの慣性パラメータを改善する。GAの選択方法を導入し、交叉と突然変異の確率モデルを改善する。最後に、MATBLABによって提案手法の有効性を検証する。

## 2章

## 3章

## 4章