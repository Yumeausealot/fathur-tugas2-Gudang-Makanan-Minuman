Nama: Dian Fathur Rahman

NPM: 2206082096

Tautan Aplikasi: http://dian-fathur-tugas.pbp.cs.ui.ac.id

**TUGAS 2**

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   jwb:
   
   Pertama saya membuat project Django baru di dalam virtual environment. Kemudian membuat directory baru bernama main di direktori utama. Setelah itu routing main sehingga main dapat berjalan. Di dalam model saya menambahkan atribut wajib. Lalu views ditambahkan file html yang akan dikembalikan sebagai template untuk ditampilkan pada pengguna. Dari urls di dalam main juga kita routing views. setelah itu aplikasi dapat di deploy.
   
   
3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   jwb:
   
   <img width="332" alt="Screenshot 2023-09-13 111531" src="https://github.com/Yumeausealot/fathur-tugas2-mc-shipyards/assets/119997657/0b98492f-c8b1-45a7-b4de-8b444f4084af">

   
5. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   jwb:
   
   Kita menggunakan virtual environment karena dapat mencegah terjadinya masalah dependencies saat melakukan perubahan dalam suatu proyek. Ya bisa, tetapi tidak terisolasi sehingga package yang di instal dapat digunakan oleh project yang lain juga, selain itu proyek akan menjadi berantakan.
   
   
7. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   jwb:

   a. MVC (Model-View-Controller)
   
   Pada MVC, user berinteraksi dengan view, yang meneruskan request kepada controller, lalu controller mengupdate model dan view sesuai dengan modelnya.
   
   b. MVT (Model-View-Template)
   
   Pada MVT, biasanya request diterima oleh URL routing, lalu requestnya akan dijalankan ke directory view yang ingin ditampilkan, dan model juga menerima request sesuai ketentuan. Lalu view akan memberikan template yang berupa file html yang akan ditampilkan ke user.
   
   c. MVVM (Model-View-ViewModel)
   
   Pada MVVM, view dikendalikan oleh viewmodel, jadi jika ada perubahan pada model, viewmodel akan langsung merespon dengan mengubah view.
   
   Perbedaannya adalah dalam interface dengan view dan modelnya MVC menggunakan controller, MVT menggunakan url, MVVM menggunakan viewmodel.


**TUGAS 3**

1. Apa perbedaan antara form POST dan form GET dalam Django?

   POST dipakai untuk mengirim data ke server dan mengembalikan HTTP status code 201 jika sukses terkirim, sedangkan GET dipakai untuk me-read atau retrieve data dari web server dan mengembalikan HTTP status code 200 jika data sukses di retrieve dari server
   
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

   XML mengidentifikasi berbagai jenis data dan menentukan struktur data , JSON digunakan untuk mengirim data dari client ke server, atau sebaliknya, HTML berfungsi untuk menggambarkan bagaimana data akan ditampilkan di dalam web
   
4. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

   Karena JSON memiliki format pertukaran data yang sangat ringan dan lebih mudah dibaca dan ditulis oleh manusia, sehingga mudah untuk diterjemahkan dan generate oleh komputer
   
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

   Pertama, setelah routing dan implementasi skeleton, saya membuat form untuk menerima input data. Setelah itu, pada views saya membuat fungsi yang menerima request dan menambahkan input data baru. Kemudian saya meng-import fungsi yang baru dibuat ke urls agar dapat diakses. Lalu saya membuat file HTML baru untuk menampung input dan menampilkannya. Terakhir saya membuat fungsi untuk JSON, XML, JSON berdasar ID, dan XML berdasar ID di views yang kemudian di import ke urls.
   
6. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

   HTML
   
   <img width="804" alt="Screenshot 2023-09-20 050733" src="https://github.com/Yumeausealot/fathur-tugas2-mc-shipyards/assets/119997657/ed9897ec-8965-4797-9905-2bd2008c2bb6">


   JSON ID
   
   <img width="801" alt="Screenshot 2023-09-20 050918" src="https://github.com/Yumeausealot/fathur-tugas2-mc-shipyards/assets/119997657/87047783-68ff-4bcd-9301-bf15e0fe5b99">


   XML ID
   
   <img width="794" alt="Screenshot 2023-09-20 050857" src="https://github.com/Yumeausealot/fathur-tugas2-mc-shipyards/assets/119997657/1f83cdb1-491e-4290-a2c2-92bf1f8a4be6">


   JSON
   
   <img width="797" alt="Screenshot 2023-09-20 050816" src="https://github.com/Yumeausealot/fathur-tugas2-mc-shipyards/assets/119997657/d9790f00-a101-4e3a-b955-a711e00e7687">


   XML
   
   <img width="799" alt="Screenshot 2023-09-20 050802" src="https://github.com/Yumeausealot/fathur-tugas2-mc-shipyards/assets/119997657/76870d5c-bc09-4ad7-943d-b43649b1e827">


**Tugas 4**

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

   Django UserCreationForm adalah form input user baru bawaan django. Kelebihannya lebih praktis karena sudah menjadi bawaan django. Kekurangannya UserCreationForm adalah tidak memiliki email field, sehingga kita tidak dapat menggunakan email verification untuk memverivikasi akun.
      
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

   Autentikasi adalah proses menentukan identitas pengguna untuk memastikan apakah pengguna asli atau tidak, proses ini biasanya terjadi saat login. Otorisasi adalah proses menentukan akses yang dimiliki oleh pengguna dalam sebuah aplikasi. Keduanya penting karena berhubungan dengan keamanaan informasi pengguna sehingga tidak mudah di akses oleh orang yang tidak berhak.
   
3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah kumpulan informasi yang berisi rekam jejak dan aktivitas ketika menelusuri sebuah web. Django akan menyimpan waktu login dengan fungsi set_cookie, lalu dapat ditampiklkan kembali menggunakan fungsi get.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

   Umumnya cookies tidak bisa mentransfer malware atau virus karena data yang dibawa cookies tidak berubah ketika berpindah dari komputer ke web dan sebaliknya. Namun, hindari mengunjungi situs-situs yang mencurigakan agar mengurangi kemungkinan terjadinya bahaya. 
   
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

   Pertama, saya menambahkan form registrasi, fungsi login, dan fungsi logout. Kemudian, saya menambahkan restriksi akses halaman main sehingga hanya yang telah login yang bisa akses. Lalu saya membuat last login dengan memakai data dari cookies. Terakhir saya menghubungkan produk dengan pengguna yang membuatnya, sehingga pengguna hanya melihat produk-produk yang telah dibuat sendiri. 


**Tugas 5**
1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

   Untuk pemilihan suatu elemen yang memiliki banyak data elemen.
   
2. Jelaskan HTML5 Tag yang kamu ketahui.

   <title>	Tag untuk membuat judul dari sebuah halaman, <head>	Tag untuk membuat informasi tentang dokumen, <body>	Tag untuk membuat tubuh dari sebuah halaman, <form>	Tag untuk membuat sebuah form HTML untuk input pengguna, <button>	Tag untuk membuat sebuah tombol yang dapat diklik, <table>	Tag untuk membuat tabel, <tr>	Tag untuk membuat baris dalam sebuah tabel, <td>	Tag untuk membuat sel dalam sebuah tabel
 
3. Jelaskan perbedaan antara margin dan padding.

   margin dipakai untuk menata letak dari sisi luar, sedangkan padding dipakai untuk menata letak dari sisi dalam

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

   Bootstrap memiliki desain yang sudah jadi (opinionated) dengan gaya dan komponen bawaan yang sudah dirancang. Ini membuatnya cepat untuk digunakan tanpa banyak kustomisasi. Tailwind adalah kerangka kerja yang lebih "low-level" yang memberikan sejumlah kelas utility yang dapat Anda gabungkan untuk merancang tampilan sesuai keinginan Anda. Ini memberikan lebih banyak kendali desain tetapi memerlukan lebih banyak kerja dalam merancang tampilan dari awal.
 
 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    Saya mengimplementasi checklist dengan memakai bootstrap. Seperti menambahkan navbar di setiap html dan mengubah warna bg. Namun, saya rasanya belum selesai dan akan saya tambah setelah atau saat tugas 6.


**Tugas 6**
1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

   Dalam pemrograman sinkronus, tugas dijalankan secara berurutan, satu demi satu, dan tidak dapat diinterupsi hingga tugas tersebut selesai. Setiap tugas harus menunggu tugas sebelumnya selesai dijalankan sebelum dapat dimulai. Dalam pemrograman asinkronus, tugas dapat dijalankan dalam urutan apa pun atau bahkan secara bersamaan. Pendekatan ini bekerja paling baik ketika tugasnya panjang, rumit, atau memerlukan banyak sumber daya. Setiap tugas tidak bergantung pada tugas sebelumnya yang harus diselesaikan sebelum dapat dimulai.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

   Event-driven programming adalah paradigma dimana semua bagian dari program, objek, dan lainnya berkomunikasi satu sama lain, sehingga saat kita menekan tombol tambahkan item, maka akan muncul form untuk menulis item baru. Lalu saat kita submit formnya, maka langsung diupdate item barunya pada tampilan.

3. Jelaskan penerapan asynchronous programming pada AJAX.

   Programming asinkronus pada AJAX memungkinkan JavaScript untuk mengirim suatu request tanpa harus menunggu sebuah response.

4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

   Fetch api adalah native dari javascript yang menyediakan global fetch() method yang dapat dengan mudah dan logis untuk fetch resources secara asinkronus di seluruh jaringan. JQuery hanya library yang memiliki beberapa perbedaan syntax.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

   Pertama-tama, saya membuat fungsi untuk GET dan POST pada views.py. Lalu saya menambahkan path fungsi tersebut ke urls.py. Kemudian, saya modifikasi file main.html agar tabel dapat dimodifikasi dengan AJAX. Pada main.html saya menambahkan script yang berisi getproducts dan refreshproducts untuk mengupdate tabel data secara real time dan menambahkan item ke produk menggunakan modal dari bootstrap. Terakhir saya melakukan collectstatic.
