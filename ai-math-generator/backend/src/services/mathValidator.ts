import { evaluate } from 'mathjs';

export interface ValidationResult {
  isCorrect: boolean;
  userAnswer: any;
  correctAnswer: any;
  score: number;
  feedback: string;
}

export function validateMathAnswer(
  userAnswer: string | number, 
  correctAnswer: string | number
): ValidationResult {
  try {
    // 数値の場合の比較
    if (typeof correctAnswer === 'number') {
      const userNum = typeof userAnswer === 'string' ? parseFloat(userAnswer) : userAnswer;
      const isCorrect = Math.abs(userNum - correctAnswer) < 0.001; // 小数点誤差を考慮
      
      return {
        isCorrect,
        userAnswer: userNum,
        correctAnswer,
        score: isCorrect ? 100 : 0,
        feedback: isCorrect ? '正解です！' : `残念です。正解は ${correctAnswer} です。`
      };
    }
    
    // 文字列の場合の比較（方程式の解など）
    if (typeof correctAnswer === 'string') {
      const normalizedUser = normalizeExpression(userAnswer.toString());
      const normalizedCorrect = normalizeExpression(correctAnswer);
      const isCorrect = normalizedUser === normalizedCorrect;
      
      return {
        isCorrect,
        userAnswer: normalizedUser,
        correctAnswer: normalizedCorrect,
        score: isCorrect ? 100 : 0,
        feedback: isCorrect ? '正解です！' : `残念です。正解は ${correctAnswer} です。`
      };
    }
    
    return {
      isCorrect: false,
      userAnswer,
      correctAnswer,
      score: 0,
      feedback: '答えの形式が正しくありません。'
    };
    
  } catch (error) {
    return {
      isCorrect: false,
      userAnswer,
      correctAnswer,
      score: 0,
      feedback: '答えの検証中にエラーが発生しました。'
    };
  }
}

function normalizeExpression(expression: string): string {
  return expression
    .replace(/\s+/g, '') // 空白を削除
    .replace(/[×*]/g, '*') // 掛け算記号を統一
    .replace(/[÷]/g, '/') // 割り算記号を統一
    .toLowerCase();
}

export function evaluateMathExpression(expression: string): number {
  try {
    return evaluate(expression);
  } catch (error) {
    throw new Error(`数式の評価に失敗しました: ${expression}`);
  }
} 