Nama    : Gabriel Edgar Firdausyah Nugroho
Kelas   : PBP - B
NPM     : 2106752312

Link menuju Heroku tugas3:
    https://tugas3watchlist.herokuapp.com/mywatchlist
    
1. Jelaskan Perbedaan antara JSON, XML, dan HTML!
    =>JSON atau JavaScript Object Notation berbeda dengan yang lainnya (dalam format yang serupa), JSON memiliki struktur data yang sederhana dan mudah untuk dipahami. Itulah mengapa JSON sering digunakan pada API. JSON terdiri atas dua bagian, yaitu Kumpulan value yang saling berpasangan dengan Key-nya. Dalam JSON, contohnya adalah object dan daftar value yang berurutan.
    
    =>XML merupakan markup language yang digunakan untuk menyederhanakan proses _Storing_ dan _data delivery_ antarserver. File XML digunakan untuk membuat format informasi umum serta menjadi sarana untuk membagikan format dan data yang digunakan di World Wide Web, intranet, dan lainnya yang menggunakan teks ASCII standar. XML sendiri sering dianggap mirip dengan HTML. Baik XML dan HTML mengandung simbol-simbol markup yang berfungsi untuk mendeskripsikan konten sebuah halaman atau file.
    
    =>HTML bisa didefinisikan suatu bahasa markup. Dengan HTML kita dapat membuat halaman statis milik sendiri. HTML bukan digunakan untuk _data delevery_ melainkan untuk menampilkan data. HTML adalah kombinasi dari Hypertext dan bahasa Markup. Hypertext mendefinisikan link antara halaman web.
    
    Perbedaan yang terlihat jelasa antara ketiganya :
    => JSON hanya mendukung translasi menggunakan encoding UTF-8, sedangkan XML mendukung berbagai macam encoding.
    => JSON mendukung penggunaan array sedangkan XML tidak
    => HTML digunakan untuk menyusun teks pada halaman web agar ditampilkan dengan tepat di browser web. XML umumnya digunakan untuk menyusun data atau pesan.
       Sedangkan JSON digunakan untuk merepresentasikan data sebagai pasangan key-value.

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    => Data-delivery adalah hal yang krusial di dalam proses kerja platform karena pada suatu platform seringkali terjadinya pertukaran data antara user atau clients dan juga server. Data delivery ditujukan untuk memudahkan suatu platform dalam melakukan pengiriman data. Data tersebut tentu memerlukan berbagai format dalam pertukarannya. Format yang seringkali digunakan antara lain adalah HTML, JSON, maupun XML. Jika tidak ada mekanisme tersebut, maka data dari database tidak bisa ditampilkan.

3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
    =>Pada poin 1, dengan menggunakan terminal pada vscode, saya membuat aplikasi menggunakan command yang tersedia pada python.
    Lalu, pada poin 2, menambahkan path pada project_django agar bisa mengakses app tersebut.
    Kemudian, sesuai dengan poin 3, saya membuat model di folder app tersebut dan membuat atribut satu per satu, sekaligus menggunakan command pada terminal untuk migrasi data yang berasal dari models.py.
    Setelah itu, di poin 4 dikatakan untuk memberikan minimal 10 data untuk dijadikan objek di MyWatchList, hal itu bisa dilakukan dengan membuat folder bernama fixtures yang berisi berkas dalam format .json, namun agar bisa memasukkan data tersebut diperlukan command pada terminal yaitu loaddata <nama file>. (data yang dibuat sudah sesuai atribut)
    Sesudahnya, pada poin 5 diperlukan membuat function di views.py agar bisa menampilkan xml dan json. Sedangkan untuk HTML, membuat folder bernama templates yang berisikan berkas dalam format .html yang akan menampilkan data dari berkas di folder fixtures
    Pada poin 6, membuat routing dengan membuat urls.py di floder <nama file> dan menambahkan path untuk xml, json, dan html.
    Pada poin 7, Melakukan deployment ke heroku, namun sebelum itu bisa di check beberapa hal yang diperlukan.

![HTML PostMan](https://user-images.githubusercontent.com/94152526/191652843-e8cef3bc-0afe-422b-b950-7eea762c45a4.jpg)


![JSON Postman](https://user-images.githubusercontent.com/94152526/191652694-bc4d1827-e1c8-45d4-93f5-0d5cecf2fcfb.jpg)

![XML Postman](https://user-images.githubusercontent.com/94152526/191652733-3c1c4019-d081-40c4-98ba-cf4ab9a60251.jpg)

