Nama: Dian Fathur Rahman

NPM: 2206082096

Link: https://fathur-tugas2-mc-shipyards.adaptable.app

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
