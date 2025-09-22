import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x150")
        self.root.resizable(False, False)

        # Time variables
        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        # Display label
        self.time_label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.time_label.pack(pady=20)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack()

        tk.Button(button_frame, text="Start", width=8, command=self.start).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Pause", width=8, command=self.pause).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Reset", width=8, command=self.reset).grid(row=0, column=2, padx=5)

    def update(self):
        if self.running:
            self.milliseconds += 1
            if self.milliseconds == 100:
                self.milliseconds = 0
                self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1

            # Update label
            self.time_label.config(text=f"{self.minutes:02d}:{self.seconds:02d}:{self.milliseconds:02d}")
            # Call update every 10 ms
            self.root.after(10, self.update)

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.time_label.config(text="00:00:00")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()
