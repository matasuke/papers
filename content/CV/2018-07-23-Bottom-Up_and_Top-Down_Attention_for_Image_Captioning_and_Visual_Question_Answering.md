Title: Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering
Date: 2018-07-23
Category: CV
Tags: IDG, VQA, CVPR2018
Author: Kosuke Futamata
Summary:

## 1. どんなもの？
物体検出によるbottom-up attentionと重み付き平均を用いたtop-down attentionの両方を組み合わせることにより，Image CaptioningとVisual Question Answeringの両方のタスクにおいてSOTAを達成．

![image1]({filename}/images/cv/bottom-up_and_top-down/figure1.png)

## 2. 先行研究と比べてどこがすごいの？
従来のImage captioningやVideo Question Answeringのタスクではほとんどの場合，逐次生成されるキャプションの結果や質問と画像のpixel wise feature vectorによる重み付き平均によるtop-down型のvisual attentionを用いる．
一方で本研究では，画像のpixel wise feature vectoreではなく，Faster R-CNNなどの物体検出アルゴリズムを用いたbottom-up attentionの出力結果に対してtop-down attentionを適用している．

## 3. 技術や手法の"キモ"はどこにある？
bottom-up attentionの出力結果をtop-down attentionに適用している．
物体検出アルゴリズムとして知られるFaster R-CNNの出力結果である部分画像に対してmean-pooled convolutionを適用したfeature vectoresに対してattentionを貼る．
さらに，これらfeature vectoresの平均を取ったのをNetworkの入力として用いる．

![image2]({filename}/images/cv/bottom-up_and_top-down/figure2.png)


bottom-up attentionを用いる以外はImage Captioning及びVisual Question AnsweringのNetworksに変わった構造は見られない．

![image2]({filename}/images/cv/bottom-up_and_top-down/figure3.png)

![image2]({filename}/images/cv/bottom-up_and_top-down/figure4.png)


## 4. どうやって有効だと検証した？

### データセット
- Visual Genome
- MSCOCO
- VQA v2.0

### 比較対象

### Image Captioning
- SCST(SOTAだったモデル)
- ResNet(提案手法のbottom-up attentionをResNetに置換)
- up-down(bottom-up and top-down approach)

ResNetはvisual attentionにResNet101を用いて，最終層のconv layerの出力を10\*10にリサイズ．
通常のvisual attentionと同様に，pixel-wiseのfeature vectorに対してattentionを貼る．

### 評価

- BLEU, METEOR, ROUGE-L, CIEDErは高いほど良い，
- SPICEは小さいほど良い．

![image5]({filename}/images/cv/bottom-up_and_top-down/figure5.png)

![image6]({filename}/images/cv/bottom-up_and_top-down/figure6.png)

Image Captioningのタスクでは全ての評価指標において，現SOTAのモデルを上回った．
VQAのタスクでは，2017 VQA challengeに投稿された全てのモデルを上回る正解率であった．

## 5. 議論はあるか？

![image5]({filename}/images/cv/bottom-up_and_top-down/figure7.png)

![image5]({filename}/images/cv/bottom-up_and_top-down/figure8.png)

## 6. 次に読むべき論文はあるか？
- ['Damien Teney, Peter Anderson, Xiaodong He, Anton van den Hengel', "Tips and Tricks for Visual Question Answering: Learnings from the 2017 Challenge",'2017 VQA Challenge'](https://arxiv.org/pdf/1708.02711.pdf)
- ['S. Ren, K. He, R. Girshick, and J. Sun', 'Faster R-CNN: Towards real-time object detection with region proposal networks', 'NIPS 2015'](https://arxiv.org/pdf/1506.01497.pdf)
- ['V. Kazemi and A. Elqursh', 'Show, ask, attend, and answer: A
strong baseline for visual question answering.'](https://arxiv.org/pdf/1704.03162.pdf)

### 論文情報・リンク

- ["Peter Anderson, Xiaodong He, Chris Buehler, Damien Teney, Mark Johnson, Stephen Gould, Lei Zhang"，"Bottom-Up and Top-Down Attention for Image Captioning
and Visual Question Answering"，"CVPR 2018"，2018](http://www.panderson.me/images/1707.07998-up-down.pdf)
