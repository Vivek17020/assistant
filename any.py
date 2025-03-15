from plyer import notification
import pyttsx3
import time
import datetime
import threading
from android.permissions import request_permissions, Permission
from android import activity

# Request necessary permissions
request_permissions([Permission.INTERNET, Permission.RECORD_AUDIO])

class ReminderAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.schedule = [
            ("05:30 AM", "Wake up! Time to start your day. Drink water."),
            ("05:40 AM", "Time for your run. Let's go!"),
            ("06:30 AM", "Eat chana and freshen up."),
            ("06:45 AM", "Start CAPF preparation - Current Affairs / GS."),
            ("07:30 AM", "Work on your Virtual Dressing App."),
            ("08:30 AM", "Breakfast & Relax."),
            ("09:00 AM", "College time. Stay focused!"),
            ("12:00 PM", "Drink water! Stay hydrated."),
            ("01:30 PM", "Lunch time!"),
            ("04:00 PM", "You're back from college. Have a snack & rest."),
            ("04:30 PM", "Work on your Virtual Dressing App."),
            ("05:30 PM", "Take a break, eat something, and walk."),
            ("06:00 PM", "CAPF preparation - GS / Polity / History."),
            ("07:00 PM", "Workout or relax for a while."),
            ("08:00 PM", "Dinner time!"),
            ("08:30 PM", "College studies for 1 hour."),
            ("09:30 PM", "Light reading or wind down."),
            ("10:00 PM", "Sleep time. Good night!"),
        ]
        self.running = True
        threading.Thread(target=self.reminder_loop, daemon=True).start()

    def speak(self, text):
        """Speaks the given text."""
        self.engine.say(text)
        self.engine.runAndWait()

    def send_notification(self, title, message):
        """Sends a notification to the Android device."""
        notification.notify(title=title, message=message, timeout=10)

    def reminder_loop(self):
        """Checks time and announces scheduled reminders."""
        while self.running:
            now = datetime.datetime.now().strftime("%I:%M %p")
            for time_str, message in self.schedule:
                if now == time_str:
                    self.send_notification("Reminder", message)
                    self.speak(message)
                    time.sleep(60)  # Prevent duplicate announcements
            time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    assistant = ReminderAssistant()
    while True:
        time.sleep(1)
