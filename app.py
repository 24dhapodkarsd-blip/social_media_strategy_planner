import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

from agents.trend_agent import trend_agent
from agents.content_agent import content_agent
from agents.scheduler_agent import scheduler_agent
from agents.judge_agent import judge_agent

# Load environment variables
load_dotenv()

# Create Grok client
client = OpenAI(
    api_key=os.getenv("GROK_API_KEY"),
    base_url="https://api.x.ai/v1"
)

st.title("📱 Social Media Strategy Planner (Grok Powered)")

business_type = st.text_input("Enter your business type:")
platform = st.selectbox("Select platform:", ["Instagram", "LinkedIn", "Twitter"])

if st.button("Generate Strategy"):

    trends = trend_agent(client, business_type)
    content = content_agent(client, trends, business_type, platform)
    schedule = scheduler_agent(client, platform)
    review = judge_agent(client, content)

    st.subheader("🔥 Trending Topics")
    st.write(trends)

    st.subheader("✍️ Generated Content")
    st.write(content)

    st.subheader("📅 Posting Schedule")
    st.write(schedule)

    st.subheader("🧠 AI Review")
    st.write(review)