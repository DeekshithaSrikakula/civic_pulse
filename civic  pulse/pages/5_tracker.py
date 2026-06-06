import streamlit as st

from utils.database_manager import (
    get_complaint_by_tracking_id
)

st.set_page_config(
    page_title="Complaint Tracker",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Complaint Tracker")

st.markdown(
    "Track your complaint using Tracking ID."
)

tracking_id = st.text_input(
    "Enter Tracking ID",
    placeholder="CP0001"
)

if st.button(
    "Track Complaint",
    use_container_width=True
):

    complaint = get_complaint_by_tracking_id(
        tracking_id
    )

    if complaint:

        st.success(
            "Complaint Found"
        )

        st.write(
            f"**Tracking ID:** {complaint[1]}"
        )

        st.write(
            f"**Complaint:** {complaint[2]}"
        )

        st.write(
            f"**Category:** {complaint[3]}"
        )

        st.write(
            f"**Department:** {complaint[4]}"
        )

        st.write(
            f"**Priority:** {complaint[5]}"
        )

        st.write(
            f"**Status:** {complaint[6]}"
        )

        st.write(
            f"**Created At:** {complaint[7]}"
        )

    else:

        st.error(
            "Tracking ID Not Found"
        )