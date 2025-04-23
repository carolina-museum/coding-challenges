# 思考ログ
392. Is Subsequence

### Step 1 - Pointerを使った解法
一番最初に思いついた解法です。

まず、sはtのsubsequenceなのであれば、sの長さがtの長さを超えることはありません。
このために、下記を最初に書きました：
```
if len(s) > len(t):
            return False
```

そして、sの文字を一文字ずつ見ていきます。
その文字がtに含まれるのかを確認しますが、t全体を見るのではなくて、一つ前のsの文字があった位置の次の位置からみていきます。最初はtの冒頭からみます。

計算量について：

時間計算量は、sとtをそれぞれ順に確認していくので、~~O(S+T)~~ O(T)です。（sの長さがS、tの長さがTとする）

二重ループではありますが、sのそれぞれの要素についてtの全ての要素を見て回るわけではなく、tを行き来することはないのでO(S*T)とは考えませんでした。

空間計算量は、ポインタを使っているだけなので、O(1)だと思います。


### Step 2
まずはEditorialを読みました。
Editorialで挙げられている解法は以下です：

Approach 1. Divide and Conquer with Greedy

前半の解説部分は私と同じ考えを再帰を使って説明しています。後半にはGreedyとありますが、これは一つずつ順番に前の文字に戻らずに確認していく様子がGreedyっぽいということだと思いました。

計算量についての記述でO(T)とあり、たしかにそうだなと、、SよりもTは大きいか同じなので、この場合の計算量の表記はTだけを残しますね。😣

ちなみに、、、
sとtはsourceとtargetの頭文字だったみたいです😳なるほど！


Approach 2. Two-Pointers

なんと私のStep 1での考えと同じです！嬉しい！再帰の方法よりも空間計算量が最適化されています。
while文で回しているのは私の実装と違います。勉強になります　φ(´ω`*)ﾒﾓﾒﾓ


Approach 3. Greedy Match with Character Indices Hashmap

follow-up questionに対応しています。

> Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

解説を読む前の私の考え：
- まず一番最初に思いつくのは、シンプルにsの数（k個）だけループする方法です。これはO(T*S)の時間計算量です。
- 次に、それぞれのsにポインタを作って、一回のループで全てtと確認していく方法です。これは、O(T+S*k)の時間計算量です。(自信なし)
- 他には、、、思いつきません、、、

なんとハッシュマップを使ってtに含まれる文字の位置を把握しておくみたいです！！！！天才！！！

メモ：二分探索の時に教わった関数がこの解法の実装に使われています：
```
match_index = bisect.bisect_right(indices_list, curr_match_index)
```

Approach 4: Dynamic Programming

まだある、、、深い問題です。動的計画法を使うみたいです。

DPテーブルを作って最終的にsの長さになれば、Trueということみたいです！
私はまだまだDPに慣れていないのでこうやって学んでいくのが大事ですね....練習します。

解説はここまで！次はこれらを実装してみます。
