Nama : Asfara Quaneisha Syafaziel
NPM : 2506603532
Kelas : PBP A
Prodi : Sistem Informasi

### Tugas 1
Pertanyaan Reflektif
1. Ya, saya menggunakan elemen semantik yaitu <section>, elemen tersebut membantu saya memisahkan antara bagian-bagian utama pada website, seperti bagian Profile dan Experiences. Menurut saya, penggunaan <section> membantu saya mengorganisasikan struktur website sehingga setiap bagian memiliki tujuan yang jelas dan lebih mudah dibedakan satu sama lain, instead of putting everything in once section dan jadi menumpuk. Selain itu, di dalam setiap section saya juga menggunakan <div> untuk membagi bagian di dalam section, seperti judul besar section, nama experience, deskripsi, dan waktu, dengan foto-foto experience
2. Saya ingin memasukann 4 kotak yang masing-masing berisi sebuah experience saya yang mencakup nama pengalaman, organisasi yang menaunginya, waktu pengalaman dan foto-foto saat saya menjalankan pengalaman tersebut. Awalnya, saya ingin memasukkan tiga foto dan menyusun kotaknya berurutan ke bawah, tetapi, hasilnya jadi terlalu renggang antara satu item dan lainnya, maka saya memutuskan untuk mengubah layoutnya menjadi 2 x 2 kotak, dua pengalaman di atas dan dua pengalaman di bawah. Namun muncul masalah baru, tiga foto yang sudah saya masukkan ternyata tidak muat dan tampilannya jadi keluar dari kotak. Saya kemudian berusaha mengecilkan ukuran foto nya, tetapi tetap saja keluar garis dan jadi terlalu kecil. Maka, saya memutuskan untuk menghapus satu foto dari masing-masing pengalaman.
3. Saat ini website saya masih berupa static web sehingga informasi yang ditampilkan masih ditulis secara langsung di dalam HTML. Salah satu batasan yang saya rasakan adalah ketika saya ingin menambahkan atau memperbarui pengalaman, saya harus mengubah struktur dan isi HTML secara manual. Hal ini akan menjadi kurang praktis jika jumlah pengalaman saya semakin banyak. Pada iterasi selanjutnya, saya ingin membuat bagian Experiences menjadi dinamis dengan menyimpan data pengalaman, seperti nama pengalaman, organisasi, periode, dan foto, di dalam database. Dengan begitu, informasi pada halaman portfolio dapat ditampilkan berdasarkan data yang tersimpan dan saya tidak perlu mengubah HTML secara manual setiap kali ingin menambahkan pengalaman baru. Saya juga ingin mempelajari bagaimana Django dapat digunakan untuk menghubungkan data tersebut dengan halaman website.


AI Disclosure

Dalam pengerjaan proyek ini, saya menggunakan AI sebagai alat bantu belajar, terutama untuk memahami konsep HTML dan CSS serta membantu proses debugging selama pengembangan website.
Tools AI yang saya gunakan adalah ChatGPT. Saya menggunakan AI memberikan konteks mengenai kode yang sedang saya kerjakan, masalah yang saya temui, atau hasil yang ingin saya capai, kemudian meminta penjelasan, alternatif implementasi, atau bantuan dalam menemukan penyebab suatu masalah.
Salah satu contohnya adalah pada pengembangan bagian Experiences. Saya memiliki ide mengenai tampilan yang ingin dibuat, seperti penggunaan empat experience card, informasi yang ditampilkan di dalamnya, penggunaan foto, serta susunan card menjadi layout 2 × 2. Awalnya saya tidak tahu cara membuat kotak-kotak di dalam page nya, saya juga tidak mengerti pembagian assigning color untuk masing-masing element, AI membantu saya menerjemahkan hal-hal tersebut ke dalam struktur HTML dan CSS serta memberikan saran ketika terdapat masalah pada ukuran dan responsive layout. Dari situ juga saya jadi memahami cara mengadjust width, spacing, dan size elements. Maka setelah itu, saya tetap melakukan penyesuaian sendiri terhadap kode, seperti mengubah warna, ukuran, spacing, jumlah foto, bentuk card, dan susunan elemen agar sesuai dengan desain yang saya inginkan.
AI juga saya gunakan untuk memahami kode yang belum saya mengerti. Saya tidak hanya menggunakan output kode secara langsung, tetapi meminta penjelasan mengenai fungsi elemen HTML, property CSS, dan alasan di balik suatu implementasi. Hal ini membantu saya memahami kode sebelum melakukan perubahan sendiri.
Saya menyadari bahwa meskipun AI dapat membantu saya memahami kode dengan lebih cepat, ide-ide seperti layouting dan color palette harus datang dari diri saya sendiri, karena dengan begitu hasilnya bisa lebih cocok dengan apa yang saya inginkan juga.

AI Prompting Examples

Beberapa contoh penggunaan AI selama pengerjaan proyek:
1. Understanding HTML/CSS
Saya memberikan potongan kode yang sedang digunakan dan meminta AI menjelaskan fungsi elemen/property yang belum saya pahami.
2. CSS implementation
Saya menjelaskan desain dan layout yang saya inginkan, kemudian meminta AI membantu menerjemahkan desain tersebut ke dalam CSS.
3. Debugging responsive layout
Saya menjelaskan masalah yang muncul pada layout, seperti card yang terlalu lebar atau gambar yang keluar dari batas card, lalu meminta AI membantu mengidentifikasi kemungkinan penyebab dan alternatif solusinya.
4. Evaluation and manual adjustment
Setelah mencoba solusi yang diberikan AI, saya mengevaluasi hasilnya secara langsung dan mengubah kode kembali ketika hasilnya belum sesuai dengan desain yang saya inginkan.

### Tugas 2
Pertanyaan Reflektif
1. Ketika pengguna membuka halaman Volunteering melalui navigation bar, browser bakal mengirim request ke URL /volunteering/. Request tersebut pertama diterima oleh urls.py pada level project (portofolio/urls.py). Project kemudian meneruskan request ke main.urls karena aplikasi main menangani routing halaman portofolio.
Di dalam main/urls.py, URL /volunteering/ diarahkan ke fungsi show_volunteering yang terdapat pada views.py. View tersebut mengambil seluruh data volunteering dari model Volunteering menggunakan Volunteering.objects.all().
Data yang diperoleh kemudian dimasukkan ke dalam context dengan nama volunteering_list. Context tersebut dikirim bersama template volunteering.html menggunakan fungsi render().
Di dalam template, Django Template Language menggunakan loop {% for %} untuk menampilkan setiap data volunteering. Nilai seperti judul dan deskripsi diambil dari object yang diberikan oleh view. Setelah template diproses menjadi HTML, hasil akhirnya dikirim kembali kepada browser sehingga pengguna dapat melihat daftar volunteering.
To simplify, alurnya adalah:
Browser -> portofolio/urls.py -> main/urls.py -> show_volunteering -> Model Volunteering -> Database -> View -> volunteering.html -> Browser.

2. Data Volunteering sebaiknya disimpan pada model karena data dan tampilan memiliki fungsi yang berbeda. Model digunakan untuk mengatur dan menyimpan data, sedangkan template digunakan untuk mengatur bagaimana data tersebut ditampilkan. Kalau data ditulis langsung di dalam template, setiap pengen menambah atau merubah Volunteering saya harus mengubah html. Hal ini akan menjadi sulit dipelihara jika jumlah data semakin banyak.
Dengan menyimpan data pada model dan database, template cukup menggunakan loop untuk menampilkan data yang tersedia. Artinya, ketika saya menambahkan atau mengubah data volunteering, saya tidak perlu mengubah struktur HTML. Pemisahan ini juga membuat aplikasi lebih mudah dikembangkan di kemudian hari, misalnya kalau ingin menambahkan fitur pencarian, filter, atau pengelolaan data tanpa harus menulis ulang template.

3. makemigrations digunakan untuk membuat file migration berdasarkan perubahan yang dilakukan pada model. File tersebut berisi instruksi mengenai perubahan struktur database yang perlu dilakukan. Sementara itu, migrate digunakan untuk benar-benar menerapkan perubahan yang tercatat dalam file migration ke database.
Contohnya, jika saya menambahkan field baru bernama location pada model Volunteering, saya perlu menjalankan
python manage.py makemigrations
python manage.py migrate

AI Disclosure

Dalam pengerjaan tugas ini, saya menggunakan ChatGPT sebagai alat bantu. AI digunakan untuk membantu saya memahami konsep Model-View-Template (MVT) pada Django, terutama hubungan antara model, view, URL routing, template, database, dan proses request dari browser.
ChatGPT juga terutama membantu saat proses saya menentukan section apa yang harus ditambahkan yang kemudian saya putuskan untuk memisahkan section Volunteering dari Experiences. Selain itu, ChatGPT juga digunakan untuk membantu proses debugging ketika terdapat error pada kode dan memberikan penjelasan mengenai penyebab error serta langkah untuk memperbaikinya.