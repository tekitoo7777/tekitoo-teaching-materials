#!/usr/bin/env python3
"""
Gemini Code Interactive Demo
一次関数・二次関数の高度な教材システム
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime
import json
import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# 環境変数読み込み
load_dotenv()

# 仮想環境での日本語フォント設定
try:
    import matplotlib
    matplotlib.rcParams['font.family'] = ['DejaVu Sans', 'Hiragino Sans', 'Yu Gothic']
except:
    pass

# Gemini API設定
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    model = None

class GeminiCodeInteractiveDemo:
    """Gemini Codeを活用した教材デモシステム"""
    
    def __init__(self):
        self.session_data = {
            'start_time': datetime.now(),
            'interactions': [],
            'understanding_progress': []
        }
        print("🎯 Gemini Code Interactive Demo を開始します")
        print("=" * 60)
    
    def display_welcome(self):
        """ウェルカムメッセージ"""
        welcome_msg = """
        🚀 Gemini Code Interactive 一次関数・二次関数教材
        
        このデモでは以下の機能を体験できます：
        
        📈 高度な可視化
        • 4分割プロットによる包括的分析
        • リアルタイム数値計算
        • 3D軌跡表示
        
        🎮 インタラクティブ機能
        • パラメータ調整による即座の反映
        • 物理的意味の解説
        • 数値的比較分析
        
        🤖 Gemini AI統合
        • 自然言語での質問対応
        • 個別指導スタイルの解説
        • 学習進捗の自動分析
        
        📊 実践的学習
        • 実世界の問題例
        • 段階的な理解構築
        • 継続学習サポート
        """
        print(welcome_msg)
    
    def create_advanced_visualization(self, linear_a=2, quad_a=2):
        """高度な可視化システム"""
        
        # データ生成
        x = np.linspace(0, 6, 1000)
        y_linear = linear_a * x
        y_quad = quad_a * x**2
        
        # 微分計算
        v_linear = np.full_like(x, linear_a)
        v_quad = 2 * quad_a * x
        
        # 加速度計算
        a_linear = np.zeros_like(x)
        a_quad = np.full_like(x, 2 * quad_a)
        
        # 教材データポイント
        data_x = np.array([0, 1, 2, 3, 4, 5, 6])
        data_y_linear = np.array([0, 2, 4, 6, 8, 10, 12])
        data_y_quad = np.array([0, 2, 8, 18, 32, 50, 72])
        
        # 4分割プロット作成
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                f'📊 関数比較 (線形a={linear_a}, 二次a={quad_a})',
                '⚡ 速度分析 (一階微分)',
                '🚀 加速度分析 (二階微分)',
                '🎯 実データ vs 理論値'
            ),
            specs=[[{}, {}], [{}, {}]]
        )
        
        # 1. 関数比較
        fig.add_trace(
            go.Scatter(x=x, y=y_linear, name=f'一次関数: y = {linear_a}x',
                      line=dict(color='#2E86AB', width=3)),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=x, y=y_quad, name=f'二次関数: y = {quad_a}x²',
                      line=dict(color='#A23B72', width=3)),
            row=1, col=1
        )
        
        # 2. 速度分析
        fig.add_trace(
            go.Scatter(x=x, y=v_linear, name='一次関数の速度（一定）',
                      line=dict(color='#F18F01', dash='dash', width=2)),
            row=1, col=2
        )
        fig.add_trace(
            go.Scatter(x=x, y=v_quad, name='二次関数の速度（変化）',
                      line=dict(color='#C73E1D', dash='dash', width=2)),
            row=1, col=2
        )
        
        # 3. 加速度分析
        fig.add_trace(
            go.Scatter(x=x, y=a_linear, name='一次関数の加速度（0）',
                      line=dict(color='#84C318', width=2)),
            row=2, col=1
        )
        fig.add_trace(
            go.Scatter(x=x, y=a_quad, name='二次関数の加速度（一定）',
                      line=dict(color='#6A994E', width=2)),
            row=2, col=1
        )
        
        # 4. 実データ vs 理論値
        # 実データ
        fig.add_trace(
            go.Scatter(x=data_x, y=data_y_linear, mode='markers',
                      name='一次関数実データ', 
                      marker=dict(size=10, color='#2E86AB', symbol='circle')),
            row=2, col=2
        )
        fig.add_trace(
            go.Scatter(x=data_x, y=data_y_quad, mode='markers',
                      name='二次関数実データ',
                      marker=dict(size=10, color='#A23B72', symbol='square')),
            row=2, col=2
        )
        
        # 理論曲線
        fig.add_trace(
            go.Scatter(x=x, y=y_linear, name='一次理論値',
                      line=dict(color='#2E86AB', width=2, dash='dot'),
                      showlegend=False),
            row=2, col=2
        )
        fig.add_trace(
            go.Scatter(x=x, y=y_quad, name='二次理論値',
                      line=dict(color='#A23B72', width=2, dash='dot'),
                      showlegend=False),
            row=2, col=2
        )
        
        # レイアウト設定
        fig.update_layout(
            height=700,
            title_text="🎯 Gemini Code Interactive: 一次関数 vs 二次関数 完全分析",
            showlegend=True,
            template="plotly_white"
        )
        
        # 軸ラベル設定
        fig.update_xaxes(title_text="時間 (秒)")
        fig.update_yaxes(title_text="距離 (m)", row=1, col=1)
        fig.update_yaxes(title_text="速度 (m/s)", row=1, col=2)
        fig.update_yaxes(title_text="加速度 (m/s²)", row=2, col=1)
        fig.update_yaxes(title_text="距離 (m)", row=2, col=2)
        
        return fig
    
    def calculate_physics_insights(self, linear_a=2, quad_a=2, time=6):
        """物理的洞察の計算"""
        
        insights = {
            'linear': {
                'position_6s': linear_a * time,
                'velocity': linear_a,
                'acceleration': 0,
                'distance_traveled': linear_a * time
            },
            'quadratic': {
                'position_6s': quad_a * time**2,
                'velocity_6s': 2 * quad_a * time,
                'acceleration': 2 * quad_a,
                'distance_traveled': quad_a * time**2
            }
        }
        
        # 比較分析
        insights['comparison'] = {
            'position_difference': insights['quadratic']['position_6s'] - insights['linear']['position_6s'],
            'velocity_difference': insights['quadratic']['velocity_6s'] - insights['linear']['velocity'],
            'acceleration_difference': insights['quadratic']['acceleration'] - insights['linear']['acceleration']
        }
        
        return insights
    
    def display_insights(self, insights):
        """洞察の表示"""
        
        print("\n🔍 物理的洞察分析")
        print("=" * 50)
        
        print(f"📊 一次関数（等速運動）:")
        print(f"  • 6秒後の位置: {insights['linear']['position_6s']:.1f}m")
        print(f"  • 速度: {insights['linear']['velocity']:.1f}m/s (一定)")
        print(f"  • 加速度: {insights['linear']['acceleration']:.1f}m/s² (なし)")
        
        print(f"\n📈 二次関数（等加速度運動）:")
        print(f"  • 6秒後の位置: {insights['quadratic']['position_6s']:.1f}m")
        print(f"  • 6秒後の速度: {insights['quadratic']['velocity_6s']:.1f}m/s")
        print(f"  • 加速度: {insights['quadratic']['acceleration']:.1f}m/s² (一定)")
        
        print(f"\n🔄 比較結果:")
        print(f"  • 位置の差: {insights['comparison']['position_difference']:.1f}m")
        print(f"  • 速度の差: {insights['comparison']['velocity_difference']:.1f}m/s")
        print(f"  • 加速度の差: {insights['comparison']['acceleration_difference']:.1f}m/s²")
    
    def gemini_ai_simulation(self, question_type="explain_difference"):
        """Gemini AI統合シミュレーション"""
        
        if model:
            try:
                prompts = {
                    "explain_difference": """
                    一次関数と二次関数の根本的な違いについて、中学生にも分かりやすく説明してください。
                    物理的な意味（等速運動と等加速度運動）も含めて、具体例を交えて解説してください。
                    """,
                    
                    "real_world_applications": """
                    一次関数と二次関数の実世界での応用例を教えてください。
                    日常生活や仕事でどのように使われているか、具体的な例を挙げて説明してください。
                    """,
                    
                    "learning_tips": """
                    一次関数と二次関数を効果的に学習するためのコツやアドバイスを教えてください。
                    つまずきやすいポイントと克服方法も含めて説明してください。
                    """
                }
                
                if question_type in prompts:
                    response = model.generate_content(prompts[question_type])
                    print(f"\n🤖 Gemini AI 統合デモ - {question_type}")
                    print("=" * 50)
                    print(response.text)
                else:
                    print(f"利用可能な解説タイプ: {list(prompts.keys())}")
                    
            except Exception as e:
                print(f"⚠️ Gemini AI接続エラー: {e}")
                self._fallback_responses(question_type)
        else:
            print("⚠️ GEMINI_API_KEY が設定されていません。デモモードで実行します。")
            self._fallback_responses(question_type)
    
    def _fallback_responses(self, question_type):
        """Gemini APIが利用できない場合のフォールバック"""
        
        responses = {
            "explain_difference": """
🤖 Gemini の詳細解説 (デモモード):

一次関数と二次関数の根本的な違いは「変化の仕方」にあります。

【一次関数 y = ax】
• 変化率が一定（毎秒同じ距離だけ進む）
• グラフは直線
• 物理的には「等速運動」
• 例：時速60kmで走る車、時給1000円のアルバイト

【二次関数 y = ax²】
• 変化率が変化する（時間が経つほど早くなる）
• グラフは放物線
• 物理的には「等加速度運動」
• 例：自由落下する物体、車の加速

この違いが現実世界で重要な理由は、多くの自然現象が
加速的な変化（二次関数的）をするからです。
            """,
            
            "real_world_applications": """
🤖 Gemini の実世界応用解説 (デモモード):

【一次関数の応用】
🚗 高速道路の走行距離計算
💰 従量制料金（電気、ガス、水道）
📏 単位換算（温度、長さ、重さ）

【二次関数の応用】
🚗 ブレーキ距離（速度の2乗に比例）
💸 複利計算（時間の経過で加速的増加）
🏀 投球軌道（重力による放物線運動）
📊 最適化問題（利益最大化、コスト最小化）

特に重要なのは、二次関数が「最適化」に使われることです。
企業の利益計算、建築の強度計算、投資のリスク分析など、
現代社会の多くの分野で活用されています。
            """,
            
            "learning_tips": """
🤖 Gemini の学習アドバイス (デモモード):

【効果的な学習方法】
1. 📊 まずはグラフで視覚的に理解
2. 🧮 具体的な数値で計算練習
3. 🌍 実生活の例で応用イメージ
4. 🔄 比較分析で違いを明確化

【つまずきやすいポイント】
• 「なぜ二次関数は曲線？」→ 変化率が変化するから
• 「微分って何？」→ その瞬間の変化率（速度）
• 「最大値・最小値」→ 頂点の概念

【継続学習のコツ】
• 毎日5分でも数学に触れる
• 日常で関数を見つける習慣
• 「なぜ？」を大切にする
• 間違いを恐れずに挑戦
            """
        }
        
        print("\n🤖 Gemini AI 統合デモ (デモモード)")
        print("=" * 50)
        
        if question_type in responses:
            print(responses[question_type])
        else:
            print("利用可能な解説タイプ:")
            for key in responses.keys():
                print(f"  • {key}")
    
    def interactive_demo(self):
        """インタラクティブデモの実行"""
        
        print("\n🎮 インタラクティブデモを開始します")
        print("-" * 40)
        
        # パラメータ設定
        scenarios = [
            {"linear_a": 2, "quad_a": 2, "name": "標準設定"},
            {"linear_a": 3, "quad_a": 1, "name": "高速・低加速"},
            {"linear_a": 1, "quad_a": 3, "name": "低速・高加速"}
        ]
        
        for i, scenario in enumerate(scenarios, 1):
            print(f"\n📊 シナリオ {i}: {scenario['name']}")
            print(f"一次関数: y = {scenario['linear_a']}x")
            print(f"二次関数: y = {scenario['quad_a']}x²")
            
            # 可視化
            fig = self.create_advanced_visualization(
                scenario['linear_a'], scenario['quad_a']
            )
            
            # 物理的洞察
            insights = self.calculate_physics_insights(
                scenario['linear_a'], scenario['quad_a']
            )
            self.display_insights(insights)
            
            # セッションデータ記録
            self.session_data['interactions'].append({
                'scenario': scenario['name'],
                'parameters': scenario,
                'insights': insights,
                'timestamp': datetime.now().isoformat()
            })
            
            print("\n" + "-" * 40)
    
    def generate_final_report(self):
        """最終レポート生成"""
        
        print("\n📋 学習セッション完了レポート")
        print("=" * 60)
        
        session_duration = datetime.now() - self.session_data['start_time']
        
        print(f"🕐 セッション時間: {session_duration.total_seconds():.1f}秒")
        print(f"🎯 完了シナリオ数: {len(self.session_data['interactions'])}")
        
        print(f"\n📊 学習内容:")
        print("  ✅ 一次関数と二次関数の基本概念")
        print("  ✅ 高度な4分割可視化")
        print("  ✅ 物理的意味の理解")
        print("  ✅ 数値的比較分析")
        print("  ✅ Gemini AI統合機能")
        print("  ✅ インタラクティブ体験")
        
        # 学習データ保存
        report_data = {
            'session_summary': {
                'start_time': self.session_data['start_time'].isoformat(),
                'end_time': datetime.now().isoformat(),
                'duration_seconds': session_duration.total_seconds(),
                'scenarios_completed': len(self.session_data['interactions'])
            },
            'interactions': self.session_data['interactions'],
            'learning_outcomes': [
                '一次関数と二次関数の違いを理解',
                '物理的意味（等速・等加速度運動）を把握',
                '実世界での応用例を学習',
                '数値的分析手法を習得',
                'Gemini AI統合機能を体験'
            ]
        }
        
        # JSONファイルに保存
        try:
            with open('gemini_code_session_report.json', 'w', encoding='utf-8') as f:
                json.dump(report_data, f, ensure_ascii=False, indent=2)
            print(f"\n💾 詳細レポートを保存しました: gemini_code_session_report.json")
        except Exception as e:
            print(f"⚠️ レポート保存エラー: {e}")
        
        print(f"\n🎓 Gemini Code Interactive Demo 完了！")
        print("次回はJupyter Notebookでより詳細な学習を体験してください。")

def main():
    """メイン実行関数"""
    
    demo = GeminiCodeInteractiveDemo()
    
    try:
        # ウェルカム表示
        demo.display_welcome()
        
        # Gemini AI解説デモ
        demo.gemini_ai_simulation("explain_difference")
        demo.gemini_ai_simulation("real_world_applications")
        demo.gemini_ai_simulation("learning_tips")
        
        # インタラクティブデモ
        demo.interactive_demo()
        
        # 最終レポート
        demo.generate_final_report()
        
    except KeyboardInterrupt:
        print("\n\n⏹️  デモを中断しました")
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
    finally:
        print("\n👋 Gemini Code Interactive Demo を終了します")

if __name__ == "__main__":
    main() 