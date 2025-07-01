import React, { useState } from 'react';
import { MathProblem } from '../App';

interface AnswerInputProps {
  problem: MathProblem;
  onAnswerSubmit: (isCorrect: boolean) => void;
  showAnswer: boolean;
  onNextProblem: () => void;
}

export const AnswerInput: React.FC<AnswerInputProps> = ({
  problem,
  onAnswerSubmit,
  showAnswer,
  onNextProblem
}) => {
  const [userAnswer, setUserAnswer] = useState('');
  const [feedback, setFeedback] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!userAnswer.trim()) {
      alert('答えを入力してください。');
      return;
    }

    setIsSubmitting(true);
    try {
      const response = await fetch('http://localhost:3001/api/math-problems/validate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          problemId: problem.id,
          userAnswer: userAnswer.trim(),
          correctAnswer: problem.answer,
        }),
      });

      if (!response.ok) {
        throw new Error('答えの検証に失敗しました');
      }

      const result = await response.json();
      setFeedback(result.feedback);
      onAnswerSubmit(result.isCorrect);
    } catch (error) {
      console.error('検証エラー:', error);
      setFeedback('答えの検証中にエラーが発生しました。');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleNextProblem = () => {
    setUserAnswer('');
    setFeedback('');
    onNextProblem();
  };

  return (
    <div className="answer-input">
      {!showAnswer ? (
        <form onSubmit={handleSubmit} className="answer-form">
          <div className="input-group">
            <label htmlFor="userAnswer">あなたの答え:</label>
            <input
              type="text"
              id="userAnswer"
              value={userAnswer}
              onChange={(e) => setUserAnswer(e.target.value)}
              placeholder="答えを入力してください"
              disabled={isSubmitting}
              autoFocus
            />
          </div>
          <button
            type="submit"
            className="submit-btn"
            disabled={isSubmitting || !userAnswer.trim()}
          >
            {isSubmitting ? '判定中...' : '✓ 答えを確認'}
          </button>
        </form>
      ) : (
        <div className="result-section">
          {feedback && (
            <div className={`feedback ${feedback.includes('正解') ? 'correct' : 'incorrect'}`}>
              {feedback}
            </div>
          )}
          <div className="next-problem">
            <button onClick={handleNextProblem} className="next-btn">
              🎯 次の問題へ
            </button>
          </div>
        </div>
      )}
    </div>
  );
}; 