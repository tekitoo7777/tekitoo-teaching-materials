import { evaluate } from 'mathjs';

export interface MathProblem {
  id: string;
  question: string;
  latex: string;
  answer: number | string;
  explanation: string;
  difficulty: string;
  topic: string;
  problemType: string;
  createdAt: Date;
}

export async function generateMathProblem(
  topic: string, 
  difficulty: string, 
  problemType: string
): Promise<MathProblem> {
  const id = generateUniqueId();
  const timestamp = new Date();
  
  let problem: Partial<MathProblem>;
  
  switch (topic) {
    case 'arithmetic':
      problem = generateArithmeticProblem(difficulty, problemType);
      break;
    case 'algebra':
      problem = generateAlgebraProblem(difficulty, problemType);
      break;
    case 'geometry':
      problem = generateGeometryProblem(difficulty, problemType);
      break;
    case 'calculus':
      problem = generateCalculusProblem(difficulty, problemType);
      break;
    case 'statistics':
      problem = generateStatisticsProblem(difficulty, problemType);
      break;
    default:
      throw new Error(`未対応のトピック: ${topic}`);
  }
  
  return {
    id,
    topic,
    difficulty,
    problemType,
    createdAt: timestamp,
    ...problem
  } as MathProblem;
}

function generateArithmeticProblem(difficulty: string, problemType: string): Partial<MathProblem> {
  const getRange = (diff: string) => {
    switch (diff) {
      case '基礎': return { min: 1, max: 10 };
      case '標準': return { min: 10, max: 100 };
      case '応用': return { min: 100, max: 1000 };
      default: return { min: 1, max: 10 };
    }
  };
  
  const range = getRange(difficulty);
  const a = Math.floor(Math.random() * range.max) + range.min;
  const b = Math.floor(Math.random() * range.max) + range.min;
  
  switch (problemType) {
    case '加法':
      return {
        question: `${a} + ${b} を計算してください。`,
        latex: `${a} + ${b} = ?`,
        answer: a + b,
        explanation: `${a} + ${b} = ${a + b}`
      };
    case '減法':
      const larger = Math.max(a, b);
      const smaller = Math.min(a, b);
      return {
        question: `${larger} - ${smaller} を計算してください。`,
        latex: `${larger} - ${smaller} = ?`,
        answer: larger - smaller,
        explanation: `${larger} - ${smaller} = ${larger - smaller}`
      };
    case '乗法':
      return {
        question: `${a} × ${b} を計算してください。`,
        latex: `${a} \\times ${b} = ?`,
        answer: a * b,
        explanation: `${a} × ${b} = ${a * b}`
      };
    case '除法':
      const dividend = a * b; // 割り切れるようにする
      return {
        question: `${dividend} ÷ ${a} を計算してください。`,
        latex: `${dividend} \\div ${a} = ?`,
        answer: b,
        explanation: `${dividend} ÷ ${a} = ${b}`
      };
    default:
      return generateArithmeticProblem(difficulty, '加法');
  }
}

function generateAlgebraProblem(difficulty: string, problemType: string): Partial<MathProblem> {
  switch (problemType) {
    case '一次方程式':
      const a = Math.floor(Math.random() * 10) + 1;
      const b = Math.floor(Math.random() * 20) + 1;
      const x = Math.floor(Math.random() * 10) + 1;
      const result = a * x + b;
      return {
        question: `方程式 ${a}x + ${b} = ${result} を解いてください。`,
        latex: `${a}x + ${b} = ${result}`,
        answer: x,
        explanation: `${a}x = ${result} - ${b} = ${result - b}\\n x = ${result - b} ÷ ${a} = ${x}`
      };
    case '二次方程式':
      const p = Math.floor(Math.random() * 5) + 1;
      const q = Math.floor(Math.random() * 5) + 1;
      return {
        question: `方程式 x² - ${p + q}x + ${p * q} = 0 を解いてください。`,
        latex: `x^2 - ${p + q}x + ${p * q} = 0`,
        answer: `x = ${p}, ${q}`,
        explanation: `(x - ${p})(x - ${q}) = 0 より x = ${p}, ${q}`
      };
    default:
      return generateAlgebraProblem(difficulty, '一次方程式');
  }
}

function generateGeometryProblem(difficulty: string, problemType: string): Partial<MathProblem> {
  switch (problemType) {
    case '面積':
      const width = Math.floor(Math.random() * 10) + 1;
      const height = Math.floor(Math.random() * 10) + 1;
      return {
        question: `縦${height}cm、横${width}cmの長方形の面積を求めてください。`,
        latex: `面積 = ${width} \\times ${height}`,
        answer: width * height,
        explanation: `長方形の面積 = 縦 × 横 = ${height} × ${width} = ${width * height} cm²`
      };
    case '体積':
      const l = Math.floor(Math.random() * 5) + 1;
      const w = Math.floor(Math.random() * 5) + 1;
      const h = Math.floor(Math.random() * 5) + 1;
      return {
        question: `縦${l}cm、横${w}cm、高さ${h}cmの直方体の体積を求めてください。`,
        latex: `体積 = ${l} \\times ${w} \\times ${h}`,
        answer: l * w * h,
        explanation: `直方体の体積 = 縦 × 横 × 高さ = ${l} × ${w} × ${h} = ${l * w * h} cm³`
      };
    default:
      return generateGeometryProblem(difficulty, '面積');
  }
}

function generateCalculusProblem(difficulty: string, problemType: string): Partial<MathProblem> {
  switch (problemType) {
    case '微分':
      const n = Math.floor(Math.random() * 5) + 2;
      return {
        question: `f(x) = x^${n} の導関数を求めてください。`,
        latex: `f(x) = x^${n}`,
        answer: `${n}x^${n-1}`,
        explanation: `f'(x) = ${n}x^${n-1}`
      };
    case '積分':
      const m = Math.floor(Math.random() * 4) + 1;
      return {
        question: `∫x^${m} dx を計算してください。`,
        latex: `\\int x^${m} dx`,
        answer: `x^${m+1}/${m+1} + C`,
        explanation: `∫x^${m} dx = \\frac{x^${m+1}}{${m+1}} + C`
      };
    default:
      return generateCalculusProblem(difficulty, '微分');
  }
}

function generateStatisticsProblem(difficulty: string, problemType: string): Partial<MathProblem> {
  switch (problemType) {
    case '平均':
      const numbers = Array.from({length: 5}, () => Math.floor(Math.random() * 20) + 1);
      const sum = numbers.reduce((a, b) => a + b, 0);
      const average = sum / numbers.length;
      return {
        question: `数値 ${numbers.join(', ')} の平均を求めてください。`,
        latex: `平均 = \\frac{${numbers.join(' + ')}}{${numbers.length}}`,
        answer: average,
        explanation: `平均 = (${numbers.join(' + ')}) ÷ ${numbers.length} = ${sum} ÷ ${numbers.length} = ${average}`
      };
    default:
      return generateStatisticsProblem(difficulty, '平均');
  }
}

function generateUniqueId(): string {
  return Math.random().toString(36).substr(2, 9);
} 