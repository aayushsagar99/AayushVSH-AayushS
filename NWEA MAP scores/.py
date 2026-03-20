import pandas as pd
import plotly.express as px
import os
import time

# --- INITIAL SETTINGS ---
FILE_NAME = "map_growth_data.csv"
chances = 3

def load_data():
    """Safely load the CSV or return an empty DataFrame with the correct columns."""
    if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
        return pd.read_csv(FILE_NAME)
    return pd.DataFrame(columns=['Grade', 'Timeline', 'Season', 'Subject', 'Score', 'Goal', 'Type'])

def save_data(df):
    """Save the current progress to the CSV file."""
    df.to_csv(FILE_NAME, index=False)
    print(f"\n✅ Data secure! Your journey is saved to {FILE_NAME}!")

# MAIN APP LOOP
while chances > 0:
    df_old = load_data()
    
    print("\n--- ⚙️ Settings ⚙️ ---")
    start_grade_in = input("Enter starting grade (e.g. 3) [Enter to skip]: ")
    
    # If the user just presses Enter, they lose a chance
    if not start_grade_in:
        chances -= 1
        if chances > 0:
            print(f"⚠️ No grade entered. You have {chances} chances left before logout.")
            continue
        else:
            break # Exit to the countdown
            
    start_grade = int(start_grade_in)
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
                # Check for existing data
                match = df_old[(df_old['Grade'] == g) & 
                               (df_old['Timeline'] == f"G{g} {s}") & 
                               (df_old['Subject'] == sub)]
                
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
                    all_entries.append({
                        'Grade': g, 'Timeline': f"G{g} {s}", 'Season': s, 
                        'Subject': sub, 'Score': score, 'Goal': curr_goal, 'Type': 'Actual'
                    })
                
                # AUTOMATIC PROJECTION
                if s == 'Spring' and score is None and fall_score and winter_score:
                    proj_score = winter_score + (winter_score - fall_score)
                    all_entries.append({
                        'Grade': g, 'Timeline': f"G{g} {s}", 'Season': s, 
                        'Subject': sub, 'Score': proj_score, 'Goal': curr_goal, 'Type': 'Projected'
                    })

    df = pd.DataFrame(all_entries)

    # 3. BUILD THE DASHBOARD
    if not df.empty:
        save_data(df)
        
        fig = px.line(df, x='Timeline', y='Score', color='Subject', line_dash='Type',
                    title='🏆 MAP GROWTH HALL OF FAME 🏆', markers=True,
                    hover_data={'Score': True, 'Goal': True, 'Type': True})

        # --- CONTINUOUS GOAL PATH ---
        for sub in subjects:
            sub_df = df[df['Subject'] == sub].copy()
            # Set Fall goal equal to Fall score so the line starts at your baseline
            sub_df.loc[sub_df['Season'] == 'Fall', 'Goal'] = sub_df.loc[sub_df['Season'] == 'Fall', 'Score']
            
            goal_path = sub_df.dropna(subset=['Goal'])
            if not goal_path.empty:
                fig.add_scatter(x=goal_path['Timeline'], y=goal_path['Goal'], 
                                name=f'{sub} Goal Line', 
                                line=dict(dash='dot', width=2, color='gold'),
                                mode='lines+markers', marker=dict(symbol="star", size=10))

        # --- ALL-TIME HIGHEST SCORE TROPHY ---
        for sub in subjects:
            actuals = df[(df['Subject'] == sub) & (df['Type'] == 'Actual')]
            if not actuals.empty:
                best_row = actuals.loc[actuals['Score'].idxmax()]
                fig.add_annotation(x=best_row['Timeline'], y=best_row['Score'], text="🏆", 
                                showarrow=True, arrowhead=2, arrowcolor="yellow", 
                                font=dict(size=20), yshift=15)

        fig.update_xaxes(categoryorder='array', categoryarray=df['Timeline'].unique())
        fig.update_layout(template="plotly_dark", hovermode="x unified", 
                        paper_bgcolor="#111", plot_bgcolor="#111")
        fig.show()

        # 4. CELEBRATION SUMMARY
        print("\n" + "✨"*15)
        for sub in subjects:
            best = df[df['Subject'] == sub]['Score'].max()
            if pd.notna(best):
                print(f"🥇 Personal Record ({sub}): {best} RIT points! ✨")
        print("✨"*15)
        
        # Break loop after showing chart so it doesn't immediately ask for settings again
        input("\nPress Enter to return to settings or close the window...")
    else:
        chances -= 1
        print(f"\n📭 No data to display! You have {chances} chances left.")

# 5. LOGOUT COUNTDOWN
print("\n--- ⚠️ SESSION EXPIRING ---")
logout_timer = 5
while logout_timer > 0:
    print(f"Logging out in {logout_timer} seconds...  ", end="\r")
    time.sleep(1)
    logout_timer -= 1

print("\nLogged out successfully. Goodbye! 👋")
