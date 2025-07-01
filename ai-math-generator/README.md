# 🧮 AI数学問題生成システム

CursorAIと連携して数学問題を自動生成・評価する学習支援システムです。

## 🌟 主な機能

- **自動問題生成**: 算数、代数、幾何、微積分、統計の5分野で問題を自動生成
- **難易度選択**: 基礎、標準、応用の3段階から選択可能
- **LaTeX数式表示**: KaTeXを使用した美しい数式表示
- **リアルタイム採点**: 即座に答えを検証し、フィードバックを提供
- **学習進捗管理**: 正解率や解答数の追跡
- **レスポンシブデザイン**: デスクトップ・モバイル対応

## 🛠️ 技術スタック

### フロントエンド
- React 19 + TypeScript
- KaTeX (数式表示)
- CSS Grid Layout

### バックエンド
- Node.js + Express
- TypeScript
- Math.js (数式計算)

## 🚀 セットアップ

### 前提条件
- Node.js 18以上
- npm または yarn

### インストール

1. **プロジェクトのクローン**
```bash
git clone [repository-url]
cd studyaid
```

2. **バックエンドのセットアップ**
```bash
cd backend
npm install
npm run dev
```

3. **フロントエンドのセットアップ**
```bash
cd ../frontend
npm install
npm start
```

4. **アクセス**
- フロントエンド: http://localhost:3000
- バックエンドAPI: http://localhost:3001

## 📁 プロジェクト構造

```
studyaid/
├── frontend/                 # Reactフロントエンド
│   ├── src/
│   │   ├── components/      # Reactコンポーネント
│   │   │   ├── MathProblemGenerator.tsx
│   │   │   ├── ProblemDisplay.tsx
│   │   │   ├── AnswerInput.tsx
│   │   │   └── ScoreBoard.tsx
│   │   ├── App.tsx         # メインアプリケーション
│   │   └── App.css         # スタイルシート
│   └── package.json
├── backend/                 # Node.js API
│   ├── src/
│   │   ├── routes/         # APIルート
│   │   ├── services/       # ビジネスロジック
│   │   │   ├── mathProblemGenerator.ts
│   │   │   └── mathValidator.ts
│   │   └── server.ts       # サーバーエントリーポイント
│   ├── package.json
│   └── tsconfig.json
└── README.md
```

## 🔧 API エンドポイント

### 問題生成
```
POST /api/math-problems/generate
Content-Type: application/json

{
  "topic": "arithmetic",
  "difficulty": "基礎",
  "problemType": "加法"
}
```

### 答え検証
```
POST /api/math-problems/validate
Content-Type: application/json

{
  "problemId": "abc123",
  "userAnswer": "42",
  "correctAnswer": 42
}
```

### カテゴリ一覧
```
GET /api/math-problems/categories
```

## 📚 対応分野・問題タイプ

### 算数 (arithmetic)
- 加法、減法、乗法、除法

### 代数 (algebra)
- 一次方程式、二次方程式

### 幾何 (geometry)
- 面積、体積

### 微積分 (calculus)
- 微分、積分

### 統計 (statistics)
- 平均

## 🎯 使い方

1. **分野選択**: 左パネルで学習したい数学分野を選択
2. **難易度設定**: 基礎、標準、応用から適切な難易度を選択
3. **問題タイプ選択**: 具体的な問題タイプを選択
4. **問題生成**: 「問題を生成」ボタンをクリック
5. **解答**: 表示された問題に答えを入力
6. **確認**: 「答えを確認」ボタンで採点
7. **次の問題**: 解説を確認後、次の問題に進む

## 🤖 CursorAI連携

このプロジェクトはCursorAIと連携して以下の機能を提供：

- 自然言語による問題生成
- インテリジェントな難易度調整
- 個別学習者に最適化された問題選択
- 詳細な解説と学習ガイダンス

## 🧪 開発・テスト

### 開発サーバー起動
```bash
# バックエンド (ポート3001)
cd backend && npm run dev

# フロントエンド (ポート3000)
cd frontend && npm start
```

### ビルド
```bash
# バックエンド
cd backend && npm run build

# フロントエンド
cd frontend && npm run build
```

## 📈 今後の拡張予定

- [ ] 履歴機能
- [ ] 複数ユーザー対応
- [ ] 学習アナリティクス
- [ ] より多くの数学分野の追加
- [ ] AI による個別問題生成
- [ ] グラフ描画機能

## 🤝 貢献

プルリクエストや改善提案をお待ちしています！

## 📄 ライセンス

MIT License

---

Powered by CursorAI 🚀 