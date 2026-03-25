import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import time

# --- INITIAL SETTINGS ---
FILE_NAME = "map_growth_data.csv"
LEADERBOARD_PATH = "leaderboard.csv"
EXPORT_NAME = "map_growth_dashboard.html"

BOSS_DATA = [
    (700, "GOD", "🏆x9 HYPERMEGA...", "3.14", "What is Pi to 2 decimal places?"),
    (650, "GODZILLA", "🏆x8 MEGAULTRA...", "4", "Simplify (x+4)(x-4). If it equals 0, what is positive x?"),
    (230, "ELEPHANT", "🧠 GENIUS", "3/4", "Which is larger: 3/4 or 5/8?"),
    (220, "BEAR", "🎓 SCHOLAR", "18", "What is the perimeter of a 5x4 rectangular garden?"),
    (200, "TIGER", "⚔️ STRIKER", "20", "How many stickers are in 4 rows of 5?"),
    (0,   "SLIME", "🌱 APPRENTICE", "4", "What is 2 + 2?")
]

def get_badge(score):
    for threshold, name, badge, ans, quest in BOSS_DATA:
        if score >= threshold: return badge
    return "🌱 APPRENTICE"

def load_data():
    # 🛡️ Safety: Only read if file exists AND is not empty
    if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
        df = pd.read_csv(FILE_NAME)
        if 'Goal' not in df.columns: df['Goal'] = 0
        return df
    return pd.DataFrame(columns=['Grade', 'Timeline', 'Season', 'Subject', 'Score', 'Goal'])

def update_leaderboard(name, score):
    # 🛡️ Safety: Only read if file exists AND is not empty
    if os.path.exists(LEADERBOARD_PATH) and os.path.getsize(LEADERBOARD_PATH) > 0:
        ldf = pd.read_csv(LEADERBOARD_PATH)
    else:
        ldf = pd.DataFrame(columns=['Name', 'Score'])
    
    new_entry = pd.DataFrame([{'Name': name, 'Score': score}])
    ldf = pd.concat([ldf, new_entry]).sort_values(by='Score', ascending=False).drop_duplicates(subset=['Name'])
    ldf.to_csv(LEADERBOARD_PATH, index=False)
    
    print("\n" + "💎" * 3 + " DIAMOND RANKINGS " + "💎" * 3)
    for i, (idx, row) in enumerate(ldf.head(5).iterrows()):
        tag = "👑 CHAMP" if i == 0 else f"#{i+1}"
        print(f"{tag} {row['Name']}: {row['Score']} ({get_badge(row['Score'])})")


def start_boss_fight(current_score):
    # b[0] selects the score threshold from the tuple (e.g., 700, 650, etc.)
    target = next((b for b in reversed(BOSS_DATA) if b[0] > current_score), None)

    if not target:
        print("\n🌌 YOU ARE THE DIAMOND GOD!"); return
    threshold, name, badge, answer, question = target
    print(f"\n👹 BOSS ALERT: {name} ({badge})\n❓ MATH CHALLENGE: {question}")
    if input("📝 Answer: ").strip() == answer:
        print(f"✨ CRITICAL HIT! {name} defeated! You found a 💎 DIAMOND!")
    else: print(f"🛡️ Blocked! Correct answer was {answer}. Keep practicing!")

# --- 🚀 MAIN ENGINE ---
print("🔥 Welcome to the MAP Achievement Tracker!")
player_name = input("Enter Hero Name (or type 'RESET' to clear all names): ")

# --- 🧹 RESET LOGIC ---
if player_name.upper() == 'RESET':
    confirm = input("⚠️ Are you sure you want to delete all names and scores? (y/n): ")
    if confirm.lower() == 'y':
        if os.path.exists(FILE_NAME): os.remove(FILE_NAME)
        if os.path.exists(LEADERBOARD_PATH): os.remove(LEADERBOARD_PATH)
        print("🧹 Everything cleared! Restart the program to begin a fresh journey.")
        exit()
    else:
        player_name = input("Enter Hero Name to continue: ")

df_old = load_data()

try:
    g_start = int(input("Starting Grade (e.g. 3): ") or 3)
    g_end = int(input("Ending Grade [Default 8]: ") or 8)
except ValueError:
    print("❌ Numbers only!"); exit()

subjects, seasons, all_entries = ['Math', 'Reading'], ['Fall', 'Winter', 'Spring'], []

for g in range(g_start, g_end + 1):
    for sub in subjects:
        for s in seasons:
            match = df_old[(df_old['Grade'] == g) & (df_old['Timeline'] == f"G{g} {s}") & (df_old['Subject'] == sub)]
            if not match.empty:
                # Change this line inside your loop:
                if not match.empty:
                    row = match.iloc[0]  # <--- Add the [0] here!
                    score, curr_goal = row['Score'], row['Goal']

                score, curr_goal = row['Score'], row['Goal']
                print(f"✅ Found G{g} {s} {sub}: {score if pd.notna(score) else 'Goal: ' + str(curr_goal)}")
            else:
                curr_goal = float(input(f"🎯 {sub} Goal G{g} {s} (0 for Fall): ") or 0) if s != 'Fall' else 0
                score_in = input(f"📈 {sub} Score G{g} {s} (Enter to skip): ")
                score = float(score_in) if score_in else None
            
            if pd.notna(score) or curr_goal > 0:
                all_entries.append({'Grade': g, 'Timeline': f"G{g} {s}", 'Subject': sub, 'Score': score, 'Goal': curr_goal})

df = pd.DataFrame(all_entries)

if not df.empty:
    df.to_csv(FILE_NAME, index=False)
    
    # 📊 BUILD DASHBOARD (Fixed Goal Logic)
    fig = go.Figure()
    colors = {'Math': '#3366FF', 'Reading': '#FF3333', 'Goal': '#FFD700'}
    
    for sub in subjects:
        sub_df = df[df['Subject'] == sub].sort_values(['Grade', 'Timeline'])
        goal_df = sub_df[sub_df['Goal'] > 0] # Only plot goals that aren't 0
        score_df = sub_df.dropna(subset=['Score'])

        if not score_df.empty:
            fig.add_trace(go.Scatter(x=score_df['Timeline'], y=score_df['Score'], name=sub, line=dict(color=colors[sub], width=3), mode='lines+markers'))
        
        if not goal_df.empty:
            fig.add_trace(go.Scatter(x=goal_df['Timeline'], y=goal_df['Goal'], name=f'{sub} Goal', 
                                     line=dict(color=colors['Goal'], width=2, dash='dot'), 
                                     mode='lines+markers', marker=dict(symbol="star", size=12)))

    # Rankings
    last_math = df[df['Subject'] == 'Math']['Score'].dropna().iloc[-1] if not df[df['Subject'] == 'Math']['Score'].dropna().empty else 0
    last_read = df[df['Subject'] == 'Reading']['Score'].dropna().iloc[-1] if not df[df['Subject'] == 'Reading']['Score'].dropna().empty else 0

    fig.add_annotation(text=f"<b>Current Ranks</b><br>Math: {get_badge(last_math)}<br>Reading: {get_badge(last_read)}", xref="paper", yref="paper", x=0.02, y=0.98, showarrow=False, align="left", bgcolor="rgba(10, 10, 10, 0.9)", bordercolor="gold", borderwidth=2, font=dict(size=14, color="white"))
    fig.add_hrect(y0=250, y1=300, fillcolor="red", opacity=0.1, layer="below", line_width=0)
    fig.update_layout(template="plotly_dark", paper_bgcolor="#050505", plot_bgcolor="#050505", xaxis_title="Timeline", yaxis_title="Score")
    
    fig.show()
    update_leaderboard(player_name, max(last_math, last_read))
    
    if input("\n🔥 Ready for a Boss Fight? (y/n): ").lower() == 'y':
        choice = input("Math or Reading? ").capitalize()
        start_boss_fight(last_math if choice == 'Math' else last_read)
else:
    print("\n📭 No data! Try entering a score this time!")
