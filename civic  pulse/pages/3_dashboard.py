
import streamlit as st
import plotly.express as px

from utils.database_manager import get_all_complaints

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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

[data-testid="metric-container"]{
    background:white;
    border-radius:16px;
    padding:10px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

st.info(
    "Use browser Back button to return to CivicPulse Home."
)

df = get_all_complaints()

st.markdown("""
<div style="
background:linear-gradient(
135deg,
#0F4C81,
#1976D2
);

padding:35px;
border-radius:20px;
color:white;
margin-bottom:25px;
">

<h1>📊 CivicPulse Intelligence Center</h1>

<p>
AI-Powered Civic Grievance Analytics
</p>

</div>
""", unsafe_allow_html=True)

if df.empty:

    st.warning(
        "No complaints available."
    )

    st.stop()

total = len(df)

pending = 0

if "status" in df.columns:
    pending = len(
        df[df["status"] == "Pending"]
    )

high = 0

if "priority" in df.columns:
    high = len(
        df[df["priority"] == "High"]
    )

departments = 0

if "department" in df.columns:
    departments = df["department"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("📨 Complaints", total)
c2.metric("⏳ Pending", pending)
c3.metric("🚨 High Priority", high)
c4.metric("🏢 Departments", departments)

st.divider()

if "category" in df.columns:

    category_counts = (
        df["category"]
        .value_counts()
        .reset_index()
    )

    category_counts.columns = [
        "Category",
        "Count"
    ]

    left, right = st.columns(2)

    with left:

        fig = px.bar(
            category_counts,
            x="Category",
            y="Count",
            title="Complaints by Category"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        fig = px.pie(
            category_counts,
            names="Category",
            values="Count"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.divider()

st.subheader(
    "📜 Recent Complaints"
)

st.dataframe(
    df,
    use_container_width=True
)
