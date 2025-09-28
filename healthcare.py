import streamlit as st

# Dummy hospital data
hospitals = [
    {"Hospital": "City Hospital", "Blood": ["A+", "B-"], "Organs": ["Kidney"]},
    {"Hospital": "Metro Care", "Blood": ["O+", "AB+"], "Organs": ["Liver", "Heart"]},
    {"Hospital": "LifeLine Hospital", "Blood": ["A-", "O-"], "Organs": ["Eye", "Lung"]},
]

st.set_page_config(page_title="Medical Help Portal", page_icon="🩺", layout="wide")

# ----------------- HERO SECTION -----------------
st.markdown(
    """
    <div style="text-align:center; padding:30px; background: linear-gradient(to right, #ef4444, #ec4899); color:white; border-radius:12px;">
        <h1>🩺 Medical Help Portal</h1>
        <p style="font-size:18px;">Request blood, organs, or connect with hospitals instantly</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# ----------------- REQUEST SECTION -----------------
st.subheader("🔎 Request Help")

col1, col2 = st.columns(2)

with col1:
    blood_group = st.selectbox(
        "Select Blood Group",
        ["", "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"],
    )

with col2:
    organ = st.selectbox(
        "Select Organ",
        ["", "Kidney", "Liver", "Heart", "Eye", "Lung"],
    )

# ----------------- FILTER HOSPITALS -----------------
if st.button("Search Availability"):
    filtered = []
    for h in hospitals:
        if (blood_group and blood_group in h["Blood"]) or (organ and organ in h["Organs"]):
            filtered.append(h)

    st.subheader("🏥 Available Hospitals")

    if filtered:
        for h in filtered:
            st.markdown(
                f"""
                <div style="border:1px solid #ddd; border-radius:10px; padding:15px; margin-bottom:10px;">
                    <h3>{h['Hospital']}</h3>
                    <p>🩸 <b>Blood:</b> {', '.join(h['Blood'])}</p>
                    <p>🫀 <b>Organs:</b> {', '.join(h['Organs'])}</p>
                    <button style="padding:8px 16px; background:#2563eb; color:white; border:none; border-radius:8px; cursor:pointer;">📞 Contact Hospital</button>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.warning("No matching hospitals found.")

# ----------------- FOOTER -----------------
st.markdown(
    """
    <hr>
    <div style="text-align:center; color:gray; padding:10px;">
        <p>© 2025 Medical Help Portal | Saving Lives Together</p>
    </div>
    """,
    unsafe_allow_html=True,
)
