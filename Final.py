import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="CareerCompass : Will You Regret Your Major?",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# DESIGN SYSTEM
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap');

:root {
    --bg:           #F8F9FF;
    --surface:      #FFFFFF;
    --indigo:       #4F46E5;
    --indigo-light: #6366F1;
    --indigo-pale:  #EEF2FF;
    --coral:        #F97316;
    --coral-pale:   #FFF4ED;
    --green:        #10B981;
    --green-pale:   #ECFDF5;
    --yellow:       #F59E0B;
    --yellow-pale:  #FFFBEB;
    --red:          #EF4444;
    --red-pale:     #FEF2F2;
    --text:         #0F0F23;
    --text-2:       #4B5563;
    --text-3:       #9CA3AF;
    --border:       #E5E7EB;
    --radius:       16px;
    --radius-sm:    10px;
    --shadow:       0 4px 24px rgba(79,70,229,0.08);
    --shadow-lg:    0 8px 40px rgba(79,70,229,0.14);
}

html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; }
h1,h2,h3,h4 { font-family: 'Outfit', sans-serif !important; color: var(--text) !important; }

/* INTRO SECTION */
.intro-container {
    display: flex;
    gap: 2.5rem;
    background: linear-gradient(135deg, #EEF2FF 0%, #F0FDF4 100%);
    border: 1.5px solid #C7D2FE;
    border-radius: var(--radius);
    padding: 2.2rem;
    margin-bottom: 1.5rem;
    align-items: center;
}
.intro-text { flex: 1.8; }
.intro-headline {
    font-family: 'Outfit', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--text);
    margin-bottom: 0.8rem;
    line-height: 1.2;
}
.intro-body {
    font-size: 1.05rem;
    color: var(--text-2);
    line-height: 1.65;
}
.intro-body strong { color: var(--indigo); }

.intro-stats-grid {
    flex: 1;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    min-width: 300px;
}
.intro-stat {
    background: white;
    border-radius: var(--radius-sm);
    padding: 1.2rem 0.5rem;
    border: 1px solid #C7D2FE;
    text-align: center;
    box-shadow: 0 2px 10px rgba(79,70,229,0.05);
}
.intro-stat-val { font-family:'Outfit',sans-serif; font-size: 1.6rem; font-weight:900; color:var(--indigo); }
.intro-stat-lbl { font-size:0.75rem; color:var(--text-3); font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-top:0.2rem; }

/* ENLARGED SLIDER STYLING */
[data-testid="stSlider"] {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
}

/* Slider Track */
[data-testid="stSlider"] [data-baseweb="slider"] > div:first-child {
    height: 12px !important; 
    border-radius: 6px !important;
}

/* Slider Thumb */
[data-testid="stSlider"] [role="slider"] {
    height: 28px !important; 
    width: 28px !important;
    background-color: var(--indigo) !important;
    border: 4px solid white !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2) !important;
}

/* Slider Labels/Values */
[data-testid="stSlider"] [data-baseweb="slider"] div {
    font-size: 1rem !important;
    font-weight: 600 !important;
}

/* WEIGHT CARDS */
.w-card {
    background: var(--bg);
    border: 1.5px solid var(--border);
    border-radius: var(--radius-sm);
    padding: 1.2rem;
    margin-bottom: -10px; 
}
.w-card-label { 
    font-family:'Outfit',sans-serif; 
    font-size: 1.1rem; 
    font-weight: 700; 
    color: var(--text);
    margin-bottom: 0.6rem;
}
.w-card-hint { 
    font-size: 0.95rem; 
    color: var(--text-2);
    line-height: 1.5; 
    min-height: 3em;
}

[data-testid="stMetric"] {
    background: var(--surface) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 1.1rem 1.2rem !important;
    box-shadow: var(--shadow) !important;
}

.cc-hero { display:flex; align-items:center; gap:1rem; margin-bottom:1.2rem; padding-bottom:1.2rem; border-bottom:1.5px solid var(--border); }
.cc-logo { background:var(--indigo); border-radius:14px; width:52px; height:52px; display:flex; align-items:center; justify-content:center; font-size:1.6rem; box-shadow:0 4px 14px rgba(79,70,229,0.35); flex-shrink:0; }
.cc-wordmark { font-family:'Outfit',sans-serif; font-size:1.85rem; font-weight:900; color:var(--text); line-height:1; letter-spacing:-0.03em; }
.cc-wordmark span { color:var(--indigo); }
.cc-tagline { font-size:0.85rem; color:var(--text-3); margin-top:0.15rem; font-weight:500; }

.weight-panel {
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: var(--radius);
    padding: 1.4rem 1.6rem 1rem;
    box-shadow: var(--shadow);
    margin-bottom: 1.5rem;
}
.weight-panel-title { font-family:'Outfit',sans-serif; font-size: 1.2rem; font-weight:800; color:var(--text); }
.weight-badge { background:var(--indigo-pale); color:var(--indigo); font-family:'Outfit',sans-serif; font-size:0.75rem; font-weight:700; padding:0.2rem 0.7rem; border-radius:20px; text-transform:uppercase; }

.verdict-chip { display:inline-flex; align-items:center; gap:0.4rem; padding:0.35rem 0.9rem; border-radius:20px; font-family:'Outfit',sans-serif; font-size:0.85rem; font-weight:700; margin-top:0.7rem; }
.chip-high   { background:#FEF2F2; color:#EF4444; }
.chip-medium { background:#FFFBEB; color:#B45309; }
.chip-low    { background:#ECFDF5; color:#065F46; }

.locked-field { background:#F3F4F6; border:1.5px solid var(--border); border-radius:var(--radius-sm); padding:0.55rem 0.9rem; font-family:'Outfit',sans-serif; font-size:1rem; font-weight:700; color:var(--text); display:flex; justify-content:space-between; align-items:center; }
.lock-icon { font-size:0.75rem; color:var(--text-3); }
.locked-label { font-size:0.8rem; font-weight:600; color:var(--text-2); margin-bottom:0.3rem; font-family:'Plus Jakarta Sans',sans-serif; }
.section-label { font-family:'Outfit',sans-serif; font-size:0.7rem; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:var(--text-3); margin-bottom:0.8rem; margin-top:1.4rem; }
</style>
""", unsafe_allow_html=True)

# DATA
@st.cache_data
def load_university_data():
    filename = "National Universities Rankings.csv"
    import os
    
    if not os.path.exists(filename):
        st.error(f"File missing: Please verify {filename} is in your active folder.")
        return pd.DataFrame([{"University Name": "Demo University", "Rank": 50}])
        
    try:
        df = pd.read_csv(filename)
        
        out_df = pd.DataFrame()
        out_df['University Name'] = df['Name'].astype(str).str.strip()
        
        # Extract only digits to fix Kaggle's text artifacts
        extracted_ranks = df['Rank'].astype(str).str.extract(r'(\d+)')[0]
        out_df['Rank'] = pd.to_numeric(extracted_ranks, errors='coerce')
        
        out_df['Rank'] = out_df['Rank'].fillna(150)
        
        return out_df.dropna()
        
    except Exception as e:
        st.error(f"Error parsing data: {str(e)}")
        return pd.DataFrame([{"University Name": "Demo University", "Rank": 50}])

UNI_DF = load_university_data()

MAJOR_DATA = [
    ("Computer Science",           88_907, 23_184,  15.0,  4.2,  2.5,  24,   72),
    ("Software Engineering",       82_536, 25_016,  15.0,  4.2,  2.5,  22,   74),
    ("Data Science / Statistics",  79_859, 21_480,  34.0,  2.0,  2.8,  45,   71),
    ("Electrical Engineering",     79_000, 25_612,   9.0,  3.5,  3.1,  28,   70),
    ("Mechanical Engineering",     80_482, 25_133,  11.0,  1.7,  2.9,  23,   69),
    ("Civil Engineering",          72_000, 25_611,   6.0,  1.8,  3.4,  21,   68),
    ("Economics",                  68_000, 21_537,   8.0, 43.0,  5.8,  56,   62),
    ("Business Administration",    66_578, 25_336,  11.0, 16.0,  5.5,  35,   60),
    ("Finance",                    72_000, 23_714,   9.0, 23.0,  5.2,  38,   61),
    ("Accounting",                 62_000, 25_060,   4.0, 94.0,  5.0,  30,   55),
    ("Marketing",                  60_000, 22_000,   8.0, 61.0,  6.2,  28,   58),
    ("Architecture",               58_000, 27_539,   8.0,  1.8,  5.8,  32,   66),
    ("Nursing",                    62_143, 28_000,   6.0,  0.9,  1.9,  18,   78),
    ("Public Health",              55_000, 27_002,  13.0,  2.3,  3.2,  55,   73),
    ("Biology / Pre-Med",          56_000, 24_708,   7.0,  1.1,  4.5,  72,   67),
    ("Environmental Science",      52_000, 24_443,   7.0,  2.5,  5.4,  48,   70),
    ("Political Science",          52_000, 22_582,   5.0,  3.5,  7.2,  58,   60),
    ("Communications / Journalism",47_000, 23_743,  -4.0, 11.0,  7.8,  22,   56),
    ("Criminal Justice",           48_000, 25_527,   3.0,  9.8,  5.5,  18,   62),
    ("Graphic Design",             45_000, 28_641,  -3.0,  8.2,  6.4,  20,   65),
    ("Psychology",                 45_000, 28_549,   6.0,  0.4,  6.0,  68,   64),
    ("Education (K-12 Teaching)",  44_000, 29_134,   1.0,  0.4,  2.8,  28,   72),
    ("History",                    44_000, 23_684,   1.0, 21.0,  8.4,  52,   58),
    ("English / Literature",       42_000, 23_411,   4.0, 33.0,  7.5,  48,   61),
    ("Film / Media Studies",       38_000, 26_005,   6.0, 11.0,  8.6,  28,   63),
    ("Social Work",                38_000, 29_742,   9.0,  0.3,  4.2,  45,   76),
    ("Fine Arts",                  36_000, 26_668,   2.0,  8.2,  9.1,  22,   68),
    ("Philosophy",                 40_000, 24_000,   3.0,  0.2,  8.2,  58,   65),
    ("Sociology",                  40_000, 23_000,   2.0,  5.0,  7.8,  44,   60),
]

COLS = ["Major", "StartSalary", "Debt", "JobGrowth", "AutoRisk", "UnempRate", "GradReqPct", "JobSat"]
MAJORS_DF = pd.DataFrame(MAJOR_DATA, columns=COLS)

REFERENCE_RANGES = {
    "start_salary": {"min": 30_000, "max": 95_000},
    "debt":         {"min": 10_000, "max": 50_000},
    "job_growth":   {"min": -10.0,  "max": 35.0},
    "auto_risk":    {"min": 0.0,    "max": 100.0},
    "unemp_rate":   {"min": 1.0,    "max": 12.0},
    "job_sat":      {"min": 40.0,   "max": 85.0},
}

DEFAULT_WEIGHTS = {
    "start_salary": 0.40,
    "debt":         0.20,
    "job_growth":   0.15,
    "auto_risk":    0.10,
    "unemp_rate":   0.10,
    "job_sat":      0.05,
}

WEIGHT_META = [
    ("start_salary", "💰", "Starting Salary",    "How important is first-year pay after graduation to you?"),
    ("debt",         "💳", "Student Debt",        "How much does student debt factor into your decision?"),
    ("job_growth",   "📈", "Job Growth",          "How important is future stability to you for your field?"),
    ("auto_risk",    "🤖", "Automation Risk",     "How much does AI-Replaceability matter to you?"),
    ("unemp_rate",   "🔍", "Unemployment Rate",   "Is unemployment risk a concern for you in this field?"),
    ("job_sat",      "😊", "Job Satisfaction",    "How important is it that you truly enjoy your field/job?"),
]

MAJOR_ADVICE = {
    "Computer Science": {
        "High": ["Attend a coding bootcamp before fall semester to see if you actually enjoy logic-heavy work.", "Look into IT Management as a backup major if you find Calculus 1 too punishing."],
        "Moderate": ["Join a freshman-only hackathon to build a project outside of class.", "Set up your GitHub profile in week 1 of your first semester."],
        "Low": ["Sign up for a student-run AI club to network with upperclassmen.", "Look for undergraduate research roles that pay for lab assistance early on."]
    },
    "Nursing": {
        "High": ["Treat your first semester Anatomy course like a full-time job; it's the primary 'filter' class.", "Volunteer at a clinic early to confirm you have the stomach for bedside care."],
        "Moderate": ["Shadow a nurse over winter break to understand the actual shift schedule.", "Apply for a CNA license early to get paid clinical hours."],
        "Low": ["Keep your GPA above 3.5 from day one for future Grad School options.", "Attend a meeting for the National Student Nurses' Association."]
    },
    "Psychology": {
        "High": ["Understand that 68% of your peers will need a PhD to get clinical pay.", "Pick up a Marketing or Data minor in your first semester to boost job prospects."],
        "Moderate": ["Volunteer at a campus crisis hotline to gain early experience.", "Focus on Statistics classes as they are your most marketable skill."],
        "Low": ["Join a faculty research lab as a freshman assistant.", "Start studying for the GRE during your second semester."]
    },
    "Generic": {
        "High": ["Visit the career center in month 1 to see real job placement stats for this major.", "Consider a double major with a higher-growth field."],
        "Moderate": ["Search for alumni on LinkedIn and see what their first job was.", "Join a student organization related to your major."],
        "Low": ["Apply for a competitive scholarship in your field.", "Ask a professor about undergraduate research opportunities."]
    }
}

# FORMULA
def compute_rps(row_data, weights, uni_rank=None, apply_dti_penalty=True):
    r = REFERENCE_RANGES
    def normalize(v, mn, mx): return max(0, min(1, (v - mn) / (mx - mn)))
    scores = {
        "start_salary": 1 - normalize(row_data["StartSalary"], r["start_salary"]["min"], r["start_salary"]["max"]),
        "debt":             normalize(row_data["Debt"],         r["debt"]["min"],         r["debt"]["max"]),
        "job_growth":   1 - normalize(row_data["JobGrowth"],   r["job_growth"]["min"],   r["job_growth"]["max"]),
        "auto_risk":        normalize(row_data["AutoRisk"],     r["auto_risk"]["min"],    r["auto_risk"]["max"]),
        "unemp_rate":       normalize(row_data["UnempRate"],    r["unemp_rate"]["min"],   r["unemp_rate"]["max"]),
        "job_sat":      1 - normalize(row_data["JobSat"],       r["job_sat"]["min"],      r["job_sat"]["max"]),
    }
    raw_rps = 100 * sum(weights.get(k, 0) * v for k, v in scores.items())
    dti = row_data["Debt"] / max(row_data["StartSalary"], 1)
    multiplier = 1.0 + (min(max(0, dti - 1.5), 1.5) * 0.20) if apply_dti_penalty else 1.0
    
    # Updated Rank logic with new tiers
    rank_mod = 0.0
    if uni_rank is not None:
        if uni_rank <= 20: rank_mod = -5.0
        elif uni_rank <= 50: rank_mod = -2.0
        elif uni_rank <= 100: rank_mod = 0.0
        elif uni_rank <= 150: rank_mod = 2.0
        else: rank_mod = 4.0
        
    final_rps = min(max(raw_rps * multiplier + rank_mod, 0), 100)
    return {"rps": round(final_rps, 1), "sub_scores": {k: round(v * 100) for k, v in scores.items()}, "dti": round(dti, 2)}

def verdict(score):
    if score >= 65:   return "😬 High Regret Risk",   "chip-high"
    elif score >= 40: return "🤔 Moderate Risk",      "chip-medium"
    return                   "✅ Low Regret Risk",     "chip-low"

def make_gauge(score):
    color = "#EF4444" if score >= 65 else ("#F59E0B" if score >= 40 else "#10B981")
    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=score,
        number={"font": {"family": "Outfit", "size": 48, "color": color}},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": color}, "bgcolor": "#F8F9FF", "steps": [{"range": [0, 40], "color": "#ECFDF5"}, {"range": [40, 65], "color": "#FFFBEB"}, {"range": [65, 100], "color": "#FEF2F2"}]}
    ))
    fig.update_layout(height=220, margin=dict(l=20, r=20, t=20, b=10), paper_bgcolor="rgba(0,0,0,0)", font={"family": "Outfit"})
    return fig

def make_radar(sub_scores, major_name):
    labels_map = {"start_salary": "Start Pay", "debt": "Debt Load", "job_growth": "Job Growth", "auto_risk": "Automation", "unemp_rate": "Unemployment", "job_sat": "Job Satisfaction"}
    keys = list(sub_scores.keys()); values = [sub_scores[k] for k in keys]; labels = [labels_map.get(k, k) for k in keys]
    fig = go.Figure(go.Scatterpolar(r=values + [values[0]], theta=labels + [labels[0]], fill="toself", line=dict(color="#4F46E5")))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, height=300, margin=dict(l=50, r=50, t=30, b=30), paper_bgcolor="rgba(0,0,0,0)", font={"family": "Outfit"})
    return fig

# HEADER
st.markdown("""<div class="cc-hero"><div class="cc-logo">🧭</div><div><div class="cc-wordmark">Career<span>Compass</span></div><div class="cc-tagline">Find your direction before you commit four years of your life.</div></div></div>""", unsafe_allow_html=True)

# INTRO SECTION
st.markdown("""
<div class="intro-container">
    <div class="intro-text">
        <div class="intro-headline">🎓 Choosing a major is one of the biggest financial decisions you'll ever make.</div>
        <div class="intro-body">
            Most 18 year olds pick a college major based on what they enjoy in school or what their parents suggest. But here's the reality: the average student graduates with <strong>$37,000 in debt</strong>, and nearly <strong>1 in 3 graduates</strong> say they regret their choice within 5 years of graduating. That regret usually isn't about passion it's about money, job availability, and the weight of loans that won't go away.
            <br><br>
            <strong>CareerCompass</strong> calculates a <strong>Regret Probability Score (RPS)</strong> using real data from NACE, the BLS, and leading labor economics research.
        </div>
    </div>
    <div class="intro-stats-grid">
        <div class="intro-stat"><div class="intro-stat-val">25+</div><div class="intro-stat-lbl">Majors</div></div>
        <div class="intro-stat"><div class="intro-stat-val">9</div><div class="intro-stat-lbl">Metrics</div></div>
        <div class="intro-stat"><div class="intro-stat-val">200+</div><div class="intro-stat-lbl">Colleges</div></div>
        <div class="intro-stat"><div class="intro-stat-val">100%</div><div class="intro-stat-lbl">Real Data</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# WEIGHT PANEL
st.markdown("""<div class="weight-panel"><div class="weight-panel-header"><span class="weight-panel-title">⚖️ What matters most to you?</span> <span class="weight-badge">Customize Your Score</span></div><div style="font-size:0.82rem; color:var(--text-3); margin-top:0.25rem;">Adjust the weights below to set your priorities (must sum to 1.0).</div></div>""", unsafe_allow_html=True)
wcols_top = st.columns(3); wcols_bot = st.columns(3); w_vals = {}
for i, (key, icon, label, hint) in enumerate(WEIGHT_META):
    col = wcols_top[i] if i < 3 else wcols_bot[i - 3]
    with col:
        st.markdown(f"""<div class="w-card"><div class="w-card-label">{icon} {label}</div><div class="w-card-hint">{hint}</div></div>""", unsafe_allow_html=True)
        w_vals[key] = st.slider(label, 0.0, 1.0, DEFAULT_WEIGHTS[key], 0.05, label_visibility="collapsed", key=f"w_{key}")
total_w = round(sum(w_vals.values()), 2)
bal_col, dti_col = st.columns([2, 1])
with bal_col:
    if abs(total_w - 1.0) <= 0.01: st.markdown(f"<div style='color:#10B981; font-weight:700;'>✓ Balanced (1.0)</div>", unsafe_allow_html=True)
    else: st.markdown(f"<div style='color:#EF4444; font-weight:700;'>⚠️ Sum: {total_w} (Needs 1.0)</div>", unsafe_allow_html=True)
with dti_col: 
    apply_dti = st.toggle(
        "Debt stress penalty", 
        value=True, 
        help="Increases the regret score if your projected debt exceeds 150% of your starting salary."
    )

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧮 Calculator", "📊 Comparison", "📈 Insights", "📖 Data", "📚 Sources"])

with tab1:
    left_col, right_col = st.columns([1, 1.1], gap="large")
    with left_col:
        st.markdown('<div class="section-label">Step 1: Pick a major</div>', unsafe_allow_html=True)
        majors_list = sorted(list(MAJORS_DF["Major"])); lookup = st.selectbox("Database:", ["Custom Option"] + majors_list, index=majors_list.index("Computer Science")+1)
        if lookup != "Custom Option": row = MAJORS_DF[MAJORS_DF["Major"] == lookup].iloc[0].to_dict(); is_preset = True
        else: row = {"Major": "", "StartSalary": 55000, "Debt": 30000, "JobGrowth": 5.0, "AutoRisk": 25.0, "UnempRate": 5.0, "GradReqPct": 30, "JobSat": 65}; is_preset = False
        major_name = st.text_input("Name", value=row["Major"] if is_preset else "")
        
        st.markdown('<div class="section-label">Step 2: Pick a University (Optional)</div>', unsafe_allow_html=True)
        uni_list = sorted(list(UNI_DF["University Name"]))
        options = ["Skip (National Average)"] + uni_list
        default_index = 0
        if "University of Alabama" in options:
            default_index = options.index("University of Alabama")
            
        selected_uni = st.selectbox("University:", options, index=default_index)
        
        if selected_uni == "Skip (National Average)":
            uni_rank = None
            st.caption("Rank: N/A")
        else:
            uni_rank = UNI_DF[UNI_DF["University Name"] == selected_uni].iloc[0]["Rank"]
            st.caption(f"Rank: {int(uni_rank)}")
            
        st.markdown('<div class="section-label">Step 3: Review data</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="locked-field">${row["StartSalary"]:,} <span class="lock-icon">🔒 First Year Salary: NACE 2024</span></div>', unsafe_allow_html=True)
        ec1, ec2 = st.columns(2)
        with ec1:
            debt_in = st.number_input("Projected Debt ($)", value=int(row["Debt"]), step=500, help="Average student loan debt accrued for this degree.")
            growth_in = st.number_input("Growth (%)", value=float(row["JobGrowth"]), step=0.5, help="Projected 10-year job growth rate in this field.")
            unemp_in = st.number_input("Unemployment (%)", value=float(row["UnempRate"]), step=0.1, help="Recent graduate unemployment rate.")
        with ec2:
            auto_in = st.number_input("Automation Risk (%)", value=float(row["AutoRisk"]), step=1.0, help="Likelihood of degree-related tasks being automated by AI.")
            gradreq_in = st.number_input("Graduate Degree Required (%)", value=int(row["GradReqPct"]), step=1, help="Percentage of jobs requiring a Master's or higher.")
            jobsat_in = st.number_input("Job Satisfaction (%)", value=int(row["JobSat"]), step=1, help="Average reported job satisfaction score out of 100.")
        calculate = st.button("Calculate", type="primary", use_container_width=True)

    with right_col:
        if calculate or is_preset:
            res = compute_rps({"StartSalary": int(row["StartSalary"]), "Debt": debt_in, "JobGrowth": growth_in, "AutoRisk": auto_in, "UnempRate": unemp_in, "GradReqPct": gradreq_in, "JobSat": jobsat_in}, w_vals, uni_rank, apply_dti)
            lbl, chip = verdict(res["rps"])
            st.plotly_chart(make_gauge(res["rps"]), use_container_width=True)
            st.markdown(f'<div style="text-align:center;"><span class="verdict-chip {chip}">{lbl}</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="section-label">Freshman Action Plan</div>', unsafe_allow_html=True)
            advice = MAJOR_ADVICE.get(lookup, MAJOR_ADVICE["Generic"]).get("High" if res["rps"] >= 65 else ("Moderate" if res["rps"] >= 40 else "Low"))
            for a in advice: st.markdown(f"• {a}")
            st.plotly_chart(make_radar(res["sub_scores"], lookup), use_container_width=True)

with tab2:
    comp_df = pd.DataFrame([{"Major": r["Major"], "RPS": compute_rps(r.to_dict(), w_vals, uni_rank, apply_dti)["rps"]} for _, r in MAJORS_DF.iterrows()]).sort_values("RPS")
    colors = ["#4F46E5" if m == lookup else ("#EF4444" if r >= 65 else ("#F59E0B" if r >= 40 else "#10B981")) for m, r in zip(comp_df["Major"], comp_df["RPS"])]
    st.plotly_chart(
        go.Figure(go.Bar(x=comp_df["RPS"], y=comp_df["Major"], orientation="h", marker_color=colors))
        .update_layout(
            height=700, 
            margin=dict(l=10, r=20, t=20, b=40), 
            xaxis=dict(title="Regret Probability Score", range=[0, 100]), 
            paper_bgcolor="rgba(0,0,0,0)", 
            font={"family": "Outfit"}
        ), 
        use_container_width=True
    )

with tab3:
    st.markdown("### ⚖️ The Reality Check: Pay vs. Happiness")
    st.write("Does a higher paycheck actually lead to a better career experience? This visualization maps starting salary against average job satisfaction. The top-right quadrant represents fields that offer both strong financial returns and high personal fulfillment.")
    
    fig_sat = px.scatter(
        MAJORS_DF, x="StartSalary", y="JobSat", text="Major", color="UnempRate", 
        color_continuous_scale="Tealgrn",
        labels={"StartSalary": "Starting Salary ($)", "JobSat": "Job Satisfaction Score", "UnempRate": "Unemployment Rate (%)"}
    )
    # Increased marker size, added borders, and bumped text size
    fig_sat.update_traces(marker=dict(size=14, line=dict(width=1, color='DarkSlateGrey')), textposition='top center', textfont_size=11)
    fig_sat.add_vline(x=MAJORS_DF["StartSalary"].median(), line_width=1, line_dash="dash", line_color="gray")
    fig_sat.add_hline(y=MAJORS_DF["JobSat"].median(), line_width=1, line_dash="dash", line_color="gray")
    
    fig_sat.update_layout(
        height=600, 
        paper_bgcolor="rgba(0,0,0,0)", 
        font={"family": "Outfit"}
    )
    st.plotly_chart(fig_sat, use_container_width=True)

    st.markdown("---")
    
    st.markdown("### 🤖 Future Proofing: Automation Risk vs. Job Growth")
    st.write("Labor markets are shifting rapidly. The most resilient career paths sit in the top-left quadrant, combining strong 10-year job growth with a low likelihood of core tasks being automated.")
    
    fig_future = px.scatter(
        MAJORS_DF, x="AutoRisk", y="JobGrowth", text="Major", color="UnempRate",
        color_continuous_scale="Reds",
        labels={"AutoRisk": "Automation Risk (%)", "JobGrowth": "10-Year Job Growth (%)", "UnempRate": "Unemployment Rate (%)"}
    )
    # Increased marker size, added borders, and bumped text size
    fig_future.update_traces(marker=dict(size=14, line=dict(width=1, color='DarkSlateGrey')), textposition='top center', textfont_size=11)
    fig_future.add_vline(x=MAJORS_DF["AutoRisk"].median(), line_width=1, line_dash="dash", line_color="gray")
    fig_future.add_hline(y=MAJORS_DF["JobGrowth"].median(), line_width=1, line_dash="dash", line_color="gray")
    fig_future.update_layout(height=600, paper_bgcolor="rgba(0,0,0,0)", font={"family": "Outfit"})
    st.plotly_chart(fig_future, use_container_width=True)

with tab4: st.dataframe(MAJORS_DF, use_container_width=True)

with tab5:
    st.markdown("### Data Sources & Methodology")
    st.markdown("**National Association of Colleges and Employers**: Provides the baseline starting salary and average debt figures for recent graduates across different disciplines.")
    st.markdown("**Bureau of Labor Statistics**: Powers the macroeconomic indicators, specifically the 10-year job growth projections and current unemployment rates by field.")
    st.markdown("**Kaggle National Universities Rankings**: Supplies the ranking data used to calculate the institutional prestige modifier.")
    st.markdown("**Labor Economics Research**: Informs the automation risk percentage and job satisfaction scores, aggregated from recent studies on artificial intelligence exposure in the workplace.")

st.markdown("""<div style="text-align:center; padding-top:2rem; border-top:1px solid var(--border); margin-top:2rem; font-size:0.75rem; color:#9CA3AF;">CareerCompass | NACE 2025 | BLS 2024</div>""", unsafe_allow_html=True)