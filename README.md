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
   
   jadi perbedaannya adalah dalam interface dengan view dan modelnya MVC menggunakan controller, MVT menggunakan url, MVVM menggunakan viewmodel.
