import React, { useState, useEffect } from 'react';
import { MathProblem } from '../App';

interface MathProblemGeneratorProps {
  onProblemGenerated: (problem: MathProblem) => void;
  isLoading: boolean;
  setIsLoading: (loading: boolean) => void;
}

interface Category {
  id: string;
  name: string;
  difficulties: string[];
}

const problemTypes: { [key: string]: string[] } = {
  arithmetic: ['加法', '減法', '乗法', '除法'],
  algebra: ['一次方程式', '二次方程式'],
  geometry: ['面積', '体積'],
  calculus: ['微分', '積分'],
  statistics: ['平均']
};

export const MathProblemGenerator: React.FC<MathProblemGeneratorProps> = ({
  onProblemGenerated,
  isLoading,
  setIsLoading
}) => {
  const [categories, setCategories] = useState<Category[]>([]);
  const [selectedTopic, setSelectedTopic] = useState('arithmetic');
  const [selectedDifficulty, setSelectedDifficulty] = useState('基礎');
  const [selectedProblemType, setSelectedProblemType] = useState('加法');

  useEffect(() => {
    fetchCategories();
  }, []);

  useEffect(() => {
    // トピックが変更されたら、そのトピックの最初の問題タイプを選択
    if (problemTypes[selectedTopic]) {
      setSelectedProblemType(problemTypes[selectedTopic][0]);
    }
  }, [selectedTopic]);

  const fetchCategories = async () => {
    try {
      const response = await fetch('http://localhost:3001/api/math-problems/categories');
      const data = await response.json();
      setCategories(data);
    } catch (error) {
      console.error('カテゴリの取得に失敗しました:', error);
      // フォールバック用のカテゴリ
      setCategories([
        { id: 'arithmetic', name: '算数', difficulties: ['基礎', '標準', '応用'] },
        { id: 'algebra', name: '代数', difficulties: ['基礎', '標準', '応用'] },
        { id: 'geometry', name: '幾何', difficulties: ['基礎', '標準', '応用'] },
        { id: 'calculus', name: '微積分', difficulties: ['基礎', '標準', '応用'] },
        { id: 'statistics', name: '統計', difficulties: ['基礎', '標準', '応用'] }
      ]);
    }
  };

  const generateProblem = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:3001/api/math-problems/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          topic: selectedTopic,
          difficulty: selectedDifficulty,
          problemType: selectedProblemType,
        }),
      });

      if (!response.ok) {
        throw new Error('問題の生成に失敗しました');
      }

      const problem = await response.json();
      onProblemGenerated(problem);
    } catch (error) {
      console.error('問題生成エラー:', error);
      alert('問題の生成に失敗しました。後でもう一度お試しください。');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="math-problem-generator">
      <h3>📚 問題設定</h3>
      
      <div className="form-group">
        <label htmlFor="topic">分野:</label>
        <select
          id="topic"
          value={selectedTopic}
          onChange={(e) => setSelectedTopic(e.target.value)}
          disabled={isLoading}
        >
          {categories.map((category) => (
            <option key={category.id} value={category.id}>
              {category.name}
            </option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="difficulty">難易度:</label>
        <select
          id="difficulty"
          value={selectedDifficulty}
          onChange={(e) => setSelectedDifficulty(e.target.value)}
          disabled={isLoading}
        >
          {categories
            .find((cat) => cat.id === selectedTopic)
            ?.difficulties.map((diff) => (
              <option key={diff} value={diff}>
                {diff}
              </option>
            ))}
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="problemType">問題タイプ:</label>
        <select
          id="problemType"
          value={selectedProblemType}
          onChange={(e) => setSelectedProblemType(e.target.value)}
          disabled={isLoading}
        >
          {problemTypes[selectedTopic]?.map((type) => (
            <option key={type} value={type}>
              {type}
            </option>
          ))}
        </select>
      </div>

      <button
        className="generate-btn"
        onClick={generateProblem}
        disabled={isLoading}
      >
        {isLoading ? '生成中...' : '🎲 問題を生成'}
      </button>
    </div>
  );
}; 