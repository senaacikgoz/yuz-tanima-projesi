def get_study_suggestion(emotion):
    suggestions = {
        'happy': "Mutlusun! Bu enerjiyi verimli kullan. Zorlandığın konuları çalışmak için harika bir zaman.",
        'sad': "Biraz üzgün görünüyorsun. Daha hafif, ilgi çekici konularla başlamayı deneyebilirsin. Belki de bir mola iyi gelir.",
        'angry': "Sinirli görünüyorsun. Kısa bir yürüyüş ya da nefes egzersizi yap. Sonra daha sade konulara geç.",
        'surprise': "Şaşkın görünüyorsun. Belki yeni bir konuyu keşfetmenin tam zamanı!",
        'fear': "Endişeli görünüyorsun. Basitten başla, güven kazandıkça zorluk seviyesini artır.",
        'neutral': "Nötr görünüyorsun. Planladığın sıradan çalışma düzeniyle devam edebilirsin.",
        'disgust': "Motivasyonun düşük olabilir. İlgi çekici bir video izle, sonra kısa bir çalışma ile başlayabilirsin."
    }

    # Eğer duyguyu tanıyamazsak varsayılan öneri
    return suggestions.get(emotion, "Duygun net değil, belki kısa bir mola iyi gelir!")
