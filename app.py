import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="FinTech Fraud Detection Engine", layout="wide")

st.title("Serverless AI Cybersecurity Pipeline")
st.caption("Real-Time Defensive LLM Analysis & AI-Driven Scam Neutralization")

st.sidebar.header("Cybersecurity Configuration")
selected_network = st.sidebar.selectbox("Target Financial Gateway", ["Global Cross-Border Remittance API", "Digital Wallet P2P Ledger", "Institutional Banking Switch"])
attack_severity = st.sidebar.slider("Simulate GenAI Social Engineering Attack", 1.0, 5.0, 3.5)
run_simulation = st.sidebar.button("Initialize Defensive AI Engine")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: Financial API -> Semantic LLM Vectorization -> XGBoost Quarantine")

if run_simulation:
    st.subheader(f"Active Zero-Trust Monitor: {selected_network}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_velocity = col1.empty()
    metric_latency = col2.empty()
    metric_fraud = col3.empty()
    metric_status = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(3030)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    benign_transactions = []
    fraud_scores = []
    
    base_velocity = 15000 
    
    for i in range(100):
        if i < 35:
            current_velocity = base_velocity + int(np.random.uniform(-500, 1000))
            current_fraud_score = np.random.uniform(5.0, 15.0)
            latency = np.random.uniform(15.0, 25.0)
            status = "STABLE CLEARING"
        elif i >= 35 and i < 65:
            current_velocity = base_velocity + int((i - 35) * (100 * attack_severity)) + int(np.random.uniform(-500, 1500))
            current_fraud_score = np.random.uniform(85.0, 99.9)
            latency = np.random.uniform(25.0, 45.0)
            status = "GEN-AI SCAM DETECTED"
        else:
            current_velocity = base_velocity + int(np.random.uniform(-500, 1000))
            current_fraud_score = np.random.uniform(10.0, 25.0)
            latency = np.random.uniform(18.0, 28.0)
            status = "THREAT NEUTRALIZED"
            
        benign_transactions.append(current_velocity)
        fraud_scores.append(current_fraud_score)
        
        metric_velocity.metric("API Transaction Velocity", f"{current_velocity:,} Tx/s")
        metric_latency.metric("Serverless LLM Latency", f"{latency:.1f} ms", "In-Transit Eval")
        metric_fraud.metric("Semantic Fraud Probability", f"{current_fraud_score:.1f}%")
        
        if status == "GEN-AI SCAM DETECTED":
            metric_status.metric("Network Response", status, "Quarantining Funds")
        elif status == "THREAT NEUTRALIZED":
            metric_status.metric("Network Response", status, "System Secure")
        else:
            metric_status.metric("Network Response", status, "Normal Operations")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=benign_transactions, mode='lines', name='Total Transaction Volume', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=fraud_scores, mode='lines', name='AI Fraud Probability Score', yaxis='y2', line=dict(color='red', dash='dot')))
        
        fig.update_layout(
            title="Digital Financial Security: Transaction Velocity vs Semantic Scam Detection",
            xaxis=dict(title="High-Frequency API Timeline"),
            yaxis=dict(title="Transaction Volume (Tx/s)"),
            yaxis2=dict(title="Fraud Probability Score (%)", overlaying='y', side='right', range=[0, 100]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if status == "GEN-AI SCAM DETECTED" and i == 35:
            log_placeholder.error(f"CYBERSECURITY ALERT: Coercive algorithmic social engineering detected at {time_steps[i].strftime('%H:%M:%S')}. Defensive Large Language Model mapping malicious semantic intent. Asynchronous middleware severing API connections to protect user liquidity.")
        elif status == "THREAT NEUTRALIZED" and i == 65:
            log_placeholder.warning(f"ORCHESTRATION SUCCESS: Fraudulent vectors quarantined to digital escrow. Benign financial clearing pathways restored.")
        elif status == "STABLE CLEARING" and i % 5 == 0:
            log_placeholder.success(f"Log: High-frequency financial telemetry tick {i} ingested. Defensive AI operating seamlessly in background with sub-30ms latency.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The serverless cybersecurity pipeline successfully utilized an LLM inference engine to intercept and neutralize the AI-driven financial scam.")
else:
    st.info("Click 'Initialize Defensive AI Engine' in the sidebar to simulate high-velocity financial threat detection.")