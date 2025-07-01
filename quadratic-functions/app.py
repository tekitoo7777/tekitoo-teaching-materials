#!/usr/bin/env python3
"""
一次関数・二次関数 教材システム
Gemini AI統合バージョン
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import matplotlib
matplotlib.use('Agg')  # バックエンド設定
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.utils
import json
import io
import base64
from datetime import datetime
import os
from dotenv import load_dotenv
import google.generativeai as genai

# 環境変数読み込み
load_dotenv()

# Gemini API設定
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    model = None
    print("⚠️  GEMINI_API_KEY が設定されていません。AI機能は無効化されます。")

app = Flask(__name__)

def generate_linear_data(a, x_max=6):
    """一次関数 y = ax のデータを生成"""
    x = np.linspace(0, x_max, 100)
    y = a * x
    return x, y

def generate_quadratic_data(a, x_max=6):
    """二次関数 y = ax² のデータを生成"""
    x = np.linspace(0, x_max, 100)
    y = a * x**2
    return x, y

def create_comparison_plot(linear_a=2, quadratic_a=2):
    """一次関数と二次関数の比較グラフを作成"""
    fig = go.Figure()
    
    # 一次関数のプロット
    x_linear, y_linear = generate_linear_data(linear_a)
    fig.add_trace(go.Scatter(
        x=x_linear, 
        y=y_linear,
        mode='lines',
        name=f'一次関数: y = {linear_a}x (等速運動)',
        line=dict(color='blue', width=3)
    ))
    
    # 二次関数のプロット
    x_quad, y_quad = generate_quadratic_data(quadratic_a)
    fig.add_trace(go.Scatter(
        x=x_quad, 
        y=y_quad,
        mode='lines',
        name=f'二次関数: y = {quadratic_a}x² (等加速度運動)',
        line=dict(color='red', width=3)
    ))
    
    # データポイントを追加（教材の表から）
    linear_points_x = [0, 1, 2, 3, 4, 5, 6]
    linear_points_y = [0, 2, 4, 6, 8, 10, 12]
    quad_points_x = [0, 1, 2, 3, 4, 5, 6]
    quad_points_y = [0, 2, 8, 18, 32, 50, 72]
    
    fig.add_trace(go.Scatter(
        x=linear_points_x,
        y=linear_points_y,
        mode='markers',
        name='一次関数データ点',
        marker=dict(color='blue', size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=quad_points_x,
        y=quad_points_y,
        mode='markers',
        name='二次関数データ点',
        marker=dict(color='red', size=8)
    ))
    
    fig.update_layout(
        title='一次関数 vs 二次関数：鉄球の運動比較',
        xaxis_title='時間 (秒)',
        yaxis_title='距離 (m)',
        hovermode='x unified',
        template='plotly_white',
        height=500
    )
    
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def get_gemini_explanation(linear_a, quadratic_a, question_type="basic"):
    """Gemini AIを使って説明を生成"""
    try:
        prompt = f"""
        一次関数 y = {linear_a}x と二次関数 y = {quadratic_a}x² について、
        鉄球の運動を例に分かりやすく説明してください。
        
        以下の点を含めて説明してください：
        1. それぞれの関数が表す物理現象
        2. グラフの形の違いとその意味
        3. 実生活での例
        4. 数学的な特徴の違い
        
        中学生にも分かるような表現で、300字程度で説明してください。
        """
        
        response = ask_gemini_ai(prompt)
        return response
    except Exception as e:
        return f"Gemini AIが利用できません。デモモードで実行中です。\n\n一次関数 y = {linear_a}x は等速運動を表し、時間に対して距離が一定の割合で増加します（直線のグラフ）。一方、二次関数 y = {quadratic_a}x² は等加速度運動を表し、時間が経つにつれて距離の増加率が大きくなります（曲線のグラフ）。自動車の加速や落下する物体などが二次関数の例です。"

def ask_gemini_ai(question):
    """Gemini AI に質問"""
    if not model:
        return "Gemini APIキーが設定されていません。"
    
    try:
        # プロンプト構成
        system_prompt = """
        あなたは数学教師です。一次関数と二次関数について、
        中学生にも分かりやすく説明してください。
        日本語で回答し、具体例を交えて説明してください。
        """
        
        full_prompt = f"{system_prompt}\n\n質問: {question}"
        
        # Gemini AIに質問
        response = model.generate_content(full_prompt)
        return response.text
        
    except Exception as e:
        return f"Gemini AI接続エラー: {str(e)}"

@app.route('/')
def index():
    """メインページ"""
    initial_plot = create_comparison_plot()
    initial_explanation = get_gemini_explanation(2, 2)
    return render_template('index.html', 
                         plot_json=initial_plot,
                         explanation=initial_explanation)

@app.route('/update_plot', methods=['POST'])
def update_plot():
    """パラメータ更新時のグラフ更新"""
    data = request.json
    linear_a = float(data.get('linear_a', 2))
    quadratic_a = float(data.get('quadratic_a', 2))
    
    plot_json = create_comparison_plot(linear_a, quadratic_a)
    explanation = get_gemini_explanation(linear_a, quadratic_a)
    
    return jsonify({
        'plot_json': plot_json,
        'explanation': explanation
    })

@app.route('/ask_gemini', methods=['POST'])
def ask_gemini():
    """Gemini AIに質問を送信"""
    data = request.json
    question = data.get('question', '')
    
    try:
        prompt = f"""
        一次関数と二次関数の教材に関する質問です：
        {question}
        
        鉄球の運動を例に、分かりやすく答えてください。
        """
        
        response = ask_gemini_ai(prompt)
        return jsonify({'answer': response})
    except Exception as e:
        return jsonify({'answer': f"Gemini AIが利用できません。デモモードで実行中です。\n\n'{question}' について：\n一次関数と二次関数の違いを理解するには、グラフの形（直線vs曲線）と変化率（一定vs増加）に注目してください。実際の運動で考えると、一次関数は一定速度での移動、二次関数は加速しながらの移動を表します。"})

if __name__ == '__main__':
    app.run(debug=True) 