# Program sederhana untuk mengirim notifikasi
# Versi sebelum menerapkan prinsip SOLID

# ==========================================================
# JAWABAN LANGKAH 1 - IDENTIFIKASI
# ==========================================================

# a) Prinsip SOLID yang dilanggar pada kode awal:
#
# 1. Single Responsibility Principle (SRP)
#    Kelas Notification memiliki banyak tanggung jawab:
#    - Mengirim Email
#    - Mengirim SMS
#    - Mengirim WhatsApp
#
# 2. Open/Closed Principle (OCP)
#    Jika ingin menambahkan jenis notifikasi baru (misalnya Telegram),
#    kita harus mengubah method send() dan menambah if/elif baru.
#
# 3. Dependency Inversion Principle (DIP)
#    Logika pengiriman bergantung langsung pada string
#    seperti "email", "sms", dan "whatsapp",
#    bukan pada abstraksi.
#
# 4. Liskov Substitution Principle (LSP)
#    Tidak ada inheritance, sehingga tidak ada objek turunan
#    yang dapat menggantikan objek induk.
#
# 5. Interface Segregation Principle (ISP)
#    Tidak diterapkan karena belum ada interface yang jelas.


class Notification:
    def send(self, notification_type, message):
        if notification_type == "email":
            print(f"Mengirim Email: {message}")
        elif notification_type == "sms":
            print(f"Mengirim SMS: {message}")
        elif notification_type == "whatsapp":
            print(f"Mengirim WhatsApp: {message}")
        else:
            print("Jenis notifikasi tidak dikenali")


# Penggunaan program
notif = Notification()

notif.send("email", "Halo, ini pesan melalui email.")
notif.send("sms", "Halo, ini pesan melalui SMS.")
notif.send("whatsapp", "Halo, ini pesan melalui WhatsApp.")