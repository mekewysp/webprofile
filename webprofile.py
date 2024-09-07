import streamlit as st

# Page configuration
st.set_page_config(page_title="Yossaphat Grachangpho", page_icon="🖥️")

# Title
st.title("🖥️ Myself 🖥️")

# Introduction
st.subheader("I'm Yossaphat Grachangpho (Kyu)")
st.write("""
- 2024 - Esport What? School Tour 2024 (8th Place)
- 2024 - ศิลปะหัตถกรรมครั้งที่ 71 (การสร้างเกมสร้างสรรค์จากคอมพิวเตอร์)
- 2024 - KMITL Future Innovator 2024 (Nano Technology National Level 2024)
- 2024 - K-Engineering World Tour and Workshop 2024, KMITL
- 2024 - First Aid & CPR Course at Debsirin School
""")

# Current Activities
st.subheader("🧑‍💻 What I'm Doing Now")
st.write("""
- 💻 Studying JavaScript, PHP
- 🎹 Practice Piano
- 🎮 Create Game by using HTMLs, CSS, JavaScript ("https://github.com/mekewysp/flappydeb")
- 🤖 Practice Arduino Skills
""")

# Tech Stack & Skills
st.subheader("📚 Tech Stack & Skills")

# Programming Languages
with st.expander("👨‍💻 Programming Languages"):
    st.image("https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54", use_column_width=True)
    st.image("https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E", use_column_width=True)
    st.image("https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white", use_column_width=True)

# Frontend Development
with st.expander("🪟 Frontend Development"):
    st.image("https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white", use_column_width=True)

# Backend Development
with st.expander("☠️ Backend Development"):
    st.image("https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white", use_column_width=True)

# Dev Tools
with st.expander("🐥 Dev Tools"):
    st.image("https://skillicons.dev/icons?i=git,github,gitlab,raspberrypi,arduino", use_column_width=True)

# My Skills
st.subheader("🐥 My Skills")
st.image("https://skillicons.dev/icons?i=python,cpp,js,java,php", use_column_width=True)

# Future Plans
st.subheader("🔮 What in Future")
st.write("""
- [ ] Study Computer Engineering (2026-2030)
- [ ] Working in ~~Software Development~~ User Experience Design&DevOps Engineer
""")

# Contact Information
st.subheader("📩 Connect with Me")
st.write("""
- 📩 yossaphat.gra@gmail.com
- 🔗 [Facebook](https://www.facebook.com/yossaphat.grachangpho.1?mibextid=ZbWKwL)
""")
# Footer
st.write("Thank you For Reading <3")
