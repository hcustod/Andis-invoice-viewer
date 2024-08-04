import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import fitz

class PDF_viewer:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Viewer")

        self.canvas = tk.Canvas(root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.scroll_y = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.canvas.bind("<Configure>, self.rezie_image")

        self.pdf_doc = None
        self.pdf_page = None
        self.page_image = None

        self.load_pdf()

    def load_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.pdf_doc = fitz.open(file_path)
            self.show_page(0)

    def show_page(self, page_number):
        self.pdf_page = self.pdf_doc.load_page(page_number)
        pix = self.pdf_page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        self.page_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.page_image)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
    
    def resize_image(self, event):
        if self.page_image:
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

if __name__ == "__main__":
    root = tk.Tk()
    viewer = PDF_viewer(root)
    root.mainloop()



