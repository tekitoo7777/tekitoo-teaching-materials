import express from 'express';
import { generateMathProblem } from '../services/mathProblemGenerator';
import { validateMathAnswer } from '../services/mathValidator';

const router = express.Router();

// 数学問題生成
router.post('/generate', async (req, res) => {
  try {
    const { topic, difficulty, problemType } = req.body;
    
    if (!topic || !difficulty || !problemType) {
      return res.status(400).json({
        error: 'topic, difficulty, problemType are required'
      });
    }
    
    const problem = await generateMathProblem(topic, difficulty, problemType);
    res.json(problem);
  } catch (error) {
    console.error('問題生成エラー:', error);
    res.status(500).json({ error: '問題の生成に失敗しました' });
  }
});

// 答えの検証
router.post('/validate', async (req, res) => {
  try {
    const { problemId, userAnswer, correctAnswer } = req.body;
    
    if (!problemId || userAnswer === undefined || !correctAnswer) {
      return res.status(400).json({
        error: 'problemId, userAnswer, correctAnswer are required'
      });
    }
    
    const result = validateMathAnswer(userAnswer, correctAnswer);
    res.json(result);
  } catch (error) {
    console.error('答え検証エラー:', error);
    res.status(500).json({ error: '答えの検証に失敗しました' });
  }
});

// 問題のカテゴリ一覧
router.get('/categories', (req, res) => {
  const categories = [
    { id: 'arithmetic', name: '算数', difficulties: ['基礎', '標準', '応用'] },
    { id: 'algebra', name: '代数', difficulties: ['基礎', '標準', '応用'] },
    { id: 'geometry', name: '幾何', difficulties: ['基礎', '標準', '応用'] },
    { id: 'calculus', name: '微積分', difficulties: ['基礎', '標準', '応用'] },
    { id: 'statistics', name: '統計', difficulties: ['基礎', '標準', '応用'] }
  ];
  
  res.json(categories);
});

export { router as mathProblemRoutes }; 