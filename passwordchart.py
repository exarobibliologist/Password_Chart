import hashlib
import random
import string
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

def generate_seed(phrase: str) -> int:
    md5_hash = hashlib.md5(phrase.encode()).digest()
    return int.from_bytes(md5_hash[:4], 'big')

def generate_chart(seed: int) -> dict:
    random.seed(seed)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    chart = {}
    for label in string.ascii_uppercase + string.digits:
        chart[label] = "".join(random.choices(characters, k=random.randint(2, 4)))
    
    return chart

def save_chart_as_image(chart: dict, filename: str, cell_width: int = 150, cell_height: int = 50):
    labels = list(chart.keys())
    rows = (len(labels) + 3) // 4  # Distribute over 4 columns
    img_width, img_height = 4 * cell_width, rows * cell_height
    
    img = Image.new('RGB', (img_width, img_height), 'white')
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("cour.ttf", cell_height // 2)
    except:
        font = ImageFont.load_default()
    
    for i, label in enumerate(labels):
        x, y = (i % 4) * cell_width, (i // 4) * cell_height
        draw.rectangle([(x, y), (x + cell_width, y + cell_height)], outline='black')
        draw.text((x + 5, y + 5), f"{label}: {chart[label]}", fill='black', font=font)
    
    img.save(filename)
    return img

def generate_and_display_chart():
    phrase = phrase_entry.get()
    if not phrase:
        return
    
    seed = generate_seed(phrase)
    chart = generate_chart(seed)
    img = save_chart_as_image(chart, "temp_chart.png")
    img = ImageTk.PhotoImage(img)
    chart_label.config(image=img)
    chart_label.image = img

def save_chart():
    phrase = phrase_entry.get()
    if not phrase:
        return
    
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if not filename:
        return
    
    seed = generate_seed(phrase)
    chart = generate_chart(seed)
    save_chart_as_image(chart, filename)
    print(f"Chart saved as {filename}")

# GUI Setup
root = tk.Tk()
root.title("Password Chart Generator v1.6.22")

tk.Label(root, text="Enter chart selection phrase:").pack()
phrase_entry = tk.Entry(root)
phrase_entry.pack()

generate_button = tk.Button(root, text="Generate Chart", command=generate_and_display_chart)
generate_button.pack()

save_button = tk.Button(root, text="Save Chart", command=save_chart)
save_button.pack()

chart_label = tk.Label(root)
def display_empty_chart():
    empty_chart = {label: "" for label in string.ascii_uppercase + string.digits}
    img = save_chart_as_image(empty_chart, "temp_chart.png")
    img = ImageTk.PhotoImage(img)
    chart_label.config(image=img)
    chart_label.image = img
display_empty_chart()
chart_label.pack()

decryption_entry = tk.Entry(root, width=50)
decryption_label = tk.Entry(root, state='readonly', width=50)

def encrypt_text(event):
    phrase = phrase_entry.get()
    if not phrase:
        return
    seed = generate_seed(phrase)
    chart = generate_chart(seed)
    
    input_text = decryption_entry.get().upper()
    encrypted_text = ''.join(chart.get(char, char) for char in input_text)
    decryption_label.config(state='normal')
    decryption_label.delete(0, tk.END)
    decryption_label.insert(0, encrypted_text)
    decryption_label.config(state='readonly')

decryption_label_text = tk.Label(root, text="So if you type this, your password would be:")
decryption_label_text.pack()
decryption_entry.pack()
decryption_entry.bind('<KeyRelease>', encrypt_text)
decryption_label.pack()

root.mainloop()
