"""
===============================
LLM Summarizer Guide (2026)
===============================

This file explains how to use free LLMs to summarize text, including:
- Recommended models
- Token setup
- Required libraries
- Working Python code

--------------------------------
Step 1: Install Required Libraries
--------------------------------

You will need:

1) openai compatible client (for HuggingFace Router)
2) requests (optional for direct API calls)

Install with pip:

pip install openai requests

"""

# ---------------------------------
# Step 2: Working Free LLMs (No Billing)
# ---------------------------------

# 1) HuggingFace Models (Free Tier)
# ---------------------------------
# These models are free, may require agreeing to license on model page:
# - bigcode/starcoder          (coding, instruction)
# - mistralai/Mistral-7B-Instruct-v0.2  (general purpose, instruction)
# - EleutherAI/gpt-neoX-20B   (open-source large language model)
# Notes:
#   - Some models require clicking "Access repository" / "Agree to license"
#   - Avoid deprecated models like:
#       - mistralai/Mistral-7B-Instruct-v0.1 (deprecated)
#       - bigcode/starcoder old versions
#   - Use new router endpoint: https://router.huggingface.co

# 2) Groq API (Free Tier, No Card)
# ---------------------------------
# - llama-3.1-8b-instant
# - mixtral-8x7b-32768
# Sign up: https://console.groq.com
# Get API key (no billing needed)
# Install: pip install groq

# 3) GPT4All (Local, No API)
# --------------------------
# - Phi-3-mini-4k-instruct.Q4_0.gguf  (lightweight)
# - Meta-Llama-3-8B-Instruct.Q4_0.gguf
# Install: pip install gpt4all
# No billing, runs fully locally.

# ---------------------------------
# Step 3: Create HuggingFace Token
# ---------------------------------
# 1) Go to https://huggingface.co
# 2) Log in / Sign up
# 3) Go to Settings -> Access Tokens
# 4) Click "New Token"
# 5) Choose Role: "Read"
# 6) Copy token
# 7) You will use it in Python like:
#    os.environ['HF_TOKEN'] = "hf_xxxxx"


"""
-----------------------------
Step 6: Notes and Tips
-----------------------------

1) Always use the **latest model versions** listed above.
   Old models like Mistral v0.1 or Groq llama3-8b-8192 are deprecated and will fail.

2) Free tiers may have **rate limits**.
   For heavy usage, consider local models (GPT4All, Ollama).

3) You can replace the model in the summarize_text() function:
   - bigcode/starcoder
   - mistralai/Mistral-7B-Instruct-v0.2
   - EleutherAI/gpt-neoX-20B

4) For Streamlit integration, you can wrap summarize_text() like:

import streamlit as st

st.title("Text Summarizer")
user_text = st.text_area("Paste your text here:")
if st.button("Summarize"):
    st.write(summarize_text(user_text))

5) Always keep your HF_TOKEN **secret**.
"""