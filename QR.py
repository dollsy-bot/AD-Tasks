import cv2
import qrcode
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import numpy as np

# ------------------ QR Code Generator ------------------
def generate_qr():
    data = simpledialog.askstring("QR Code Generator", "Enter text or URL to generate QR Code:")
    if data:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        filename = simpledialog.askstring("Save As", "Enter filename to save (without extension):")
        if filename:
            img.save(f"{filename}.png")
            messagebox.showinfo("Success", f"QR Code saved as {filename}.png")

# ------------------ QR Code Scanner ------------------
def scan_qr():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    messagebox.showinfo("Info", "Press 'q' to quit scanning.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)
        if bbox is not None:
            # Draw bounding box
            n_lines = len(bbox)
            for i in range(n_lines):
                pt1 = tuple(bbox[i][0].astype(int))
                pt2 = tuple(bbox[(i + 1) % n_lines][0].astype(int))
                cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

            if data:
                cv2.putText(frame, data, (int(bbox[0][0][0]), int(bbox[0][0][1])-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
                print("QR Code detected:", data)

        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# ------------------ GUI ------------------
root = tk.Tk()
root.title("QR Code Scanner & Generator")
root.geometry("300x150")

tk.Button(root, text="Scan QR Code", width=20, height=2, command=scan_qr).pack(pady=10)
tk.Button(root, text="Generate QR Code", width=20, height=2, command=generate_qr).pack(pady=10)

root.mainloop()
