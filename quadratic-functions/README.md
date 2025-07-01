# 📊 二次関数インタラクティブ教材

高校数学の二次関数を視覚的・インタラクティブに学習できる教材です。グラフと式の関係をリアルタイムで確認し、パラメータの変化による影響を直感的に理解できます。

## ✨ 特徴

- 📈 **リアルタイムグラフ**: パラメータ変更と同時にグラフが更新
- 🎯 **インタラクティブ操作**: スライダーやボタンで直感的に操作
- 📚 **段階的学習**: 基礎から応用まで段階的な学習コース
- 💡 **即座のフィードバック**: 操作結果を即座に視覚化
- 🎨 **美しい可視化**: Plotlyによる高品質なグラフ表示
- 📱 **レスポンシブ対応**: PC・タブレット・スマートフォン対応

## 🚀 セットアップ

### 前提条件
- Python 3.8以上
- Webブラウザ（Chrome, Firefox, Safari等）

### 1. 依存関係のインストール

```bash
# 仮想環境の作成（推奨）
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 依存パッケージのインストール
pip install -r requirements.txt
```

### 2. Streamlitアプリの起動

```bash
# メインアプリの起動
streamlit run app.py

# ブラウザが自動で開かない場合
# http://localhost:8501 にアクセス
```

### 3. Jupyter Notebook での利用

```bash
# Jupyter Notebook の起動
jupyter notebook interactive_functions_notebook.ipynb

# または Jupyter Lab
jupyter lab interactive_functions_notebook.ipynb
```

## 📖 使い方

### 基本的な学習フロー

1. **基本形の理解**: y = ax² の形でaの値を変更
2. **平行移動**: y = a(x-p)² + q で頂点の移動を確認
3. **一般形**: y = ax² + bx + c での係数の影響
4. **実践問題**: 与えられた条件からグラフを作成

### 操作方法

#### パラメータ調整
```python
# aの値: グラフの開き方
a_value = st.slider("aの値", -5.0, 5.0, 1.0, 0.1)

# 頂点座標: グラフの位置
vertex_x = st.slider("頂点のx座標", -10.0, 10.0, 0.0, 0.5)
vertex_y = st.slider("頂点のy座標", -10.0, 10.0, 0.0, 0.5)
```

#### グラフの表示範囲設定
```python
# x軸の範囲
x_min, x_max = st.slider("x軸の範囲", -20, 20, (-10, 10))

# y軸の範囲  
y_min, y_max = st.slider("y軸の範囲", -20, 20, (-10, 10))
```

## 📁 ファイル構成

```
quadratic-functions/
├── app.py                              # メインStreamlitアプリ
├── quadratic_functions_interactive.py  # インタラクティブ関数モジュール
├── interactive_functions_notebook.ipynb # Jupyter Notebook版
├── demo.py                             # 簡単なデモ版
├── claude_code_demo.py                 # Claude Code連携デモ
├── requirements.txt                    # Python依存関係
├── requirements_advanced.txt           # 高度な機能用依存関係
├── templates/                          # HTMLテンプレート
│   └── index.html                      # Webアプリ用HTML
├── docs/                              # ドキュメント
│   ├── setup_guide.md                 # セットアップガイド
│   ├── README_claude_code.md          # Claude Code連携ガイド
│   └── session_reports/               # セッション記録
├── venv/                              # Python仮想環境
└── README.md                          # このファイル
```

## 🎓 学習内容

### 1. 二次関数の基本形

```python
def basic_quadratic(x, a):
    """基本形: y = ax²"""
    return a * x**2
```

**学習ポイント:**
- aの符号によるグラフの向き
- |a|の大きさとグラフの開き方
- 頂点は常に原点(0, 0)

### 2. 頂点形式

```python
def vertex_form(x, a, h, k):
    """頂点形式: y = a(x-h)² + k"""
    return a * (x - h)**2 + k
```

**学習ポイント:**
- 頂点座標(h, k)の意味
- x軸・y軸方向への平行移動
- 対称軸の方程式: x = h

### 3. 一般形式

```python
def general_form(x, a, b, c):
    """一般形式: y = ax² + bx + c"""
    return a * x**2 + b * x + c
```

**学習ポイント:**
- 係数a, b, cの役割
- 頂点座標の求め方: (-b/2a, -b²+4ac/4a)
- y切片: (0, c)

### 4. 因数分解形式

```python
def factored_form(x, a, r1, r2):
    """因数分解形式: y = a(x-r1)(x-r2)"""
    return a * (x - r1) * (x - r2)
```

**学習ポイント:**
- x切片r1, r2の意味
- 軸の対称性: x = (r1+r2)/2
- 判別式との関係

## 🔧 高度な機能

### 複数の関数の比較

```python
def compare_functions():
    """複数の二次関数を同時表示"""
    st.subheader("複数の関数を比較")
    
    # 関数1の設定
    with st.expander("関数1の設定"):
        a1 = st.slider("a1", -5.0, 5.0, 1.0, 0.1, key="a1")
        h1 = st.slider("h1", -10.0, 10.0, 0.0, 0.5, key="h1")
        k1 = st.slider("k1", -10.0, 10.0, 0.0, 0.5, key="k1")
    
    # 関数2の設定
    with st.expander("関数2の設定"):
        a2 = st.slider("a2", -5.0, 5.0, 1.0, 0.1, key="a2")
        h2 = st.slider("h2", -10.0, 10.0, 0.0, 0.5, key="h2")
        k2 = st.slider("k2", -10.0, 10.0, 0.0, 0.5, key="k2")
    
    # グラフ描画
    plot_multiple_functions([
        (a1, h1, k1, "関数1"),
        (a2, h2, k2, "関数2")
    ])
```

### アニメーション機能

```python
def animated_transformation():
    """パラメータ変化のアニメーション"""
    if st.button("アニメーション開始"):
        frames = []
        for t in np.linspace(0, 2*np.pi, 60):
            a = 1 + np.sin(t)
            h = 2 * np.cos(t)
            k = np.sin(2*t)
            
            frame = create_frame(a, h, k, t)
            frames.append(frame)
        
        # アニメーショングラフの作成
        fig = go.Figure(
            data=frames[0]['data'],
            frames=frames
        )
        
        # 再生ボタンの追加
        fig.update_layout(
            updatemenus=[{
                'type': 'buttons',
                'showactive': False,
                'buttons': [
                    {'label': '▶️', 'method': 'animate', 'args': [None]},
                    {'label': '⏸️', 'method': 'animate', 'args': [[None], {'mode': 'immediate'}]}
                ]
            }]
        )
        
        st.plotly_chart(fig, use_container_width=True)
```

### 練習問題モード

```python
def practice_mode():
    """練習問題とクイズ機能"""
    st.subheader("🧩 練習問題")
    
    # 問題データベース
    problems = [
        {
            'question': '頂点が(2, -3)で、点(0, 1)を通る二次関数を求めよ',
            'answer_a': 1,
            'answer_h': 2, 
            'answer_k': -3,
            'explanation': 'y = a(x-2)² - 3 に (0,1) を代入して a を求める'
        }
    ]
    
    # ランダムに問題を選択
    problem = random.choice(problems)
    st.write(f"**問題:** {problem['question']}")
    
    # 解答入力
    user_a = st.number_input("aの値", value=1.0)
    user_h = st.number_input("hの値", value=0.0)
    user_k = st.number_input("kの値", value=0.0)
    
    if st.button("解答チェック"):
        if (abs(user_a - problem['answer_a']) < 0.1 and
            abs(user_h - problem['answer_h']) < 0.1 and
            abs(user_k - problem['answer_k']) < 0.1):
            st.success("🎉 正解です！")
        else:
            st.error("❌ 不正解です。もう一度挑戦してみましょう。")
            st.info(f"ヒント: {problem['explanation']}")
```

## 📊 学習分析機能

### 操作ログの記録

```python
def log_interaction(action, parameters):
    """学習者の操作を記録"""
    log_entry = {
        'timestamp': datetime.now(),
        'action': action,
        'parameters': parameters,
        'session_id': st.session_state.session_id
    }
    
    # セッションステートに保存
    if 'interaction_log' not in st.session_state:
        st.session_state.interaction_log = []
    
    st.session_state.interaction_log.append(log_entry)
```

### 学習進捗の可視化

```python
def show_learning_progress():
    """学習進捗の表示"""
    if 'interaction_log' in st.session_state:
        logs = st.session_state.interaction_log
        
        # 操作回数の集計
        action_counts = {}
        for log in logs:
            action = log['action']
            action_counts[action] = action_counts.get(action, 0) + 1
        
        # グラフで表示
        fig = px.bar(
            x=list(action_counts.keys()),
            y=list(action_counts.values()),
            title="操作回数の統計"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # 学習時間の表示
        if logs:
            start_time = logs[0]['timestamp']
            end_time = logs[-1]['timestamp']
            duration = end_time - start_time
            st.metric("学習時間", f"{duration.seconds // 60}分{duration.seconds % 60}秒")
```

## 🎨 カスタマイズ

### テーマの変更

```python
# カラーテーマの設定
THEMES = {
    'default': {
        'background': '#ffffff',
        'grid': '#f0f0f0',
        'line': '#1f77b4'
    },
    'dark': {
        'background': '#2f2f2f',
        'grid': '#555555', 
        'line': '#ff7f0e'
    },
    'colorful': {
        'background': '#fafafa',
        'grid': '#e0e0e0',
        'line': '#ff6b6b'
    }
}

def apply_theme(fig, theme_name):
    """指定されたテーマを適用"""
    theme = THEMES.get(theme_name, THEMES['default'])
    
    fig.update_layout(
        plot_bgcolor=theme['background'],
        paper_bgcolor=theme['background']
    )
    
    fig.update_xaxes(gridcolor=theme['grid'])
    fig.update_yaxes(gridcolor=theme['grid'])
    
    return fig
```

### 新しい関数の追加

```python
def cubic_function(x, a, b, c, d):
    """三次関数: y = ax³ + bx² + cx + d"""
    return a * x**3 + b * x**2 + c * x + d

def exponential_function(x, a, b):
    """指数関数: y = ab^x"""
    return a * (b ** x)

def trigonometric_function(x, a, b, c):
    """三角関数: y = a*sin(bx + c)"""
    return a * np.sin(b * x + c)
```

## 📱 モバイル対応

### レスポンシブレイアウト

```python
def get_device_config():
    """デバイスに応じた設定を取得"""
    # ユーザーエージェントの判定（簡易版）
    user_agent = st.experimental_get_query_params().get('user_agent', [''])[0]
    
    if 'Mobile' in user_agent:
        return {
            'slider_step': 0.5,  # モバイルでは大きめのステップ
            'plot_height': 400,  # 縦向き画面対応
            'sidebar_width': 'auto'
        }
    else:
        return {
            'slider_step': 0.1,
            'plot_height': 600,
            'sidebar_width': 300
        }
```

### タッチ操作の最適化

```python
def create_mobile_friendly_plot(fig):
    """モバイル向けプロット設定"""
    fig.update_layout(
        # タッチ操作しやすいマージン
        margin=dict(l=20, r=20, t=40, b=20),
        
        # ピンチズーム対応
        dragmode='pan',
        
        # ボタンサイズの調整
        font=dict(size=14),
        
        # グリッドを見やすく
        xaxis=dict(showgrid=True, gridwidth=2),
        yaxis=dict(showgrid=True, gridwidth=2)
    )
    
    return fig
```

## 🐛 トラブルシューティング

### よくある問題

#### 1. Streamlit が起動しない

```bash
# ポートが使用中の場合
streamlit run app.py --server.port 8502

# 仮想環境の確認
which python
pip list | grep streamlit
```

#### 2. グラフが表示されない

```python
# Plotlyのバージョン確認
import plotly
print(plotly.__version__)

# ブラウザのJavaScriptエラーを確認
# 開発者ツール > Console
```

#### 3. 計算が重い場合

```python
# 計算点数を減らす
x = np.linspace(-10, 10, 100)  # 400 → 100に削減

# キャッシュの活用
@st.cache_data
def calculate_function_values(a, h, k, x_min, x_max):
    x = np.linspace(x_min, x_max, 200)
    y = a * (x - h)**2 + k
    return x, y
```

## 📈 今後の拡張予定

- [ ] 3D関数グラフの表示
- [ ] 音声読み上げ機能
- [ ] 多言語対応（英語、中国語）
- [ ] VR/AR対応
- [ ] 協調学習機能（複数人同時操作）
- [ ] 学習管理システム（LMS）連携

## 🤝 貢献

新しい機能や改善案をお待ちしています！

## 📄 ライセンス

MIT License - 教育利用歓迎

---

[← メインリポジトリに戻る](../) 