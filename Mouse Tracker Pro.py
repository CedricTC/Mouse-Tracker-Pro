import tkinter as tk
import pyautogui
from PIL import ImageGrab
from threading import Thread
import time

class MouseTrackerPro:
    def __init__(self):
       
        self.root = tk.Tk()
        self.root.title("Mouse Tracker Pro")
        self.root.geometry("500x400")
        self.root.configure(bg='#2E2E2E')
        self.root.resizable(False, False)

       
        self.tracking = False

       
        self.title_label = tk.Label(
            self.root,
            text="MOUSE TRACKER PRO",
            font=('Helvetica', 18, 'bold'),
            bg='#2E2E2E',
            fg='#00FF00'
        )
        self.title_label.pack(pady=20)

        
        self.info_frame = tk.Frame(self.root, bg='#2E2E2E')
        self.info_frame.pack(pady=10)

      
        self.coords_frame = tk.LabelFrame(
            self.info_frame,
            text="Koordinatlar",
            font=('Helvetica', 12),
            bg='#2E2E2E',
            fg='#00FF00',
            padx=10,
            pady=5
        )
        self.coords_frame.pack(pady=10)

      
        self.x_label = tk.Label(
            self.coords_frame,
            text="X:",
            font=('Helvetica', 14),
            bg='#2E2E2E',
            fg='white'
        )
        self.x_label.grid(row=0, column=0, padx=5)

        self.x_value = tk.Label(
            self.coords_frame,
            text="0",
            font=('Helvetica', 14),
            bg='#2E2E2E',
            fg='#00FF00',
            width=6
        )
        self.x_value.grid(row=0, column=1, padx=5)

        
        self.y_label = tk.Label(
            self.coords_frame,
            text="Y:",
            font=('Helvetica', 14),
            bg='#2E2E2E',
            fg='white'
        )
        self.y_label.grid(row=0, column=2, padx=5)

        self.y_value = tk.Label(
            self.coords_frame,
            text="0",
            font=('Helvetica', 14),
            bg='#2E2E2E',
            fg='#00FF00',
            width=6
        )
        self.y_value.grid(row=0, column=3, padx=5)

        
        self.color_frame = tk.LabelFrame(
            self.info_frame,
            text="Renk Bilgisi",
            font=('Helvetica', 12),
            bg='#2E2E2E',
            fg='#00FF00',
            padx=10,
            pady=5
        )
        self.color_frame.pack(pady=10)


        self.rgb_label = tk.Label(
            self.color_frame,
            text="RGB: (0, 0, 0)",
            font=('Helvetica', 12),
            bg='#2E2E2E',
            fg='white'
        )
        self.rgb_label.pack(pady=5)

      
        self.color_sample = tk.Canvas(
            self.color_frame,
            width=50,
            height=50,
            bg='black',
            highlightthickness=0
        )
        self.color_sample.pack(pady=5)

       
        self.hex_label = tk.Label(
            self.color_frame,
            text="HEX: #000000",
            font=('Helvetica', 12),
            bg='#2E2E2E',
            fg='white'
        )
        self.hex_label.pack(pady=5)

        
        self.button_style = {
            'font': ('Helvetica', 12),
            'bg': '#00FF00',
            'fg': 'black',
            'width': 15,
            'height': 1,
            'cursor': 'hand2',
            'relief': 'flat'
        }

        self.toggle_button = tk.Button(
            self.root,
            text="BAŞLAT",
            command=self.toggle_tracking,
            **self.button_style
        )
        self.toggle_button.pack(pady=5)

        
        self.status_label = tk.Label(
            self.root,
            text="Durum: Beklemede",
            font=('Helvetica', 10),
            bg='#2E2E2E',
            fg='white'
        )
        self.status_label.pack(pady=5)

        
        self.toggle_button.bind("<Enter>", self.on_enter)
        self.toggle_button.bind("<Leave>", self.on_leave)

    def rgb_to_hex(self, rgb):
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

    def on_enter(self, e):
        self.toggle_button.configure(bg='#00CC00')

    def on_leave(self, e):
        self.toggle_button.configure(bg='#00FF00')

    def toggle_tracking(self):
        self.tracking = not self.tracking
        if self.tracking:
            self.toggle_button.configure(text="DURDUR", bg='#FF3333')
            self.status_label.configure(text="Durum: Aktif", fg='#00FF00')
            self.tracking_thread = Thread(target=self.track_mouse)
            self.tracking_thread.daemon = True
            self.tracking_thread.start()
        else:
            self.toggle_button.configure(text="BAŞLAT", bg='#00FF00')
            self.status_label.configure(text="Durum: Beklemede", fg='white')

    def track_mouse(self):
        while self.tracking:
            try:
                
                x, y = pyautogui.position()
                self.x_value.configure(text=str(x))
                self.y_value.configure(text=str(y))

                
                screen = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
                color = screen.getpixel((0, 0))

                
                self.rgb_label.configure(text=f"RGB: {color}")
                hex_color = self.rgb_to_hex(color)
                self.hex_label.configure(text=f"HEX: {hex_color}")
                self.color_sample.configure(bg=hex_color)

                time.sleep(0.1)
            except:
                self.tracking = False
                break

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MouseTrackerPro()
    app.run()