import streamlit as st
from llm.mixed_chat import MixedChat

if __name__ == "__main__":
    st.title("混合 LLM 問答系統")

    question = st.text_input("請輸入您的問題：")

    if st.button("開始"):
        if not question.strip():
            st.error("請輸入一個問題！")
        else:
            with st.spinner("正在生成回應..."):
                mixed_llm = MixedChat()
                final_answer = mixed_llm.mixed_chat(question)
            
            st.success("生成完成！")
            st.write("最終回答：")
            st.write(final_answer)
            
            st.write("詳細回應：")
            for response in mixed_llm.responses:
                with st.expander(f"{response['character']} ({response['model_name']}) 的回應", expanded=False):
                    st.write(response['response'])