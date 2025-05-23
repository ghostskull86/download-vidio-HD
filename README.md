# download-vidio-HD
Simple Python script to download videos from YouTube in HD quality using the yt_dlp library. Supports the download process with a progress bar, audio-video merging (using ffmpeg), and URL retrieval automation.

🚀 Fitur Utama:
✅ Download video YouTube dalam resolusi tinggi (HD, hingga 1080p+ jika tersedia)

🎵 Audio dan video otomatis digabung dengan ffmpeg

🔁 Progress download realtime langsung di terminal

🧩 Penanganan otomatis berbagai format dan metadata YouTube

📂 Struktur File:
load.py — Skrip utama Python untuk mengunduh video

requirements.txt — Daftar dependencies Python

📦 Dependensi:
yt_dlp

ffmpeg (pastikan ffmpeg.exe ada di PATH)

⚙️ Cara Pakai:

# 1. Clone repository
https://github.com/ghostskull86/download-vidio-HD.git
cd download-vidio-HD

# 2. (Opsional) Aktifkan virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Jalankan script dan masukkan URL YouTube
python load.py
💡 Catatan:
Pastikan ffmpeg telah terinstal dan ditambahkan ke PATH agar penggabungan video berhasil tanpa error.


