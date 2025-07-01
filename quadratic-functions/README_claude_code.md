# 🎯 Gemini Code Interactive: 一次関数 vs 二次関数教材

Gemini AIと統合した高度な一次関数・二次関数学習システムです。鉄球の運動を通して関数の違いを視覚的・対話的に学習できます。

## ✨ 特徴

### 🚀 Gemini Code統合
- **自然言語対話**: 関数について自由に質問
- **個別指導**: 学習者のレベルに応じた解説
- **リアルタイム解析**: パラメータ変更時の即座な説明
- **学習進捗分析**: 理解度の自動評価と提案

### 📊 高度な可視化
- **4分割分析**: 関数・速度・加速度・データ比較
- **3D軌跡表示**: 運動の立体的理解
- **インタラクティブ操作**: リアルタイムパラメータ調整
- **美しいデザイン**: 現代的で直感的なUI

### 🎮 インタラクティブ機能
- **Jupyter ウィジェット**: スライダーによる直感的操作
- **複数シナリオ**: 様々な物理状況の比較
- **数値分析**: 詳細な計算結果の表示
- **物理的洞察**: 運動の意味の深い理解

## 📋 ファイル構成

```
二次関数/
├── 🎯 Gemini Code関連
│   ├── quadratic_functions_interactive.py    # メインクラス
│   ├── claude_code_demo.py                   # デモスクリプト（Gemini対応）
│   ├── interactive_functions_notebook.ipynb  # Jupyter教材
│   └── requirements_advanced.txt             # 高度な依存関係
│
├── 🌐 Web版（Gemini対応）
│   ├── app.py                               # Flask アプリ
│   ├── templates/index.html                 # Web UI
│   └── requirements.txt                     # 基本依存関係
│
├── 📚 ドキュメント
│   ├── README.md                           # 基本README
│   ├── README_claude_code.md               # このファイル
│   ├── setup_guide.md                      # セットアップガイド
│   └── env_example.txt                     # 環境変数例
│
└── 🛠️ ユーティリティ
    ├── demo.py                             # 基本デモ
    └── learning_progress.json             # 学習進捗データ
```

## 🚀 クイックスタート

### 1. 環境準備

```bash
# リポジトリクローン
cd 二次関数

# 仮想環境作成
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 高度な依存関係インストール
pip install -r requirements_advanced.txt
```

### 2. Gemini API設定

```bash
# Google AI StudioでAPIキー取得
# https://makersuite.google.com/app/apikey

# 環境変数設定
cp env_example.txt .env
# .envファイルを編集してAPIキーを設定
```

### 3. Gemini Code デモ実行

```bash
# デモスクリプト実行
python claude_code_demo.py  # ファイル名はそのまま（Gemini対応済み）
```

### 4. Jupyter Notebook教材

```bash
# Jupyter Lab起動
jupyter lab

# interactive_functions_notebook.ipynb を開く
```

### 5. Web版（オプション）

```bash
# Web版アプリ起動
python app.py
# ブラウザで http://localhost:5000 にアクセス
```

## 🔧 高度な機能

### Gemini AI統合

```python
# Gemini APIの設定
# .env ファイルに設定
GEMINI_API_KEY=your_gemini_api_key_here
```

### カスタマイズ

```python
# Gemini AIモデルの変更
model = genai.GenerativeModel('gemini-1.5-pro')  # より高性能なモデル

# プロンプトのカスタマイズ
system_prompt = """
あなたは高校数学の専門教師です。
微分積分の概念も含めて詳しく解説してください。
"""
```

### 学習データ分析

```python
# 学習進捗の詳細分析
with open('gemini_code_session_report.json') as f:
    data = json.load(f)
    
# 理解度の可視化
# 学習時間の追跡
# 弱点分野の特定
```

## 📊 使用例

### 基本的な使用

```python
from quadratic_functions_interactive import QuadraticFunctionLearning

# 学習システム初期化
learner = QuadraticFunctionLearning()

# 理論説明
learner.theory_explanation()

# インタラクティブ探索
interactive_widget = learner.interactive_widget()
display(interactive_widget)

# 運動分析
motion_fig = learner.motion_analysis()
motion_fig.show()

# Gemini AIに質問
response = learner.ask_gemini_ai("二次関数の頂点の求め方を教えてください")
print(response)
```

### 高度な分析

```python
# 比較分析の実行
comparison_data = learner.comparative_analysis()

# 物理問題の生成
learner.physics_problem_generator()

# 学習進捗の保存
learner.save_learning_progress("関数基礎", 8, "理解度良好")
```

## 🎯 学習目標

### 初級レベル
- ✅ 一次関数と二次関数の基本概念理解
- ✅ グラフの形状の違いを視覚的に把握
- ✅ 物理的意味（等速・等加速度）の理解

### 中級レベル
- ✅ 微分の概念（速度・加速度）の理解
- ✅ 実生活での応用例の把握
- ✅ 数値的分析手法の習得

### 上級レベル
- ✅ 最適化問題への応用
- ✅ 複雑な物理現象の数学的モデリング
- ✅ Gemini AIとの対話的学習の活用

## 🔍 トラブルシューティング

### よくある問題

1. **Gemini API接続エラー**
   ```bash
   # APIキーの確認
   echo $GEMINI_API_KEY
   
   # .envファイルの確認
   cat .env
   
   # デモモードでの実行（APIキー不要）
   python claude_code_demo.py
   ```

2. **Jupyter ウィジェットが表示されない**
   ```bash
   jupyter nbextension enable --py widgetsnbextension
   jupyter labextension install @jupyter-widgets/jupyterlab-manager
   ```

3. **日本語フォントが表示されない**
   ```python
   # システムフォントの確認
   import matplotlib.font_manager as fm
   [f.name for f in fm.fontManager.ttflist if 'Gothic' in f.name]
   ```

## 🔄 Claude → Gemini 移行ガイド

### 主な変更点

1. **API依存関係**
   ```bash
   # 旧: anthropic>=0.7.0
   # 新: google-generativeai>=0.3.0
   ```

2. **APIキー設定**
   ```bash
   # 旧: ANTHROPIC_API_KEY
   # 新: GEMINI_API_KEY
   ```

3. **API呼び出し**
   ```python
   # 旧: client.messages.create()
   # 新: model.generate_content()
   ```

### 移行手順

1. 新しい依存関係をインストール
2. Gemini APIキーを取得・設定
3. アプリケーションを再起動
4. 動作確認

## 🤝 貢献・カスタマイズ

### 新機能の追加

```python
# 新しいGeminiモデルの利用
def use_advanced_gemini():
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    # より高度な数学解析機能
```

### Gemini AI プロンプトのカスタマイズ

```python
# カスタム解説プロンプト
custom_prompt = """
あなたは数学教師です。高校生に以下の内容を説明してください：
{topic}

以下の点を含めてください：
1. 基本概念と定義
2. グラフの特徴
3. 実生活での応用例
4. 練習問題
5. よくある間違いと対策
"""
```

## 📈 今後の発展

### 計画中の機能
- 🌟 Gemini Pro Vision対応（グラフ画像解析）
- 🎨 マルチモーダル学習
- 📱 モバイル最適化
- 🔄 リアルタイム協調学習
- 🧠 Gemini AI学習分析の高度化

### 拡張可能性
- 三次関数・指数関数への拡張
- 微分積分の基礎教材
- 統計・確率分野への応用
- 大学レベル数学への発展

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🙏 謝辞

- **Google Gemini AI**: 自然言語処理と教育的解説
- **Plotly**: 美しいインタラクティブ可視化
- **Jupyter**: 優れたノートブック環境
- **教育現場の皆様**: 実用的なフィードバック

---

## 🎉 さあ、始めましょう！

```bash
# 今すぐ体験
python claude_code_demo.py

# または Jupyter で
jupyter lab interactive_functions_notebook.ipynb
```

**Gemini Code Interactive で、数学学習の新しい世界を体験してください！** 