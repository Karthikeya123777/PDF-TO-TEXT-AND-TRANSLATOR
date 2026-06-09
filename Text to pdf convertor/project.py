import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from deep_translator import GoogleTranslator
import pdfplumber

class PDFTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TransPDF")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f4f4f4")
        
        self.title_label = tk.Label(root, text="PDF Translator", font=("Arial", 24, "bold"), bg="#f4f4f4")
        self.title_label.pack(pady=20)
        
        self.upload_btn = tk.Button(root, text="Upload PDF", font=("Arial", 14), command=self.upload_pdf, bg="#3498db", fg="white", padx=20, pady=10)
        self.upload_btn.pack()
        
    def upload_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if not file_path:
            return
        
        with pdfplumber.open(file_path) as pdf:
            extracted_text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        
        self.open_translation_window(extracted_text)
        
    def open_translation_window(self, text):
        popup = tk.Toplevel(self.root)
        popup.geometry("1000x600")
        popup.title("Extracted Text and Translation")
        popup.configure(bg="#ffffff")
        
        tk.Label(popup, text="Choose Language:", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)
        
        lang_select = ttk.Combobox(popup, values=GoogleTranslator.get_supported_languages(), width=30)
        lang_select.pack()
        lang_select.set("choose language")
        
        frame = tk.Frame(popup, bg="#ffffff")
        frame.pack(pady=10, padx=20)
        
        tk.Label(frame, text="Original Text", font=("Arial", 12, "bold"), bg="#ffffff").grid(row=0, column=0, padx=10)
        tk.Label(frame, text="Translated Text", font=("Arial", 12, "bold"), bg="#ffffff").grid(row=0, column=1, padx=10)
        
        original_text = tk.Text(frame, height=20, width=60, wrap=tk.WORD, bg="#ecf0f1")
        original_text.grid(row=1, column=0, padx=10, pady=5)
        original_text.insert(tk.END, text)
        
        output_text = tk.Text(frame, height=20, width=60, wrap=tk.WORD, bg="#ecf0f1")
        output_text.grid(row=1, column=1, padx=10, pady=5)
        
        def translate():
            if lang_select.get() == "choose language":
                messagebox.showerror("Error", "Please select a language")
                return
            
            translator = GoogleTranslator(source='auto', target=lang_select.get())
            translated_text = translator.translate(text)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, translated_text)
        
        translate_btn = tk.Button(popup, text="Translate", font=("Arial", 14, "bold"), command=translate, bg="#e67e22", fg="white", padx=15, pady=5)
        translate_btn.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFTranslatorApp(root)
    root.mainloop()