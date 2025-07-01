#!/usr/bin/env python3
"""
一次関数と二次関数教材のデモスクリプト
Claude APIなしでも動作します
"""

import os
import sys
from app import create_comparison_plot, get_claude_explanation

def main():
    print("🎯 一次関数 vs 二次関数 - インタラクティブ教材")
    print("=" * 50)
    
    # Claude APIキーの確認
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key or api_key == 'demo_key':
        print("⚠️  Claude APIキーが設定されていません")
        print("   デモモードで実行します")
        print("   実際のClaude AIを使用するには:")
        print("   1. https://console.anthropic.com/ でAPIキーを取得")
        print("   2. .env ファイルに ANTHROPIC_API_KEY=your_key を設定")
        print()
    else:
        print("✅ Claude APIキーが設定されています")
        print()
    
    print("📊 グラフデータの生成テスト")
    print("-" * 30)
    
    # 基本のグラフ生成テスト
    try:
        plot_json = create_comparison_plot(2, 2)
        print("✅ グラフの生成に成功しました")
    except Exception as e:
        print(f"❌ グラフの生成に失敗: {e}")
        return
    
    print("\n🤖 Claude AI解説の生成テスト")
    print("-" * 30)
    
    # Claude解説の生成テスト
    try:
        explanation = get_claude_explanation(2, 2)
        print("✅ Claude解説の生成に成功しました")
        print("\n📝 生成された解説:")
        print("-" * 20)
        print(explanation)
        print("-" * 20)
    except Exception as e:
        print(f"❌ Claude解説の生成に失敗: {e}")
    
    print("\n🚀 Webアプリケーションの起動方法")
    print("-" * 30)
    print("1. ターミナルで以下を実行:")
    print("   python app.py")
    print("2. ブラウザで以下にアクセス:")
    print("   http://localhost:5000")
    print()
    print("📚 教材の特徴:")
    print("- インタラクティブなグラフ表示")
    print("- リアルタイムパラメータ調整")
    print("- Claude AIによる詳細解説")
    print("- 質問機能付き")
    print()

if __name__ == "__main__":
    main() 