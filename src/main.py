import argparse
import os
from pdf_processor import extract_text_from_pdfs
from hypothesis_generator import generate_hypotheses

def main():
    """
    Fungsi utama untuk menjalankan AI Scientific Hypothesis Formulator.
    """
    # Siapkan parser argumen
    parser = argparse.ArgumentParser(
        description="Menganalisis makalah penelitian dari direktori dan menghasilkan hipotesis ilmiah baru.",
        epilog="Contoh penggunaan: python src/main.py papers/ --num_hypotheses 10"
    )
    parser.add_argument(
        "directory",
        type=str,
        help="Path ke direktori yang berisi makalah penelitian PDF."
    )
    parser.add_argument(
        "--num_hypotheses",
        type=int,
        default=5,
        help="Jumlah hipotesis yang akan dihasilkan."
    )

    args = parser.parse_args()

    # Validasi bahwa direktori input ada
    if not os.path.isdir(args.directory):
        print(f"Error: Direktori yang ditentukan '{args.directory}' tidak ditemukan.")
        return

    print("="*50)
    print("Memulai AI Scientific Hypothesis Formulator")
    print("="*50)

    # Langkah 1: Ekstrak teks dari PDF
    print(f"\n[Langkah 1/3] Memproses file PDF dari '{args.directory}'...")
    document_corpus = extract_text_from_pdfs(args.directory)

    if not document_corpus:
        print("\nTidak ada teks yang diekstrak. Tidak dapat melanjutkan. Pastikan direktori berisi file PDF yang valid.")
        return

    print(f"Berhasil memproses {len(document_corpus)} dokumen.")

    # Langkah 2: Hasilkan hipotesis
    print("\n[Langkah 2/3] Menghasilkan hipotesis berdasarkan teks yang diekstrak...")
    hypotheses = generate_hypotheses(document_corpus, num_hypotheses=args.num_hypotheses)

    # Langkah 3: Tampilkan hasilnya
    print(f"\n[Langkah 3/3] Berhasil Menghasilkan {len(hypotheses)} Hipotesis:")
    print("-"*50)

    if hypotheses:
        for i, h in enumerate(hypotheses, 1):
            print(f"Hipotesis {i}: {h}")
    else:
        print("Tidak dapat menghasilkan hipotesis apa pun dari dokumen yang diberikan.")

    print("\nProses selesai.")
    print("="*50)


if __name__ == "__main__":
    main()
