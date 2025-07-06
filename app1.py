import streamlit as st
import pandas as pd
import webbrowser
import os

# CSV file path
csv_file = "riyadh_barbershop_data.csv"

# Ensure CSV exists with correct headers
if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=[
        "اسم الصالون", "الحي", "العنوان", "رقم الجوال", "رابط الإنستغرام", "رابط الواتساب", "ملاحظات", "رابط البحث"])
    df.to_csv(csv_file, index=False, encoding="utf-8-sig")

st.title("📋 Riyadh Barbershop Data Entry")

# Form UI
with st.form("barber_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("اسم الصالون")
        district = st.text_input("الحي")
        address = st.text_input("العنوان")
        phone = st.text_input("رقم الجوال")
    with col2:
        instagram = st.text_input("رابط الإنستغرام")
        whatsapp = st.text_input("رابط الواتساب")
        notes = st.text_area("ملاحظات")
        search_link = st.text_input("رابط البحث")

    submitted = st.form_submit_button("💾 Save Entry")

    if submitted:
        new_entry = {
            "اسم الصالون": name,
            "الحي": district,
            "العنوان": address,
            "رقم الجوال": phone,
            "رابط الإنستغرام": instagram,
            "رابط الواتساب": whatsapp,
            "ملاحظات": notes,
            "رابط البحث": search_link
        }

        df = pd.read_csv(csv_file, encoding="utf-8-sig")
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(csv_file, index=False, encoding="utf-8-sig")
        st.success("تم حفظ البيانات بنجاح ✅")

# Option to open search link manually
st.markdown("---")
st.subheader("🔎 Open Google Maps Link")
open_link = st.text_input("أدخل رابط البحث هنا:")
if st.button("فتح الرابط في المتصفح"):
    if open_link:
        webbrowser.open(open_link)
    else:
        st.warning("يرجى إدخال رابط صالح.")
