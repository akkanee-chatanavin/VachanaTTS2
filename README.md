# VachanaTTS2 🔊

> VachanaTTS โมเดล Text-to-Speech (TTS) สำหรับภาษาไทย สร้างเสียงพูดจากข้อความอย่างรวดเร็ว  
> Fork จาก [VYNCX/VachanaTTS2](https://github.com/VYNCX/VachanaTTS2)

---

## ✨ Features
- 🇹🇭 รองรับภาษาไทยเต็มรูปแบบ
- ⚡ เร็วด้วย ONNX Runtime + CUDA 13
- 🖥️ รองรับทั้ง GPU และ CPU
- 📦 ติดตั้งง่าย ใช้ได้เลยใน Python

---

## 🖥️ System Requirements
- Python 3.8+
- NVIDIA GPU ที่รองรับ CUDA 13 (สำหรับ GPU mode)

---

## 🚀 Installation

### GPU (CUDA 13) — แนะนำ
```bash
git clone https://github.com/akkanee-chatanavin/VachanaTTS2.git
cd VachanaTTS2
install.bat
```

### CPU only
```bash
pip install git+https://github.com/akkanee-chatanavin/VachanaTTS2.git
```

---

## 📖 Usage

```python
from vachanatts import TTS

TTS(
    text="สวัสดีครับ ยินดีต้อนรับ",
    voice="th_f_1",
    output="output.wav"
)
```

### ⚙️ Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `text` | - | ข้อความที่ต้องการแปลงเป็นเสียง |
| `voice` | `th_f_1` | เสียงที่ใช้ |
| `output` | `output.wav` | ชื่อไฟล์เสียงที่ได้ |
| `volume` | `1.0` | ระดับเสียง |
| `speed` | `1.0` | ความเร็วในการพูด |
| `noise_scale` | `0.667` | ความหลากหลายของเสียง |
| `noise_w_scale` | `0.8` | ความหลากหลายของจังหวะ |

---

## 📦 Dependencies & เหตุผลที่เลือกใช้

| Package | เหตุผล |
|---------|--------|
| `pythainlp` | ใช้ประมวลผลข้อความภาษาไทย เช่น tokenization และ g2p |
| `ssg` | ใช้แปลงข้อความภาษาไทยเป็น phoneme สำหรับ TTS |
| `requests` | ใช้ดาวน์โหลดโมเดลเสียงจาก HuggingFace อัตโนมัติ |
| `torch + torchaudio (cu130)` | ใช้ตรวจสอบ GPU และรองรับ CUDA 13 ซึ่งเป็น stable default แล้ว |
| `nvidia-cudnn-cu13` | cuDNN ที่จำเป็นสำหรับ onnxruntime-gpu CUDA 13 |
| `onnxruntime-gpu (CUDA 13 nightly)` | ใช้รัน ONNX model บน GPU ได้เร็วกว่า CPU มาก ยังเป็น nightly เพราะ CUDA 13 stable ยังไม่ออก |

> **หมายเหตุ:** `onnxruntime-gpu` ไม่ได้อยู่ใน `requirements.txt` เพราะต้องติดตั้งจาก custom index URL พิเศษ ให้ใช้ `install.bat` แทนครับ

---

## 🙏 Credits
- ต้นฉบับ: [VYNCX/VachanaTTS2](https://github.com/VYNCX/VachanaTTS2) by [VYNCX](https://github.com/VYNCX)