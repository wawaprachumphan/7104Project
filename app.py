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
    if st.button("Home", key="sidebar_home"):
        st.session_state.menu = "Home"
    if st.button("Member Login", key="sidebar_member"):
        st.session_state.menu = "Member Login"
    if st.button("Vendor Login", key="sidebar_vendor"):
        st.session_state.menu = "Vendor Login"
    if st.button("คำทำนายและสินค้าแนะนำ", key="sidebar_result"):
        st.session_state.menu = "คำทำนายและสินค้าแนะนำ"

menu = st.session_state.menu

# --------------------------
# HOME PAGE
# --------------------------
if menu == "Home":
    st.markdown("<h1 style='color:#6B4C3B;'>🔮 PryPround</h1>", unsafe_allow_html=True)
    st.write("เว็บไซต์ดูดวงออนไลน์ที่ให้คุณพบกับหมอดูจากทั่วไทย พร้อมระบบ AI แนะนำสินค้าเฉพาะคุณ ✨")

    st.markdown("---")

    # Banner ที่เปลี่ยนใหม่
    st.image("https://media.ganeshasnaga.com/2020/01/Ganeshas-Naga-for-web.jpg", use_container_width=True)

    st.markdown("---")
    
    st.markdown("## Freemium Content")
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
            <h4>ดวงประจำวัน</h4>
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
            <h4>❤ดวงความรัก</h4>
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
            <h4>ดวงการงาน</h4>
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
            <h4>ดวงการเงิน</h4>
            <p>โชคลาภ รายได้ การลงทุน การใช้จ่าย</p>
            <img src="https://raw.githubusercontent.com/wawaprachumphan/7104Project/main/%E0%B8%94%E0%B8%A7%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%87%E0%B8%B4%E0%B8%99.png" style="width: 100%; border-radius: 10px; margin-top: 10px;" />
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Member Login", key="home_member_btn"):
            st.session_state.menu = "Member Login"
            st.experimental_rerun()

    with col2:
        if st.button("Vendor Login", key="home_vendor_btn"):
            st.session_state.menu = "Vendor Login"
            st.experimental_rerun()


# --------------------------
# MEMBER LOGIN PAGE
# --------------------------
elif menu == "Member Login":
    st.markdown("## เข้าสู่ระบบสำหรับสมาชิก")
    email = st.text_input("Email", key="member_email")
    password = st.text_input("Password", type="password", key="member_password")
    if st.button("เข้าสู่ระบบ", key="member_login_btn"):
        if email and password:
            st.success(f"Login สำเร็จสำหรับสมาชิกที่ใช้ Email: {email}")
        else:
            st.error("กรุณากรอก Email และ Password ให้ครบ")

# --------------------------
# VENDOR LOGIN PAGE
# --------------------------
elif menu == "Vendor Login":
    st.markdown("## เข้าสู่ระบบสำหรับหมอดู")
    email = st.text_input("Email", key="vendor_email")
    password = st.text_input("Password", type="password", key="vendor_password")
    if st.button("เข้าสู่ระบบ", key="vendor_login_btn"):
        if email and password:
            st.success(f"Login สำเร็จสำหรับหมอดูที่ใช้ Email: {email}")
        else:
            st.error("กรุณากรอก Email และ Password ให้ครบ")

    st.markdown("---")

    # ส่วน สร้าง Slot การทำนาย
    with st.container():
        st.markdown("### 🗓สร้าง Slot การทำนาย")

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
elif menu == "คำทำนายและสินค้าแนะนำ":
    st.markdown("## คำทำนายของคุณ")
    st.write("""
    ✨ ช่วงเวลานี้ดวงของคุณโดดเด่นเรื่องโชคลาภทางการงานอย่างชัดเจน โอกาสใหม่ ๆ และความสำเร็จรอคุณอยู่
    ดวงชะตาของคุณกำลังเปิดประตูสู่โอกาสสำคัญที่ไม่ควรพลาด ความมุ่งมั่นและความตั้งใจของคุณจะนำพาความรุ่งเรือง
    และผลตอบแทนที่ดีอย่างต่อเนื่อง ไม่ว่าจะเป็นโปรเจกต์ใหม่ การขยับขยายตำแหน่ง หรือการได้รับเกียรติยศในสายงาน
    ทั้งหมดนี้จะเกิดขึ้นในช่วงเวลานี้อย่างเด่นชัด ดังนั้นจงเตรียมพร้อมและรับมือกับความสำเร็จที่จะเข้ามาอย่างมั่นใจ
    """)
    st.markdown("### สินค้าแนะนำสำหรับคุณ")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "https://abovediamond.com/wp-content/uploads/2024/06/ring-style.jpg",
            caption="💍 แหวนเสริมดวง - แหวนนี้ถูกออกแบบมาเพื่อเสริมโชคลาภและความมั่งคั่ง",
            use_column_width=True
        )
        st.button("ซื้อแหวน", key="buy_ring")

    with col2:
        st.image(
            "https://cdn.shopify.com/s/files/1/0680/4150/7113/products/horoscopecrystalset_2_1400x.jpg?v=1667579769",
            caption="🔮 เซตคริสตัลดูดวง - ช่วยเพิ่มพลังงานบวกและเสริมโชคลาภ",
            use_column_width=True
        )
        st.button("ซื้อคริสตัล", key="buy_crystal")

    with col3:
        st.image(
            "https://img.purichshop.com/2021/09/%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B1%E0%B8%AA%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B8%A3%E0%B8%93%E0%B9%8C-1-1.jpg",
            caption="📿 สร้อยข้อมือเสริมดวง - เพิ่มเสน่ห์และความมั่นใจ",
            use_column_width=True
        )
        st.button("ซื้อสร้อยข้อมือ", key="buy_bracelet")
