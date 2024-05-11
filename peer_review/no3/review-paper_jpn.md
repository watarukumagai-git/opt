論文翻訳　TEEE No.3
Analysis of Enterprise Production and Transportation Collaborative Scheduling Algorithm in Intelligent Manufacturing Environment
Intelligent Manufacturing環境における企業生産と交通の協調計画アルゴリズムの分析

【概要】
Intelligent manufacturingは、世界規模の経済発展の現状によって、アカデミアやビジネスから多くの関心を集めている。工業ビジネスの2つの必須な要素は生産と交通である。しかし、伝統的な生産と交通の計画管理は独立になされており、システムの操作効率を下げている。地理的に工業施設の間の協調的な生産計画は、生産注文の配送顧客のための輸送を通して、分散している。計画手法は、リクエストに答えるために必要な分だけ、限られたリソースを使う。これを解くには、メタヒューリスティクスのハイブリッドである、多目的関数に基づくHPWL-IMEをされている、異なる生産と交通の元での協調計画問題に対処するために。
Particle(P) swarm optimization, Whale(W) optimization algorithm associated with Local(L) neighborhood search。これは資源最適効率を達成するために工夫する、注文生産のマシーン指令をアレンジすることで、生産時間の最小化をして。PSOのアプローチは、解空間を効率的に探索し、ポテンシャルがある生産計画や交通経路を特定するのを目指す。The whale optimization algorithmは、効果増加のための解を特定するために、探索の多様化と集中化のバランス点を探す。それは、機械のアクセス可能性や処理時間、より早期な顧客需要などのいくつかの計画の制約を考慮している。
よって、実装したHPWL-IMEアプローチは、顧客の配送納期を改善させる。最適な交通時間、最短の生産発注のメイクスパン、Average Relative Deviation Index (ARDI)、Earliest Due Date Assignment (EDDA) rule、生産と交通の効果的な活用のためのスケジューリング制約付きの全ての目的関数を達成する、を確保することで。

【1章 導入】
Currently, nations all over the world are pushing for the transformation of intelligent manufacturing processes, and conventional production techniques are consistently undergoing intelligent modifications as a result of the ongoing development of society. The growth of the global marketplace and the variety of industrial needs make it challenging for a single enterprise to complete complicated or customized ventures. The issues above can be resolved effectively by collaboration between various businesses. An intelligent manufacturing procedure has the capacity for autonomy and controls over oneself production and transportation to build the product following the design parameters.
現在、世界中の国々がインテリジェントな製造プロセスへの転換を推し進めており、社会の継続的な発展の結果、従来の生産技術は常にインテリジェントな変化を遂げている。グローバル市場の成長と産業ニーズの多様化により、一企業で複雑な事業やカスタマイズされた事業を完遂することは困難になっている。上記の問題は、様々な企業間のコラボレーションによって効果的に解決することができる。インテリジェントな製造手順には、設計パラメーターに従って製品を製造するために、自ら生産と輸送を自律的に制御する能力がある。

Collaboration enables enterprises to cooperate on resources and activities to accomplish a clear and shared business goal related to production and transportation in an intelligent manufacturing environment. The swarm intelligence-based systems for scheduling have the potential to revolutionize the way manufacturing executives approach challenging scheduling problems by using the power of decentralized decision-making and combined intelligence. Implementing collaborative scheduling in enterprises increases the employee involvement ratio and improves productivity. Intelligent manufacturing processes address the degrees of innovative and progressive cleverness to promote its development, its ability to be understood as a manufacturing system, and its ability to adapt to changing conditions without sacrificing goals [1]. Using novel communication and information technologies enhanced the connectivity and openness of intelligent manufacturing infrastructure, changing how information interacts, how the work is completed, and how work should be managed. 
コラボレーションは、インテリジェントな製造環境において、生産と輸送に関連する明確で共有されたビジネス目標を達成するために、企業がリソースとアクティビティに関して協力することを可能にする。スケジューリングのための群知能ベースのシステムは、分散された意思決定と結合された知能の力を利用することで、製造業の幹部が困難なスケジューリング問題にアプローチする方法に革命を起こす可能性を秘めている。企業における協調スケジューリングの導入は、従業員の関与率を高め、生産性を向上させる。インテリジェント製造プロセスは、その発展を促進するための革新的で進歩的な賢さの程度、製造システムとして理解される能力、目標を犠牲にすることなく状況の変化に適応する能力に対処する[1]。斬新な通信・情報技術を使うことで、インテリジェント製造インフラの接続性と開放性が強化され、情報の相互作用、作業の完了方法、作業の管理方法が変化する。

For Intelligent Manufacturing (IM) and operations management, such developments call for cooperation, adaptability, communication, and autonomous and collaborative decision-making [2]. Thereby [3] created a novel intelligent manufacturing framework that emphasizes correct decisions through big data-driven evaluation in the industrial environment and real-time adaptive observation. But it has a limitation related to reliability and a big data field that indirectly affects production decision-making. Hence [4] created a platform that gathers distributed resources and implements a platform-based intelligent manufacturing environment to maximize the collaborative arrangement of resources across enterprise levels with multi-agent systems. 
インテリジェント・マニュファクチャリング(IM)とオペレーションズ・マネジメントでは、このような発展により、協調性、適応性、コミュニケーション、自律的かつ協調的な意思決定が求められる[2]。これにより[3]は、産業環境におけるビッグデータ主導の評価とリアルタイムの適応的観察を通じて、正しい意思決定を重視する新しいIMのフレームワークを作成した。しかし、このフレームワークには、信頼性に関する限界と、生産意思決定に間接的に影響するビッグデータ分野がある。そこで[4]は、分散資源を集めるプラットフォームを作成し、マルチエージェントシステムにより企業レベルを超えた資源の協調配置を最大化するプラットフォームベースのインテリジェント製造環境を実装した。

Then [5] explored thestrategies for implementing collaborative smart technology for manufacturing to increase the robustness and survival of supply chains for manufacturing and businesses to fend off big calamities with smart technologies IoT,5G, big data, and others to maintain the manufacturing sector's endurance and sustainability. [6] provided a range of digital designs of circuit break intelligent manufacturing processes, cost and quality efficiency, and environmental effects concerning the intelligent enterprise paradigm in the preproduction stage and offered dependable options for real the real world. 
そして、[5]は、製造業の耐久性と持続可能性を維持するために、スマート技術IoT、5G、ビッグデータなどを用いて、製造業と企業のサプライチェーンの堅牢性と生存率を高め、大きな災難を退けるための製造業向け協調スマート技術の導入戦略を探求した。[6]は、インテリジェント企業のパラダイムに関する回路ブレークインテリジェント製造プロセス、コストと品質効率、環境効果のデジタル設計の範囲をプリプロダクションの段階で提供し、現実の世界のための信頼できるオプションを提供した。

In [7], the quality and total cost of the product in an enterprise could be impacted by the manufacturing unit's efficiency and the factory's overall production efficiency. The intelligent manufacturing facility can break down an order after receiving it from the user and transmit it to every component to set up specific duties.[8] offered a digital twin and blockchain technologies improved manufacturing service cooperation mechanism for the Industrial Internet platforms to solve the lack of physical and digital space contact and credibility issues during the establishment of the present manufacturing network platform-based production. Outlined an instantaneous collaborative scheduling approach based on online Cyber-Physical System for Production (CPPS) observation to tackle the issue of quick reaction repair of interruption in the rapid railroad wheelset manufacture. Scheduling is crucial in intelligent manufacturing processes for reducing production expenses and raising consumer satisfaction [9]. 
[7]では、企業における製品の品質と総コストは、製造ユニットの効率と工場全体の生産効率によって影響を受ける可能性がある。インテリジェントな製造設備は、ユーザーから注文を受け取った後、注文を分解し、各構成要素に送信して特定の職務を設定することができる。[8]は、現在の製造ネットワークプラットフォームをベースとした生産の確立中の物理的およびデジタル空間の接触と信頼性の問題の欠如を解決するために、デジタルツインとブロックチェーン技術によって改善された産業インターネットプラットフォームのための製造サービス協力メカニズムを提供した。オンライン生産サイバーフィジカルシステム（CPPS）観測に基づく瞬時協調スケジューリングアプローチを概説し、迅速な鉄道車輪製造における中断の迅速な反応修復の問題に取り組む。スケジューリングは、生産コストを削減し、消費者の満足度を高めるためのインテリジェントな製造プロセスにおいて極めて重要である[9]。

The scheduling method should use the fewest resources necessary to meet the demand for services, such as scheduling the shortest task first and the earliest due date first [10]. An integrated discrete multifaceted imperial competition approach is suggested by [11] to minimize processing time consumption of energy and noise by building a multifaceted, dynamic job shop scheduling constraint paradigm bounded by job transportation time and learning impact. Likewise, [12] outlined an instantaneous collaboration scheduling approach based on the online cyber-physical system for production observation to deal with the issue of quick reaction repair of interruption in the rapid railroad wheelset manufacture. Additionally, an improved neighborhood-discrete Particle swarm algorithm features an extended neighborhood search strategy for the equipment production process.
スケジューリング方法は、最短タスクを最初にスケジューリングし、最も早い期日を最初にスケジューリングするなど、サービスの需要を満たすために必要な最小のリソースを使用する必要がある[10]。また、[11]では、ジョブの輸送時間と学習影響に束縛された多面的で動的なジョブショップ・スケジューリング制約パラダイムを構築することにより、エネルギーとノイズの処理時間消費を最小化する、統合された離散多面的帝国競争アプローチが提案されている。同様に、[12]は、迅速な鉄道車輪製造における中断の迅速な反応修復の問題に対処するために、生産観察のためのオンラインサイバーフィジカルシステムに基づく瞬時コラボレーションスケジューリングアプローチを概説した。さらに、改良された近傍-離散粒子群アルゴリズムは、設備生産プロセスのための拡張近傍探索戦略を特徴とする。

[13], addressed a hybrid flow shop scheduling challenge with a parallel machine in each stage to reduce the weighted sum of makespan and overall flow time while accounting for human factors. The limitation here is the weighted average of makespan, and the entire flow time is the only performance metric used in the study. In [14] analyzed an effective order-merging approach that combines a selection of orders of the same kind across the course of production while weighing the benefits of continuous processing. Although simple, this tactic could result in higher deviation rates, raising scheduling costs.[15] provided a thorough analysis of how prepared SMEs are in emerging nations to use the cutting-edge technology associated with Intelligent Industry version 4.0. 
[13]は、各ステージに並列機を持つハイブリッドフローショップスケジューリングの課題に取り組み、人的要因を考慮しながら、メイクスパンと全体のフロー時間の加重和を削減した。ここでの限界は、メイクスパンの加重平均であり、全体のフロー時間は、この研究で使用された唯一のパフォーマンス指標である。[14]では、連続処理の利点を考慮しながら、生産過程にわたって同じ種類のオーダーの選択を結合する効果的なオーダー結合アプローチを分析している。[15]では、新興国の中小企業がインテリジェント・インダストリー・バージョン4.0に関連する最先端技術を利用する準備がどの程度できているかについて徹底的な分析を行っている。

These methods include cyber-physical systems, intelligent manufacturing systems, and other essential technology tools for enhancing connectivity and communication inside production and manufacturing processes. To strengthen the capacity of enterprises and transportation at various levels to handle all crucial aspects, [16] defined collaborative scheduling of intelligent manufacturing technologies ought to include 5G connection, cloud concepts in manufacturing, IoT for sensing, cutting-edge computing, big data analytics, and virtual reality. 
これらの手法には、サイバーフィジカルシステム、インテリジェント製造システム、および生産・製造プロセス内部の接続性と通信を強化するためのその他の不可欠な技術ツールが含まれる。あらゆる重要な局面に対応できるよう、様々なレベルの企業や交通機関の能力を強化するため、[16]は、インテリジェント製造技術の共同スケジューリングには、5G接続、製造におけるクラウドコンセプト、センシングのためのIoT、最先端コンピューティング、ビッグデータ分析、バーチャルリアリティを含めるべきだと定義した。

本研究の主な革新点は以下の通りである：
- IMEにおける協調的な生産と輸送のスケジューリングを改善するために、ハイブリッド化されたソリューションは、顧客の要求を満たすために、生産オーダーの最も早い納期で、強化された方法で3つのメタ・ヒューリスティック・アプローチをブレンドする。
- 顧客の完全なサービス要求を可能にし、最小の生産時間を確保し、最も少ない生産資源を効果的に資源利用を考慮し、コストを下げ、輸送効率を改善する。
- 車両の最大キャパシティと配送ウィンドウを採用することで、生産オーダーを迅速に顧客に届けるための最適な輸送ルーティングを重視する。
- より良い生産・輸送スケジュールを実現するために、生産スパンの短縮、最小ARDI、最適輸送時間、EDDAルールなどのパフォーマンス指標を評価する。
この原稿の残りのセクションは以下のように構成されている。2章では、企業における生産と輸送スケジューリングのコラボレーション関連技術に関する文献研究について述べる。3章では、インテリジェントな方法で効果的な企業管理環境を実現するための目的定式化、制約条件、およびハイブリッド・メタヒューリスティクス・アルゴリズムの実装から始める。4章では、提案手法の結果と現状技術との比較について議論する。最後に、結論として研究結果をまとめ、5章で今後の研究を提案する。


【2. Relevant literature survey】
Xiongら[20]は、生産と交通のためのDTベースの協調スケジューリング技術(DTCST)を使うことを提案した。生産、配送、調達の3フェーズの協調スケジューリングモデルは、柔軟なジョブショップ製造環境内の交通で求められる時間を最小化するために構築された。強化されたGAがそのモデルを解くのに使われている、解のエンコードデコードされた情報を扱う、動的なインターフェースを扱うのに有用なDTベースのモデルで、重要な需要の入り時間と実世界で設定されるような実際の観察時間のような。成果は、協調スケジューリング技術がこのシナリオ研究と実験結果を通して有益であることを示している。
Liuら[22]は、生産と輸送ルーティングのスケジューリングにおいて、全体のオーダーのバランス納期を短縮することを考慮に入れており、そのために、拡張大規模近傍探索(ELNSs)アプローチを用いて、両者の相互作用を考慮に入れて共同化することを提案している。初期解は二段階の手続きで生成され、最初に車のルートを確立し、そのルートを使って、最適な生産順序を特定するために、ヒューリスティックの挿入と削除のための特定のルールが使用されます。計算結果は、提案するELNS法がGA（Genetic Algorithm）を凌駕し、初期解を約50秒大幅に改善することを示している。主な欠点は、この統合解の下限制約と上限制約を考慮していないことである。
Luら[23]は、Hybridized Multi-verse Optimizer-Variable NS (HMOVNS)アルゴリズムを開発した。ファジイ計算と過去シーケンスに依存する配達時間付きの強い並行バッチスケジューリング問題の研究的な課題に素早く対処するために。単一機械スケジューリングは、インテリジェント製造プロセスにおける対応する企業課題の構造的特性で最適化される。この実装で、このハイブリッドメタヒューリスティクスは、様々な研究において、良い結果、ロバストネス、計算時間性能を示す。
この結果は、平均の計算時間が0.561秒で、最小の標準偏差が2.51%、相対割合偏差が6.461であることを示している。本研究の不足は、様々な問題状況や産業的文脈に対するアプローチの一般性を決定することである。

前述の文献レビューから明らかなように、メタヒューリスティクスは、企業生産における自明でない困難な状況を処理する能力を向上させてきた。
さらに、HPWL-IMEは、DTCST、
ELNSs、HMOVNSのような他のヒューリスティクスと比較した場合、SA、GA、CWOT、ACOのような他の手法を様々な性能指標で上回った。様々な協調アプローチによる生産と輸送のスケジューリングモジュールは、最適化アルゴリズムによるインテリジェントな製造プロセスのために分析されたバランスの取れた最適化された技術を使用しています。
intelligent manufacturingシナリオでは、目標は生産過程と交通の両方の期間を考慮しながら、全体のメイクスパンを減らせることだろう。目標は、全体を最小化し、マシーンμとルート交通のコンビネーションと関係した、Tを求めること。


【3. Implementation of the Proposed technique】
限られた資源の中で、共同スケジューリングという課題は、一般的に顧客対応時間を優先し、物流コストを削減しながら顧客サービスを向上させる。資源をより効果的に活用し、共に意思決定を行うことで企業の対応時間を早めることは、スマート・マニュファクチャリングの2つのメリットである。製造企業のグローバル化は、低遅延要件を確保するための調整スケジューリング技術の欠如を含め、intelligent manufacturingに多くのハードルをもたらしたが、製造最適化の問題は複雑な生産システムで頻繁に発生する。ヒューリスティックと呼ばれる手法によって任意に作成されたシーケンスは、メタヒューリスティックに基づく手法の出発点であり、停止要件が満たされるまで繰り返される。これらのメタヒューリスティック・アルゴリズムのハイブリッド化された組み合わせは、様々なプロセス、機械、人間、その他のリソースの相互関連関係や相互作用を考慮することにより、生産プロセス全体の有効性、生産性、適応性を高める。スケジューリングシステムは、動的な状況において優れた性能を発揮する群知能アルゴリズムのおかげで、生産状況、設備の稼働率、クライアントの要求の変化に対してリアルタイムで調整することができる。この柔軟性は、intelligent manufacturingの環境において、生産リードタイムを短縮し、顧客対応力を向上させる。企業は、ロジスティクス活動を組織的に計画し実行するために作成された科学的技術やソフトウェアを採用しなければならない。これらの技術やプログラムは、輸送業務の有効性と効率を改善し、管理者に大きな利益をもたらす。生産スケジュールの最適化、納期遵守の強化、全体的な製造効率の向上はすべて、インテリジェント製造アプローチにEDDAを加えることによって促進される。
図1に示すように、あらゆる選択肢の中で、企業の生産活動管理とコラボレーションを調整することが重要である。包括的な理解と相互作用は、コラボレーションを成功させるための基礎となる。製造業では、センサーやIoTデバイスが、輸送や生産手順の監視や可視化に頻繁に活用されている。新しい通信技術は、共同生産エンティティ間のより効果的でオンデマンドな相互作用を可能にする。問題を解くためにハイブリッド化されたPSOアルゴリズムを実行することにより、可能性の出発点である初期母集団が発見される。これらの解は、潜在的な生産スケジュールと輸送ルートを示している。PSO集団の最適解は、PSOアルゴリズムがラウンドを完了した後、WOAアルゴリズムの開始集団として使用される。この初期母集団を出発点として、WOAアルゴリズムはさらに探索と利用を行い、解を研ぎ澄まし、強化する。

【3.1 生産段階】

【3.2 交通計画】

【3.3 改良方法におけるPSO-WOA-based LNSハイブリッドメタヒューリスティクス実装】


【3.4 生産発注シーケンスの計算のための疑似コード】

【4. 実験検証】
DTCST [20], ELNSs [22], and HMOVNS [23]

【4.1 様々なスケジューリング制約付きの目的関数の達成を特定する】
図4は、IMEにおける効率的な生産と輸送の協調スケジューリング制約のために取られる目的関数の数を示した図である。横軸は、目的関数に到達するために必要なスケジューリング制約を示す。
多目的関数は、生産と輸送について式1と4を使用して精緻化される。したがって、提案アルゴリズムは、複雑な環境生産・輸送問題において、目的基準を満たすためのメタヒューリスティック最適化アプローチに従っている。

【4.2 スケジューリングアルゴリズムのための平均相対偏差指標RDI】

【4.3 生産タスクの増加数のメイクスパンの計算】

【4.4 Earliest Due Date Assignment (EDDA) rule】

【4.5 輸送時間】

【5. 結論】
単純な技術はもはや顧客の需要を満たすのに十分でないため、デジタル企業はintelligent manufacturingを必要とする。
提案のHPWL-IMEアプローチは、各手法の長所を活用することで、効率的かつ公平に生産計画と交通経路を最適化する。
このハイブリッドな技術は、解空間を効率的に探索し、全体効果を改善可能な、実行可能な経路とタイムテーブルを求めるのを可能にする。
局所的探索と大域的探索のバランスはより効率性の高い解に改善する。

異なる目的と制約は顧客の要求と生産時間の削減を満たすのを考慮される必要がある。
統合されたメタヒューリスティクスの利益は、より良い配達コミットメント、より短い工業メイクスパン、より効率的な交通時間で結果を出すことだ。
この方法は、柔軟で賢く、グリーンな工業プロセスを実装するのに、アカデミックな重要性と有益性の両方を提供することで、世界的経済が早く変わる中でビジネスのための計画、などの技術において相当な改善を提供する。
この提案された研究で直面した限界は、スケジューリング問題の複数の目的(タイムスパン、配達重量付きの交通時間、最小相対差の最小化)をすべて同時に満たす最良のアプローチがないことである。
将来的には、多目的最適化のNon-determined sortingや選択技術は、解空間における多様性を維持することや意思決定者によくバランスがとれた選択肢の選択自由度を与えるために適用されるだろう。それは企業目標や決定する計画の制約に合致している。
