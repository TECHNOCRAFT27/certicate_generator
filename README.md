
# 🎓 Certificate Generator

This project is a simple **Certificate Generator** built using **Python**, **PIL (Pillow)**, and **OpenCV**.
It allows you to automatically place participant names on a certificate template by selecting the text position interactively.

---

## 🚀 Features

* Select the exact text placement on your certificate using **right-click**.
* Generate certificates for multiple participants from a text file.
* Save certificates automatically into an output folder.
* Customizable font and text size.

---

## 📂 Project Structure

```
.
├── certificate.png   # Certificate template (blank certificate image)
├── name.txt          # List of participant names (one per line)
├── script.py         # Main Python script
├── output/           # Generated certificates (saved here)
└── README.md         # Project documentation
```

---

## 🛠️ Requirements

Make sure you have Python installed (>=3.7). Then install the dependencies:

```bash
pip install pillow opencv-python
```

---

## ▶️ Usage

1. Place your certificate template in the root folder and name it `certificate.png`.
2. Create a `name.txt` file containing participant names (one per line).
   Example:

   ```
   Alice Johnson
   Bob Smith
   Charlie Brown
   ```
3. Run the script:

   ```bash
   python script.py
   ```
4. When the certificate opens in a new window:

   * **Right-click** on the position where the name should appear.
   * Press `ENTER` to generate certificates.
5. Certificates will be saved inside the `output/` folder.

---

## 🖼️ Example Output

**Before (Blank Template):**

*(certificate.png placeholder)*

**After (Generated Certificate):**

*(output/Alice Johnson.png placeholder)*

---

## ⚙️ Customization

* Change **font** and **size** by editing:

  ```python
  font = ImageFont.truetype("arial.ttf", 40)
  ```
* Modify **text color** by changing:

  ```python
  fill='black'
  ```

---

## 📌 Notes

* Ensure `arial.ttf` (or any .ttf font file) is available in your system.
* Works with `.png` or `.jpg` certificate templates.
* Names are directly taken from `name.txt`.

---

## 🤝 Contribution

Pull requests are welcome! If you’d like to add new features (like dynamic font scaling, CSV input, or PDF export), feel free to fork and improve this project.

---

## 📜 License

This project is licensed under the MIT License – you are free to use, modify, and distribute.

