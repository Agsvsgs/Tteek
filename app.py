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
        border: 1px solid #222b45;
    }
    .money-amount {
        font-size: 28px;
        font-weight: bold;
        color: #f4c430;
        margin-top: 5px;
    }
    .section-title {
        font-size: 15px;
        font-weight: bold;
        color: #ffffff;
        margin: 15px 0 8px 0;
    }
    .empty-box {
        background-color: #161b2e;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        color: #8b92a5;
        border: 1px solid #222b45;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# التهيئة المبدئية للبيانات في الذاكرة (Session State)
if 'inventory' not in st.session_state:
    st.session_state.inventory = pd.DataFrame([
        {"المعدة": "Sony FX3", "النوع": "كاميرا", "الحالة": "مؤجر", "السعر اليومي ($)": 150},
        {"المعدة": "Canon EOS R5", "النوع": "كاميرا", "الحالة": "متاح", "السعر اليومي ($)": 120},
        {"المعدة": "Godox SK400", "النوع": "إضاءة", "الحالة": "متاح", "السعر اليومي ($)": 30},
        {"المعدة": "Rode Wireless GO II", "النوع": "صوت", "الحالة": "متاح", "السعر اليومي ($)": 25},
    ])

if 'bookings' not in st.session_state:
    st.session_state.bookings = pd.DataFrame(columns=["اسم العميل", "المعدة", "تاريخ البدء", "تاريخ الإرجاع", "الإجمالي ($)"])

if 'expenses' not in st.session_state:
    st.session_state.expenses = 0

# شريط التنقل السفلي التجريبي عبر القائمة الجانبية المدمجة
nav_option = st.sidebar.selectbox("القائمة الرئيسية", ["🏠 الرئيسية", "📷 المعدات", "📑 التأجيرات", "👥 العملاء", "💳 المصروفات"])

if nav_option == "🏠 الرئيسية":
    # رأس الصفحة
    st.markdown("""
        <div class="main-header">
            <div>
                <div style="font-size: 18px; font-weight: bold; color: #ffffff;">Teek Studio</div>
                <div style="font-size: 10px; color: #8b92a5;">إدارة تأجير معدات التصوير</div>
            </div>
        </div>
        <div style="margin-top: 10px;">
            <div class="welcome-text">مرحباً بك 👋</div>
            <div class="sub-welcome">إليك ملخص حركة المحل اليوم</div>
        </div>
    """, unsafe_allow_html=True)

    # حساب الإحصائيات بناءً على البيانات الحية
    total_items = len(st.session_state.inventory)
    rented_items = len(st.session_state.inventory[st.session_state.inventory['الحالة'] == 'مؤجر'])
    available_items = total_items - rented_items

    # زر إضافة عملية تأجير جديدة
    if st.button("➕ إضافة عملية تأجير جديدة", use_container_width=True):
        st.session_state['open_add_modal'] = True

    # شبكة الإحصائيات العلوية
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="stat-card">
                <div style="text-align: left; color: #4cd137; font-size: 16px;">📦</div>
                <div class="stat-number">{available_items}</div>
                <div class="stat-label">المتاح الآن</div>
            </div>
            <div class="stat-card">
                <div style="text-align: left; color: #e84118; font-size: 16px;">⏰</div>
                <div class="stat-number">0</div>
                <div class="stat-label">المتأخرون</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="stat-card">
                <div style="text-align: left; color: #00a8ff; font-size: 16px;">📷</div>
                <div class="stat-number">{rented_items}</div>
                <div class="stat-label">المؤجر الآن</div>
            </div>
            <div class="stat-card">
                <div style="text-align: left; color: #fbc531; font-size: 16px;">📅</div>
                <div class="stat-number">{len(st.session_state.bookings)}</div>
                <div class="stat-label">الحجوزات القادمة</div>
            </div>
        """, unsafe_allow_html=True)

    # قسم المبالغ المالية
    st.markdown("""
        <div class="money-card">
            <div style="color: #8b92a5; font-size: 12px;">المبالغ المتبقية لدى العملاء</div>
            <div class="money-amount">5,000 ريال</div>
        </div>
    """, unsafe_allow_html=True)

    # إحصائيات مالية مصغرة
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        st.markdown("""
            <div class="stat-card" style="padding: 12px;">
                <div class="stat-label">محصل التأجير</div>
                <div style="font-size: 16px; font-weight: bold; color: #ffffff; margin-top: 4px;">0 ريال</div>
            </div>
            <div class="stat-card" style="padding: 12px;">
                <div class="stat-label">ربح البيع المحصل</div>
                <div style="font-size: 16px; font-weight: bold; color: #8b92a5; margin-top: 4px;">مخفي</div>
            </div>
        """, unsafe_allow_html=True)

    with m_col2:
        st.markdown("""
            <div class="stat-card" style="padding: 12px;">
                <div class="stat-label">محصل البيع اليوم</div>
                <div style="font-size: 16px; font-weight: bold; color: #ffffff; margin-top: 4px;">0 ريال</div>
            </div>
            <div class="stat-card" style="padding: 12px;">
                <div class="stat-label">مصروفات اليوم</div>
                <div style="font-size: 16px; font-weight: bold; color: #ffffff; margin-top: 4px;">0 ريال</div>
            </div>
        """, unsafe_allow_html=True)

    # قسم أقرب مواعيد الإرجاع
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px; margin-bottom: 8px;">
            <span style="color: #f4c430; font-size: 12px; cursor: pointer;">عرض الكل</span>
            <span class="section-title" style="margin: 0;">أقرب مواعيد الإرجاع</span>
        </div>
        <div class="empty-box">
            لا توجد عمليات إرجاع قريبة.
        </div>
    """, unsafe_allow_html=True)

elif nav_option == "📷 المعدات":
    st.subheader("📦 إدارة مخزون المعدات")
    st.dataframe(st.session_state.inventory, use_container_width=True)
    
    with st.form("add_gear"):
        st.write("إضافة معدة جديدة")
        g_name = st.text_input("اسم المعدة")
        g_type = st.selectbox("النوع", ["كاميرا", "عدسة", "إضاءة", "صوت"])
        g_price = st.number_input("السعر اليومي ($)", value=50)
        if st.form_submit_button("حفظ المعدة") and g_name:
            new_row = pd.DataFrame([{"المعدة": g_name, "النوع": g_type, "الحالة": "متاح", "السعر اليومي ($)": g_price}])
            st.session_state.inventory = pd.concat([st.session_state.inventory, new_row], ignore_index=True)
            st.success(f"تمت إضافة {g_name} بنجاح!")
            st.rerun()

elif nav_option == "📑 التأجيرات":
    st.subheader("📑 سجل التأجيرات والحجوزات")
    if st.session_state.bookings.empty:
        st.info("لا توجد حجوزات مسجلة حالياً.")
    else:
        st.dataframe(st.session_state.bookings, use_container_width=True)

elif nav_option == "👥 العملاء":
    st.subheader("👥 قائمة العملاء")
    st.info("قسم إدارة العملاء والديون المرتبطة بهم.")

elif nav_option == "💳 المصروفات":
    st.subheader("💳 سجل المصروفات اليومية")
    expense_input = st.number_input("قيمة المصروف الجديد", min_value=0, value=0)
    if st.button("إضافة مصروف"):
        st.session_state.expenses += expense_input
        st.success(f"تم تسجيل المصروف بنجاح. الإجمالي: {st.session_state.expenses}")
