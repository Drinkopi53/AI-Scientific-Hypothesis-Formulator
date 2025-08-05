import itertools
import random
from sklearn.feature_extraction.text import TfidfVectorizer

# Template untuk merumuskan hipotesis
HYPOTHESIS_TEMPLATES = [
    "Ada hubungan potensial antara '{concept1}' dan '{concept2}' yang memerlukan penyelidikan lebih lanjut.",
    "Mekanisme yang menghubungkan '{concept1}' dan '{concept2}' dapat menjadi target terapi baru.",
    "Peningkatan regulasi '{concept1}' mungkin secara langsung mempengaruhi aktivitas '{concept2}'.",
    "Ada kesenjangan dalam literatur mengenai interaksi antara '{concept1}' dan '{concept2}'.",
    "Studi lebih lanjut diperlukan untuk memahami bagaimana '{concept1}' memodulasi '{concept2}'."
]

def generate_hypotheses(corpus, num_hypotheses=5, top_n_keywords=5):
    """
    Menghasilkan hipotesis ilmiah berdasarkan korpus teks yang diberikan.

    Args:
        corpus (list[str]): Daftar string, di mana setiap string adalah dokumen.
        num_hypotheses (int): Jumlah hipotesis yang akan dihasilkan.
        top_n_keywords (int): Jumlah kata kunci teratas yang akan dipertimbangkan dari setiap dokumen.

    Returns:
        list[str]: Daftar hipotesis yang dihasilkan.
    """
    if not corpus:
        return ["Korpus input kosong, tidak dapat menghasilkan hipotesis."]

    try:
        # Gunakan TF-IDF untuk mengekstrak kata kunci dari setiap dokumen
        vectorizer = TfidfVectorizer(stop_words='english', max_df=0.85, ngram_range=(1, 2))
        tfidf_matrix = vectorizer.fit_transform(corpus)
        feature_names = vectorizer.get_feature_names_out()

        # Dapatkan kata kunci teratas untuk setiap dokumen
        doc_keywords = []
        for i in range(len(corpus)):
            doc_vector = tfidf_matrix[i]
            # Dapatkan indeks fitur yang diurutkan berdasarkan skor TF-IDF
            sorted_indices = doc_vector.toarray().argsort()[0][::-1]
            # Pilih N kata kunci teratas
            top_keywords = [feature_names[idx] for idx in sorted_indices[:top_n_keywords]]
            doc_keywords.append(top_keywords)

        # Hasilkan hipotesis dengan menggabungkan kata kunci dari dokumen yang sama
        generated_hypotheses = set()
        for keywords in doc_keywords:
            if len(keywords) >= 2:
                # Buat semua pasangan kata kunci yang mungkin
                keyword_pairs = list(itertools.combinations(keywords, 2))
                for pair in keyword_pairs:
                    # Pilih template secara acak
                    template = random.choice(HYPOTHESIS_TEMPLATES)
                    # Format hipotesis
                    hypothesis = template.format(concept1=pair[0], concept2=pair[1])
                    generated_hypotheses.add(hypothesis)

        # Jika tidak ada cukup kombinasi, tambahkan beberapa hipotesis lintas dokumen
        while len(generated_hypotheses) < num_hypotheses:
            # Ambil dua dokumen acak
            doc1_keys = random.choice(doc_keywords)
            doc2_keys = random.choice(doc_keywords)
            if doc1_keys and doc2_keys:
                key1 = random.choice(doc1_keys)
                key2 = random.choice(doc2_keys)
                if key1 != key2:
                    template = random.choice(HYPOTHESIS_TEMPLATES)
                    hypothesis = template.format(concept1=key1, concept2=key2)
                    generated_hypotheses.add(hypothesis)
            # Pencegahan loop tak terbatas
            if len(generated_hypotheses) == 0 and len(doc_keywords) <=1 :
                 break # Tidak dapat menghasilkan lebih banyak

        # Kembalikan jumlah hipotesis yang diminta
        return random.sample(list(generated_hypotheses), min(num_hypotheses, len(generated_hypotheses)))

    except Exception as e:
        return [f"Terjadi kesalahan saat menghasilkan hipotesis: {e}"]

if __name__ == '__main__':
    # Contoh data korpus untuk pengujian
    test_corpus = [
        "Genetic engineering and CRISPR-Cas9 for gene editing.",
        "Photosynthesis efficiency is linked to crop yields.",
        "Alzheimer's disease and amyloid-beta plaques.",
        "The human microbiome and immune system regulation.",
        "Climate change causes coral bleaching."
    ]

    print("--- Menghasilkan Hipotesis dari Data Uji ---")
    hypotheses = generate_hypotheses(test_corpus, num_hypotheses=5)

    if hypotheses:
        for i, h in enumerate(hypotheses, 1):
            print(f"{i}. {h}")
    else:
        print("Tidak ada hipotesis yang dihasilkan.")
