import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Psychiatric Nursing AI Teaching Module",
    page_icon="🧠",
    layout="wide"
)

# =========================
# Custom Styling
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    background: linear-gradient(135deg, #F8FAFC 0%, #EEF4FF 55%, #FFF7ED 100%);
}

.hero {
    padding: 36px 34px;
    border-radius: 28px;
    background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 55%, #7C2D12 100%);
    color: white;
    box-shadow: 0 20px 45px rgba(15, 23, 42, 0.25);
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero p {
    font-size: 18px;
    opacity: 0.92;
}

.card {
    padding: 24px;
    border-radius: 22px;
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(148,163,184,0.35);
    box-shadow: 0 12px 30px rgba(15,23,42,0.08);
    margin-bottom: 18px;
}

.metric-card {
    text-align: center;
    padding: 22px;
    border-radius: 22px;
    color: white;
    background: linear-gradient(135deg, #2563EB, #7C3AED);
    box-shadow: 0 14px 28px rgba(37,99,235,0.25);
}

.metric-card h2 {
    font-size: 34px;
    font-weight: 800;
    margin: 0;
}

.metric-card p {
    margin: 0;
    opacity: 0.95;
}

.section-title {
    font-size: 28px;
    font-weight: 800;
    color: #0F172A;
    margin-top: 10px;
    margin-bottom: 15px;
}

.sub-title {
    font-size: 20px;
    font-weight: 700;
    color: #1E3A8A;
    margin-top: 15px;
}

.good {
    background: #ECFDF5;
    border-left: 6px solid #10B981;
    padding: 16px;
    border-radius: 14px;
}

.warn {
    background: #FFF7ED;
    border-left: 6px solid #F97316;
    padding: 16px;
    border-radius: 14px;
}

.danger {
    background: #FEF2F2;
    border-left: 6px solid #EF4444;
    padding: 16px;
    border-radius: 14px;
}

.info {
    background: #EFF6FF;
    border-left: 6px solid #2563EB;
    padding: 16px;
    border-radius: 14px;
}

.patient {
    padding: 18px;
    border-radius: 18px;
    background: linear-gradient(135deg, #FDF2F8, #EEF2FF);
    border: 1px solid #CBD5E1;
    margin-bottom: 12px;
}

.student {
    padding: 18px;
    border-radius: 18px;
    background: linear-gradient(135deg, #ECFDF5, #F0FDFA);
    border: 1px solid #CBD5E1;
    margin-bottom: 12px;
}

.footer {
    text-align: center;
    color: #64748B;
    margin-top: 35px;
    padding: 18px;
}
</style>
""", unsafe_allow_html=True)


# =========================
# Data
# =========================
theory_topics = {
    "Depression and Suicide Risk": {
        "overview": """
Depression is a mood disorder characterized by persistent sadness, loss of interest or pleasure, low energy,
sleep and appetite disturbance, impaired concentration, feelings of worthlessness, and possible suicidal ideation.
""",
        "clinical": """
In psychiatric nursing, suicide risk assessment is a priority. The nurse should assess suicidal thoughts,
plan, means, previous attempts, hopelessness, social withdrawal, and protective factors.
""",
        "nursing": [
            "Establish a therapeutic relationship based on trust and empathy.",
            "Assess suicidal ideation directly and non-judgmentally.",
            "Remove dangerous objects and ensure a safe environment.",
            "Monitor the patient closely according to risk level.",
            "Encourage expression of feelings.",
            "Involve family/support system when appropriate.",
            "Educate about medication adherence and follow-up."
        ]
    },
    "Schizophrenia": {
        "overview": """
Schizophrenia is a chronic psychotic disorder characterized by severe disturbances in thinking, perception,
emotions, behavior, and contact with reality.
""",
        "clinical": """
Positive symptoms include hallucinations, delusions, and disorganized thinking. Negative symptoms include
flat affect, alogia, avolition, anhedonia, and social withdrawal.
""",
        "nursing": [
            "Assess hallucinations and delusional content without reinforcing false beliefs.",
            "Use simple, clear, and concrete communication.",
            "Maintain a low-stimulus environment.",
            "Ensure safety if command hallucinations are present.",
            "Encourage reality-based conversation.",
            "Promote medication adherence.",
            "Support social interaction gradually."
        ]
    },
    "Therapeutic Relationship": {
        "overview": """
The therapeutic nurse-patient relationship is a professional relationship that uses communication, empathy,
acceptance, trust, boundaries, and respect to promote patient recovery.
""",
        "clinical": """
The relationship usually includes pre-interaction, orientation, working, and termination phases.
""",
        "nursing": [
            "Use active listening.",
            "Show empathy and acceptance.",
            "Avoid judgment.",
            "Maintain professional boundaries.",
            "Encourage patient participation.",
            "Use open-ended questions.",
            "Clarify and validate patient feelings."
        ]
    },
    "ECT and Psychotropic Treatment": {
        "overview": """
Treatment in psychiatric disorders may include antidepressants, antipsychotics, mood stabilizers, psychotherapy,
and Electroconvulsive Therapy (ECT).
""",
        "clinical": """
ECT may be used in severe depression, treatment-resistant depression, catatonia, and urgent clinical situations.
Nursing care includes preparation, informed consent, fasting, monitoring, reorientation, and post-procedure safety.
""",
        "nursing": [
            "Assess patient before treatment.",
            "Monitor side effects and therapeutic response.",
            "Educate patient and family.",
            "Observe for suicide risk especially early in antidepressant treatment.",
            "Monitor vital signs and mental status.",
            "Ensure informed consent for ECT.",
            "Provide post-ECT reorientation and safety."
        ]
    },
    "Legal and Ethical Issues": {
        "overview": """
Psychiatric nursing practice must respect patient rights, confidentiality, informed consent, safety, and legal
responsibilities.
""",
        "clinical": """
Patients may be admitted voluntarily or involuntarily depending on safety, capacity, and risk. Nurses must document
clearly and protect patients from harm.
""",
        "nursing": [
            "Maintain confidentiality.",
            "Obtain and respect informed consent.",
            "Document accurately.",
            "Report suicide risk and safety concerns.",
            "Respect patient rights.",
            "Use the least restrictive intervention.",
            "Protect patient dignity."
        ]
    }
}

patient_cases = {
    "Depression with Suicide Risk": {
        "profile": {
            "Name": "Sarah",
            "Age": "22 years",
            "Gender": "Female",
            "Status": "University student",
            "Main Complaint": "I feel empty and I do not see a reason to continue living."
        },
        "mse": {
            "Appearance": "Tired, poor eye contact, low energy",
            "Mood": "Depressed",
            "Affect": "Constricted / flat",
            "Speech": "Slow, low tone",
            "Thought Content": "Worthlessness, hopelessness, passive suicidal ideation",
            "Perception": "No hallucinations",
            "Insight": "Partial",
            "Judgment": "Impaired due to hopelessness"
        }
    },
    "Schizophrenia with Auditory Hallucinations": {
        "profile": {
            "Name": "Omar",
            "Age": "25 years",
            "Gender": "Male",
            "Status": "Unemployed",
            "Main Complaint": "I hear voices and I feel people are watching me."
        },
        "mse": {
            "Appearance": "Poor grooming, suspicious look",
            "Mood": "Anxious",
            "Affect": "Inappropriate / flat",
            "Speech": "Sometimes irrelevant",
            "Thought Content": "Persecutory delusions",
            "Perception": "Auditory hallucinations",
            "Insight": "Poor",
            "Judgment": "Impaired"
        }
    }
}


# =========================
# Helper Functions
# =========================
def patient_response(case, question):
    q = question.lower().strip()

    if case == "Depression with Suicide Risk":
        if any(word in q for word in ["feel", "mood", "sad", "how are you"]):
            return "I feel empty most of the time. I wake up tired and I do not enjoy anything anymore."
        if any(word in q for word in ["sleep", "insomnia"]):
            return "I cannot sleep well. I stay awake for hours thinking that my life has no meaning."
        if any(word in q for word in ["appetite", "eat", "weight"]):
            return "I do not feel hungry. I lost weight because I rarely finish my meals."
        if any(word in q for word in ["suicide", "kill", "harm", "death", "hurt"]):
            return "Sometimes I think it would be easier if I did not wake up. I thought about harming myself, but I do not have a clear plan."
        if any(word in q for word in ["family", "support", "friend"]):
            return "My family tries to help, but they keep telling me to be strong. I feel they do not understand me."
        if any(word in q for word in ["study", "work", "function"]):
            return "I cannot focus on my studies. I stopped attending lectures and I feel guilty all the time."
        if any(word in q for word in ["medication", "treatment", "doctor"]):
            return "The doctor prescribed an antidepressant. I started it recently, but I still feel hopeless."
        return "I do not know how to explain it. Everything feels heavy, but I feel a little safer when someone listens."

    else:
        if any(word in q for word in ["voice", "hear", "hallucination"]):
            return "I hear a man's voice, especially at night. It tells me that people are against me."
        if any(word in q for word in ["believe", "watching", "spy", "delusion"]):
            return "I believe my neighbors are watching me. I know you may not believe me, but I feel it is real."
        if any(word in q for word in ["sleep", "insomnia"]):
            return "I barely sleep because the voices become louder at night."
        if any(word in q for word in ["family", "support"]):
            return "My mother tries to help me, but I do not trust many people."
        if any(word in q for word in ["medication", "treatment", "doctor"]):
            return "I was given antipsychotic medication. Sometimes I stop taking it because I do not like the side effects."
        if any(word in q for word in ["harm", "suicide", "kill", "danger"]):
            return "The voices sometimes scare me. I do not want to hurt anyone, but I feel unsafe when they become intense."
        return "I feel confused. Sometimes it is difficult to know what is real and what is not."


def communication_feedback(question):
    q = question.lower()
    if any(word in q for word in ["why did you", "crazy", "not real", "stop thinking"]):
        return "⚠️ Feedback: This may sound judgmental or invalidating. Try using empathy, clarification, and acceptance."
    if any(word in q for word in ["tell me", "can you describe", "how do you feel", "what happened"]):
        return "✅ Feedback: Good therapeutic communication. The question is open-ended and encourages expression."
    if any(word in q for word in ["suicide", "harm", "death"]):
        return "✅ Feedback: Direct suicide assessment is appropriate and important in psychiatric nursing."
    return "ℹ️ Feedback: Consider using open-ended, clear, and empathetic questions."


def risk_level(score):
    if score <= 2:
        return "Low Risk", "good"
    elif score <= 5:
        return "Moderate Risk", "warn"
    return "High Risk", "danger"


# =========================
# Header
# =========================
st.markdown("""
<div class="hero">
    <h1>🧠 Psychiatric Nursing AI Teaching Module</h1>
    <p>Integrating theoretical content with clinical practice through virtual patient simulation.</p>
    <p><b>Focus:</b> Depression, Suicide Risk, Schizophrenia, Nursing Process, ECT, Legal and Ethical Care</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("📌 Module Navigator")
    st.info("Faculty of Nursing - Psychiatric Mental Health Nursing")
    st.markdown("### Learning Outcomes")
    st.write("✅ Understand psychiatric theory")
    st.write("✅ Practice clinical interview")
    st.write("✅ Assess suicide risk")
    st.write("✅ Build nursing care plans")
    st.write("✅ Receive instant feedback")
    st.markdown("---")
    st.caption(f"Generated prototype | {datetime.now().strftime('%Y')}")

tabs = st.tabs([
    "🏠 Overview",
    "📚 Theory Hub",
    "🧑‍⚕️ Virtual Patient",
    "📂 Clinical Scenario",
    "📝 Clinical Assessment",
    "🩺 Nursing Process",
    "🎯 Quiz",
    "👩‍🏫 Instructor Guide",
    "📖 References"
])

# =========================
# Overview
# =========================
with tabs[0]:
    st.markdown('<div class="section-title">Module Overview</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="metric-card"><h2>5</h2><p>Theory Domains</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-card"><h2>2</h2><p>Virtual Cases</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-card"><h2>5</h2><p>Nursing Process Steps</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="metric-card"><h2>15</h2><p>Quiz Items</p></div>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">
<h3>🎯 Purpose of the Module</h3>
<p>
This AI-based teaching module is designed to help nursing students connect psychiatric mental health theory
with clinical practice. It provides virtual patient scenarios, clinical assessment tools, nursing care planning,
and self-assessment activities.
</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="info">
<b>Core Educational Idea:</b> Students do not only read about depression or schizophrenia; they interact with simulated patients,
assess symptoms, make nursing decisions, and receive instant learning feedback.
</div>
""", unsafe_allow_html=True)

# =========================
# Theory Hub
# =========================
with tabs[1]:
    st.markdown('<div class="section-title">📚 Theoretical Content Hub</div>', unsafe_allow_html=True)

    selected_topic = st.selectbox("Select a theoretical topic", list(theory_topics.keys()))

    topic = theory_topics[selected_topic]
    st.markdown(f'<div class="card"><h3>{selected_topic}</h3><p>{topic["overview"]}</p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info"><b>Clinical Relevance:</b><br>{topic["clinical"]}</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-title">Nursing Implications</div>', unsafe_allow_html=True)
    for item in topic["nursing"]:
        st.write(f"✅ {item}")

    st.markdown("---")
    st.markdown("### Depression vs Schizophrenia")

    comparison = pd.DataFrame({
        "Aspect": ["Main Domain", "Core Symptoms", "Risk Priority", "Common Treatment", "Nursing Focus"],
        "Depression": [
            "Mood disorder",
            "Sadness, anhedonia, low energy, suicidal ideation",
            "Suicide risk",
            "Antidepressants, psychotherapy, ECT in severe cases",
            "Safety, emotional support, suicide assessment"
        ],
        "Schizophrenia": [
            "Psychotic/thought disorder",
            "Hallucinations, delusions, disorganized thinking",
            "Risk from hallucinations or impaired judgment",
            "Antipsychotics, psychosocial rehabilitation",
            "Reality orientation, safety, medication adherence"
        ]
    })
    st.dataframe(comparison, use_container_width=True)

# =========================
# Virtual Patient
# =========================
with tabs[2]:
    st.markdown('<div class="section-title">🧑‍⚕️ Virtual Patient Simulation</div>', unsafe_allow_html=True)

    case_name = st.selectbox("Choose a patient case", list(patient_cases.keys()))
    case = patient_cases[case_name]

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="card"><h3>Patient Profile</h3>', unsafe_allow_html=True)
        for key, value in case["profile"].items():
            st.write(f"**{key}:** {value}")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card"><h3>Mental Status Summary</h3>', unsafe_allow_html=True)
        for key, value in case["mse"].items():
            st.write(f"**{key}:** {value}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="info">
<b>Instructions:</b> Ask the virtual patient a therapeutic interview question.
Try questions about mood, sleep, appetite, hallucinations, suicide, family support, medication, and daily functioning.
</div>
""", unsafe_allow_html=True)

        suggested_questions = {
            "Depression with Suicide Risk": [
                "How do you feel today?",
                "How is your sleep?",
                "Do you have thoughts of suicide or self-harm?",
                "How is your appetite?",
                "Do you have family support?",
                "How does this affect your study?"
            ],
            "Schizophrenia with Auditory Hallucinations": [
                "Do you hear voices?",
                "What do the voices say?",
                "Do you feel people are watching you?",
                "Are you taking your medication?",
                "How is your sleep?",
                "Do you feel unsafe or at risk of harming yourself or others?"
            ]
        }

        question_choice = st.selectbox("Suggested questions", ["Write my own question"] + suggested_questions[case_name])
        if question_choice == "Write my own question":
            question = st.text_input("Type your question to the patient")
        else:
            question = st.text_input("Selected question", value=question_choice)

        if st.button("Send Question", type="primary"):
            if question.strip():
                response = patient_response(case_name, question)
                feedback = communication_feedback(question)

                st.markdown(f'<div class="student"><b>Student:</b> {question}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="patient"><b>Virtual Patient:</b> {response}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="good">{feedback}</div>', unsafe_allow_html=True)
            else:
                st.warning("Please write a question first.")

# =========================
# Clinical Scenario
# =========================
with tabs[3]:
    st.markdown('<div class="section-title">📂 Clinical Scenarios</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">
<h3>Interactive Clinical Scenario Files</h3>
<p>
These clinical scenario PDFs are designed to help nursing students apply psychiatric theory in realistic clinical situations.
Students can review the scenarios, analyze patient conditions, identify nursing diagnoses, and discuss interventions.
</p>
</div>
""", unsafe_allow_html=True)

    scenarios = [
        ("Clinical Scenario 1", "clinical_scenarios/clinical scenario1.pdf"),
        ("Clinical Scenario 2", "clinical_scenarios/clinical scenario2.pdf"),
        ("Clinical Scenario 3", "clinical_scenarios/clinical scenario3.pdf"),
    ]

    for title, path in scenarios:
        with open(path, "rb") as file:
            st.download_button(
                label=f"📥 Download {title}",
                data=file,
                file_name=path.split("/")[-1],
                mime="application/pdf"
            )

# =========================
# Clinical Assessment
# =========================
with tabs[4]:
    st.markdown('<div class="section-title">📝 Clinical Assessment Tool</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">
<h3>Suicide Risk Screening</h3>
<p>Select the findings present in the patient. The tool will estimate the risk level for educational purposes.</p>
</div>
""", unsafe_allow_html=True)

    risk_items = {
        "Hopelessness": 1,
        "Social withdrawal": 1,
        "Talking about death": 1,
        "Passive suicidal ideation": 2,
        "Active suicidal thoughts": 2,
        "Specific suicide plan": 3,
        "Access to means": 3,
        "Previous suicide attempt": 3,
        "Poor family support": 1,
        "Severe insomnia": 1
    }

    score = 0
    selected = []
    cols = st.columns(2)
    for i, (item, points) in enumerate(risk_items.items()):
        with cols[i % 2]:
            if st.checkbox(item):
                score += points
                selected.append(item)

    level, style = risk_level(score)

    st.markdown(f"### Total Risk Score: {score}")
    if style == "good":
        st.markdown(f'<div class="good"><b>Estimated Risk Level:</b> {level}</div>', unsafe_allow_html=True)
    elif style == "warn":
        st.markdown(f'<div class="warn"><b>Estimated Risk Level:</b> {level}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="danger"><b>Estimated Risk Level:</b> {level} — Immediate safety interventions are required.</div>', unsafe_allow_html=True)

    st.markdown("### Priority Nursing Actions")
    if score <= 2:
        st.write("✅ Continue assessment and provide emotional support.")
        st.write("✅ Encourage expression of feelings.")
        st.write("✅ Educate about follow-up and support systems.")
    elif score <= 5:
        st.write("⚠️ Increase observation and assess suicidal ideation directly.")
        st.write("⚠️ Remove potentially harmful objects.")
        st.write("⚠️ Inform clinical supervisor/team.")
    else:
        st.write("🚨 Ensure constant observation.")
        st.write("🚨 Remove all dangerous objects.")
        st.write("🚨 Notify psychiatrist/clinical team immediately.")
        st.write("🚨 Do not leave the patient alone.")

# =========================
# Nursing Process
# =========================
with tabs[5]:
    st.markdown('<div class="section-title">🩺 Nursing Process Builder</div>', unsafe_allow_html=True)

    condition = st.selectbox("Select condition", ["Depression with Suicide Risk", "Schizophrenia"])

    if condition == "Depression with Suicide Risk":
        diagnoses = [
            "Risk for self-directed violence related to hopelessness and suicidal ideation",
            "Ineffective coping related to depressive symptoms",
            "Disturbed sleep pattern related to persistent sadness and anxiety",
            "Low self-esteem related to feelings of worthlessness"
        ]
        interventions = [
            "Establish a trusting therapeutic relationship.",
            "Ask directly about suicidal thoughts, plan, and means.",
            "Provide a safe environment and remove harmful objects.",
            "Observe the patient closely according to risk level.",
            "Encourage verbalization of feelings.",
            "Support medication adherence and follow-up care."
        ]
        outcomes = [
            "Patient will remain safe and free from self-harm.",
            "Patient will verbalize feelings and seek help when suicidal thoughts increase.",
            "Patient will identify at least two coping strategies.",
            "Patient will show improvement in sleep and daily functioning."
        ]
    else:
        diagnoses = [
            "Disturbed sensory perception related to auditory hallucinations",
            "Disturbed thought process related to delusional beliefs",
            "Impaired verbal communication related to disorganized thinking",
            "Impaired social interaction related to suspiciousness and poor trust"
        ]
        interventions = [
            "Assess hallucination content and risk of command hallucinations.",
            "Use simple and clear communication.",
            "Do not argue with delusions or reinforce hallucinations.",
            "Provide a calm, structured, low-stimulus environment.",
            "Encourage reality-based conversation.",
            "Teach coping strategies for hallucinations.",
            "Encourage medication adherence and family education."
        ]
        outcomes = [
            "Patient will discuss hallucinations with nurse.",
            "Patient will use coping strategies to manage voices.",
            "Patient will communicate basic needs clearly.",
            "Patient will participate gradually in structured activities."
        ]

    st.markdown("### Suggested Nursing Diagnoses")
    for d in diagnoses:
        st.write(f"🧾 {d}")

    st.markdown("### Priority Nursing Interventions")
    for i in interventions:
        st.write(f"✅ {i}")

    st.markdown("### Expected Outcomes")
    for o in outcomes:
        st.write(f"🎯 {o}")

# =========================
# Quiz
# =========================
with tabs[6]:
    st.markdown('<div class="section-title">🎯 Self-Assessment Quiz</div>', unsafe_allow_html=True)

    questions = [
        ("Which symptom is strongly associated with depression?", ["Hallucination", "Anhedonia", "Grandiosity"], "Anhedonia"),
        ("What is the priority when a patient expresses suicidal ideation?", ["Give advice", "Ensure safety", "Ignore it"], "Ensure safety"),
        ("Which is a positive symptom of schizophrenia?", ["Flat affect", "Avolition", "Hallucination"], "Hallucination"),
        ("Which neurotransmitter theory is commonly linked with schizophrenia?", ["Dopamine hypothesis", "Insulin theory", "Calcium theory"], "Dopamine hypothesis"),
        ("ECT may be indicated in:", ["Severe treatment-resistant depression", "Simple headache", "Mild fatigue"], "Severe treatment-resistant depression"),
        ("The nurse should respond to delusions by:", ["Arguing strongly", "Accepting the feeling without validating the belief", "Laughing"], "Accepting the feeling without validating the belief"),
        ("Therapeutic communication includes:", ["Judgment", "Active listening", "Threatening"], "Active listening"),
        ("Legal and ethical care includes:", ["Breach of confidentiality", "Informed consent", "Ignoring patient rights"], "Informed consent"),
        ("A patient hearing voices is experiencing:", ["Delusion", "Hallucination", "Apathy"], "Hallucination"),
        ("The safest environment for a suicidal patient includes:", ["Sharp objects nearby", "Low observation", "Removing harmful objects"], "Removing harmful objects"),
        ("Negative symptoms of schizophrenia include:", ["Avolition", "Grandiosity", "Panic attack"], "Avolition"),
        ("The nursing process begins with:", ["Evaluation", "Assessment", "Discharge"], "Assessment"),
        ("A direct question about suicide is:", ["Forbidden", "Appropriate and important", "Always harmful"], "Appropriate and important"),
        ("A low-stimulus environment is useful for:", ["Agitated psychotic patients", "All healthy visitors", "Only surgical patients"], "Agitated psychotic patients"),
        ("One key role of the psychiatric nurse is:", ["Promoting safety", "Making fun of symptoms", "Avoiding communication"], "Promoting safety")
    ]

    answers = []
    for idx, (q, options, correct) in enumerate(questions, start=1):
        answers.append(st.radio(f"{idx}. {q}", options, key=f"quiz_{idx}"))

    if st.button("Submit Quiz", type="primary"):
        total = 0
        for ans, (_, _, correct) in zip(answers, questions):
            if ans == correct:
                total += 1

        st.markdown(f"## Your Score: {total} / {len(questions)}")
        if total >= 13:
            st.success("Excellent performance. You demonstrate strong theoretical and clinical understanding.")
        elif total >= 9:
            st.info("Good performance. Review the areas you missed.")
        else:
            st.warning("Needs improvement. Review the theoretical content and nursing process sections.")

# =========================
# Instructor Guide
# =========================
with tabs[7]:
    st.markdown('<div class="section-title">👩‍🏫 Instructor Guide</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">
<h3>How to Use This Module</h3>
<ol>
<li>Start with the Theory Hub to review key psychiatric concepts.</li>
<li>Use the Virtual Patient tab for interview practice.</li>
<li>Use the Clinical Scenario tab to download and discuss PDF-based clinical cases.</li>
<li>Ask students to assess suicide risk using the Clinical Assessment Tool.</li>
<li>Guide students to build a nursing care plan through the Nursing Process Builder.</li>
<li>End with the Quiz to evaluate learning outcomes.</li>
</ol>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="warn">
<b>Important:</b> This module is an educational simulation. It does not replace real clinical supervision,
medical diagnosis, or professional psychiatric care.
</div>
""", unsafe_allow_html=True)

# =========================
# References
# =========================
with tabs[8]:
    st.markdown('<div class="section-title">📖 References</div>', unsafe_allow_html=True)
    st.write("1. Stuart, G. W. (2016). Principles and Practice of Psychiatric Nursing.")
    st.write("2. Videbeck, S. L. (2016). Psychiatric-Mental Health Nursing.")
    st.write("3. Varcarolis, E. M. (2017). Essentials of Psychiatric Mental Health Nursing.")
    st.write("4. Faculty of Nursing, Cairo University. Psychiatric Mental Health Nursing Lecture Notes.")
    st.write("5. Course materials: NUR 401 and NUR 402.")

st.markdown("""
<div class="footer">
Psychiatric Nursing AI Teaching Module | Educational Prototype | Developed for Academic Use
</div>
""", unsafe_allow_html=True)

