import yt_dlp
import os


def test_indir(url):
    print(f"🚀 Test başlıyor: {url}")

    # Railway'e yüklediğin çerez dosyasının yolu
    cookie_path = "railway_cookies.txt"

    if not os.path.exists(cookie_path):
        print("❌ HATA: railway_cookies.txt dosyası bulunamadı!")
        return

    ydl_opts = {
        'format': 'best[ext=mp4]/mp4',
        'outtmpl': 'test_video.mp4',
        'cookiefile': cookie_path,  # İŞTE YOUTUBE'U KANDIRAN KISIM
        'quiet': False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ BAŞARILI: Video Railway sunucusuna indi!")
    except Exception as e:
        print(f"❌ BAŞARISIZ: Yine engel yedik. Hata: {e}")


if __name__ == "__main__":
    # Test için kısa bir video linki koy
    test_indir("https://www.youtube.com/watch?v=aqz-KE-bpKQ")