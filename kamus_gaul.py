meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL" : "tanggapan terhadap lelucon"
            }

word = input('masukkan kata gaul:')
if word.upper() in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word.upper()])
else:
    print('error!')
