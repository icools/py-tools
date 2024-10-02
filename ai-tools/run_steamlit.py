import streamlit as st
from llm.mixed_llm import MixedLlm

st.title("混合 LLM 問答系統")

question = st.text_input("請輸入您的問題：", "能躺著是不是就不要坐著")

if st.button("提交"):
    mixed_llm = MixedLlm()
    final_answer = mixed_llm.mixed_chat(question)
    
    st.write("最終回答：")
    st.write(final_answer)
    
    if "groq" in mixed_llm.responses:
        with st.expander("Groq 回應", expanded=False):
            st.write(mixed_llm.responses["groq"])
    
    if "samba_nova" in mixed_llm.responses:
        with st.expander("Samba Nova 回應", expanded=False):
            st.write(mixed_llm.responses["samba_nova"])
    
    if "gemini_flash" in mixed_llm.responses:
        with st.expander("Gemini Flash 回應", expanded=False):
            st.write(mixed_llm.responses["gemini_flash"])
    
    with st.expander("查看各模型回應"):
        if "groq" in mixed_llm.responses:
            st.write("Groq 回應：")
            st.write(mixed_llm.responses["groq"])
        if "samba_nova" in mixed_llm.responses:
            st.write("Samba Nova 回應：")
            st.write(mixed_llm.responses["samba_nova"])
        if "gemini_flash" in mixed_llm.responses:
            st.write("Gemini Flash 回應：")
            st.write(mixed_llm.responses["gemini_flash"])