
import streamlit as st
from utils.classifier import classify_complaint
from utils.mapper import get_department
from utils.priority import get_priority
from utils.generator import generate_summary
from utils.database_manager import (
    create_table,
    insert_complaint
)

create_table()

st.title("📢 CivicPulse")

st.markdown(
    "### Submit Civic Complaint"
)

tab1, tab2, tab3 = st.tabs(
    [
        "📝 Text Complaint",
        "🎤 Voice Complaint",
        "📷 Image Complaint"
    ]
)

complaint = ""

with tab1:

    complaint = st.text_area(
        "Enter Complaint in Telugu",
        height=150
    )

with tab2:

    st.info(
        "Voice Complaint Module Coming Soon"
    )

with tab3:

    st.info(
        "Image Complaint Module Coming Soon"
    )

if st.button(
    "Analyze Complaint",
    use_container_width=True
):

    if complaint:

        category = classify_complaint(
            complaint
        )

        department = get_department(
            category
        )

        priority = get_priority(
            complaint
        )

        summary = generate_summary(
            complaint,
            category
        )

        tracking_id = insert_complaint(
            complaint,
            category,
            department,
            priority
        )

        st.success(
            f"Complaint Registered Successfully - {tracking_id}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Category",
                category
            )

        with col2:
            st.metric(
                "Department",
                department
            )

        with col3:
            st.metric(
                "Priority",
                priority
            )

        st.subheader(
            "Generated Complaint Summary"
        )

        st.write(summary)

        st.download_button(
            "Download Complaint",
            summary,
            file_name=f"{tracking_id}.txt"
        )

    else:

        st.warning(
            "Please enter a complaint."
        )

