import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# إعداد الصفحة بثيم داكن وتخطيط واسع
st.set_page_config(
    page_title="Teek Studio - نظام إدارة الاستوديو",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تخصيص التصميم والألوان لتطابق الواجهة الاحترافية تماماً
st.markdown("""
    <style>
    .stApp {
        background-color: #0c0f1d;
        color: #ffffff;
        font-family: sans-serif;
    }
    .main-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0;
    }
    .welcome-text {
        font-size: 22px;
        font-weight: bold;
        color: #ffffff;
    }
    .sub-welcome {
        color: #8b92a5;
        font-size: 13px;
        margin-bottom: 15px;
    }
    .stat-card {
        background-color: #161b2e;
        border-radius: 14px;
        padding: 15px;
        text-align: right;
        margin-bottom: 12px;
        border: 1px solid #222b45;
    }
    .stat-number {
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
    }
    .stat-label {
        color: #8b92a5;
        font-size: 12px;
        margin-top: 4px;
    }
    .money-card {
        background-color: #161b2e;
        border-radius: 14px;
        padding: 18px;
        text-align: center;
        margin-bottom: 15px;
        border: 1px solid #
