# Program sederhana untuk mengirim notifikasi
# Versi sebelum menerapkan prinsip SOLID

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