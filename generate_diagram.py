import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Membuat kanvas visualisasi
fig, ax = plt.subplots(figsize=(8, 10))

# Konfigurasi warna latar dan garis tepi boks alir
colors = ['#ffebeb', '#ebefff', '#ebffeb', '#fffbeb', '#f7ebff']
borders = ['#ff4b4b', '#4b86ff', '#4bff4b', '#ffd44b', '#9b4bff']

texts = [
    "1. USER INPUT\nKeluhan Tamu & Keanggotaan\n(VIP / Gold / Standard)",
    "2. PROMPT ENGINE\nSystem Prompt + Strict Guardrails\n(No AI Chatter, No Auto-Refund)",
    "3. LOCAL INFERENCE ENGINE\nLlama-3.1-8B local on Apple Silicon M2\n(Unified Memory)",
    "4. HUMAN-IN-THE-LOOP\nCS Agent Review & Edit Draft\n(Safety Gate)",
    "5. FINAL ACTION EXECUTION\nResponse sent to Guest & Route to PMS"
]

y_positions = [8, 6, 4, 2, 0]

for i, (text, y, color, border) in enumerate(zip(texts, y_positions, colors, borders)):
    # Menggambar kotak proses (rounded rectangle)
    rect = patches.FancyBboxPatch((1, y), 6, 1.2, boxstyle="round,pad=0.1", 
                                 linewidth=2, edgecolor=border, facecolor=color, zorder=2)
    ax.add_patch(rect)
    
    # Menambahkan teks ke dalam kotak
    ax.text(4, y + 0.6, text, ha='center', va='center', fontsize=10, fontweight='bold', color='#333333', zorder=3)
    
    # Menggambar garis panah penghubung alur antar kotak
    if i < len(texts) - 1:
        ax.annotate('', xy=(4, y_positions[i+1] + 1.3), xytext=(4, y),
                    arrowprops=dict(arrowstyle="->", color='#888888', lw=2.5, ls='-'), zorder=1)

ax.set_xlim(0, 8)
ax.set_ylim(-1, 10)
ax.axis('off')

# Menyimpan diagram langsung ke format PNG dan PDF beresolusi tinggi
plt.tight_layout()
plt.savefig('architecture_diagram.png', dpi=300, bbox_inches='tight')
plt.savefig('architecture_diagram.pdf', bbox_inches='tight')
print("Sukses! Berkas 'architecture_diagram.png' dan 'architecture_diagram.pdf' telah dibuat di folder Anda.")