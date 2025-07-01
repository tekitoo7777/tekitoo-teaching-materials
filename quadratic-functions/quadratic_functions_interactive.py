#!/usr/bin/env python3
"""
Gemini Code Interactive 一次関数・二次関数教材
高度な視覚化とインタラクティブ機能を提供
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display, HTML, Markdown
import seaborn as sns
from datetime import datetime
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

# 環境変数読み込み
load_dotenv()

# 日本語フォントの設定
plt.rcParams['font.family'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

# Gemini API設定
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    model = None

class QuadraticFunctionLearning:
    """一次関数・二次関数の包括的学習システム"""
    
    def __init__(self):
        self.learning_data = {
            'linear_experiments': [],
            'quadratic_experiments': [],
            'user_questions': [],
            'understanding_scores': []
        }
        self.setup_learning_environment()
    
    def setup_learning_environment(self):
        """学習環境の初期化"""
        print("🎯 Gemini Code Interactive 一次関数・二次関数教材")
        print("=" * 60)
        print("この教材では以下の内容を学習できます：")
        print("1. 📈 一次関数と二次関数の基本概念")
        print("2. 🎮 インタラクティブなパラメータ調整")
        print("3. 🔬 物理的意味の理解（等速・等加速度運動）")
        print("4. 📊 データ分析と予測")
        print("5. 🧮 実際の計算問題")
        print("6. 🤖 Gemini AIによる個別指導")
        print()
    
    def theory_explanation(self):
        """理論的説明セクション"""
        display(Markdown("""
        # 📚 理論的基礎
        
        ## 一次関数 y = ax + b
        
        - **定義**: xの1乗に比例する関数
        - **グラフ**: 直線
        - **物理的意味**: 等速運動（一定の速度）
        - **傾き**: a（変化率が一定）
        - **切片**: b（x=0での値）
        
        ## 二次関数 y = ax² + bx + c
        
        - **定義**: xの2乗を含む関数
        - **グラフ**: 放物線（パラボラ）
        - **物理的意味**: 等加速度運動（加速度が一定）
        - **頂点**: 最大値または最小値を持つ点
        - **軸**: 対称軸
        
        ## 実生活での例
        
        ### 一次関数の例
        - 🚗 高速道路での等速運動
        - 💰 時給制アルバイトの収入
        - 🌡️ 標高と気温の関係
        
        ### 二次関数の例
        - 🏀 ボールの軌道
        - 🚗 ブレーキ距離
        - 📈 利益の最大化問題
        """))
    
    def create_interactive_plot(self, linear_a=2, linear_b=0, quad_a=1, quad_b=0, quad_c=0, x_range=10):
        """インタラクティブなグラフ作成"""
        
        # データ生成
        x = np.linspace(-x_range/2, x_range/2, 1000)
        y_linear = linear_a * x + linear_b
        y_quad = quad_a * x**2 + quad_b * x + quad_c
        
        # Plotlyサブプロット
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('関数比較', '速度比較', '加速度比較', 'データ点プロット'),
            specs=[[{"secondary_y": True}, {"secondary_y": True}],
                   [{"secondary_y": True}, {"secondary_y": True}]]
        )
        
        # メインプロット：関数比較
        fig.add_trace(
            go.Scatter(x=x, y=y_linear, name=f'一次関数: y = {linear_a}x + {linear_b}',
                      line=dict(color='blue', width=3)),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(x=x, y=y_quad, name=f'二次関数: y = {quad_a}x² + {quad_b}x + {quad_c}',
                      line=dict(color='red', width=3)),
            row=1, col=1
        )
        
        # 速度比較（一階微分）
        v_linear = np.full_like(x, linear_a)  # 一次関数の微分は定数
        v_quad = 2 * quad_a * x + quad_b      # 二次関数の微分
        
        fig.add_trace(
            go.Scatter(x=x, y=v_linear, name='一次関数の速度（一定）',
                      line=dict(color='lightblue', dash='dash')),
            row=1, col=2
        )
        
        fig.add_trace(
            go.Scatter(x=x, y=v_quad, name='二次関数の速度（変化）',
                      line=dict(color='orange', dash='dash')),
            row=1, col=2
        )
        
        # 加速度比較（二階微分）
        a_linear = np.zeros_like(x)           # 一次関数の二階微分は0
        a_quad = np.full_like(x, 2 * quad_a)  # 二次関数の二階微分は定数
        
        fig.add_trace(
            go.Scatter(x=x, y=a_linear, name='一次関数の加速度（0）',
                      line=dict(color='lightgreen')),
            row=2, col=1
        )
        
        fig.add_trace(
            go.Scatter(x=x, y=a_quad, name='二次関数の加速度（一定）',
                      line=dict(color='purple')),
            row=2, col=1
        )
        
        # データ点（教材の表データ）
        data_x = np.array([0, 1, 2, 3, 4, 5, 6])
        data_y_linear = np.array([0, 2, 4, 6, 8, 10, 12])
        data_y_quad = np.array([0, 2, 8, 18, 32, 50, 72])
        
        fig.add_trace(
            go.Scatter(x=data_x, y=data_y_linear, mode='markers',
                      name='一次関数データ点', marker=dict(size=10, color='blue')),
            row=2, col=2
        )
        
        fig.add_trace(
            go.Scatter(x=data_x, y=data_y_quad, mode='markers',
                      name='二次関数データ点', marker=dict(size=10, color='red')),
            row=2, col=2
        )
        
        # レイアウト設定
        fig.update_layout(
            height=800,
            title_text="📊 一次関数 vs 二次関数：包括的分析",
            showlegend=True
        )
        
        # 軸ラベル
        fig.update_xaxes(title_text="時間 (秒)", row=1, col=1)
        fig.update_yaxes(title_text="距離 (m)", row=1, col=1)
        fig.update_xaxes(title_text="時間 (秒)", row=1, col=2)
        fig.update_yaxes(title_text="速度 (m/s)", row=1, col=2)
        fig.update_xaxes(title_text="時間 (秒)", row=2, col=1)
        fig.update_yaxes(title_text="加速度 (m/s²)", row=2, col=1)
        fig.update_xaxes(title_text="時間 (秒)", row=2, col=2)
        fig.update_yaxes(title_text="距離 (m)", row=2, col=2)
        
        return fig
    
    def interactive_widget(self):
        """インタラクティブウィジェット"""
        
        # パラメータスライダー
        linear_a_slider = widgets.FloatSlider(
            value=2.0, min=-5.0, max=5.0, step=0.1,
            description='一次 a:', style={'description_width': 'initial'}
        )
        
        linear_b_slider = widgets.FloatSlider(
            value=0.0, min=-10.0, max=10.0, step=0.5,
            description='一次 b:', style={'description_width': 'initial'}
        )
        
        quad_a_slider = widgets.FloatSlider(
            value=1.0, min=-3.0, max=3.0, step=0.1,
            description='二次 a:', style={'description_width': 'initial'}
        )
        
        quad_b_slider = widgets.FloatSlider(
            value=0.0, min=-5.0, max=5.0, step=0.1,
            description='二次 b:', style={'description_width': 'initial'}
        )
        
        quad_c_slider = widgets.FloatSlider(
            value=0.0, min=-10.0, max=10.0, step=0.5,
            description='二次 c:', style={'description_width': 'initial'}
        )
        
        x_range_slider = widgets.IntSlider(
            value=10, min=4, max=20, step=2,
            description='x範囲:', style={'description_width': 'initial'}
        )
        
        # インタラクティブ表示
        interactive_plot = interactive(
            self.create_interactive_plot,
            linear_a=linear_a_slider,
            linear_b=linear_b_slider,
            quad_a=quad_a_slider,
            quad_b=quad_b_slider,
            quad_c=quad_c_slider,
            x_range=x_range_slider
        )
        
        return interactive_plot
    
    def motion_analysis(self, initial_velocity=0, acceleration=2, time_max=6):
        """運動解析シミュレーション"""
        
        t = np.linspace(0, time_max, 100)
        
        # 等速運動（一次関数）
        v_constant = 2  # 一定速度
        x_linear = v_constant * t
        
        # 等加速度運動（二次関数）
        x_quad = initial_velocity * t + 0.5 * acceleration * t**2
        v_quad = initial_velocity + acceleration * t
        a_quad = np.full_like(t, acceleration)
        
        # 3Dプロット
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('位置-時間グラフ', '速度-時間グラフ', 
                          '加速度-時間グラフ', '3D軌跡'),
            specs=[[{}, {}], [{}, {"type": "scene"}]]
        )
        
        # 位置
        fig.add_trace(go.Scatter(x=t, y=x_linear, name='等速運動', 
                                line=dict(color='blue')), row=1, col=1)
        fig.add_trace(go.Scatter(x=t, y=x_quad, name='等加速度運動', 
                                line=dict(color='red')), row=1, col=1)
        
        # 速度
        fig.add_trace(go.Scatter(x=t, y=np.full_like(t, v_constant), 
                                name='等速運動の速度', line=dict(color='blue')), 
                     row=1, col=2)
        fig.add_trace(go.Scatter(x=t, y=v_quad, name='等加速度運動の速度', 
                                line=dict(color='red')), row=1, col=2)
        
        # 加速度
        fig.add_trace(go.Scatter(x=t, y=np.zeros_like(t), 
                                name='等速運動の加速度', line=dict(color='blue')), 
                     row=2, col=1)
        fig.add_trace(go.Scatter(x=t, y=a_quad, name='等加速度運動の加速度', 
                                line=dict(color='red')), row=2, col=1)
        
        # 3D軌跡
        fig.add_trace(go.Scatter3d(x=t, y=x_linear, z=np.full_like(t, v_constant),
                                  mode='lines', name='等速運動3D',
                                  line=dict(color='blue', width=6)), 
                     row=2, col=2)
        fig.add_trace(go.Scatter3d(x=t, y=x_quad, z=v_quad,
                                  mode='lines', name='等加速度運動3D',
                                  line=dict(color='red', width=6)), 
                     row=2, col=2)
        
        fig.update_layout(height=800, title_text="🚀 運動解析シミュレーション")
        
        return fig
    
    def physics_problem_generator(self):
        """物理問題生成器"""
        
        problems = [
            {
                "title": "🚗 自動車の等速運動",
                "description": "自動車が時速60kmで走行している。3時間後の移動距離は？",
                "function": "y = 60x",
                "answer": "180km",
                "explanation": "一次関数 y = 60x で、x=3を代入すると y = 180"
            },
            {
                "title": "🏀 ボールの放物運動",
                "description": "初速度20m/sで上向きに投げたボールの高さ（重力加速度g=10m/s²）",
                "function": "y = 20t - 5t²",
                "answer": "最高到達点：20m（t=2秒）",
                "explanation": "二次関数の頂点公式を使用。頂点のt座標は -b/2a = -20/(-10) = 2"
            },
            {
                "title": "💰 利益最大化問題",
                "description": "商品価格をx円とすると、利益がy = -2x² + 400x - 10000円。最大利益は？",
                "function": "y = -2x² + 400x - 10000",
                "answer": "最大利益：10000円（価格100円）",
                "explanation": "頂点のx座標：-400/(-4) = 100、y座標：-2(100)² + 400(100) - 10000 = 10000"
            }
        ]
        
        for i, problem in enumerate(problems, 1):
            display(Markdown(f"""
            ### 問題 {i}: {problem['title']}
            
            **問題**: {problem['description']}
            
            **関数**: `{problem['function']}`
            
            <details>
            <summary>💡 解答を見る</summary>
            
            **答え**: {problem['answer']}
            
            **解説**: {problem['explanation']}
            
            </details>
            """))
    
    def comparative_analysis(self):
        """比較分析"""
        
        # データフレーム作成
        x_vals = np.arange(0, 7)
        data = pd.DataFrame({
            '時間(秒)': x_vals,
            '一次関数(等速)': 2 * x_vals,
            '二次関数(加速)': 2 * x_vals**2,
            '一次関数_速度': [2] * len(x_vals),
            '二次関数_速度': 4 * x_vals
        })
        
        # 比較表
        display(Markdown("## 📊 数値比較表"))
        display(data[['時間(秒)', '一次関数(等速)', '二次関数(加速)']])
        
        # 差分分析
        data['距離の差'] = data['二次関数(加速)'] - data['一次関数(等速)']
        data['速度の差'] = data['二次関数_速度'] - data['一次関数_速度']
        
        # 可視化
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # 距離比較
        axes[0,0].plot(data['時間(秒)'], data['一次関数(等速)'], 'b-o', label='等速運動', linewidth=2)
        axes[0,0].plot(data['時間(秒)'], data['二次関数(加速)'], 'r-o', label='等加速度運動', linewidth=2)
        axes[0,0].set_title('距離比較')
        axes[0,0].set_xlabel('時間(秒)')
        axes[0,0].set_ylabel('距離(m)')
        axes[0,0].legend()
        axes[0,0].grid(True, alpha=0.3)
        
        # 速度比較
        axes[0,1].plot(data['時間(秒)'], data['一次関数_速度'], 'b-o', label='等速運動', linewidth=2)
        axes[0,1].plot(data['時間(秒)'], data['二次関数_速度'], 'r-o', label='等加速度運動', linewidth=2)
        axes[0,1].set_title('速度比較')
        axes[0,1].set_xlabel('時間(秒)')
        axes[0,1].set_ylabel('速度(m/s)')
        axes[0,1].legend()
        axes[0,1].grid(True, alpha=0.3)
        
        # 距離の差
        axes[1,0].bar(data['時間(秒)'], data['距離の差'], color='green', alpha=0.7)
        axes[1,0].set_title('距離の差（加速度運動 - 等速運動）')
        axes[1,0].set_xlabel('時間(秒)')
        axes[1,0].set_ylabel('距離の差(m)')
        axes[1,0].grid(True, alpha=0.3)
        
        # 速度の差
        axes[1,1].bar(data['時間(秒)'], data['速度の差'], color='orange', alpha=0.7)
        axes[1,1].set_title('速度の差（加速度運動 - 等速運動）')
        axes[1,1].set_xlabel('時間(秒)')
        axes[1,1].set_ylabel('速度の差(m/s)')
        axes[1,1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        return data
    
    def save_learning_progress(self, topic, score, notes=""):
        """学習進捗の保存"""
        
        progress_entry = {
            'timestamp': datetime.now().isoformat(),
            'topic': topic,
            'score': score,
            'notes': notes
        }
        
        self.learning_data['understanding_scores'].append(progress_entry)
        
        # JSONファイルに保存
        with open('learning_progress.json', 'w', encoding='utf-8') as f:
            json.dump(self.learning_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 学習進捗を保存しました: {topic} (スコア: {score}/10)")
    
    def generate_quiz(self):
        """クイズ生成"""
        
        questions = [
            {
                "question": "一次関数 y = 3x において、x = 4 のときの y の値は？",
                "options": ["10", "12", "15", "16"],
                "correct": 1,
                "explanation": "y = 3 × 4 = 12"
            },
            {
                "question": "二次関数 y = x² - 4x + 3 の頂点のx座標は？",
                "options": ["1", "2", "3", "4"],
                "correct": 1,
                "explanation": "頂点のx座標は -b/2a = -(-4)/(2×1) = 2"
            },
            {
                "question": "等速運動を表すグラフはどれか？",
                "options": ["直線", "放物線", "指数曲線", "正弦波"],
                "correct": 0,
                "explanation": "等速運動は一定の速度なので、位置-時間グラフは直線になる"
            }
        ]
        
        for i, q in enumerate(questions, 1):
            print(f"\n問題 {i}: {q['question']}")
            for j, option in enumerate(q['options']):
                print(f"  {j+1}. {option}")
            
            # 回答入力（実際の実装では対話的にする）
            print(f"\n💡 正解: {q['options'][q['correct']]}")
            print(f"📝 解説: {q['explanation']}")
    
    def gemini_integration_demo(self):
        """Gemini統合デモ"""
        
        display(Markdown("""
        ## 🤖 Gemini AI 統合機能
        
        この教材では、Gemini AIと連携して以下の機能を提供します：
        
        ### 1. 個別質問対応
        - 関数に関する疑問を自然言語で質問
        - 段階的な解説の提供
        - 類似問題の生成
        
        ### 2. 学習進捗分析
        - 理解度の自動評価
        - 弱点分野の特定
        - 個別学習プランの提案
        
        ### 3. 応用問題生成
        - レベルに応じた問題作成
        - 実生活に関連した問題設定
        - 詳細な解答解説
        
        ### 4. リアルタイム解説
        - パラメータ変更時の即座な説明
        - 数学的意味の解釈
        - 物理的意味の説明
        
        ### サンプル質問例：
        - 「なぜ二次関数のグラフは曲線になるのですか？」
        - 「一次関数と二次関数の実生活での使い分けは？」
        - 「加速度と二次関数の関係を詳しく教えて」
        - 「この問題の解き方が分からないので段階的に教えて」
        """))
    
    def ask_gemini_ai(self, question):
        """Gemini AIに質問"""
        
        if not model:
            return "Gemini APIキーが設定されていません。.envファイルにGEMINI_API_KEYを設定してください。"
        
        try:
            system_prompt = """
            あなたは数学教師です。一次関数と二次関数について、
            中学生にも分かりやすく説明してください。
            日本語で回答し、具体例を交えて説明してください。
            """
            
            full_prompt = f"{system_prompt}\n\n質問: {question}"
            response = model.generate_content(full_prompt)
            return response.text
            
        except Exception as e:
            return f"Gemini AI接続エラー: {str(e)}"

# 使用例
def run_interactive_learning():
    """インタラクティブ学習の実行"""
    
    learner = QuadraticFunctionLearning()
    
    # 理論説明
    learner.theory_explanation()
    
    # インタラクティブプロット
    print("🎮 以下のスライダーでパラメータを調整してください：")
    interactive_widget = learner.interactive_widget()
    display(interactive_widget)
    
    # 運動分析
    print("\n🚀 運動解析シミュレーション：")
    motion_fig = learner.motion_analysis()
    motion_fig.show()
    
    # 比較分析
    print("\n📊 数値比較分析：")
    comparison_data = learner.comparative_analysis()
    
    # 問題演習
    print("\n📝 物理問題演習：")
    learner.physics_problem_generator()
    
    # クイズ
    print("\n🧩 理解度確認クイズ：")
    learner.generate_quiz()
    
    # Gemini統合デモ
    learner.gemini_integration_demo()
    
    # 学習進捗保存
    learner.save_learning_progress("関数基礎", 8, "一次関数と二次関数の基本概念を理解")
    
    return learner

if __name__ == "__main__":
    # スタンドアロン実行
    learner = run_interactive_learning()
    
    print("""
    🎓 学習完了！
    
    この教材で学んだこと：
    ✅ 一次関数と二次関数の基本概念
    ✅ グラフの形状の違いとその意味
    ✅ 物理運動との関係
    ✅ 実生活での応用例
    ✅ 数値的な比較分析
    
    さらなる学習のために：
    📖 より高度な関数の学習
    🔬 微分積分の基礎
    💼 実務での数学活用
    """) 