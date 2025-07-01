# 📖 tekitoo-teaching-materials

インタラクティブ教材集です。数学、プログラミング、科学分野でのデジタル教材を通じて、学習者の理解を深め、教師の授業準備を効率化します。

## 📋 収録教材

### 📊 [二次関数インタラクティブ教材](./quadratic-functions/)
グラフと式の関係を視覚的に学習
- **対象**: 高校数学（数学I・II）
- **特徴**: リアルタイムグラフ描画、パラメータ操作、練習問題
- **技術**: Python, Plotly, Streamlit, Jupyter Notebook

### 🧮 [AI数学問題生成システム](./ai-math-generator/)
個別最適化された数学問題の自動生成
- **対象**: 中学・高校数学全般
- **特徴**: 難易度調整、解法ヒント、進捗管理
- **技術**: React, Node.js, TypeScript, AI API

## 🚀 クイックスタート

各教材は独立して動作します。使いたい教材のディレクトリに移動して、個別のREADMEを参照してください。

```bash
# リポジトリのクローン
git clone https://github.com/tekitoo7777/tekitoo-teaching-materials.git
cd tekitoo-teaching-materials

# 使いたい教材のディレクトリに移動
cd quadratic-functions  # 例：二次関数教材
```

## 🎯 対象学習者

### 生徒・学生
- 中学生（数学基礎）
- 高校生（数学I〜III、情報）
- 大学生（数学基礎、プログラミング入門）

### 教師・講師
- 中学・高校数学教師
- 塾講師・予備校講師
- 大学教員・研究者
- プログラミング教育関係者

## 🌟 各教材の特色

| 教材 | 学習効果 | 準備時間 | 対話性 | 技術難易度 |
|------|----------|----------|--------|------------|
| 二次関数 | ⭐⭐⭐⭐⭐ | 5分 | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| AI数学問題 | ⭐⭐⭐⭐⭐ | 10分 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## 🛠️ 技術スタック

### 📊 データ可視化
- **Plotly**: インタラクティブグラフ
- **Matplotlib**: 静的・アニメーショングラフ
- **D3.js**: カスタムビジュアライゼーション
- **Chart.js**: 軽量チャート

### 🖥 フロントエンド
- **React**: モダンUIフレームワーク
- **Streamlit**: Python Webアプリ
- **Jupyter Notebook**: 教育用ノートブック
- **HTML5/CSS3**: 軽量Webアプリ

### ⚙️ バックエンド
- **Node.js**: JavaScript実行環境
- **Python Flask**: 軽量Webフレームワーク
- **TypeScript**: 型安全な開発
- **FastAPI**: 高速API開発

### 🧮 数学・計算
- **NumPy**: 数値計算ライブラリ
- **SymPy**: 数式処理システム
- **SciPy**: 科学計算ライブラリ
- **Pandas**: データ解析

### 🤖 AI・機械学習
- **OpenAI API**: 問題生成・解説作成
- **Anthropic Claude**: 数学的推論
- **Local LLM**: プライバシー重視の処理
- **Scikit-learn**: 学習分析

## 📱 デモサイト

各教材のライブデモは GitHub Pages で公開予定です：
- 二次関数教材: [デモサイト](https://tekitoo7777.github.io/tekitoo-teaching-materials/quadratic-functions/)
- AI数学問題: [デモサイト](https://tekitoo7777.github.io/tekitoo-teaching-materials/ai-math-generator/)

## 🎓 教育効果・活用例

### 📈 学習効果の向上
- **視覚的理解**: 抽象的概念を具体的に表示
- **試行錯誤**: パラメータ変更による即座のフィードバック
- **個別学習**: 学習者のペースに合わせた進行
- **興味喚起**: インタラクティブな操作で飽きさせない

### 👨‍🏫 授業での活用
```markdown
## 二次関数の授業例（50分）

### 導入（10分）
- 教材を使ったグラフ表示
- パラメータaの変化の観察

### 展開（25分）
- 生徒個別での操作・探究
- グループでの発見の共有

### まとめ（15分）
- 法則性の整理・確認
- 練習問題の解法
```

### 🏠 家庭学習での利用
- 復習用のセルフチェック
- 予習での概念理解
- 定期テスト対策
- 受験勉強の効率化

## 🔧 カスタマイズ・拡張

### 問題レベルの調整

```python
# 難易度設定例
DIFFICULTY_SETTINGS = {
    'beginner': {
        'a_range': (-3, 3),
        'vertex_range': (-5, 5),
        'hints': True
    },
    'advanced': {
        'a_range': (-10, 10),
        'vertex_range': (-20, 20),
        'hints': False
    }
}
```

### 新しい関数の追加

```python
# 三次関数の追加例
def cubic_function(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

def plot_cubic(a, b, c, d):
    x = np.linspace(-10, 10, 400)
    y = cubic_function(x, a, b, c, d)
    # プロット処理
```

### 言語の多言語化

```json
{
  "ja": {
    "title": "二次関数のグラフ",
    "parameter_a": "aの値",
    "vertex": "頂点"
  },
  "en": {
    "title": "Quadratic Function Graph",
    "parameter_a": "Value of a",
    "vertex": "Vertex"
  }
}
```

## 📊 学習分析・効果測定

### 学習ログの収集

```python
def log_interaction(user_id, action, parameters, timestamp):
    """学習者の操作ログを記録"""
    log_data = {
        'user_id': user_id,
        'action': action,
        'parameters': parameters,
        'timestamp': timestamp,
        'session_id': get_session_id()
    }
    save_to_database(log_data)
```

### 理解度の可視化

```python
def analyze_learning_progress(user_id):
    """学習進捗の分析・可視化"""
    logs = get_user_logs(user_id)
    
    # 操作パターンの分析
    interaction_patterns = analyze_patterns(logs)
    
    # 理解度スコアの算出
    comprehension_score = calculate_score(logs)
    
    # 推奨学習プランの生成
    recommended_plan = generate_plan(comprehension_score)
    
    return {
        'patterns': interaction_patterns,
        'score': comprehension_score,
        'plan': recommended_plan
    }
```

## 🔒 プライバシー・セキュリティ

### 学習データの保護
- ローカル実行によるプライバシー保護
- 匿名化された学習ログ
- GDPR準拠のデータ処理
- 保護者同意機能（未成年者向け）

### セキュアな運用
- HTTPS通信の強制
- XSS・CSRF対策
- 入力値の検証・サニタイズ
- 定期的なセキュリティ監査

## 📈 今後の拡張予定

### 教科・分野の拡大
- [ ] 物理学（力学、電磁気学）
- [ ] 化学（分子構造、反応式）
- [ ] 生物学（遺伝、生態系）
- [ ] 地学（天体運動、地質）
- [ ] 情報科学（アルゴリズム、データ構造）

### 技術的機能強化
- [ ] VR/AR対応（3次元可視化）
- [ ] 音声入力・出力機能
- [ ] 手書き数式認識
- [ ] 協調学習機能（複数人同時操作）
- [ ] 適応学習システム（AI家庭教師）

### プラットフォーム対応
- [ ] モバイルアプリ版
- [ ] LMS統合（Moodle, Google Classroom）
- [ ] デスクトップアプリ版
- [ ] オフライン動作対応

## 📚 関連リソース

### 教育理論・手法
- **構成主義学習**: 学習者が能動的に知識を構築
- **発見学習**: 試行錯誤を通じた法則発見
- **視覚的学習**: グラフ・図形による理解促進
- **個別化学習**: 学習者のペースに合わせた進行

### 技術文献
- [Interactive Mathematics Visualization](https://example.com/math-viz)
- [Educational Technology Best Practices](https://example.com/edtech-practices)
- [Web-based Learning Analytics](https://example.com/learning-analytics)

## 🤝 コミュニティ・貢献

### 教材の改善提案
- 新しい問題・例題の追加
- UI/UX の改善アイデア
- バグ報告・修正提案
- パフォーマンス最適化

### 新教材の開発
- 担当教科・分野の専門知識
- プログラミング・Web開発スキル
- 教育現場での実践経験
- 学習者フィードバックの収集

### 教育実践での活用報告
- 授業での使用レポート
- 学習効果の測定結果
- 改善点・要望の共有
- 成功事例の紹介

## 💰 利用コスト

### 基本利用（無料）
- ローカル実行での教材利用
- 基本的な可視化機能
- 標準問題セット
- オープンソースライセンス

### 高度な機能（有料APIサービス）
- AI問題生成: ~$10/月（100問題）
- クラウド学習分析: ~$5/月（30ユーザー）
- 音声合成・認識: ~$15/月
- 高度なグラフィックス: ~$20/月

## 📄 ライセンス・利用規約

### オープンソース部分
- MIT License（基本教材・ツール）
- Apache 2.0 License（ライブラリ・フレームワーク）
- Creative Commons（教育コンテンツ）

### 商用利用について
- 教育機関での利用: 完全無料
- 営利企業での利用: ライセンス料要相談
- カスタマイズ・サポート: 有償対応可能

## 📞 お問い合わせ・サポート

### 技術的なサポート
- GitHub Issues: バグ報告・機能要望
- Discord Server: リアルタイム質問・交流
- メール: technical-support@example.com

### 教育的な相談
- 授業での活用方法
- 学習効果の測定
- カリキュラムへの組み込み
- 教員研修・ワークショップ

### 連絡先
- Twitter: [@tekitoo_t_cher](https://mobile.twitter.com/tekitoo_t_cher)
- Note: [tekitooooo](https://note.com/tekitooooo)
- Email: contact@example.com

---

**📖 知識の可視化で、学習をもっと楽しく、もっと深く！** 