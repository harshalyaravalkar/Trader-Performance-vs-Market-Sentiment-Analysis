# Trader Performance vs Market Sentiment Analysis

## Overview
This project analyzes how market sentiment (Fear vs Greed) affects trader behavior and performance. The goal is to understand whether traders behave differently under different market conditions and what patterns can help improve trading strategies.

---

## Dataset
Two datasets were used:
- Bitcoin Market Sentiment (Fear/Greed index)
- Historical Trader Data from Hyperliquid

The datasets were merged on date to align trader activity with market sentiment.

---

## Methodology
- Cleaned and prepared both datasets
- Converted timestamps and aligned data on a daily level
- Created key metrics such as:
  - daily PnL
  - number of trades
  - win rate
  - total trading volume (used as a proxy for exposure)
- Performed analysis comparing Fear vs Greed conditions
- Segmented traders based on risk levels
- Applied clustering to identify trader types
- Built a simple predictive model to estimate profitability

---

## Key Insights

- Trading activity increases during Fear periods, suggesting reactive or emotional behavior
- Win rate remains similar across Fear and Greed, meaning sentiment does not affect accuracy much
- Higher trading volume and activity do not lead to better returns
- High-risk traders experience larger gains and losses, but not better overall performance
- Profit per trade remains similar across different risk levels, showing overtrading reduces efficiency
- Clustering shows that balanced traders perform better than both high-frequency and low-activity traders

---

## Trader Archetypes

- Balanced Traders: Moderate activity with more stable performance
- High-Frequency Traders: Very active but less efficient per trade
- Low-Activity Traders: Few trades with poor performance

---

## Predictive Model

We built a simple model to predict whether a trader would be profitable using features like number of trades, trading volume, win rate, and market sentiment.

We noticed that trading behavior was more useful for prediction than market sentiment alone.

Initially, we included pnl_per_trade, but it caused unrealistically high accuracy since it is directly related to the target. This feature was removed to keep the model fair.

---

## Strategy Recommendations

- Reduce trading activity during Fear periods to avoid losses caused by volatility
- Avoid overtrading, as more trades do not improve performance
- Focus on trade quality instead of increasing trade size or volume
- Avoid emotional or reactive trading during uncertain market conditions
- Maintain a balanced trading approach instead of extreme strategies

---

## Dashboard

A simple Streamlit dashboard was built to explore:
- PnL distribution
- Trading activity
- Risk vs return relationships

---

## How to Run

1. Clone the repository  
2. Install required libraries:
   pip install pandas numpy matplotlib seaborn scikit-learn streamlit  
3. Run the notebook for analysis  
4. Launch dashboard:
   streamlit run my_app.py  

---

## Conclusion

This analysis shows that trader behavior changes with market sentiment, especially in terms of activity and risk-taking. However, higher activity and exposure do not lead to better results.

A balanced and disciplined approach performs better than aggressive or reactive trading.
