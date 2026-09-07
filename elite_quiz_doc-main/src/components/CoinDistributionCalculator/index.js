import React, { useState, useMemo } from 'react';
import styles from './styles.module.css';

export default function CoinDistributionCalculator() {
  const [maxCoins, setMaxCoins] = useState(10);
  const [quizWinningPercentage, setQuizWinningPercentage] = useState(30);
  const [maxCoinsPercentage, setMaxCoinsPercentage] = useState(70);
  const [playerScore, setPlayerScore] = useState(50);
  const [distributionMode, setDistributionMode] = useState('scaled'); // 'scaled' or 'linear'

  // Calculate coins based on the formula
  const calculateCoins = (score, maxCoinsPct, maxWinningCoins, quizWinPct) => {
    if (score < quizWinPct) {
      return 0;
    }

    if (score >= maxCoinsPct) {
      return maxWinningCoins;
    }

    const earnedCoins = maxWinningCoins - (maxCoinsPct - score) / 10;
    return Math.max(0, Math.floor(earnedCoins));
  };

  const effectiveMaxCoinsPercentage = distributionMode === 'linear' ? 100 : maxCoinsPercentage;
  const earnedCoins = useMemo(
    () => calculateCoins(playerScore, effectiveMaxCoinsPercentage, maxCoins, quizWinningPercentage),
    [playerScore, effectiveMaxCoinsPercentage, maxCoins, quizWinningPercentage]
  );

  // Generate chart data for visualization
  const chartData = useMemo(() => {
    const data = [];
    for (let score = 0; score <= 100; score += 5) {
      data.push({
        score,
        coins: calculateCoins(score, effectiveMaxCoinsPercentage, maxCoins, quizWinningPercentage),
      });
    }
    return data;
  }, [effectiveMaxCoinsPercentage, maxCoins, quizWinningPercentage]);

  const maxChartCoins = Math.max(...chartData.map(d => d.coins));
  const rewardPercentage = maxCoins > 0 ? (earnedCoins / maxCoins) * 100 : 0;

  // Find the closest bar to the current player score
  const closestBarScore = useMemo(() => {
    return chartData.reduce((prev, curr) => {
      return Math.abs(curr.score - playerScore) < Math.abs(prev.score - playerScore) ? curr : prev;
    }).score;
  }, [chartData, playerScore]);

  return (
    <div className={styles.calculator}>
      {/* Distribution Mode Toggle */}
      <div className={styles.modeToggle}>
        <button
          className={distributionMode === 'scaled' ? styles.active : ''}
          onClick={() => setDistributionMode('scaled')}
        >
          Scaled Distribution
        </button>
        <button
          className={distributionMode === 'linear' ? styles.active : ''}
          onClick={() => setDistributionMode('linear')}
        >
          Linear Distribution
        </button>
      </div>

      {/* Input Controls */}
      <div className={styles.controls}>
        <div className={styles.control}>
          <label>
            <span className={styles.label}>Max Winning Coins</span>
            <span className={styles.value}>{maxCoins} 🎯</span>
          </label>
          <input
            type="range"
            min="1"
            max="50"
            value={maxCoins}
            onChange={e => setMaxCoins(Number(e.target.value))}
            className={styles.slider}
          />
        </div>

        <div className={styles.control}>
          <label>
            <span className={styles.label}>Quiz Winning Percentage</span>
            <span className={styles.value}>{quizWinningPercentage}%</span>
          </label>
          <input
            type="range"
            min="0"
            max="100"
            value={quizWinningPercentage}
            onChange={e => setQuizWinningPercentage(Number(e.target.value))}
            className={styles.slider}
          />
          <small className={styles.hint}>Minimum score to earn any coins</small>
        </div>

        {distributionMode === 'scaled' && (
          <div className={styles.control}>
            <label>
              <span className={styles.label}>Max Coins Winning Percentage</span>
              <span className={styles.value}>{maxCoinsPercentage}%</span>
            </label>
            <input
              type="range"
              min="0"
              max="100"
              value={maxCoinsPercentage}
              onChange={e => setMaxCoinsPercentage(Number(e.target.value))}
              className={styles.slider}
            />
            <small className={styles.hint}>Score needed for full reward</small>
          </div>
        )}

        {distributionMode === 'linear' && (
          <div className={styles.infoBox}>
            <strong>Linear Mode Active:</strong> Max Coins Winning Percentage is set to 100%. Coins
            are awarded proportionally to the score.
          </div>
        )}

        <div className={styles.control}>
          <label>
            <span className={styles.label}>Player Percentage</span>
            <span className={styles.value}>{playerScore}%</span>
          </label>
          <input
            type="range"
            min="0"
            max="100"
            value={playerScore}
            onChange={e => setPlayerScore(Number(e.target.value))}
            className={`${styles.slider} ${styles.playerSlider}`}
          />
        </div>
      </div>

      {/* Distribution Chart */}
      <div className={styles.chart}>
        <div className={styles.chartHeader}>
          <span className={styles.chartTitle}>Distribution Chart</span>
          <div className={styles.resultBadge}>
            <span className={styles.resultLabel}>Your Coins:</span>
            <span className={styles.resultValue}>{earnedCoins}</span>
          </div>
        </div>
        <div className={styles.chartContainer}>
          {chartData.map((point, index) => (
            <div key={index} className={styles.chartBar}>
              {point.coins > 0 && <span className={styles.coinLabel}>{point.coins}</span>}
              <div
                className={`${styles.bar} ${point.score === closestBarScore ? styles.currentBar : ''}`}
                style={{
                  height: `${maxChartCoins > 0 ? (point.coins / maxChartCoins) * 100 : 0}%`,
                  backgroundColor:
                    point.score < quizWinningPercentage
                      ? 'var(--ifm-color-danger)'
                      : point.score >= effectiveMaxCoinsPercentage
                        ? 'var(--ifm-color-success)'
                        : 'var(--ifm-color-warning)',
                }}
              ></div>
              {point.score % 20 === 0 && <span className={styles.chartLabel}>{point.score}%</span>}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
