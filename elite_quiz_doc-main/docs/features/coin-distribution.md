---
sidebar_position: 4
---

# Coin Distribution System

Understanding how coins are awarded to players based on their quiz performance is essential for configuring your Elite Quiz platform. This guide explains the coin distribution mechanism in detail.

---

## Overview

The coin distribution system uses a formula that scales rewards based on player performance. It ensures that players are rewarded proportionally between a minimum winning threshold and a maximum reward threshold.

:::info Key Concept
Coin rewards scale smoothly between your **winning threshold** and your **max reward threshold**, encouraging players to aim for higher accuracy.
:::

---

## Where to Configure

You can configure these coin distribution settings in the **Admin Panel**:

**Admin Panel → Settings → System Utilities → General Settings**

This is where you'll find the following configuration options:

- **Max Winning Coins** - Maximum coins a player can earn from a quiz
- **Quiz Winning Percentage** - Minimum accuracy required to win and earn coins
- **Max Coins Winning Percentage** - Percentage required to earn the full reward (set to 100% for linear distribution)

![Admin Panel System Utilities Settings](/img/panel/system_utilities.webp)

---

## Core Configuration Parameters

### 1. Max Winning Coins

This is the **maximum number of coins** a player can earn from a quiz.

**Example:**
If `maxCoins = 10`, the most a player can earn from that quiz is **10 coins**.

---

### 2. Quiz Winning Percentage

This is the **minimum accuracy required to win** a quiz and earn any coins.

**Example:**
If `quizWinningPercentage = 30%` and the quiz has 10 questions, a player needs to answer **at least 3 questions correctly** to be considered a winner.

:::warning Below Threshold
If a player scores below the Quiz Winning Percentage, they receive **0 coins**, regardless of their performance.
:::

---

### 3. Max Coins Winning Percentage

This determines when a player earns **the full reward**.

It's the percentage of correct answers required to earn **100% of the max coins**.

**Example:**
If `maxCoinsWinningPercentage = 70%`, then:

- Scoring **70% or higher** → Player gets **10 coins** (full reward)
- Scoring **below 30%** → Player gets **0 coins** (didn't meet winning threshold)
- Scoring **between 30% and 70%** → Player gets a **proportionate amount** based on their performance

:::note Edge Cases
- If Quiz Winning Percentage is set to 0%, players get coins for any score
- If Max Coins Winning Percentage ≤ Quiz Winning Percentage, all winners get full coins immediately
:::

---

## How the Formula Works

The coin distribution formula scales rewards linearly between the winning threshold and the max reward threshold.

### The Formula

```dart
coins = maxCoins - ((maxCoinsPct - userPct) / 10)
```

**Where:**

- `maxCoins` = Maximum coins available for the quiz
- `maxCoinsPct` = Max Coins Winning Percentage (e.g., 70%)
- `userPct` = Player's actual percentage score

### Example Calculation

For a quiz with these settings:

- `maxCoins = 10`
- `maxCoinsWinningPercentage = 70%`
- `quizWinningPercentage = 30%`

If a player scores **50%** correct:

```
coins = 10 - ((70 - 50) / 10)
      = 10 - (20 / 10)
      = 10 - 2
      = 8 coins
```

So a player with 50% correct answers earns **8 coins**.

---

## Reward Tiers Summary

Using the example settings above (`maxCoins = 10`, winning threshold = 30%, max threshold = 70%):

| Player Score | Coins Earned | Status           |
| ------------ | ------------ | ---------------- |
| Below 30%    | 0            | ❌ Did not win   |
| 30%          | 6            | 💰 Scaled reward |
| 40%          | 7            | 💰 Scaled reward |
| 50%          | 8            | 💰 Scaled reward |
| 60%          | 9            | 💰 Scaled reward |
| 70%+         | 10           | 🏆 Full reward   |

:::tip Scaling Behavior
The formula ensures that each 10% increase in performance (within the scaling range) adds approximately 1 coin to the reward, creating a smooth progression that motivates players to improve.
:::

---

## Interactive Calculator

Play with the values below to see how coin distribution works in real-time:

import CoinDistributionCalculator from '@site/src/components/CoinDistributionCalculator';

<CoinDistributionCalculator />

---

## Configuration Best Practices

### Setting Thresholds

1. **Quiz Winning Percentage (30% recommended)**

   - Set low enough to encourage participation
   - High enough to require genuine effort
   - Common range: 25-40%

2. **Max Coins Winning Percentage (70% recommended)**

   - Should be challenging but achievable
   - Creates motivation for mastery
   - Common range: 60-80%

3. **Max Winning Coins**
   - Balance economy and player motivation
   - Consider quiz difficulty and length
   - Higher stakes = more engagement

---

## Alternative: Fully Linear Distribution

If you prefer a **purely linear** coin distribution system where coins are awarded **directly proportional** to the number of correct answers, you can achieve this by setting the **Max Coins Winning Percentage to 100%**.

### How It Works

With `maxCoinsWinningPercentage = 100%`:

- A player earns coins **exactly proportional** to their score
- No "sweet spot" or scaling range
- Simple 1:1 relationship between accuracy and coins

**Example:**

Configuration:

- `maxCoins = 10`
- `maxCoinsWinningPercentage = 100%`
- `quizWinningPercentage = 30%` (minimum threshold to earn any coins)
- Quiz has 10 questions

Results:

- Answer **3/10 questions** (30%) → Earn **3 coins** (minimum to win)
- Answer **5/10 questions** (50%) → Earn **5 coins**
- Answer **7/10 questions** (70%) → Earn **7 coins**
- Answer **10/10 questions** (100%) → Earn **10 coins**

### Calculation Example

With the formula:

```
coins = maxCoins - ((maxCoinsPct - userPct) / 10)
```

For a player scoring **50%**:

```
coins = 10 - ((100 - 50) / 10)
      = 10 - (50 / 10)
      = 10 - 5
      = 5 coins
```

Perfect linear distribution!

### When to Use Linear Distribution

**Use Linear Distribution when:**

- You want a simple, predictable reward system
- Every correct answer should have equal value
- You're targeting casual players who prefer straightforward mechanics
- You want to minimize complexity in reward calculations

**Use Scaled Distribution (default 70%) when:**

- You want to create achievement tiers
- You want to motivate players to reach higher scores
- You're designing competitive or educational content
- You want to reward mastery with bonus coins

:::tip Quick Setup
To enable linear distribution, simply set **Max Coins Winning Percentage to 100%** in your admin panel's coin configuration settings.
:::

---

## Summary

- **Below winning threshold** → ❌ No coins
- **Between thresholds** → 💰 Scaled coins (linear progression)
- **At or above max threshold** → 🏆 Full coins

The coin distribution system creates a fair, motivating reward structure that encourages players to improve their knowledge while maintaining engagement at all skill levels.
