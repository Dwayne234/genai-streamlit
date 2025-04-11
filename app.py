import streamlit as st
import requests

st.set_page_config(page_title="AI Research Assistant", layout="wide")

# Title and instructions
st.title("📚 Dwayne AI Research Assistant")
st.markdown("Ask me anything about Transformers, Attention Mechanisms, or recent ML papers!")

# Input box for user query
query = st.text_input("🔍 Enter your research question:")

# If the button is pressed, send the query to the agent
if st.button("Ask"):
    if query:
        with st.spinner("Thinking..."):
            try:
                # GenAI agent URL
                url = "https://agent-ulu33zblg2glgvqbbyvx3ehm-z4n7t.ondigitalocean.app/api/v1/chat/completions"
                
                # access key
                headers = {
                    "Authorization": "Bearer bgs5M_ebwySa-gCuda98uquc5RApNzFs",
                    "Content-Type": "application/json"
                }

                payload = {
                    "messages": [{"role": "user", "content": query}],
                    "stream": False
                }

                res = requests.post(url, json=payload, headers=headers)
                answer = res.json().get("choices", [{}])[0].get("message", {}).get("content", "No answer returned.")
                
                st.success("✅ Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"❌ Error: {e}")
