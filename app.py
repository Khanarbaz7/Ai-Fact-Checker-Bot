import streamlit as st
from fact_checker_bot.src.fact_checker import fact_check_claim

st.set_page_config(page_title="AI Fact Checker Bot", page_icon="🕵️‍♂️", layout="wide")
st.title("🕵️‍♂️ AI Fact Checker Bot")
st.markdown("Enter a claim below and let AI verify it for you with evidence.")

# Session state for results
if "result" not in st.session_state:
    st.session_state.result = None
if "claim" not in st.session_state:
    st.session_state.claim = ""

# Input field
claim = st.text_input("✍️ Enter a claim to fact-check:", value=st.session_state.claim)

def verdict_badge(verdict):
    verdict = verdict.lower().strip()
    if verdict == "true":
        return "✅ **True**"
    elif verdict == "false":
        return "❌ **False**"
    else:
        return "⚠️ **Uncertain**"

# Fact Check button
if st.button("🔍 Fact Check"):
    if claim.strip():
        with st.spinner("Analyzing and verifying..."):
            st.session_state.result = fact_check_claim(claim)
            st.session_state.claim = claim
    else:
        st.warning("Please enter a claim first.")

# Quit / Clear button
if st.button("❌ Quit / Clear"):
    st.session_state.result = None
    st.session_state.claim = ""
    st.success("Session cleared. You can start fresh.")

# Show results if available
if st.session_state.result:
    result = st.session_state.result
    st.markdown("## 📜 Fact-Check Report")
    st.write(f"**Claim:** {result['claim']}")
    st.write(f"**Initial Answer:** {result['initial_answer']}")

    st.markdown("## 🔍 Assumptions & Verification")
    if result['assumptions']:
        for r in result['assumptions']:
            st.markdown(f"**Assumption:** {r['assumption']}")
            st.markdown(f"**Verdict:** {verdict_badge(r['verdict'])}")
            st.markdown(f"**Explanation:** {r['explanation']}")
            if r.get("evidence_links"):
                with st.expander("📂 View Evidence Links"):
                    for link in r["evidence_links"]:
                        st.markdown(f"- [{link}]({link})")
            st.markdown("---")
    else:
        st.warning("No assumptions extracted for this claim.")

    st.markdown("## ✅ Final Answer")
    st.success(result['final_answer'])
