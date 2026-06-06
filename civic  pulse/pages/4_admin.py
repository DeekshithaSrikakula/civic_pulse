import streamlit as st
from utils.database_manager import (
    get_all_complaints,
    update_status,
    delete_complaint
)
if (
    "logged_in" not in st.session_state
    or not st.session_state.logged_in
):
    st.error(
        "Please login first."
    )
    st.stop()

if st.session_state.role != "Officer":

    st.error(
        "Access Denied."
    )

    st.stop()
st.set_page_config(
    page_title="Officer Dashboard",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 Officer Dashboard")

st.markdown(
    "Manage civic complaints and update their status."
)

df = get_all_complaints()

if df.empty:

    st.warning(
        "No complaints available."
    )

else:

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    tracking_id = st.selectbox(
        "Select Complaint",
        df["tracking_id"]
    )

    status = st.selectbox(
        "Select Status",
        [
            "Pending",
            "In Progress",
            "Resolved",
            "Rejected"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "✅ Update Status",
            use_container_width=True
        ):

            st.write("Tracking ID:", tracking_id)
            st.write("Selected Status:", status)

            update_status(
                tracking_id,
                status
            )

            st.success(
                f"{tracking_id} updated to {status}"
            )

            st.rerun()

    with col2:

        if st.button(
            "🗑 Delete Complaint",
            use_container_width=True
        ):

            delete_complaint(
                tracking_id
            )

            st.success(
                f"{tracking_id} deleted successfully"
            )

            st.rerun()
total = len(df)

pending = len(
    df[df["status"] == "Pending"]
)

resolved = len(
    df[df["status"] == "Resolved"]
)

in_progress = len(
    df[df["status"] == "In Progress"]
)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Total", total)
c2.metric("Pending", pending)
c3.metric("In Progress", in_progress)
c4.metric("Resolved", resolved)