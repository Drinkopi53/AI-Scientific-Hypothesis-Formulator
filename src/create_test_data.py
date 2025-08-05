import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
import textwrap

# Direktori untuk menyimpan PDF
OUTPUT_DIR = "papers"

# Teks abstrak untuk disimulasikan sebagai makalah penelitian
ABSTRACTS = [
    {
        "title": "Genetic_Engineering_Advances",
        "text": """Genetic engineering has advanced significantly. The CRISPR-Cas9 system allows for precise gene editing. This could lead to new therapies for genetic disorders. However, ethical considerations for gene editing in humans are significant."""
    },
    {
        "title": "Photosynthesis_Efficiency",
        "text": """Photosynthesis in plants converts light energy into chemical energy. Chlorophyll is a key pigment in this process. The efficiency of photosynthesis is affected by light intensity, carbon dioxide concentration, and temperature. Understanding these factors is crucial for improving crop yields."""
    },
    {
        "title": "Neuro-degenerative_Diseases",
        "text": """Neuro-degenerative diseases like Alzheimer's are a growing concern. The accumulation of amyloid-beta plaques in the brain is a primary pathological marker. Research is focused on developing drugs that can clear these plaques. Early diagnosis is also critical for effective treatment."""
    },
    {
        "title": "The_Human_Microbiome",
        "text": """The human microbiome plays a key role in health and disease. Gut bacteria, for instance, aid in digestion and immune system development. A disbalance in the microbiome is linked to various conditions, including obesity and autoimmune disorders. Probiotics are being explored as a way to restore balance."""
    },
    {
        "title": "Climate_Change_and_Biodiversity",
        "text": """Climate change impacts biodiversity across ecosystems. Rising temperatures are causing shifts in species distribution. Coral bleaching is a direct consequence of warmer ocean waters. Conservation efforts must address the root causes of climate change to be effective."""
    }
]

def create_pdf(title, text, directory):
    """Membuat file PDF dari judul dan teks yang diberikan."""
    filepath = os.path.join(directory, f"{title}.pdf")
    c = canvas.Canvas(filepath, pagesize=letter)
    width, height = letter

    # Atur judul
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height - 72, title.replace('_', ' '))

    # Atur isi teks dengan pembungkusan
    styles = getSampleStyleSheet()
    style = styles['BodyText']
    p = Paragraph(text, style)

    # Hitung ukuran paragraf dan gambar
    p_width, p_height = p.wrapOn(c, width - 144, height) # 72 point margin on each side
    p.drawOn(c, 72, height - 100 - p_height)

    c.save()
    print(f"Berhasil membuat: {filepath}")

def main():
    """Fungsi utama untuk membuat semua PDF uji."""
    # Pastikan direktori output ada
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Buat PDF untuk setiap abstrak
    for abstract in ABSTRACTS:
        create_pdf(abstract["title"], abstract["text"], OUTPUT_DIR)

if __name__ == "__main__":
    main()
