Nama    : Gabriel Edgar Firdausyah Nugroho
Kelas   : PBP - B
NPM     : 2106752312

Link menuju Heroku tugas3:
    https://tugas3watchlist.herokuapp.com/mywatchlist
    
1. Jelaskan Perbedaan antara JSON, XML, dan HTML!
    => 

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    =>

3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
    =>Pada poin 1, dengan menggunakan terminal pada vscode, saya membuat aplikasi menggunakan command yang tersedia pada python.
    Lalu, pada poin 2, menambahkan path pada project_django agar bisa mengakses app tersebut.
    Kemudian, sesuai dengan poin 3, saya membuat model di folder app tersebut dan membuat atribut satu per satu, sekaligus menggunakan command pada terminal untuk migrasi data yang berasal dari models.py.
    Setelah itu, di poin 4 dikatakan untuk memberikan minimal 10 data untuk dijadikan objek di MyWatchList, hal itu bisa dilakukan dengan membuat folder bernama fixtures yang berisi berkas dalam format .json, namun agar bisa memasukkan data tersebut diperlukan command pada terminal yaitu loaddata <nama file>. (data yang dibuat sudah sesuai atribut)
    Sesudahnya, pada poin 5 diperlukan membuat function di views.py agar bisa menampilkan xml dan json. Sedangkan untuk HTML, membuat folder bernama templates yang berisikan berkas dalam format .html yang akan menampilkan data dari berkas di folder fixtures
    Pada poin 6, membuat routing dengan membuat urls.py di floder <nama file> dan menambahkan path untuk xml, json, dan html.
    Pada poin 7, Melakukan deployment ke heroku, namun sebelum itu bisa di check beberapa hal yang diperlukan.