
import streamlit as st
from utils.database_manager import get_all_complaints

st.set_page_config(
    page_title="Complaint History",
    page_icon="📜",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background:#F4F7FA;
}

h1,h2,h3,h4,h5,h6{
    color:#0F172A !important;
}

p, label, span, div{
    color:#334155 !important;
}

[data-testid="stDataFrame"]{
    color:#0F172A !important;
}

</style>
""", unsafe_allow_html=True)

st.info(
    "Use browser Back button to return to CivicPulse Home."
)

st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:20px;
box-shadow:0px 4px 12px rgba(0,0,0,0.08);
">

<h1>📜 Complaint History</h1>

<p>
View all submitted complaints
</p>

</div>
""", unsafe_allow_html=True)

df = get_all_complaints()

if df.empty:

    st.warning(
        "No complaints found."
    )

else:

    st.dataframe(
        df,
        use_container_width=True
    )