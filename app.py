import streamlit as st
import requests
import json
import time

# Ganti dengan API key Perplexity kamu
PERPLEXITY_API_KEY = "YOUR_PERPLEXITY_API_KEY"

def query_perplexity(university_name):
    prompt = (
        f"Provide the following structured information about {university_name}: "
        "Country, City, Year Founded, Number of Students, Website, Notable Programs or Faculties, "
        "Accreditation, Tuition (if available). Please format your answer as JSON."
    )

    # Contoh endpoint, sesuaikan dengan endpoint Perplexity API kamu
    url = "https://api.perplexity.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3-sonar-large-32k-online",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 800,
        "temperature": 0.2
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        # Ambil konten text hasil LLM
        try:
            content = response.json()["choices"][0]["message"]["content"]
            # Ekstrak JSON dari response (kadang LLM kasih code block, hapus jika ada)
            if content.startswith("```json"):
                content = content.replace("```json", "").replace("```", "").strip()
            return json.loads(content)
        except Exception as e:
            return {"error": f"Parsing error: {str(e)}", "raw": response.text}
    else:
        return {"error": f"API error: {response.status_code}", "detail": response.text}

st.title("University Data Extractor with Perplexity API")

st.write(
    "Masukkan nama universitas (satu per baris), lalu klik **Fetch Data** untuk mengambil data terstruktur."
)

universities_input = st.text_area(
    "Nama Universitas", 
    "Stanford University\nMassachusetts Institute of Technology\nUniversity of Oxford"
)
universities = [u.strip() for u in universities_input.splitlines() if u.strip()]

if st.button("Fetch Data"):
    all_results = []
    progress = st.progress(0)
    for idx, uni in enumerate(universities):
        st.write(f"Fetching data for: **{uni}** ...")
        result = query_perplexity(uni)
        all_results.append(result)
        progress.progress((idx + 1) / len(universities))
        time.sleep(1.5)  # Hindari rate limit, sesuaikan jika perlu

    st.success("Selesai! Berikut hasilnya:")
    st.json(all_results)
    json_str = json.dumps(all_results, indent=2)
    st.download_button("Download JSON", json_str, file_name="universities.json", mime="application/json")