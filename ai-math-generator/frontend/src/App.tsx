import React, { useState } from 'react';
import './App.css';
import { MathProblemGenerator } from './components/MathProblemGenerator';
import { ProblemDisplay } from './components/ProblemDisplay';
import { AnswerInput } from './components/AnswerInput';
import { ScoreBoard } from './components/ScoreBoard';

export interface MathProblem {
  id: string;
  question: string;
  latex: string;
  answer: number | string;
  explanation: string;
  difficulty: string;
  topic: string;
  problemType: string;
  createdAt: string;
}

export interface Score {
  correct: number;
  total: number;
  percentage: number;
}

function App() {
  const [currentProblem, setCurrentProblem] = useState<MathProblem | null>(null);
  const [showAnswer, setShowAnswer] = useState(false);
  const [score, setScore] = useState<Score>({ correct: 0, total: 0, percentage: 0 });
  const [isLoading, setIsLoading] = useState(false);

  const handleNewProblem = (problem: MathProblem) => {
    setCurrentProblem(problem);
    setShowAnswer(false);
  };

  const handleAnswerSubmit = (isCorrect: boolean) => {
    const newScore = {
      correct: score.correct + (isCorrect ? 1 : 0),
      total: score.total + 1,
      percentage: 0
    };
    newScore.percentage = Math.round((newScore.correct / newScore.total) * 100);
    setScore(newScore);
    setShowAnswer(true);
  };

  const handleNextProblem = () => {
    setCurrentProblem(null);
    setShowAnswer(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🧮 StudyAid - 数学問題生成システム</h1>
        <p>CursorAIと連携した数学学習アプリケーション</p>
      </header>
      
      <main className="App-main">
        <div className="container">
          <div className="sidebar">
            <ScoreBoard score={score} />
            <MathProblemGenerator 
              onProblemGenerated={handleNewProblem}
              isLoading={isLoading}
              setIsLoading={setIsLoading}
            />
          </div>
          
          <div className="content">
            {currentProblem ? (
              <>
                <ProblemDisplay 
                  problem={currentProblem}
                  showAnswer={showAnswer}
                />
                <AnswerInput 
                  problem={currentProblem}
                  onAnswerSubmit={handleAnswerSubmit}
                  showAnswer={showAnswer}
                  onNextProblem={handleNextProblem}
                />
              </>
            ) : (
              <div className="welcome">
                <h2>数学問題を生成してください</h2>
                <p>左側のパネルから問題の種類と難易度を選択して、「問題を生成」ボタンをクリックしてください。</p>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
