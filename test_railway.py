import yt_dlp


def test_indir_cookisiz(url):
    print(f"🚀 Çerezsiz ve güvenli test başlıyor: {url}")

    path = "test_video.mp4"

    ydl_opts = {
        'format': 'best[ext=mp4]/mp4',
        'outtmpl': path,
        # Çerez dosyası satırı TAMAMEN KALDIRILDI, kontrol yok
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'ios']
            }
        },
        'user_agent': 'android-app/com.google.android.youtube/19.05.36 (Linux; U; Android 14; tr_TR)',
        'quiet': False,
        'no_warnings': True,
    }

    try:
        print("🤖 Android taklidi yapılıyor (Çerez kullanılmıyor)...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ BAŞARILI! Railway'de çerezsiz indirmeyi başardık.")
    except Exception as e:
        print(f"❌ BAŞARISIZ! YouTube yine 'bot' dedi. Hata: {e}")


if __name__ == "__main__":
    # Test linki
    test_indir_cookisiz("https://www.youtube.com/watch?v=aqz-KE-bpKQ")