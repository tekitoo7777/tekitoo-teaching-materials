# 🚀 セットアップガイド

## 🎯 概要

一次関数と二次関数の違いを視覚的に学べるインタラクティブな教材です。
Claude AIを活用してリアルタイムで詳細な解説を生成します。

## 📋 必要な環境

- Python 3.8以上
- インターネット接続（Claude API使用時）
- モダンなWebブラウザ

## ⚡ クイックスタート

### 1. プロジェクトのダウンロード

```bash
# このプロジェクトをダウンロードまたはクローン
cd 二次関数
```

### 2. 仮想環境の作成と依存関係のインストール

```bash
# 仮想環境を作成
python3 -m venv venv

# 仮想環境をアクティベート
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate     # Windows

# 依存関係をインストール
pip install -r requirements.txt
```

### 3. デモモードでの実行

```bash
# システムテストの実行
python demo.py

# Webアプリケーションの起動
python app.py
```

ブラウザで http://localhost:5000 にアクセスして教材を使用できます。

## 🔑 Claude APIの設定（オプション）

Claude AIの詳細な解説機能を使用したい場合：

### 1. APIキーの取得

1. [Anthropic Console](https://console.anthropic.com/) にアクセス
2. アカウント作成またはログイン
3. APIキーを生成

### 2. 環境変数の設定

```bash
# env_example.txt を .env にコピー
cp env_example.txt .env

# .env ファイルを編集
# ANTHROPIC_API_KEY=your_actual_api_key_here
```

### 3. API機能付きで実行

```bash
# .env ファイルが設定されていれば自動的にClaude APIを使用
python app.py
```

## 🎮 使用方法

### 基本操作

1. **パラメータ調整**: 上部のスライダーで関数の係数を変更
2. **グラフ観察**: リアルタイムでグラフが更新される
3. **Claude解説**: パラメータに応じた詳細な解説を確認
4. **質問機能**: 疑問点をClaude AIに直接質問

### 学習ポイント

- **一次関数 (y = ax)**: 等速運動、直線グラフ、一定の変化率
- **二次関数 (y = ax²)**: 等加速度運動、曲線グラフ、増加する変化率

## 🔧 トラブルシューティング

### よくある問題

1. **依存関係のエラー**
   ```bash
   pip install --upgrade pip setuptools
   pip install -r requirements.txt
   ```

2. **Claude APIエラー**
   - APIキーが正しく設定されているか確認
   - インターネット接続を確認
   - デモモードでも基本機能は使用可能

3. **ポートが使用中**
   ```bash
   # 別のポートで起動
   python app.py
   # または app.py の最後の行を以下に変更
   # app.run(debug=True, port=5001)
   ```

## 📚 ファイル説明

- `app.py`: メインのWebアプリケーション
- `demo.py`: システムテスト用スクリプト
- `requirements.txt`: Python依存関係
- `templates/index.html`: Webページのテンプレート
- `env_example.txt`: 環境変数の例
- `README.md`: プロジェクト概要

## 🤝 カスタマイズ

### パラメータの調整

`app.py` の以下の部分を編集：

```python
# データポイントを変更
linear_points_x = [0, 1, 2, 3, 4, 5, 6]
linear_points_y = [0, 2, 4, 6, 8, 10, 12]

# グラフの範囲を変更
def generate_linear_data(a, x_max=6):  # x_maxを変更
```

### デザインの変更

`templates/index.html` のCSSセクションを編集して見た目をカスタマイズできます。

## 📞 サポート

質問やバグ報告がありましたら、プロジェクトの Issues セクションまでお願いします。 