import streamlit as st
import pandas as pd

# إعداد الصفحة بثيم داكن وتخطيط واسع
st.set_page_config(
    page_title="Teek Studio - لوحة التحكم",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تخصيص التصميم والألوان عبر CSS لتطابق الواجهة تماماً
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
        padding: 10px 0;
    }
    .welcome-text {
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
    }
    .sub-welcome {
        color: #8b92a5;
        font-size: 14px;
        margin-bottom: 20px;
    }
    .action-btn {
        background-color: #f4c430;
        color: #0c0f1d;
        font-weight: bold;
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        width: 100%;
        margin-bottom: 20px;
        cursor: pointer;
    }
    .stat-card {
        background-color: #161b2e;
        border-radius: 16px;
        padding: 20px;
        text-align: right;
        margin-bottom: 15px;
        border: 1px solid #222b45;
    }
    .stat-number {
        font-size: 28px;
        font-weight: bold;
        color: #ffffff;
    }
    .stat-label {
        color: #8b92a5;
        font-size: 13px;
        margin-top: 5px;
    }
    .money-card {
        background-color: #161b2e;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #222b45;
    }
    .money-amount {
        font-size: 32px;
        font-weight: bold;
        color: #f4c430;
        margin-top: 5px;
    }
    .section-title {
        font-size: 16px;
        font-weight: bold;
        color: #ffffff;
        margin: 20px 0 10px 0;
    }
    .empty-box {
        background-color: #161b2e;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        color: #8b92a5;
        border: 1px solid #222b45;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# رأس الصفحة (اسم الاستوديو والشعار والتحية)
st.markdown("""
    <div class="main-header">
        <div>
            <div style="font-size: 20px; font-weight: bold; color: #ffffff;">Teek Studio</div>
            <div style="font-size: 11px; color: #8b92a5;">إدارة تأجير معدات التصوير</div>
        </div>
    </div>
    <div style="margin-top: 15px;">
        <div class="welcome-text">مرحباً بك 👋</div>
        <div class="sub-welcome">إليك ملخص حركة المحل اليوم</div>
    </div>
""", unsafe_allow_html=True)

# زر إضافة عملية تأجير جديدة
if st.button("➕ إضافة عملية تأجير جديدة", use_container_width=True):
    st.toast("جاري فتح نافذة إضافة تأجير جديد...")

# شبكة الإحصائيات (المتاح، المؤجر، المتأخرون، الحجوزات القادمة)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <div class="stat-card">
            <div style="text-align: left; color: #4cd137; font-size: 18px;">📦</div>
            <div class="stat-number">66</div>
            <div class="stat-label">المتاح الآن</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="stat-card">
            <div style="text-align: left; color: #e84118; font-size: 18px;">⏰</div>
            <div class="stat-number">0</div>
            <div class="stat-label">المتأخرون</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stat-card">
            <div style="text-align: left; color: #00a8ff; font-size: 18px;">📷</div>
            <div class="stat-number">10</div>
            <div class="stat-label">المؤجر الآن</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="stat-card">
            <div style="text-align: left; color: #fbc531; font-size: 18px;">📅</div>
            <div class="stat-number">0</div>
            <div class="stat-label">الحجوزات القادمة</div>
        </div>
    """, unsafe_allow_html=True)

# قسم المبالغ المالية
st.markdown("""
    <div class="money-card">
        <div style="color: #8b92a5; font-size: 13px;">المبالغ المتبقية لدى العملاء</div>
        <div class="money-amount">5,000 ريال</div>
    </div>
""", unsafe_allow_html=True)

# إحصائيات مالية مصغرة (شبكة 2×2)
m_col1, m_col2 = st.columns(2)
with m_col1:
    st.markdown("""
        <div class="stat-card" style="padding: 15px;">
            <div class="stat-label">محصل التأجير</div>
            <div style="font-size: 18px; font-weight: bold; color: #ffffff; margin-top: 5px;">0 ريال</div>
        </div>
        <div class="stat-card" style="padding: 15px;">
            <div class="stat-label">ربح البيع المحصل</div>
            <div style="font-size: 18px; font-weight: bold; color: #8b92a5; margin-top: 5px;">مخفي</div>
        </div>
    """, unsafe_allow_html=True)

with m_col2:
    st.markdown("""
        <div class="stat-card" style="padding: 15px;">
            <div class="stat-label">محصل البيع اليوم</div>
            <div style="font-size: 18px; font-weight: bold; color: #ffffff; margin-top: 5px;">0 ريال</div>
        </div>
        <div class="stat-card" style="padding: 15px;">
            <div class="stat-label">مصروفات اليوم</div>
            <div style="font-size: 18px; font-weight: bold; color: #ffffff; margin-top: 5px;">0 ريال</div>
        </div>
    """, unsafe_allow_html=True)

# قسم أقرب مواعيد الإرجاع
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 25px; margin-bottom: 10px;">
        <span style="color: #f4c430; font-size: 13px; cursor: pointer;">عرض الكل</span>
        <span class="section-title" style="margin: 0;">أقرب مواعيد الإرجاع</span>
    </div>
    <div class="empty-box">
        لا توجد عمليات إرجاع قريبة.
    </div>
""", unsafe_allow_html=True)

# قسم الوصول السريع
st.markdown('<div class="section-title">وصول سريع</div>', unsafe_allow_html=True)
q1, q2, q3 = st.columns(3)
with q1:
    st.button("👥 العملاء", use_container_width=True)
with q2:
    st.button("📷 المعدات", use_container_width=True)
with q3:
    st.button("🏷️ المبيعات", use_container_width=True)

q4, q5, q6 = st.columns(3)
with q4:
    st.button("💳 المصروفات", use_container_width=True)
with q5:
    st.button("📑 التأجيرات", use_container_width=True)
with q6:
    st.button("📅 الحجوزات", use_container_width=True)
