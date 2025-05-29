st.markdown("### 🎁 สินค้าแนะนำสำหรับคุณ")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/ring-style.jpg", caption="💍 แหวนเสริมดวง")
    st.write("แหวนดีไซน์พิเศษ ช่วยเสริมโชคลาภและความรัก")

with col2:
    st.image("images/necklace-style.jpg", caption="📿 สร้อยคอพลังงาน")
    st.write("สร้อยคอที่ช่วยเสริมพลังงานบวก และความมั่นใจ")

with col3:
    st.image("images/bracelet-style.jpg", caption="🧿 กำไลข้อมือพิเศษ")
    st.write("กำไลข้อมือช่วยป้องกันสิ่งไม่ดีและเสริมโชคลาภ")
