import yt_dlp
import os

def download_highest_quality(url):
    # Konfigurasi untuk resolusi & bitrate tertinggi
    ydl_opts = {
        # Prioritas: VP9/AV1 (kualitas terbaik) -> H.264 (kompatibel)
        'format': '(bestvideo[vcodec^=vp9][height>=2160]/bestvideo[vcodec^=av01][height>=2160]/bestvideo[height>=2160])+(bestaudio[acodec=opus]/bestaudio)',
        
        # Paksa merge ke MP4 (jika sumbernya WebM/MKV)
        'merge_output_format': 'mp4',
        
        # Simpan dengan detail bitrate & resolusi di nama file
        'outtmpl': '%(title)s [%(height)sp][%(tbr).0fkbps].%(ext)s',
        
        # Optimalisasi untuk kualitas (bukan kecepatan)
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        
        # Extra settings untuk bitrate tinggi
        'extract_flat': False,
        'verbose': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"\n✅ Download Berhasil!")
            print(f"📁 File: {ydl.prepare_filename(info)}")
            print(f"🖥️ Resolusi: {info.get('height', '?')}p")
            print(f"⚡ Bitrate: {info.get('tbr', '?')} kbps")
            print(f"🔊 Codec: {info.get('vcodec', '?')}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    print("===========================================")
    print("  YouTube Ultra-HD Downloader (4K+ & High Bitrate)")
    print("===========================================")
    url = input("Masukkan URL YouTube: ")
    download_highest_quality(url)