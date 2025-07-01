import React from 'react';
import { Score } from '../App';

interface ScoreBoardProps {
  score: Score;
}

export const ScoreBoard: React.FC<ScoreBoardProps> = ({ score }) => {
  const getPerformanceLevel = (percentage: number) => {
    if (percentage >= 90) return { level: '優秀', emoji: '🌟', color: '#4CAF50' };
    if (percentage >= 70) return { level: '良好', emoji: '👍', color: '#FF9800' };
    if (percentage >= 50) return { level: '普通', emoji: '📝', color: '#2196F3' };
    return { level: '要改善', emoji: '💪', color: '#F44336' };
  };

  const performance = getPerformanceLevel(score.percentage);

  return (
    <div className="scoreboard">
      <h3>📈 学習成績</h3>
      
      <div className="score-stats">
        <div className="stat-item">
          <div className="stat-value">{score.correct}</div>
          <div className="stat-label">正解数</div>
        </div>
        
        <div className="stat-item">
          <div className="stat-value">{score.total}</div>
          <div className="stat-label">解答数</div>
        </div>
        
        <div className="stat-item">
          <div className="stat-value" style={{ color: performance.color }}>
            {score.total > 0 ? `${score.percentage}%` : '-%'}
          </div>
          <div className="stat-label">正解率</div>
        </div>
      </div>

      {score.total > 0 && (
        <div className="performance-badge" style={{ backgroundColor: performance.color }}>
          <span className="performance-emoji">{performance.emoji}</span>
          <span className="performance-level">{performance.level}</span>
        </div>
      )}

      <div className="progress-bar">
        <div 
          className="progress-fill" 
          style={{ 
            width: `${score.percentage}%`,
            backgroundColor: performance.color 
          }}
        ></div>
      </div>

      {score.total === 0 && (
        <div className="no-data">
          <p>まだ問題を解いていません</p>
          <p>頑張って学習しましょう！</p>
        </div>
      )}
    </div>
  );
}; 