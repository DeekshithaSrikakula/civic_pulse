import plotly.express as px

def category_chart(df):

    counts = (
        df["category"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "Category",
        "Count"
    ]

    fig = px.bar(
        counts,
        x="Category",
        y="Count",
        title="Complaint Categories"
    )

    return fig