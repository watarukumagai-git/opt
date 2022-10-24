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
### 2.1 Environmental Model
The 3D path planning of the UAV needs to obtain in formation from the terrain model, and the actual situation should be considered when modeling the terrain.
By considering obstacles, environment and other factors, the established terrain model (14) is described as follows.
Z1(x,y)(1) 
where x and y are the horizontal and vertical coordinates, and Zi are the corresponding height values.
a,b,c,d,e,f,and g are constants used to control the height distribution of the map.
For a mountain in 3D environment, it can be represented by the following model. 
z(x,y)(2)
where n represents the total number of mountain peaks, (xi,yi) represents the center coordinate of the i-th peak, and hi is the parameter that controls the height.
xsi and ysi are the attenuations of the i-th peak along the x-axis and y-axis which can be used to control the slope, respectively.

### 2.2 キュービックBスプライン曲線に基づく経路平滑化アルゴリズム 
飛行中の頻繁な角度調整を避け、UAVの安全性を確保し、航行時間を短縮するために、キュービックBスプライン曲線を導入する(15). 
m+n+1個の平面または空間頂点Pi(i=0,1,...,m+n)において, 緑色のパラメトリック曲線セグメントと呼ばれる.
この曲線は,次のように定義される: Pk,n(t)= n i=0 Pi+kGi,n(t)t∈[0,1](3) 
ここで, Pk,n(t) は, 数番目のセグメントの3次B曲線, 数番目のセグメントはn次Bsplinecurvesと呼ぶ. 
Gi,n(t) は式（4）に従って定義された基本関数である. 
Gi.n(t)=1 n! n-i j=0 (-1)jCj n+1(t+n-i-j)n t∈[0,1]i=0,1,...n (4) 
経路の滑らかさを確保するために, 難易度を考慮し, n=3にして立方Bスプライン曲線で経路を平滑化した.

## 3章　Improve Particle Swarm Optimization
### 3.1 Particle Swarm Optimization
Particle Swarm Optimization (PSO) is an evolutionary computational technique proposed by Dr. Eberhart and Dr. Kennedy (16) by simulating the foraging behavior of birds.
A mass-less particle is designed to simulate a bird in a flock, and the particle has only two properties: velocity and position.
The velocity represents the speed of movement and the position represents the direction of movement.
Each particle individually searches

### 3.2 Fitness Function Design
The quality of the path length is one of the important indicators to measure the success of the algorithm improvement.
Due to the lack of battery capacity of the UAV, the flight distance is limited.
The shorter the flight path, the less time and energy it takes. 
Based on the cubic B-spline curve fitting path, the interpolation process is performed, and the interpolation is differentiated to obtain the fitness function: 
fitness=(xi+1−xi)2+(yi+1−yi)2+(zi+1−zi)2 (7) 
The obstacle risk factor f is introduced to avoid the collision between the UAV and the obstacle.
The barrier coefficient formula is described as follows: 
f=0Lmin>Ld 1Lmin<Ld (8) 
Considering the real environment, UAV is not a particle, and it has its own size.
So, setting Lmin as the minimum distance close to the peak, and Ld as the safe distance.
When f=1, the minimum distance is less than the safe distance, and it is easy to cause danger, so the fitness function needs to be increased.
At the same time, the fitness function is modified to Eq.(9). 
fitness = k fitness (9) 
where k is the multiple of expansion, k=5.

### 3.4 選択操作 
遺伝的アルゴリズム（GA）は、ダーウィン生物進化の自然選択と遺伝のメカニズムを模擬した生物進化過程の計算モデルであり、自然進化過程を模擬して最適解を探索する手法である(18)。
その主な手順は、選択、交叉、変異、適合度関数設計である。
選択操作とは、集団の中から良い個体を選び出し、悪い個体を排除する操作のことである。
適性値の評価により、適性の高い個体ほど選択されやすく、次世代に引き継がれる確率が高くなる。
このような早熟な状況を回避するために、本論文では混合選択演算子を採用している。
第一の方法は、最適フィットネス選択法を用いてフィットネスを並べ替え、より良いフィットネスを親1として選択し、母集団の割合をpとして選択する。
第二の方法は、確率psecを選択してルーレット法を用いる。
選択された母集団を親2とし、母集団の割合を1-pとする。

### 3.5 交叉・突然変異確率モデルの改良 
交叉操作は，選択された親個体の部分構造を置換・再結合して新しい個体を生成する操作であり，探索能力を向上させることができる．
突然変異操作は、突然変異確率を小さくしていくつかの遺伝子の値をランダムに変化させる操作であり、補助的な探索操作に属し、集団の多様性を維持することを目的とする。
一般に乱数randを発生させ、rand < Pmであれば演算を行う。
交叉確率と突然変異確率は新しい集団の選択に重要な影響を与える。
交叉確率Pcは交叉操作の頻度を制御する。
交叉確率を大きくすると探索能力が向上するが、探索性能が低下しやすくなる。
また、交叉確率が低すぎると、アルゴリズム性能の低下を招きやすい。
また、変動確率が大きすぎると、アルゴリズムがランダムに探索する傾向があるため、大きすぎることはできない(19)。
本論文では、交叉と突然変異の確率を変更するためにシグモイド関数を導入している。
固定された交叉確率と突然変異確率では、反復が進むにつれて母集団の一部の個体が破壊されてしまうのを防ぐためである(20)。
その式は以下のように記述される。
1 1 +efibest - fiave 
Pc = Pcro + Pm = Pmut + 1 1 +efibest-fiave (11) (12) 
ここで、Pcro = 0.8, Pmut = 0.2, fibest はi番目の世代の母集団における適性の最適値、fiave はi番目の世代の母集団における適性の平均値である。

### 3.6 制約条件 
飛行中のUAVの危険を防止するために、実際の状況に応じて制約条件を設定する必要がある。
まずUAVに大きな影響を与えるのは高度である。
高高度での飛行は温度や気流の影響を受けやすく、低高度での飛行は建物や樹木による外乱の影響を受けやすい。
したがって、適切な高度で飛行するために、式(13) 
zmin < zj < zmax (13)
ここで、zjはj番目の時刻の高度位置、zmin，zmaxは最小と最大の高さを表します。
また、UAVが設定された環境から飛び出さないように、環境の大きさを100×100×100mとした。

### 3.7 改良型 PSO アルゴリズムのフローチャート
改良型 PSO アルゴリズムのフローチャートは 
- (1) 式 (1) および式 (2) により 3 次元シーンを設定し、開始点と終了点を設定する。
- (2) パラメータの初期化。粒子集団サイズ、最大反復回数、慣性重み、社会的重み、認知的重みを設定する。
- (3) 母集団の初期化。粒子のランダム生成と速度の初期化、初期適応度の計算と衝突検出を行い、個別最適と全体最適を更新する。
- (4) メインループに入る。速度と位置を更新し、境界外を避けるために速度と位置の検出を同時に行い、フィットネス値の計算と衝突検出を行い、個別最適と大域最適を更新する。
- (5) 遺伝的アルゴリズムを導入する。最適な粒子集団を選択するための選択操作と、交叉、突然変異の操作を行う。
新しい世代の個体群は、次の世代のサイクルの初期個体群として使用されます。
- (6) 終了条件 最大反復回数に達したかどうかを判定し、達した場合はループを抜けて結果を出力し、そうでない場合はステップ(4)に戻る。



## 4章
提案する改良型PSOアルゴリズムの優位性を検証するために、従来のPSOアルゴリズムとGAアルゴリズムを対照群として選択し、反復回数などのパラメータは変更しない。
上記の3つのアルゴリズムは、MATLAB上でシミュレーションとテストが行われる。2組の実験を行い、実験結果を分析する。
テスト環境はWindows10、64ビットシステム、MATLAB R2020bシミュレーションプラットフォームである。
アルゴリズムのパラメータは表1の通りである。
3次元経路計画における改良型PSOアルゴリズムの優位性を検証するために、以下の2つの実験をそれぞれ実施した。

### 4.1 同一環境下での比較分析
改良型PSOアルゴリズム、PSOアルゴリズム、GAアルゴリズムの3次元経路計画結果の正面図を図2,3,4に、3つのアルゴリズムの適応曲線を図5に示す。
Fig.2,FIg.3,Fig.4に示すように、上記3つのアルゴリズムは、3次元環境における経路計画タスクを達成することができる。
しかし、Fig.4では、複雑な環境のため、従来のGAアルゴリズムでは「デッドゾーン」に陥りやすく、生成される経路が複雑で長すぎることがわかります。
一方、Fig.3では、従来のPSOはGAよりも優れた経路計画を行い、グローバルな探索能力にも優れています。
Fig.2と比較すると、改良型PSOアルゴリズムは、局所最適に陥らないように後段で局所探索能力を強化し、計画された経路の長さと滑らかさは従来のPSOアルゴリズムより優れています。
図5では、フィットネスカーブの変化から、GAアルゴリズムでは、20回目くらいの反復で局所最適に陥り、局所最適から飛び出す能力に欠けていることがわかります。
PSOアルゴリズムでは、9回目の反復で局所最適に陥っている。
115回目の反復では、まだ最適解を求めているが、その効果はもはや明らかではない。
改良型PSOアルゴリズムでは、RIのグローバル探索能力を確保するために、初期の反復でより大きな重みを持つ動的慣性重みを追加し、フィットネスカーブが急激に低下している。
反復回数が増加するにつれて、重みは減少する。局所探索能力を強化し、収束速度を上げ、基本的に23世代目で最適に到達することができる。
遺伝的アルゴリズムにおける選択、交叉、突然変異の操作は、母集団の多様性を向上させ、探索能力を強化するために導入され、局所最適化探索は後期反復で引き続き実行される。

###　4.2 Comparative Analysis In Random Environment 
制限環境を100×100×100m以内の3次元ランダム環境とし、開始点を(1,1,1)m、終了点を(100,100,50)mとし、ランダムに10個の障害物を生成し、200回反復させる。
改良型PSOアルゴリズムの平均適応度はPSOやGAアルゴリズムより低く、良好なメリット探索能力を示している。また、分散比較により、改良型アルゴリズムは安定性が高いことがわかった。
改良型アルゴリズムは PSO アルゴリズムよりも実行時間が長いが、表 2 の反復回数と平均適合度値に到達するまでの時間を比較すると、改良型アルゴ リズムは PSO アルゴリズムよりも優れていることがわかる。
その結果、改良型アルゴリズムは、14 回目の反復で 14.48s という短い時間で平均適合度に到達できることがわかった。
従来のPSOアルゴリズムでは、26回目の反復で23.13秒を費やしています。一方、GAアルゴリズムは36回目の反復を必要とし、57.76秒を消費します。
これは、改良されたアルゴリズムが他の2つのアルゴリズムよりも安定で高速であることを証明しています。

## 5章
本論文では、従来のPSOアルゴリズムの欠点である局所最適に陥る傾向を克服するため、改良型PSOアルゴリズムを提案し、3次元経路計画に適用した。
改良方法は、動的な慣性重みの導入と、遺伝的アルゴリズムに選択、交叉、突然変異の操作を追加することである。
ハイブリッド選択操作を用い、クロスオーバーと遺伝的確率モデルを改良し、母集団の多様性を高め、粒子群アルゴリズムのグローバル探索能力を維持し、後期反復におけるローカル探索能力を向上させる。
改良型PSOアルゴリズムをMATLABでシミュレーションし、PSOアルゴリズムおよびGAアルゴリズムと比較した。
その結果、改良型PSOアルゴリズムは、より優れた探索能力と安定性を持つことがわかった。
また、PSOアルゴリズムやGAアルゴリズムと比較して、改良型PSOアルゴリズムはより短い経路長とより良い経路平滑化を生成し、UAVの経路計画における探索量と探索効率を向上させることができた。
