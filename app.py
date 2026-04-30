import streamlit as st
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchAI — Pipeline",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&f[]=cabinet-grotesk@700,800&display=swap');

:root {
  --bg:           #f7f6f2;
  --surface:      #f9f8f5;
  --surface-2:    #ffffff;
  --border:       rgba(40,37,29,0.1);
  --text:         #28251d;
  --text-muted:   #7a7974;
  --primary:      #01696f;
  --primary-h:    #0c4e54;
  --primary-hl:   #cedcd8;
  --success:      #437a22;
  --warning:      #964219;
  --error:        #a12c7b;
  --radius:       0.75rem;
  --shadow:       0 2px 12px rgba(40,37,29,0.08);
}

html, body, [data-testid="stAppViewContainer"] {
  background: var(--bg) !important;
  font-family: 'Satoshi', system-ui, sans-serif !important;
  color: var(--text) !important;
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }

[data-testid="stAppViewContainer"] > .main > .block-container {
  padding: 2rem 2.5rem 4rem !important;
  max-width: 1100px !important;
}

/* ── Header ── */
.app-header {
  display: flex; align-items: center; gap: 1rem;
  margin-bottom: 2.5rem; padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--border);
}
.app-logo {
  width: 42px; height: 42px; background: var(--primary);
  border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.app-title { font-family: 'Cabinet Grotesk', sans-serif; font-size: 1.5rem; font-weight: 800; color: var(--text); letter-spacing: -0.02em; }
.app-subtitle { font-size: 0.875rem; color: var(--text-muted); margin-top: 1px; }

/* ── Input card ── */
.input-card {
  background: var(--surface-2); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 1.5rem; margin-bottom: 2rem; box-shadow: var(--shadow);
}

/* ── Pipeline section label ── */
.pipeline-label {
  font-size: 0.75rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 0.75rem;
}

/* ── Progress bar ── */
.progress-wrap { margin-bottom: 1.5rem; }
.progress-track { height: 5px; background: rgba(40,37,29,0.08); border-radius: 999px; overflow: hidden; }
.progress-fill  { height: 100%; background: var(--primary); border-radius: 999px; transition: width 400ms cubic-bezier(.4,0,.2,1); }
.progress-meta  { display:flex; justify-content:space-between; margin-top:0.35rem; }
.progress-meta span { font-size: 0.75rem; color: var(--text-muted); }

/* ── st.status() overrides ── */
[data-testid="stStatusContainer"] {
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  background: var(--surface-2) !important;
  box-shadow: var(--shadow) !important;
  margin-bottom: 0.75rem !important;
}

/* ── Result sections inside status ── */
.res-label {
  font-size: 0.7rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.07em; color: var(--text-muted); margin: 0.75rem 0 0.3rem;
}
.res-box {
  background: var(--bg); border: 1px solid var(--border); border-radius: 0.5rem;
  padding: 0.875rem 1rem; font-size: 0.875rem; color: var(--text-muted);
  line-height: 1.7; max-height: 260px; overflow-y: auto;
  white-space: pre-wrap; word-break: break-word;
}

/* ── Report card ── */
.report-card {
  background: var(--surface-2); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 2rem 2.25rem; margin-top: 2rem; box-shadow: var(--shadow);
}
.report-heading {
  font-family: 'Cabinet Grotesk', sans-serif; font-size: 1.15rem; font-weight: 800;
  color: var(--text); margin-bottom: 0.25rem;
}
.report-divider { border: none; border-top: 1px solid var(--border); margin: 1rem 0; }
.critic-box {
  background: #fffdf7; border: 1px solid #e8e2d0; border-radius: 0.5rem;
  padding: 1rem 1.25rem; font-size: 0.875rem; line-height: 1.75; color: var(--text-muted);
  margin-top: 0.5rem;
}

/* ── Completion banner ── */
.done-banner {
  display: flex; align-items: center; gap: 0.75rem;
  background: #d4dfcc; border: 1px solid #b5c9ab; border-radius: 0.5rem;
  padding: 0.75rem 1rem; margin-bottom: 1.5rem; font-size: 0.875rem;
  color: var(--success); font-weight: 600;
}

/* ── Step counter pills ── */
.step-pills {
  display: flex; gap: 0.5rem; margin-bottom: 1rem; flex-wrap: wrap;
}
.pill {
  font-size: 0.72rem; font-weight: 600; padding: 0.2rem 0.65rem;
  border-radius: 999px; border: 1px solid;
}
.pill-done    { background: #d4dfcc; color: var(--success); border-color: #b5c9ab; }
.pill-running { background: #dff0f0; color: var(--primary); border-color: #a8cfd1; }
.pill-pending { background: #f0ede8; color: var(--text-muted); border-color: #dbd8d3; }
.pill-error   { background: #e0ced7; color: var(--error); border-color: #c9afc0; }

/* ── Streamlit input/button overrides ── */
[data-testid="stTextInput"] input {
  background: var(--bg) !important; border: 1px solid var(--border) !important;
  border-radius: 0.5rem !important; color: var(--text) !important;
  font-family: 'Satoshi', sans-serif !important; font-size: 0.9375rem !important;
  padding: 0.6rem 0.9rem !important; box-shadow: none !important;
}
[data-testid="stTextInput"] input:focus {
  border-color: var(--primary) !important;
  box-shadow: 0 0 0 3px rgba(1,105,111,0.12) !important;
}
[data-testid="baseButton-primary"] {
  background: var(--primary) !important; border: none !important; border-radius: 0.5rem !important;
  font-family: 'Satoshi', sans-serif !important; font-weight: 600 !important;
  font-size: 0.9375rem !important; transition: background 150ms ease !important; box-shadow: none !important;
}
[data-testid="baseButton-primary"]:hover { background: var(--primary-h) !important; }
[data-testid="baseButton-secondary"] {
  background: transparent !important; border: 1px solid var(--border) !important;
  border-radius: 0.5rem !important; color: var(--text-muted) !important;
  font-family: 'Satoshi', sans-serif !important; font-size: 0.875rem !important;
}

/* Tabs */
[data-testid="stTabs"] [role="tablist"] { border-bottom: 1px solid var(--border) !important; gap: 0.25rem; }
[data-testid="stTabs"] [role="tab"] { font-family: 'Satoshi', sans-serif !important; font-size: 0.875rem !important; font-weight: 500 !important; }
[data-testid="stTabs"] [role="tab"][aria-selected="true"] { color: var(--primary) !important; border-bottom-color: var(--primary) !important; }
</style>
""", unsafe_allow_html=True)


# ── App header ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
  <div class="app-logo">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.2"
         stroke-linecap="round" stroke-linejoin="round">
      <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
      <path d="M11 8v6M8 11h6"/>
    </svg>
  </div>
  <div>
    <div class="app-title">ResearchAI Pipeline</div>
    <div class="app-subtitle">Search → Scrape → Write → Critique — fully automated research in 4 steps</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Session state defaults ────────────────────────────────────────────────────
for key, val in {
    "pipeline_done": False,
    "state": {},
    "last_topic": "",
    "error": None,
}.items():
    if key not in st.session_state:
        st.session_state[key] = val


# ── Input card ────────────────────────────────────────────────────────────────
st.markdown('<div class="input-card">', unsafe_allow_html=True)
col_in, col_btn, col_clr = st.columns([5, 1.2, 0.8], gap="small")
with col_in:
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Latest advances in multimodal LLMs",
        label_visibility="collapsed",
        key="topic_input",
    )
with col_btn:
    run_clicked = st.button("▶ Run Pipeline", type="primary", use_container_width=True)
with col_clr:
    if st.button("Clear", type="secondary", use_container_width=True):
        st.session_state.pipeline_done = False
        st.session_state.state = {}
        st.session_state.last_topic = ""
        st.session_state.error = None
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)


# ── Run pipeline (live execution with st.status) ───────────────────────────────
if run_clicked and topic.strip():
    st.session_state.pipeline_done = False
    st.session_state.state = {}
    st.session_state.error = None
    st.session_state.last_topic = topic.strip()

    from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

    t = topic.strip()
    s = {}

    # Progress bar (placeholder updated across steps)
    prog_ph = st.empty()

    def render_progress(n, label):
        pct = int(n / 4 * 100)
        prog_ph.markdown(f"""
        <div class="progress-wrap">
          <div class="progress-track">
            <div class="progress-fill" style="width:{pct}%"></div>
          </div>
          <div class="progress-meta">
            <span>{label}</span>
            <span>Step {n} / 4</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    render_progress(0, "Starting pipeline…")

    try:
        # ── Step 1: Search ─────────────────────────────────────────────────
        with st.status("🔍 **Search Agent** — querying the web for reliable information…",
                       expanded=True, state="running") as step1:
            st.caption("Sending query to search tools and aggregating recent sources.")
            render_progress(0, "Step 1 — Search Agent running…")

            agent = build_search_agent()
            result = agent.invoke({
                "messages": [("user", f"Find recent, reliable and detailed information about: {t}")]
            })
            s["search_results"] = result["messages"][-1].content

            st.markdown('<div class="res-label">Search Results</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="res-box">{s["search_results"][:3000]}{"…" if len(s["search_results"]) > 3000 else ""}</div>',
                        unsafe_allow_html=True)
            step1.update(label="🔍 **Search Agent** — complete ✓", state="complete", expanded=False)

        render_progress(1, "Step 2 — Reader Agent running…")

        # ── Step 2: Reader ─────────────────────────────────────────────────
        with st.status("📄 **Reader Agent** — scraping the most relevant URL…",
                       expanded=True, state="running") as step2:
            st.caption("Picking the best URL from search results and extracting full page content.")

            agent2 = build_reader_agent()
            result2 = agent2.invoke({
                "messages": [("user",
                    f"Based on the following search result about '{t}', "
                    f"pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search results:\n {s['search_results'][:800]}")]
            })
            s["scraped_content"] = result2["messages"][-1].content

            st.markdown('<div class="res-label">Scraped Page Content</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="res-box">{s["scraped_content"][:3000]}{"…" if len(s["scraped_content"]) > 3000 else ""}</div>',
                        unsafe_allow_html=True)
            step2.update(label="📄 **Reader Agent** — complete ✓", state="complete", expanded=False)

        render_progress(2, "Step 3 — Writer Chain running…")

        # ── Step 3: Writer ─────────────────────────────────────────────────
        with st.status("✍️ **Writer Chain** — drafting a comprehensive report…",
                       expanded=True, state="running") as step3:
            st.caption("Synthesising search results and scraped content into a structured report.")

            combined = (
                f"SEARCH RESULT:\n{s['search_results']}\n\n"
                f"DETAILED SCRAPED CONTENT:\n{s['scraped_content']}\n\n"
            )
            s["report"] = writer_chain.invoke({"topic": t, "research": combined})

            preview = s["report"][:600] + ("…" if len(s["report"]) > 600 else "")
            st.markdown('<div class="res-label">Draft Report Preview</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="res-box">{preview}</div>', unsafe_allow_html=True)
            step3.update(label="✍️ **Writer Chain** — complete ✓", state="complete", expanded=False)

        render_progress(3, "Step 4 — Critic Chain running…")

        # ── Step 4: Critic ─────────────────────────────────────────────────
        with st.status("🧐 **Critic Chain** — reviewing and critiquing the draft…",
                       expanded=True, state="running") as step4:
            st.caption("Evaluating the report for accuracy, completeness, and clarity.")

            s["critic_report"] = critic_chain.invoke({"report": s["report"]})

            st.markdown('<div class="res-label">Critic Feedback</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="res-box">{s["critic_report"][:2000]}{"…" if len(s["critic_report"]) > 2000 else ""}</div>',
                        unsafe_allow_html=True)
            step4.update(label="🧐 **Critic Chain** — complete ✓", state="complete", expanded=False)

        render_progress(4, "Pipeline complete!")

        st.session_state.state = s
        st.session_state.pipeline_done = True
        st.toast("✅ Research pipeline complete!", icon="🔬")

    except Exception as exc:
        st.session_state.error = str(exc)
        st.session_state.state = s  # save partial results


# ── Post-run: final report card ───────────────────────────────────────────────
if st.session_state.pipeline_done and st.session_state.state:
    s = st.session_state.state
    topic_label = st.session_state.last_topic

    st.markdown("""
    <div class="done-banner">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="20 6 9 17 4 12"/>
      </svg>
      Pipeline completed — all 4 steps finished successfully.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="report-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="report-heading">📋 Research Report — {topic_label}</div>', unsafe_allow_html=True)
    st.markdown('<hr class="report-divider">', unsafe_allow_html=True)

    tab_report, tab_sources, tab_critic = st.tabs(["📝 Full Report", "🔍 Source Data", "🧐 Critic Review"])

    with tab_report:
        if s.get("report"):
            st.markdown(s["report"])
        else:
            st.info("Report not generated.")

    with tab_sources:
        with st.expander("🔍 Search Results", expanded=False):
            st.text(s.get("search_results", "—"))
        with st.expander("📄 Scraped Content", expanded=False):
            st.text(s.get("scraped_content", "—"))

    with tab_critic:
        if s.get("critic_report"):
            st.markdown(f'<div class="critic-box">{s["critic_report"]}</div>', unsafe_allow_html=True)
        else:
            st.info("Critic review not available.")

    st.markdown('<hr class="report-divider">', unsafe_allow_html=True)

    if s.get("report"):
        full_text = (
            f"# Research Report: {topic_label}\n\n"
            f"{s['report']}\n\n---\n\n"
            f"## Critic Review\n\n{s.get('critic_report', '')}"
        )
        st.download_button(
            label="⬇ Download Report (.txt)",
            data=full_text,
            file_name=f"research_{topic_label[:40].replace(' ', '_')}.txt",
            mime="text/plain",
        )

    st.markdown('</div>', unsafe_allow_html=True)


# ── Error display ─────────────────────────────────────────────────────────────
if st.session_state.error:
    st.error(f"**Pipeline error:** {st.session_state.error}")
    if st.session_state.state:
        with st.expander("🔎 Partial results saved", expanded=False):
            for k, v in st.session_state.state.items():
                st.markdown(f"**{k}**")
                st.text(str(v)[:1000])


# ── Empty / idle state ────────────────────────────────────────────────────────
if not st.session_state.last_topic and not st.session_state.pipeline_done and not st.session_state.error:
    st.markdown("""
    <div style="text-align:center;padding:3.5rem 1rem 2rem;color:#7a7974">
      <div style="font-size:2.75rem;margin-bottom:1rem">🔬</div>
      <div style="font-size:1rem;font-weight:700;color:#28251d;margin-bottom:0.5rem">
        Enter a research topic to get started
      </div>
      <div style="font-size:0.875rem;max-width:46ch;margin:0 auto;line-height:1.65">
        The pipeline will search the web, scrape a source, write a full report, and critically
        review it — all automatically.
      </div>
      <div style="display:flex;justify-content:center;gap:1.5rem;margin-top:1.75rem;flex-wrap:wrap">
        <span style="font-size:0.8rem;display:flex;align-items:center;gap:0.4rem">
          <span style="color:#01696f;font-size:1rem">🔍</span> Web search
        </span>
        <span style="font-size:0.8rem;color:#dcd9d5">│</span>
        <span style="font-size:0.8rem;display:flex;align-items:center;gap:0.4rem">
          <span style="color:#01696f;font-size:1rem">📄</span> Deep scrape
        </span>
        <span style="font-size:0.8rem;color:#dcd9d5">│</span>
        <span style="font-size:0.8rem;display:flex;align-items:center;gap:0.4rem">
          <span style="color:#01696f;font-size:1rem">✍️</span> AI-written report
        </span>
        <span style="font-size:0.8rem;color:#dcd9d5">│</span>
        <span style="font-size:0.8rem;display:flex;align-items:center;gap:0.4rem">
          <span style="color:#01696f;font-size:1rem">🧐</span> Critic review
        </span>
      </div>
    </div>
    """, unsafe_allow_html=True)