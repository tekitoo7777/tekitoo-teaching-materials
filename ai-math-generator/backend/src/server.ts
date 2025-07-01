import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { mathProblemRoutes } from './routes/mathProblems';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3001;

// ミドルウェア
app.use(cors());
app.use(express.json());

// ルート
app.use('/api/math-problems', mathProblemRoutes);

// ヘルスチェック
app.get('/health', (req, res) => {
  res.json({ status: 'OK', message: 'StudyAid Math Problem Generator API is running' });
});

app.listen(PORT, () => {
  console.log(`🚀 StudyAid API Server running on port ${PORT}`);
}); 