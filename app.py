import streamlit as st
import ollama

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Sakura CS Assistant", page_icon="🌸")
st.title("🌸 Hotel Sakura: CS Triage & Response Assistant")
st.markdown("Prototipe Sistem Pakar + Local LLM untuk Eskalasi Keluhan Tamu")

# --- SIDEBAR: PENGATURAN MODEL ---
with st.sidebar:
    st.header("Konfigurasi Sistem")
    # Pilihan model disesuaikan dengan Step C
    selected_model = st.selectbox(
        "Pilih Model Lokal (Ollama):",
        ["llama3.1", "mistral-nemo", "qwen2.5"]
    )
    st.info("Pastikan model sudah diunduh via 'ollama run <nama_model>' di terminal.")

# --- FORM INPUT DATA TAMU ---
st.subheader("Data Keluhan Tamu")
customer_tier = st.selectbox("Status Keanggotaan Tamu:", ["Standard", "Gold", "VIP"])
complaint_text = st.text_area("Masukkan teks keluhan tamu:", height=150)

# --- PROSES INFERENSI ---
if st.button("Analisis Keluhan"):
    if not complaint_text:
        st.warning("Silakan masukkan teks keluhan terlebih dahulu.")
    else:
        with st.spinner(f"Menganalisis menggunakan {selected_model}..."):
            
            # --- SYSTEM PROMPT & GUARDRAILS (Draft Awal) ---
            system_prompt = f"""
            Anda adalah AI Customer Service Assistant untuk Hotel Sakura Kyoto.
            Tugas Anda adalah membaca keluhan tamu dan memberikan 3 output:
            1. PRIORITY: (High/Medium/Low)
            2. ESCALATION TEAM: (Misal: IT Support, Finance, Front Office, Housekeeping)
            3. DRAFT RESPONSE: (Respons empatik dalam bahasa Indonesia. Jangan berikan janji mutlak seperti 'uang pasti kembali', dan jangan menyetujui refund secara otomatis).
            
            ATURAN KETAT: 
            - Berikan HANYA 3 output di atas. 
            - JANGAN tambahkan kalimat sapaan AI, penutup, atau komentar seperti 'Saya berharap jawaban ini membantu'.
            
            Status Tamu: {customer_tier}
            Keluhan: {complaint_text}
            
            Berikan jawaban Anda dengan format yang rapi.
            """

            try:
                # Memanggil API lokal Ollama
                response = ollama.chat(model=selected_model, messages=[
                    {
                        'role': 'user',
                        'content': system_prompt
                    }
                ])
                
                # --- MENAMPILKAN HASIL ---
                st.success("Analisis Selesai! (Human-in-the-loop diperlukan sebelum aksi final)")
                st.markdown(response['message']['content'])
                
            except Exception as e:
                st.error(f"Terjadi kesalahan saat menghubungi Ollama: {e}")
                st.markdown("**Fallback Mechanism:** Pastikan aplikasi Ollama berjalan di *background* MacBook Anda.")