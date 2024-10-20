'''[
    {
        "private_key": "PRIVATE_KEY_1"
    },
    {
        "private_key": "PRIVATE_KEY_2"
    }
] '''

Jika ada masalah terkait port yang sudah digunakan, coba hentikan container yang berjalan dengan:

bash
Salin kode
docker ps
docker stop [container_id]

Build Image Docker
Jalankan perintah ini di terminal untuk membangun image Docker dari Dockerfile:

bash
Salin kode
docker build -t faucet-bot .

Jalankan Container
Setelah image selesai dibangun, jalankan container dengan perintah berikut:

bash
Salin kode
docker run -d faucet-bot
