# University Data Extractor (Streamlit + Docker)

## Cara Menjalankan

### 1. Siapkan Docker
- Install Docker Desktop dari https://www.docker.com/products/docker-desktop/

### 2. Setting API Key Perplexity
- Edit file `app.py` pada baris:
  ```python
  PERPLEXITY_API_KEY = "ISI_API_KEY_ANDA"
  ```
  atau gunakan `.env` (lihat instruksi di atas).

### 3. Build Docker Image
```bash
docker build -t university-data-extractor .
```

### 4. Jalankan Container
```bash
docker run -p 8501:8501 university-data-extractor
```
atau jika pakai `.env`:
```bash
docker run --env-file .env -p 8501:8501 university-data-extractor
```

### 5. Akses dari Browser
Buka [http://localhost:8501](http://localhost:8501)  
dan gunakan aplikasinya.

---

### Credit
Dikembangkan oleh [Malika]
