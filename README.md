# 🚲 Bike Sharing Dashboard

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda menggunakan Bike Sharing Dataset dan menampilkan hasil analisis dalam bentuk dashboard interaktif menggunakan Streamlit.

---

## ⚙️ Setup Environment - Anaconda

conda create --name main-ds python=3.9  
conda activate main-ds  
pip install -r requirements.txt  

---

## ⚙️ Setup Environment - Shell / Terminal

mkdir proyek_analisis_data  
cd proyek_analisis_data  
pipenv install  
pipenv shell  
pip install -r requirements.txt  

---

## ▶️ Menjalankan Dashboard

Masuk ke folder dashboard:

cd dashboard  

Jalankan perintah berikut:

streamlit run dashboard.py  

---

## ✨ Fitur Dashboard
- Rata-rata penyewaan sepeda per bulan  
- Rata-rata penyewaan sepeda berdasarkan kondisi cuaca  
- Filter interaktif berdasarkan kondisi cuaca  

---

## 📂 Struktur Folder

submission/
├── dashboard/
│   ├── dashboard.py  
│   └── main_data.csv  
├── data/
│   └── day.csv  
├── notebook.ipynb  
├── README.md  
├── requirements.txt  
└── url.txt  
