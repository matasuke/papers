Title: Stacked Attention Networks for Image Question Answering
Date: 2018-08-02
Category: CV
Tags: VQA
Author: Kosuke Futamata
Summary:

## 1. どんなもの？
Visual Question Answerigに用いられるStacked Attention networkを提案。

<img src="{filename}/images/cv/stacked-attention-network/figure1.png" alt="image1" title="image1" width="100" height="100">

## 2. 先行研究と比べてどこがすごいの？
本論文で提案しているStacked Attention Mechanismを用いることで、VQAのタスクにおいてSOTAを達成。
また、本論文の投稿時にはAttention mechanismをVQAのタスクに適用したものとしては初。

## 3. 技術や手法の"キモ"はどこにある？
Stacked attention mechanismによって画像内の物体と質問文のアライメントを行う。
Attentionをスタック構造にすることによって画像内の物体への注意がよりシャープになるため、より特定の物体に注意を向けることが容易になっている。

ネットワークの構造は主に３つに分解される。
1つ目はImage model, 2つ目はQuestion Model,そして3つ目がStacked Attention Networksである。
Image modelはVGGNetを用いて画像の特徴量を抽出するのに用いられる。
Question modelはLSTMまたはCNNを用いてQuestionをEncodeする。

Stacked Sttention Networksは画像特徴量と質問文の特徴量を用いて画像に対するAttentionを得る。

<img src="{filename}/images/cv/stacked-attention-network/figure3.png" alt="image1" title="image1" width="100" height="50">
<img src="{filename}/images/cv/stacked-attention-network/figure4.png" alt="image1" title="image1" width="200" height="50">
<img src="{filename}/images/cv/stacked-attention-network/figure5.png" alt="image1" title="image1" width="200" height="50">
<img src="{filename}/images/cv/stacked-attention-network/figure6.png" alt="image1" title="image1" width="200" height="50">
<img src="{filename}/images/cv/stacked-attention-network/figure7.png" alt="image1" title="image1" width="200" height="50">

## 4. どうやって有効だと検証した？

### データセット
- DAQUAR-ALL
- DAQUAR-REDUCED
- COCO-QA
- VQA

### 評価

<img src="{filename}/images/cv/stacked-attention-network/figure8.png" alt="image1" title="image1" width="200" height="200">
<img src="{filename}/images/cv/stacked-attention-network/figure9.png" alt="image1" title="image1" width="200" height="200">
<img src="{filename}/images/cv/stacked-attention-network/figure10.png" alt="image1" title="image1" width="200" height="200">
<img src="{filename}/images/cv/stacked-attention-network/figure11.png" alt="image1" title="image1" width="200" height="200">

人間を除く全ての比較対象と比べ提案手法が一番精度が良かった。

## 5. 議論はあるか？
image captioningやmultimoda NMTの領域にstacked attentionを適用するのも良さそう。


<img src="{filename}/images/cv/stacked-attention-network/figure14.png" alt="image1" title="image1" width="200" height="200">

解答に失敗した例を見るとほとんどの場合、質問文に対するvisual attentionの画像内領域は正しい。


<img src="{filename}/images/cv/stacked-attention-network/figure15.png" alt="image1" title="image1" width="200" height="200">


### 論文情報・リンク

- ["Zichao Yang, Xiaodong He, Jianfeng Gao, Li Deng, Alex Smola"，"Stacked Attention Networks for Image Question Answering"，"CoRR"，2015](https://arxiv.org/pdf/1511.02274.pdf)
