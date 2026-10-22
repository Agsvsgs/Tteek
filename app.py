import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# إعداد الصفحة بثيم داكن وتخطيط واسع
st.set_page_config(
    page_title="Teek Studio - نظام إدارة الاستوديو",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تخصيص التصميم والألوان لتطابق واجهة Teek Studio الفخمة
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

if 'rentals' not in st.session_state:
    st.session_state.rentals = pd.DataFrame([
        {"اسم العميل": "أحمد محمد", "المعدة": "Sony FX3", "تاريخ البدء": "2026-10-20", "تاريخ الإرجاع": "2026-10-23", "الإجمالي ($)": 450, "الحالة": "نشط"}
    ])

if 'bookings' not in st.session_state:
    st.session_state.bookings = pd.DataFrame([
        {"اسم العميل": "خالد علي", "المعدة": "Canon EOS R5", "موعد الحجز": "2026-10-25", "الحالة": "قيد الانتظار"}
    ])

if 'customers' not in st.session_state:
    st.session_state.customers = pd.DataFrame([
        {"اسم العميل": "أحمد محمد", "رقم الجوال": "777123456", "الديون المتبقية ($)": 0, "ملاحظات": "عميل مميز"},
        {"اسم العميل": "خالد علي", "رقم الجوال": "777987654", "الديون المتبقية ($)": 120, "ملاحظات": "حجز قادم"}
    ])

# القائمة الرئيسية للتنقل بين الأقسام
nav_option = st.sidebar.selectbox("القائمة الرئيسية", ["🏠 الرئيسية", "📑 التأجيرات", "📅 الحجوزات", "👥 العملاء", "📦 المخزون"])

if nav_option == "🏠 الرئيسية":
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

    total_items = len(st.session_state.inventory)
    rented_items = len(st.session_state.inventory[st.session_state.inventory['الحالة'] == 'مؤجر'])
    available_items = total_items - rented_items

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

    st.markdown("""
        <div class="money-card">
            <div style="color: #8b92a5; font-size: 12px;">المبالغ المتبقية لدى العملاء</div>
            <div class="money-amount">5,000 ريال</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px; margin-bottom: 8px;">
            <span style="color: #f4c430; font-size: 12px; cursor: pointer;">عرض الكل</span>
            <span class="section-title" style="margin: 0;">أقرب مواعيد الإرجاع</span>
        </div>
        <div class="empty-box">
            لا توجد عمليات إرجاع قريبة.
        </div>
    """, unsafe_allow_html=True)

elif nav_option == "📑 التأجيرات":
    st.subheader("📑 قسم التأجيرات النشطة")
    st.dataframe(st.session_state.rentals, use_container_width=True)
    
    with st.form("add_rental"):
        st.write("إضافة عملية تأجير جديدة")
        r_client = st.text_input("اسم العميل")
        r_gear = st.selectbox("المعدة", st.session_state.inventory[st.session_state.inventory['الحالة'] == 'متاح']['المعدة'].tolist() if not st.session_state.inventory.empty else ["لا توجد معدات متاحة"])
        r_days = st.number_input("عدد الأيام", min_value=1, value=2)
        if st.form_submit_button("تأكيد وحفظ التأجير") and r_client:
            new_r = pd.DataFrame([{"اسم العميل": r_client, "المعدة": r_gear, "تاريخ البدء": datetime.now().strftime("%Y-%m-%d"), "تاريخ الإرجاع": (datetime.now() + timedelta(days=r_days)).strftime("%Y-%m-%d"), "الإجمالي ($)": 150 * r_days, "الحالة": "نشط"}])
            st.session_state.rentals = pd.concat([st.session_state.rentals, new_r], ignore_index=True)
            st.session_state.inventory.loc[st.session_state.inventory['المعدة'] == r_gear, 'الحالة'] = 'مؤجر'
            st.success("تم تسجيل التأجير بنجاح!")
            st.rerun()

elif nav_option == "📅 الحجوزات":
    st.subheader("📅 قسم الحجوزات القادمة")
    st.dataframe(st.session_state.bookings, use_container_width=True)
    
    with st.form("add_booking"):
        st.write("تسجيل حجز جديد")
        b_client = st.text_input("اسم العميل للحجز")
        b_gear = st.text_input("المعدة المطلوبة")
        if st.form_submit_button("حفظ الحجز") and b_client:
            new_b = pd.DataFrame([{"اسم العميل": b_client, "المعدة": b_gear, "موعد الحجز": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"), "الحالة": "قيد الانتظار"}])
            st.session_state.bookings = pd.concat([st.session_state.bookings, new_b], ignore_index=True)
            st.success("تم إضافة الحجز بنجاح!")
            st.rerun()

elif nav_option == "👥 العملاء":
    st.subheader("👥 قاعدة بيانات العملاء")
    st.dataframe(st.session_state.customers, use_container_width=True)
    
    with st.form("add_customer"):
        st.write("إضافة عميل جديد")
        c_name = st.text_input("اسم العميل الكامل")
        c_phone = st.text_input("رقم الجوال")
        c_note = st.text_input("ملاحظات")
        if st.form_submit_button("حفظ العميل") and c_name:
            new_c = pd.DataFrame([{"اسم العميل": c_name, "رقم الجوال": c_phone, "الديون المتبقية ($)": 0, "ملاحظات": c_note}])
            st.session_state.customers = pd.concat([st.session_state.customers, new_c], ignore_index=True)
            st.success("تم حفظ العميل بنجاح!")
            st.rerun()

elif nav_option == "📦 المخزون":
    st.subheader("📦 إدارة المخزون")
    st.dataframe(st.session_state.inventory, use_container_width=True)
