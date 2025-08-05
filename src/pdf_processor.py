import os
import PyPDF2

def extract_text_from_pdfs(directory):
    """
    Mengekstrak teks dari semua file PDF di direktori yang ditentukan.

    Args:
        directory (str): Path ke direktori yang berisi file PDF.

    Returns:
        list[str]: Daftar string, di mana setiap string adalah teks dari satu PDF.
    """
    all_texts = []
    print(f"Memindai file PDF di direktori: {directory}")

    # Iterasi melalui semua file di direktori
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            filepath = os.path.join(directory, filename)
            try:
                doc_text = ""
                with open(filepath, "rb") as file:
                    # Buat objek pembaca PDF
                    pdf_reader = PyPDF2.PdfReader(file)
                    # Ekstrak teks dari setiap halaman
                    for page in pdf_reader.pages:
                        doc_text += page.extract_text()

                all_texts.append(doc_text)
                print(f"Berhasil memproses: {filename}")

            except Exception as e:
                print(f"Gagal memproses {filename}: {e}")

    return all_texts

if __name__ == '__main__':
    # Contoh penggunaan:
    # Skrip ini dapat dijalankan secara independen untuk pengujian.
    paper_directory = 'papers'
    if os.path.exists(paper_directory):
        texts = extract_text_from_pdfs(paper_directory)
        print(f"\nBerhasil mengekstrak {len(texts)} dokumen.")
        if texts:
            print("\n--- Contoh Teks dari Dokumen Pertama ---")
            print(texts[0][:500]) # Cetak 500 karakter pertama dari dokumen pertama
    else:
        print(f"Direktori '{paper_directory}' tidak ditemukan. Jalankan create_test_data.py terlebih dahulu.")
