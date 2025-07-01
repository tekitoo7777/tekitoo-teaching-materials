import React, { useEffect, useRef } from 'react';
import { MathProblem } from '../App';

// KaTeXを直接使用するためのインポート
declare global {
  interface Window {
    katex: any;
  }
}

interface ProblemDisplayProps {
  problem: MathProblem;
  showAnswer: boolean;
}

const MathRenderer: React.FC<{ math: string; display?: boolean }> = ({ math, display = false }) => {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (ref.current && window.katex) {
      try {
        window.katex.render(math, ref.current, {
          displayMode: display,
          throwOnError: false,
        });
      } catch (error) {
        console.error('KaTeX rendering error:', error);
        ref.current.textContent = math;
      }
    } else {
      // Fallback: display as plain text
      if (ref.current) {
        ref.current.textContent = math;
      }
    }
  }, [math, display]);

  return <div ref={ref} className={display ? 'math-display' : 'math-inline'} />;
};

export const ProblemDisplay: React.FC<ProblemDisplayProps> = ({ problem, showAnswer }) => {
  const formatDifficulty = (difficulty: string) => {
    const levels = {
      '基礎': '🟢',
      '標準': '🟡', 
      '応用': '🔴'
    };
    return levels[difficulty as keyof typeof levels] || '⚪';
  };

  const formatTopic = (topic: string) => {
    const topics = {
      'arithmetic': '➕ 算数',
      'algebra': '🔢 代数',
      'geometry': '📐 幾何',
      'calculus': '📈 微積分',
      'statistics': '📊 統計'
    };
    return topics[topic as keyof typeof topics] || topic;
  };

  return (
    <div className="problem-display">
      <div className="problem-header">
        <div className="problem-meta">
          <span className="topic">{formatTopic(problem.topic)}</span>
          <span className="difficulty">{formatDifficulty(problem.difficulty)} {problem.difficulty}</span>
          <span className="type">{problem.problemType}</span>
        </div>
        <div className="problem-id">問題ID: {problem.id}</div>
      </div>

      <div className="problem-content">
        <h3>問題</h3>
        <div className="question">
          <p>{problem.question}</p>
          {problem.latex && (
            <div className="latex-display">
              <MathRenderer math={problem.latex} display={true} />
            </div>
          )}
        </div>
      </div>

      {showAnswer && (
        <div className="answer-section">
          <h3>解答と解説</h3>
          <div className="correct-answer">
            <strong>正解: </strong>
            {typeof problem.answer === 'number' ? (
              <MathRenderer math={problem.answer.toString()} />
            ) : (
              <MathRenderer math={problem.answer} />
            )}
          </div>
          <div className="explanation">
            <strong>解説:</strong>
            <p>{problem.explanation}</p>
          </div>
        </div>
      )}
    </div>
  );
}; 