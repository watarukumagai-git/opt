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

## 照会事項1
- 現原稿は、本論文の動機・目的が不明瞭である。
先行研究[2]-[13]は、改良したアルゴリズムをUAVの3次元経路問題に適用しているのみに留まっていると推測される。
しかしながら、本論文はこれらの先行研究と同じカテゴリに属しているにも関わらず、先行研究における研究課題や、それを踏まえた研究動機が現原稿には明記されていない。
以上を踏まえ、先行研究と比較しながら、本論文が着目しているUAVの3次元経路問題における研究課題や動機を明記すべきである。

## 照会事項2
- 現原稿は、本論文の独創性・新規性の主張が不明瞭である。
先行研究と比べて本論文の新しい点として、問題の定式化、適用したアルゴリズム、得た経路のどこにあるのかが明記されていない。
しかしながら、私が見る限り、独創性・新規性は、UAVの3次元経路問題における多峰性を克服するために提案したアルゴリズムに存在すると推測される。
もしこの推測が正しいなら、この問題を解くために本論文が提案したアルゴリズムが、先行研究のアルゴリズムと本質的に異なる点を提示することが必要である。
以上を踏まえ、先行研究と比較しながら、本論文の独創性・新規性を明記すべきである。

## 照会事項3
- 現原稿は、本論文の提案手法の計算効率・探索性能が古いGAやPSOよりも優れていることを主張している。
一方、読者は、提案手法の性能が現実の応用問題でも耐えられるのか知りたいはずだが、新原稿では、その性能と応用問題での適用可能性が明記されていない。
例えば、現実のUAVの自律制御の場面において広く使える水準を満たすのか、あるいは一部の場面なら使える水準を満たすのかなど、適用可能性について、先行研究を引用しながら、著者らの考えを明記すべきである。

## 照会事項4
- 提案手法は、様々なアイディアから構成されているが、現原稿では、本論文の提案手法における各アイディアに関する有用性の論述が不明瞭である。
もし著者らがUAVの3次元経路問題を解く難しさが多峰性にあると問題視するならば、提案手法の各アイディアの有効性を示す必要がある。
しかしながら、現原稿では、数値実験を通じて各アイディアの有効性について示されていない。
例えば、各アイディア単体を付加したアルゴリズム（dynamic weightだけを加えたPSO, 交叉・突然変異のみを工夫したGAなど）の探索性能との比較を通じて、この問題においてこれらのアイディアを組み合わせる必要性を示すべきである。

## 照会事項5
- 現原稿では、提案手法の探索性能が古いGAやPSOよりも優れていることを示しているが、
本論文の提案手法の比較手法が適切であることは非常に疑問である。
メタヒューリスティクスの分野では、多峰性関数を含めた多くのベンチマーク問題において、CMA-ES[1,2]やSHADE[3,4]、あるいはその改良手法の探索性能は、PSOやGAよりもはるかに優れていることが一般的に知られている。
この事実は、CECやGECCOなどのトップカンファレンスで開催されるコンペティション[5]など、様々な文献を通じて示されている。
もし著者らがUAVの3次元経路問題を解く難しさが多峰性にあると問題視するならば、CMA-ESやSHADEベースのアルゴリズムはこの問題においても高速かつ良好な探索性能を示すことが十分期待されるだろう。
これらの事実を踏まえると、本論文は、提案手法の比較手法が、CMA-ESやSHADEベースのアルゴリズムではなく、古いGAやPSOのみで十分である理由、あるいは、CMA-ESやSHADEベースのアルゴリズムのいずれかの探索性能と、この問題において直接比較する必要がある。以上を踏まえ、適切な文献を追加で引用すると共に、適切な比較手法を選定すべきである。

- [1]: CMAES、[2]: multistart CMAES、[3]: SHADE、[4]: LSHADE、[5]: BBOB

## 照会事項6
- 新原稿の数値実験では、経路を構成する最適化変数の数が明記されていない。
メタヒューリスティクスのアルゴリズムの探索ダイナミクスは、最適化変数の個数との関連性が強いため、原稿に明記すべきである。


## コメント1
- 照会事項6に関連するが、もしUAVの3次元経路問題が30以上などの高次元ならば、PSOベースのアルゴリズムは元々不利である可能性がある。PSOのパラメータ空間には安定・不安定領域が存在しており、PSOの探索ダイナミクス（収束性／発散性）はその空間内での配置に強く依存すること、さらに、最適化変数の個数の増加に伴い、その安定領域は若干狭くなることが知られている[6]。Constriction Method[7]や本論文で使用されているIWAは、慣性パラメータの設定・調整方法だが、探索過程におけるPSOの探索ダイナミクスを明確に考慮しておらず、探索前にパラメータの時系列変化を決めているため、適切な多様化・集中化が実現せず、局所解に陥りやすい。したがって、高次元かつ多峰性の問題では、PSOのパラメータ調整としては[8]などの適応的な方法が望ましいと考えられる。このため、本論文の数値実験で提案手法と比較する必要はないが、今後の発展においては有力だろうとアドバイスする。

- [6]: PSO
- [7]: CM

## コメント2
- 

## Total Comment
- This paper proposed an improved particle swarm optimization (PSO) and applied in three-dimensional path planning of UAV. The proposed method is the PSO algorithm introduced to the following several ideas: imporved operations (crossover/mutation/selection) in real-coded genetic algorithm (GA) and inertia weight parameter tuning. Moreover, the paper built a three-dimensional environment model for the problem and constructed a fitness function based on obstacles and path lengths.
Finally, it is verified that the obtained path of the proposed method is superior to that of conventional PSO and GA by solving the problem through numerical simulations.
- It provides an interesting observation and data.
- But, I think it still needs a considerable and major revision to be acceptable for publication in terms of motivation/object and originality/usability.
- From this reason, the judge is C.
- The authors should also clarify/correct the points listed below and improve the manuscript as necessary.

