import streamlit as st

# --------------------------
# Set page config
# --------------------------
st.set_page_config(
    page_title="PryPround",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------
# Set background color (สีพื้นหลังแบบเดิม #f9f3ee)
# --------------------------
page_bg_color = """
    <style>
    .stApp {
        background-color: #f9f3ee;
    }
    </style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# --------------------------
# Handle navigation via session state
# --------------------------
if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Home"

# --------------------------
# Sidebar buttons as navigation
# --------------------------
with st.sidebar:
    if st.button("🏠 Home", key="sidebar_home"):
        st.session_state.menu = "🏠 Home"
    if st.button("🔐 Member Login", key="sidebar_member"):
        st.session_state.menu = "🔐 Member Login"
    if st.button("🔮 Vendor Login", key="sidebar_vendor"):
        st.session_state.menu = "🔮 Vendor Login"
    if st.button("📜 คำทำนายและสินค้าแนะนำ", key="sidebar_result"):
        st.session_state.menu = "📜 คำทำนายและสินค้าแนะนำ"

menu = st.session_state.menu

# --------------------------
# HOME PAGE
# --------------------------
if menu == "🏠 Home":
    st.markdown("<h1 style='color:#6B4C3B;'>🔮 MysticSense: แพลตฟอร์มดูดวงออนไลน์</h1>", unsafe_allow_html=True)
    st.write("เว็บไซต์ดูดวงออนไลน์ที่ให้คุณพบกับหมอดูจากทั่วไทย พร้อมระบบ AI แนะนำสินค้าเฉพาะคุณ ✨")

    st.markdown("---")

    # Banner ที่เปลี่ยนใหม่
    st.image("https://media.ganeshasnaga.com/2020/01/Ganeshas-Naga-for-web.jpg", use_column_width=True)

    st.markdown("---")
    
    st.markdown("## 📚 Freemium Content")
    st.write("อ่านบทความดูดวงฟรี เช่น ดวงประจำวัน ดวงความรัก การงาน การเงิน ฯลฯ")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="
            border: 1px solid #D2B48C; 
            padding: 15px; 
            border-radius: 10px; 
            background-color: #f9f3ee;
            text-align: center;">
            <h4>🔮 ดวงประจำวัน</h4>
            <p>อัปเดตดวงรายวันตามวันเกิด</p>
            <img src="https://raw.githubusercontent.com/wawaprachumphan/7104Project/main/%E0%B8%94%E0%B8%A7%E0%B8%87%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%88%E0%B8%B3%E0%B8%A7%E0%B8%B1%E0%B8%99.png" style="width: 100%; border-radius: 10px; margin-top: 10px;" />
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
            border: 1px solid #D2B48C; 
            padding: 15px; 
            margin-top: 10px;
            border-radius: 10px; 
            background-color: #f9f3ee;
            text-align: center;">
            <h4>❤️ ดวงความรัก</h4>
            <p>เช็คเสน่ห์ ความสัมพันธ์ และโอกาสความรักของคุณ</p>
            <img src="https://raw.githubusercontent.com/wawaprachumphan/7104Project/main/%E0%B8%94%E0%B8%A7%E0%B8%87%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B1%E0%B8%81.png" style="width: 100%; border-radius: 10px; margin-top: 10px;" />
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            border: 1px solid #D2B48C; 
            padding: 15px; 
            border-radius: 10px; 
            background-color: #f9f3ee;
            text-align: center;">
            <h4>💼 ดวงการงาน</h4>
            <p>ทำนายโอกาสงาน การโปรโมท หรือการเปลี่ยนงาน</p>
            <img src="https://raw.githubusercontent.com/wawaprachumphan/7104Project/main/%E0%B8%94%E0%B8%A7%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%87%E0%B8%B2%E0%B8%99.png" style="width: 100%; border-radius: 10px; margin-top: 10px;" />
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
            border: 1px solid #D2B48C; 
            padding: 15px; 
            margin-top: 10px;
            border-radius: 10px; 
            background-color: #f9f3ee;
            text-align: center;">
            <h4>💰 ดวงการเงิน</h4>
            <p>โชคลาภ รายได้ การลงทุน การใช้จ่าย</p>
            <img src="https://raw.githubusercontent.com/wawaprachumphan/7104Project/main/%E0%B8%94%E0%B8%A7%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%87%E0%B8%B4%E0%B8%99.png" style="width: 100%; border-radius: 10px; margin-top: 10px;" />
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔐 Member Login", key="home_member_btn"):
            st.session_state.menu = "🔐 Member Login"
            st.experimental_rerun()

    with col2:
        if st.button("🧙 Vendor Login", key="home_vendor_btn"):
            st.session_state.menu = "🔮 Vendor Login"
            st.experimental_rerun()


# --------------------------
# MEMBER LOGIN PAGE
# --------------------------
elif menu == "🔐 Member Login":
    st.markdown("## 🔐 เข้าสู่ระบบสำหรับสมาชิก")
    st.text_input("ชื่อผู้ใช้")
    st.text_input("อีเมล")
    st.text_input("วันเดือนปีเกิด")
    st.text_input("ราศี")
    st.text_input("รหัสผ่าน", type="password")
    st.button("เข้าสู่ระบบ", key="login_btn")

# --------------------------
# VENDOR LOGIN PAGE (ปรับใหม่แบ่ง 2 ส่วนตามขอ)
# --------------------------
elif menu == "🔮 Vendor Login":
    st.markdown("## 🧙 เข้าสู่ระบบสำหรับหมอดู")

    # ส่วน Login
    with st.container():
        st.markdown("### 🔐 Login")
        username = st.text_input("ชื่อผู้ใช้", key="vendor_username")
        email = st.text_input("อีเมล", key="vendor_email")
        password = st.text_input("รหัสผ่าน", type="password", key="vendor_password")
        if st.button("Login", key="vendor_login_btn"):
            if username and email and password:
                st.success(f"Login สำเร็จสำหรับ {username}")
            else:
                st.error("กรุณากรอกข้อมูลให้ครบทุกช่อง")

    st.markdown("---")

    # ส่วน สร้าง Slot การทำนาย
    with st.container():
        st.markdown("### 🗓️ สร้าง Slot การทำนาย")

        # ตัวอย่างรายชื่อลูกค้า (สมมติ)
        customer_list = ["ลูกค้า A", "ลูกค้า B", "ลูกค้า C", "ลูกค้า D"]
        selected_customer = st.selectbox("เลือกลูกค้า", options=customer_list, key="select_customer")

        selected_date = st.date_input("เลือกวันที่", key="slot_date")
        selected_time = st.time_input("เลือกเวลา", key="slot_time")

        if st.button("สร้าง Slot", key="create_slot_btn"):
            st.success(f"สร้าง Slot สำหรับ {selected_customer} วันที่ {selected_date} เวลา {selected_time} เรียบร้อยแล้ว")

# --------------------------
# RESULT PAGE
# --------------------------
elif menu == "📜 คำทำนายและสินค้าแนะนำ":
    st.markdown("## 📜 คำทำนายของคุณ")
    st.write("""
✨ ช่วงเวลานี้ดวงของคุณโดดเด่นเรื่องโชคลาภทางการงานอย่างชัดเจน โอกาสใหม่ ๆ และความสำเร็จรอคุณอยู่...
เปรียบเสมือนประตูสู่ความก้าวหน้าได้เปิดอ้าออกกว้าง พร้อมต้อนรับคุณให้ก้าวเข้าไปคว้าชัยชนะที่รอคอย

ยิ่งไปกว่านั้น พลังแห่งดวงดาวกำลังส่งเสริมให้คุณเป็นที่จับตามองของผู้หลักผู้ใหญ่หรือผู้มีอำนาจในการตัดสินใจ
นี่คือจังหวะทองที่คุณจะได้แสดงศักยภาพอย่างเต็มที่ ผลงานที่เคยสร้างไว้จะปรากฏเด่นชัด
และความสามารถของคุณจะได้รับการยอมรับในวงกว้าง

อย่าปล่อยให้โอกาสทองนี้หลุดลอยไป! เปิดใจรับสิ่งใหม่ๆ กล้าที่จะเสี่ยง และทุ่มเทอย่างสุดกำลัง
เพราะความสำเร็จครั้งยิ่งใหญ่กำลังรอคุณอยู่เบื้องหน้าอย่างแน่นอน
""")

    st.markdown("### 🎁 สินค้าแนะนำสำหรับคุณ")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://abovediamond.com/wp-content/uploads/2024/06/ring-style.jpg", caption="💍 แหวนเสริมดวง")
        st.write("แหวนดีไซน์พิเศษ ช่วยเสริมโชคลาภและความรัก")

    with col2:
        st.image("https://abovediamond.com/wp-content/uploads/2024/06/necklace-style.jpg", caption="📿 สร้อยคอพลังงาน")
        st.write("สร้อยคอที่ช่วยเสริมพลังงานบวก และความมั่นใจ")

    with col3:
        st.image("https://abovediamond.com/wp-content/uploads/2024/06/bracelet-style.jpg", caption="🧿 กำไลข้อมือพิเศษ")
        st.write("กำไลข้อมือช่วยป้องกันสิ่งไม่ดีและเสริมโชคลาภ")

