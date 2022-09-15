Nama  : Gabriel Edgar Firdausyah Nugroho
NPM   : 2106752312
Kelas : PBP - B

Link ke Django App Heroku  :
https://catalogtugas2pbp.herokuapp.com/katalog/

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
=> virtual environment merupakan alat untuk memisahkan dependencies dari proyek yang berbeda dengan menciptakan lingkungan terisolasi yang terpisah untuk setiap proyek. Hal ini hanyalah direktori sehingga virtual environment tak terbatas dapat dibuat.
Jika tidak menggunakan virtual environment, aplikasi web berbasis Django masih bisa dijalankan hal itu disebabkan karena requirements yang diperlukan aplikasi bisa diinstall di luar virtual environment. Namun, untuk hasil terbaik disarankan untuk menggunakan virtual environment agar lingkungan pengembangan aplikasi web sesuai dengan apa yang dibutuhkan.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
=> Untuk poin 1, Dengan membuat fungsi pada views.py yang dapat melakukan pengambilan data dari models.py, yang telah mendapatkan data dari initial_catalog_data.json dengan menggunakan terminal melalui perintah "python manage.py makemigrations" dan "python manage.py migrate", lalu mengembalikannya ke dalam sebuah HTML. Untuk poin 2, dapat dilakukan dengan membuat routing dengan menggunakan fungsi path dan include di urls.py pada folder katalog dan membuat routing tambahan di urls.py di folder project_django agar aplikasi bisa dibuka dengan menambahkan /katalog pada web. Untuk poin 3, berdasarkan fungsi yang telah dibuat pada poin 1, kita hanya perlu menuliskan loop untuk menampilkan data pada html. Untuk poin 4, hanya perlu menambahkan beberapa potongan kode ke settings.py karena hal seperti .yml atau procfile telah ada sesuai template, lalu add, commit, dan push. Kemudian, mencari api key untuk heroku dan pembuatan aplikasi melalui heroku dan melihat workflow dan deployment telash selesai.