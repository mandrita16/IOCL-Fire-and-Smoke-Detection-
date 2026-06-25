import streamlit as st
import pandas as pd
import os
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

LOG_FILE = "logs/fire_log.csv"
SCREENSHOT_DIR = "screenshots"

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="IOCL Fire Monitoring",
    page_icon="🔥",
    layout="wide"
)

# Auto Refresh
st_autorefresh(
    interval=5000,
    key="refresh"
)

# ==================================
# CSS
# ==================================

st.markdown("""
<style>

.main{
    background-color:#0f172a;
}

[data-testid="metric-container"]{
    background-color:#1e293b;
    border-radius:15px;
    padding:15px;
    border:1px solid #334155;
}

h1,h2,h3{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# HEADER
# ==================================

st.markdown("""
# 🔥 IOCL Fire & Smoke Monitoring Dashboard
### Real-Time Industrial Surveillance System
""")

# ==================================
# LOG FILE
# ==================================

if os.path.exists(LOG_FILE):

    df = pd.read_csv(LOG_FILE)

    if len(df) > 0:

        df = df.sort_values(
            "Timestamp",
            ascending=False
        )

        # =========================
        # TOP METRICS
        # =========================

        total_events = len(df)

        highest_conf = round(
            df["Confidence"].max(),
            3
        )

        screenshot_count = 0

        if os.path.exists(SCREENSHOT_DIR):
            screenshot_count = len(
                os.listdir(SCREENSHOT_DIR)
            )

        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.metric(
                "🔥 Fire Events",
                total_events
            )

        with col2:
            st.metric(
                "🎯 Max Confidence",
                highest_conf
            )

        with col3:
            st.metric(
                "📸 Screenshots",
                screenshot_count
            )

        with col4:
            st.metric(
                "🚨 System Status",
                "ACTIVE"
            )

        st.divider()
        st.subheader("🚨 Fire Risk Meter")

        latest_conf = float(df["Confidence"].iloc[0])

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=latest_conf * 100,
            title={'text': "Risk Level (%)"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "red"},
                'steps': [
                    {'range': [0, 40], 'color': "green"},
                    {'range': [40, 70], 'color': "orange"},
                    {'range': [70, 100], 'color': "red"}
                ]
            }
        ))

        fig_gauge.update_layout(
            template="plotly_dark",
            height=350
        )

        st.plotly_chart(
            fig_gauge,
            use_container_width=True
        )
        # =========================
        # 3D GRAPH
        # =========================

        st.subheader(
            "📈 3D Confidence Analysis"
        )

        df_plot = df.copy()

        df_plot["Index"] = range(
            len(df_plot)
        )

        fig3d = go.Figure(
            data=[
                go.Scatter3d(
                    x=df_plot["Index"],
                    y=df_plot["Confidence"],
                    z=df_plot["Confidence"],
                    mode="lines+markers",
                    marker=dict(
                        size=5
                    )
                )
            ]
        )

        fig3d.update_layout(
            template="plotly_dark",
            height=500
        )

        st.plotly_chart(
            fig3d,
            use_container_width=True
        )

        # =========================
        # TREND GRAPH
        # =========================

        st.subheader(
            "📊 Confidence Trend"
        )

        fig2 = px.line(
            df_plot,
            x="Index",
            y="Confidence",
            markers=True
        )

        fig2.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )
        st.subheader("📈 Detection Confidence Distribution")

        fig_hist = px.histogram(
            df,
            x="Confidence",
            nbins=20
        )

        fig_hist.update_layout(
            template="plotly_dark",
            height=400
        )

        st.plotly_chart(
            fig_hist,
            use_container_width=True
        )
        # =========================
        # LOG TABLE
        # =========================
        
        st.subheader(
                    "📋 Event Logs"
                    )

        st.dataframe(
                    df,
                    use_container_width=True,
                    height=400
                )

    else:

        st.warning(
                "No fire events detected yet."
                )

# ==================================
# SCREENSHOT SECTION
# ==================================

st.divider()

st.subheader(
    "📸 Latest Detection Screenshot"
)

if os.path.exists(SCREENSHOT_DIR):

    files = sorted(
        os.listdir(
            SCREENSHOT_DIR
        )
    )

    if len(files) > 0:

        latest = os.path.join(
            SCREENSHOT_DIR,
            files[-1]
        )

        img = Image.open(
            latest
        )

        st.image(
            img,
            use_container_width=True
        )

        st.success(
            f"Latest Event : {files[-1]}"
        )

    else:

        st.info(
            "No screenshots available."
        )