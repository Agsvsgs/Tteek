import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# إعداد الصفحة وتدعم اللغة العربية
st.set_page_config(page_title="نظام تأجير معدات التصوير - تجريبي", layout="wide")

st.title("📷 نظام إدارة وتأجير معدات التصوير (نسخة تجريبية MVP)")
st.write("نظام داخلي لإدارة المخزون وتسجيل الحجوزات بالذكاء الاصطناعي.")

# 1. قاعدة بيانات المخزون المبدئية (Session State لحفظ البيانات أثناء الاستخدام)
if 'inventory' not in st.session_state:
    st.session_state.inventory = pd.DataFrame([
        {"المعدة": "Sony FX3", "النوع": "كاميرا", "الحالة": "متاح", "السعر اليومي ($)": 150},
        {"المعدة": "Canon EOS R5", "النوع": "كاميرا", "الحالة": "متاح", "السعر اليومي ($)": 120},
        {"المعدة": "Sony 24-70mm f/2.8", "النوع": "عدسة", "الحالة": "مؤجر", "السعر اليومي ($)": 50},
        {"المعدة": "Godox SK400", "النوع": "إضاءة", "الحالة": "متاح", "السعر اليومي ($)": 30},
        {"المعدة": "Rode Wireless GO II", "النوع": "صوت", "الحالة": "متاح", "السعر اليومي ($)": 25},
    ])

if 'bookings' not in st.session_state:
    st.session_state.bookings = pd.DataFrame(columns=["اسم العميل", "المعدة", "تاريخ البدء", "تاريخ الإرجاع", "الإجمالي ($)"])

# القائمة الجانبية للتنقل
menu = st.sidebar.selectbox("القائمة الرئيسية", ["لوحة المخزون", "حجز ذكي (AI Parser)", "سجل الحجوزات"])

if menu == "لوحة المخزون":
    st.subheader("📦 حالة المخزون الحالي")
    st.dataframe(st.session_state.inventory, use_container_width=True)
    
    st.markdown("---")
    st.subheader("إضافة معدة جديدة للمخزون")
    with st.form("add_item"):
        new_name = st.text_input("اسم المعدة")
        new_type = st.selectbox("النوع", ["كاميرا", "عدسة", "إضاءة", "صوت", "اكسسوارات"])
        new_price = st.number_input("السعر اليومي ($)", min_value=5, value=50)
        submitted = st.form_submit_button("إضافة للمخزون")
        if submitted and new_name:
            new_row = pd.DataFrame([{"المعدة": new_name, "النوع": new_type, "الحالة": "متاح", "السعر اليومي ($)": new_price}])
            st.session_state.inventory = pd.concat([st.session_state.inventory, new_row], ignore_index=True)
            st.success(تمت إضافة {new_name} بنجاح!)
            st.rerun()

elif menu == "حجز ذكي (AI Parser)":
    st.subheader("🤖 إدخال حجز ذكي بالنص الحر")
    st.write("اكتب طلب الحجز بشكل طبيعي، وسيقوم النظام باستخراج التفاصيل:")
    
    sample_text = "حجز أحمد محمد كاميرا Sony FX3 ليوم غد وإرجاعها بعد يومين"
    user_input = st.text_area("أدخل تفاصيل الحجز:", value=sample_text, height=100)
    
    if st.button("معالجة وتحليل الحجز ذكياً"):
        # محاكاة تحليل الذكاء الاصطناعي للنص
        st.success("تم تحليل النص بنجاح بواسطة محرك الذكاء الاصطناعي التجريبي:")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("اسم العميل", "أحمد محمد")
        col2.metric("المعدة المطلوبة", "Sony FX3")
        col3.metric("مدة التأجير", "يومان")
        
        # زر تأكيد وحفظ الحجز
        if st.button("تأكيد وحفظ الحجز في النظام"):
            start_date = datetime.now().strftime("%Y-%m-%d")
            end_date = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")
            price = 150 * 2
            
            new_booking = pd.DataFrame([{
                "اسم العميل": "أحمد محمد",
                "المعدة": "Sony FX3",
                "تاريخ البدء": start_date,
                "تاريخ الإرجاع": end_date,
                "الإجمالي ($)": price
            }])
            st.session_state.bookings = pd.concat([st.session_state.bookings, new_booking], ignore_index=True)
            
            # تحديث حالة المعدة في المخزون
            st.session_state.inventory.loc[st.session_state.inventory['المعدة'] == 'Sony FX3', 'الحالة'] = 'مؤجر'
            st.success("تم تسجيل الحجز وتحديث حالة المخزون بنجاح!")

elif menu == "سجل الحجوزات":
    st.subheader("📋 سجل الحجوزات الحالية والسابقة")
    if st.session_state.bookings.empty:
        st.info("لا توجد حجوزات مسجلة حتى الآن.")
    else:
        st.dataframe(st.session_state.bookings, use_container_width=True)
