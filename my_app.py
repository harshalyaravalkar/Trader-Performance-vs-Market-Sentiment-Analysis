import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("C:/Users/hally/Downloads/df_grouped.csv")

st.title("Trader Behavior vs Market Sentiment")

# Sidebar filter
sentiment = st.sidebar.selectbox(
    "Select Sentiment",
    ["All", "Fear", "Greed"]
)

if sentiment != "All":
    df = df[df['sentiment_binary'] == sentiment]

st.metric("Avg PnL", round(df['daily_pnl'].mean(), 2))
st.metric("Avg Trades", round(df['trades'].mean(), 2))

# 1.PnL Distribution
st.subheader("PnL Distribution")

fig, ax = plt.subplots()
sns.histplot(df['daily_pnl'], kde=True, ax=ax)
st.pyplot(fig)

# 2.Risk vs Return
st.subheader("Risk vs Return")

fig, ax = plt.subplots()
sns.scatterplot(
    data=df,
    x='total_volume',
    y='daily_pnl',
    ax=ax
)
st.pyplot(fig)

# 3.Trades
st.subheader("Trading Activity")

fig, ax = plt.subplots()
sns.boxplot(
    data=df,
    x='sentiment_binary',
    y='trades',
    ax=ax
)
st.pyplot(fig)