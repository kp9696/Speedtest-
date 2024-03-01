import tkinter as tk
from tkinter import ttk, Label, Button, messagebox
from threading import Timer
import speedtest
from PIL import Image, ImageTk
import requests
from io import BytesIO


class SpeedTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Speed Test GUI")

        # Configure a ttk style for themed widgets
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Create and configure labels
        self.title_label = Label(master, text="Ciel et Terre Solar Pvt Ltd", font=('Helvetica', 16, 'bold'),
                                 fg='#00ADEF')
        self.title_label.pack(pady=10)

        # Provide a direct image URL
        self.logo_url = "https://ciel-et-terre.net/wp-content/uploads/2023/03/LOGO_CT_WEB.png"
        self.logo = self.load_image(self.logo_url)
        self.logo_label = Label(master, image=self.logo)
        self.logo_label.pack(pady=10)

        self.download_label = Label(master, text="Download Speed:", font=('Helvetica', 14), fg='#00539C')
        self.download_label.pack(pady=10)

        self.upload_label = Label(master, text="Upload Speed:", font=('Helvetica', 14), fg='#00539C')
        self.upload_label.pack(pady=10)

        self.ping_label = Label(master, text="Ping:", font=('Helvetica', 14), fg='#00539C')
        self.ping_label.pack(pady=10)

        # Create and configure the speed test button
        self.test_button = Button(master, text="Run Speed Test", command=self.run_speed_test, font=('Helvetica', 12),
                                  relief=tk.GROOVE, bg='#00ADEF', fg='white')
        self.test_button.pack(pady=20)

        # Periodically update the GUI for a simple animation effect
        self.animate()

        # Schedule speed test every 10 seconds
        self.timer = Timer(10, self.run_speed_test)
        self.timer.start()

    def run_speed_test(self):
        try:
            st = speedtest.Speedtest()
            download_speed = st.download() / 1_000_000  # Convert to Mbps
            upload_speed = st.upload() / 1_000_000  # Convert to Mbps
            ping = st.results.ping

            # Update labels with the speed test results
            self.download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
            self.upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
            self.ping_label.config(text=f"Ping: {ping:.2f} ms")

            # Reschedule speed test every 10 seconds
            self.timer = Timer(10, self.run_speed_test)
            self.timer.start()
        except Exception as e:
            # Display an error message box if an exception occurs
            messagebox.showerror("Error", f"An error occurred: {e}")

    def load_image(self, url):
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img = img.resize((100, 100), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            return img
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def animate(self):
        # Simulate a simple animation effect by changing the color periodically
        current_color = self.title_label.cget("fg")
        new_color = "#FF6347" if current_color == "#00ADEF" else "#00ADEF"
        self.title_label.config(fg=new_color)

        # Schedule the next animation frame after 1000 milliseconds (1 second)
        self.master.after(1000, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestApp(root)
    root.mainloop()
