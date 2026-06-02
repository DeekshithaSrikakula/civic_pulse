from utils.database_manager import insert_complaint
import streamlit as st

st.set_page_config(
    page_title="CivicPulse",
    page_icon="📢",
    layout="wide"
)

# Hide sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

.stApp{
background:#F4F7FA;
}
.stButton > button {

    background-color:#1976D2 !important;

    color:white !important;

    border:none !important;

    border-radius:10px !important;

    height:45px !important;

    font-weight:600 !important;
}
.hero{

background:linear-gradient(
135deg,
#0F4C81,
#1976D2
);

padding:80px;

border-radius:24px;

text-align:center;

margin-bottom:30px;

color:white !important;
}
.portal-card{

    background:white;

    color:#0F172A;

    padding:30px;

    border-radius:20px;

    text-align:center;

    box-shadow:
    0px 4px 15px rgba(
        0,0,0,0.08
    );

    min-height:180px;

    margin-bottom:10px;
}  

html, body, [class*="css"]  {
    color: #1E293B !important;
}
.portal-card h1,
.portal-card h2,
.portal-card h3,
.portal-card h4,
.portal-card h5,
.portal-card h6 {
    color:#0F172A !important;
}

p {
    color: #334155 !important;
}

label {
    color: #0F172A !important;
}

span {
    color: #0F172A !important;
}
div.stButton > button,
div[data-testid="stPageLink"] a {
    width: 100%;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "landing"

# =========================
# LANDING PAGE
# =========================

if st.session_state.page == "landing":

    st.markdown("""
    <div class='hero'>

    <h1>📢 CivicPulse</h1>

    <h3>
    AI-Powered Civic Grievance Platform
    </h3>

    <p>
    Submit civic complaints through
    Text • Voice • Image
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Civic Services")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.info("""
### 📝 Text Complaints

Submit complaints directly.
""")

    with c2:
        st.info("""
### 🎤 Voice Complaints

Speak instead of typing.
""")

    with c3:
        st.info("""
### 📷 Image Complaints

Upload complaint images.
""")

    st.markdown("## Civic Impact")

    m1,m2,m3,m4 = st.columns(4)

    m1.metric("Complaints", "12,450")
    m2.metric("Resolved", "9,860")
    m3.metric("Departments", "24")
    m4.metric("Languages", "3")

    st.write("")

    if st.button(
        "🚀 Explore Platform",
        use_container_width=True
    ):
        st.session_state.page = "portal"
        st.rerun()

# =========================
# PORTAL PAGE
# =========================

elif st.session_state.page == "portal":

    st.markdown("""
    <div class='hero'>
        <h1 style='color:white;'>CivicPulse Services</h1>
        <p style='color:white;'>Choose a service</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # ======================
    # COMPLAINT CARD
    # ======================

    with col1:

        st.markdown("""
        <div class='portal-card'>
            <div style='font-size:50px;'>📝</div>
            <h3>File Complaint</h3>
            <p>Submit Civic Issues</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Open Complaint",
            use_container_width=True,
            key="complaint_btn"
        ):
            st.session_state.page = "complaint"
            st.rerun()

    # ======================
    # DASHBOARD CARD
    # ======================

    with col2:

        st.markdown("""
        <div class='portal-card'>
            <div style='font-size:50px;'>📊</div>
            <h3>Dashboard</h3>
            <p>Analytics & Insights</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Open Dashboard",
            use_container_width=True,
            key="dashboard_btn"
        ):
            st.switch_page("pages/3_dashboard.py")

    # ======================
    # HISTORY CARD
    # ======================

    with col3:

        st.markdown("""
        <div class='portal-card'>
            <div style='font-size:50px;'>📜</div>
            <h3>History</h3>
            <p>Complaint Records</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Open History",
            use_container_width=True,
            key="history_btn"
        ):
            st.switch_page("pages/2_history.py")

    st.write("")

    if st.button("⬅ Back Home"):
        st.session_state.page = "landing"
        st.rerun()


# =========================
# COMPLAINT PAGE
# =========================

elif st.session_state.page == "complaint":

    st.title("📝 File Civic Complaint")

    if st.button("⬅ Back to Portal"):
        st.session_state.page="portal"
        st.rerun()

    tab1,tab2,tab3 = st.tabs(
        [
            "📝 Text",
            "🎤 Voice",
            "📷 Image"
        ]
    )

    complaint=""

    with tab1:

        complaint = st.text_area(
            "Describe your issue",
            height=200
        )

    with tab2:

        st.info(
            "Voice Recording Coming Soon"
        )

    with tab3:

        st.file_uploader(
            "Upload Complaint Image"
        )

    if st.button(
        "🚀 Analyze Complaint",
        use_container_width=True
    ):

        if complaint.strip() == "":

            st.warning(
                "Please enter a complaint."
            )

        else:

            category="Other"
            department="Citizen Support"
            priority="Low"

            if "చెత్త" in complaint:
                category="Garbage"
                department="GHMC"
                priority="Medium"

            elif "నీరు" in complaint:
                category="Water"
                department="Water Board"
                priority="High"

            tracking_id = insert_complaint(
            complaint,
            category,
            department,
            priority
            )

            st.success(
    f"Complaint Registered Successfully - {tracking_id}"
)

            c1,c2,c3 = st.columns(3)

            c1.metric("Category", category)
            c2.metric("Department", department)
            c3.metric("Priority", priority)