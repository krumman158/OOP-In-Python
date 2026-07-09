#                   Abstraction

# Reduce complexity by hiding uncessary details

class EmailService:
    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authenticating...")

    def _disconnect(self):
        print("Disconnecting...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email")
        self._disconnect()

e1=EmailService()
e1.send_email()