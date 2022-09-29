Link Heroku
https://tugas3watchlist.herokuapp.com/todolist/

**Kegunaan `{% csrf_token %}` pada elemen '<form>'**
  CSRF Token bersifat rahasia dan ditangani dengan cara yang aman sepanjang life cicyle program. Biasanya tindakan yang efektif adalah mengirimkan token ke klien secara tersembunyi pada bagian Form HTML yang dikirimkan menggunakan metode POST. Token kemudian akan sisipkan sebagai parameter permintaan saat Form HTML dikirmkan.
Untuk keamanan tambahan, bagian yang berisi token CSRF harus ditempatkan sedini mungkin dalam HTML, idealnya sebelum bagian input dan lokasi mana pun di mana data yang dapat dikontrol pengguna disematkan di dalam HTML.
Sehingga akan mengurangi berbagai teknik di mana penyerang dapat menggunakan data yang dibuat untuk memanipulasi dokumen HTML dan menangkap bagian dari isinya.

**Apakah kita dapat membuat elemen <form> secara manual tanpa menggunakan generator seperti {{ form.as_table }}**
  Hal itu dapat dilakukan dengan membuat elemen <form> dengan menggunakan wrapper, lalu menentukan attribut function dan action dengan value yang sesuai. attribut action digunakan untuk menspesifikasikan endpoint request yang akan diberikan. attribut function ini digunakan untuk menspesifikasi HTTP method yang akan digunakan untuk mengirim request ke server.

**Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
**
  Disaat user melakukan submit form yang telah dibuat, HTTP akan me-request ke server dengan function dan action yang ada pada form. kemudian action akan memetakan request ke URL, sesuai dengan yang ada pada urls.py. kemudian akan dilanjutkan ke function yang ada di views.py, kemudian akan me-render data di html.
  
**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
  - Membuat aplikasi dengan command prompt/terminal pada folder
  - Mengimplementasi models untuk menambahkan atribut 
  - Mengimplemntasi views untuk membuat function-based views 
  - Mengimplementasi urls untuk menambahkan path/url sesuai dengan views
  - Mengimplementasi templates dengan membuat html yang diperlukan seperti form login dan logout, main page(halaman utama), dan lain-lain
  - Untuk implementasi menghapus Task, dengan membuat function di 'views.py' dan mengimplementasi function tersebut ke sebuah button
  - Deploy ke heroku, dan membuat 2 akun dan 3 dummy data setiap akun
