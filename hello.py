from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()
df = get_df("personality_dataset")

text("# Personality Trait Explorer")
text("## Visualizing Social Behavior Data")
text("This app analyzes social interaction patterns and personality traits.")

sql = """
SELECT * FROM personality_dataset
WHERE Social_event_attendance > 10
"""
filtered_df = query(sql, "personality_dataset")

table(filtered_df, title="High Social Event Attendance")

fig = px.scatter(
    df,
    x="Time_spent_Alone",
    y="Social_event_attendance",
    color="Personality_Type",
    title="Alone Time vs. Social Attendance"
)
plotly(fig)
