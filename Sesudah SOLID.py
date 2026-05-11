from abc import ABC, abstractmethod

# ==========================================
# 1. Interface (Abstraction)
# ==========================================
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


# ==========================================
# 2. Implementasi Email
# ==========================================
class EmailNotification(Notification):
    def send(self, message):
        print(f"Mengirim Email: {message}")


# ==========================================
# 3. Implementasi SMS
# ==========================================
class SMSNotification(Notification):
    def send(self, message):
        print(f"Mengirim SMS: {message}")


# ==========================================
# 4. Implementasi WhatsApp
# ==========================================
class WhatsAppNotification(Notification):
    def send(self, message):
        print(f"Mengirim WhatsApp: {message}")


# ==========================================
# 5. Fungsi untuk mengirim notifikasi
# ==========================================
def send_notification(notification, message):
    notification.send(message)


# ==========================================
# 6. Penggunaan Program
# ==========================================
email = EmailNotification()
sms = SMSNotification()
whatsapp = WhatsAppNotification()

send_notification(email, "Halo, ini pesan melalui email.")
send_notification(sms, "Halo, ini pesan melalui SMS.")
send_notification(whatsapp, "Halo, ini pesan melalui WhatsApp.")