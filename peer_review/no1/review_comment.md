# レビューコメント
## 総括コメント
- 本論文は、改良したPSOを提案し、UAVの3次元経路計画問題に適用している。提案手法は、GAの操作や慣性パラメータの調整など、様々なアイディアを組み込んだPSOである。そして、3次元環境モデルを構築し、障害物や経路長に基づく適合度関数を設計している。数値実験を通じて、提案手法で経路計画問題を解き、他の手法と比較して、得た経路が優れていることを確認している。
- 一方、現原稿は、本論文の動機・目的、数値実験結果について、大幅な修正と追記が必要だと感じた。この理由から、本論文は、独創性・新規性・有用性のそれぞれで不足していると判断し、照会後判定とした。下記の照会事項およびコメントへの回答と、必要に応じた原稿修正を要求する。
  - C判定：照会後判定？

## 照会事項1
- 現原稿は、本論文の動機・目的が不明瞭である。先行研究[2]-[13]は、改良したアルゴリズムをUAVの3次元経路問題に適用しているのみに留まっていると推測される。しかしながら、本論文はこれらの先行研究と同じカテゴリに属しているにも関わらず、先行研究における研究課題や、それを踏まえた研究動機が現原稿には明記されていない。先行研究と比較しながら、本論文が着目しているUAVの3次元経路問題における研究課題や動機を明記すべきである。

## 照会事項2
- 現原稿は、本論文の独創性・新規性の主張が不明瞭である。先行研究と比べて本論文の新しい点として、問題の定式化、適用したアルゴリズム、得た経路のどこにあるのかが明記されていない。しかしながら、私が見る限り、適用したアルゴリズムに独創性があり、得た経路に新規性があると推測される。もしこれが正しいなら、この問題を解くために本論文が提案したアルゴリズムが先行研究のアルゴリズムと本質的に異なる点や、本論文が得た経路が先行研究によって得た経路がまだ得られていないことを提示すべきである。
以上を踏まえ、先行研究と比較しながら、本論文の新規性を主張すべきである。

## 照会事項3
- 現原稿は、本論文の有用性の主張が不明瞭である。照会事項2で示した通り、本論文の新規性が適用したアルゴリズムと得た経路にあると仮定すると、それぞれ下記の点で有用性が不明瞭である。
  - アルゴリズム：
    - 提案手法は、様々なアイディアから構成されている。もしあなたたちがUAVの3次元経路問題を解く難しさが多峰性にあると問題視するならば、提案手法の各アイディアの有効性を示す必要がある。しかしながら、現原稿では、数値実験を通じて各アイディアの有効性について示されていない。例えば、各アイディア単体を付加したアルゴリズム（dynamic weightだけを加えたPSO, 交叉・突然変異のみを工夫したGAなど）の探索性能との比較を通じて、この問題においてこれらのアイディアを組み合わせる効果を示す必要がある。
    - さらに、メタヒューリスティクスの分野では、多峰性関数を含めた多くのベンチマーク問題において、CMA-ES[1,2]やSHADE[3,4]、あるいはその改良手法の探索性能は、PSOやGAよりもはるかに優れていることが一般的に知られている。この事実は、CECやGECCOなどのトップカンファレンスで開催されるコンペティション[5]など、様々な文献を通じて示されている。もしあなたたちがUAVの3次元経路問題を解く難しさが多峰性にあると問題視するならば、CMA-ESやSHADEベースのアルゴリズムはこの問題においても高速かつ良好な探索性能を示すことが十分期待されるだろう。これらの事実を踏まえると、本論文は、提案手法の比較手法が、CMA-ESやSHADEベースのアルゴリズムではなく、古いGAやPSOのみで十分である理由、あるいは、CMA-ESやSHADEベースのアルゴリズムのいずれかの探索性能と、この問題において直接比較する必要がある。
- 以上を踏まえ、適切な文献を追加で引用すると共に、先行研究と比較しながら本論文の有用性を主張すべきである。

- [1]: CMA-ES
- [2]: multi-start CMA-ES
- [3]: SHADE
- [4]: L-SHADE
- [5]: BBOB

## 照会事項4
  - 得た経路：
    - 先行研究で得られた経路と比べて、

## コメント1


## Total Comment
- The paper proposed an improved particle swarm optimization (PSO) and applied in three-dimensional path planning of UAV. The proposed method is the PSO algorithm introduced to the following several ideas: imporved operations (crossover/mutation/selection) in real-coded genetic algorithm (GA) and inertia weight parameter tuning. Moreover, the paper built a three-dimensional environment model for the problem and constructed a fitness function based on obstacles and path lengths.
Finally, it is verified that the obtained path of the proposed method is superior to that of conventional PSO and GA by solving the problem through numerical simulations.
- However, the current manuscript needs significant modification and explanation about 本論文の動機・目的、新規性・有用性について、大幅な修正と追記が必要だと感じたため、
