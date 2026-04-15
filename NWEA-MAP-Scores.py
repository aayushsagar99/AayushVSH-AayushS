import pandas as pd
import plotly.express as px
import os

# --- FILE SETTINGS ---
FILE_NAME = "map_growth_data.csv"

def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    return pd.DataFrame(columns=['Grade', 'Timeline', 'Season', 'Subject', 'Score', 'Goal', 'Type'])

def save_data(df):
    df.to_csv(FILE_NAME, index=False)
    print(f"\n✅ Data secure! Your journey is saved to {FILE_NAME}!")

# 1. INITIAL SETUP
df_old = load_data()
start_grade = int(input("Enter starting grade (e.g. 3): ") or 3)
end_grade = int(input("Enter ending grade (e.g. 8): ") or 8)

seasons = ['Fall', 'Winter', 'Spring']
subjects = ['Math', 'Reading']
all_entries = []

# 2. DATA ENTRY LOOP
print(f"\n--- 🏆 MAP ACHIEVEMENT TRACKER 🏆 ---")
for g in range(start_grade, end_grade + 1):
    for sub in subjects:
        fall_score, winter_score = None, None
        
        for s in seasons:
            match = df_old[(df_old['Grade'] == g) & (df_old['Timeline'] == f"G{g} {s}") & (df_old['Subject'] == sub)]
            
            if not match.empty:
                score = float(match.iloc[0]['Score'])
                curr_goal = float(match.iloc[0]['Goal']) if pd.notna(match.iloc[0]['Goal']) else None
                print(f"  [Record Found] G{g} {s} {sub}: {score}")
            else:
                curr_goal = None
                if s != 'Fall':
                    goal_in = input(f"  🎯 {sub} Goal for Grade {g} in {s}: ")
                    curr_goal = float(goal_in) if goal_in else 0
                
                score_in = input(f"  📈 {sub} Score for Grade {g} in {s} (Enter to skip): ")
                score = float(score_in) if score_in else None
            
            if s == 'Fall': fall_score = score
            if s == 'Winter': winter_score = score
            
            if score is not None:
                all_entries.append({'Grade': g, 'Timeline': f"G{g} {s}", 'Season': s, 'Subject': sub, 'Score': score, 'Goal': curr_goal, 'Type': 'Actual'})
            
            if s == 'Spring' and score is None and fall_score and winter_score:
                proj_score = winter_score + (winter_score - fall_score)
                all_entries.append({'Grade': g, 'Timeline': f"G{g} {s}", 'Season': s, 'Subject': sub, 'Score': proj_score, 'Goal': curr_goal, 'Type': 'Projected'})

df = pd.DataFrame(all_entries)
save_data(df)

# 3. BUILD THE DASHBOARD
fig = px.line(df, x='Timeline', y='Score', color='Subject', line_dash='Type',
              title='🏆 MAP GROWTH HALL OF FAME 🏆', markers=True,
              hover_data={'Score':True, 'Goal':True, 'Type':True})

# ADD GOLD STAR GOALS
goal_df = df.dropna(subset=['Goal'])
for sub in subjects:
    sub_goal = goal_df[goal_df['Subject'] == sub]
    fig.add_scatter(x=sub_goal['Timeline'], y=sub_goal['Goal'], name=f'{sub} Target', mode='markers', marker=dict(symbol="star", size=10, color='gold'))

# --- NEW: ALL-TIME HIGHEST SCORE TROPHY ---
for sub in subjects:
    actuals = df[(df['Subject'] == sub) & (df['Type'] == 'Actual')]
    if not actuals.empty:
        best_row = actuals.loc[actuals['Score'].idxmax()]
        fig.add_annotation(x=best_row['Timeline'], y=best_row['Score'], text="🏆", showarrow=True, arrowhead=2, arrowcolor="yellow", font=dict(size=20), yshift=10)

# FINISHING TOUCHES
fig.update_xaxes(categoryorder='array', categoryarray=df['Timeline'].unique())
fig.update_layout(template="plotly_dark", hovermode="x unified", paper_bgcolor="#111", plot_bgcolor="#111")
fig.show()

# 4. CELEBRATION SUMMARY
print("\n" + "✨"*15)
for sub in subjects:
    best = df[df['Subject'] == sub]['Score'].max()
    print(f"🥇 Personal Record ({sub}): {best} RIT points!")
print("✨"*15)
