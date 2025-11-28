# Vachana TTS

VachanaTTS โมเดล **Text-to-Speech (TTS)** สำหรับภาษาไทย  
สร้างเสียงพูดจากข้อความอย่างรวดเร็ว รองรับการใช้งานทั้ง **CPU** และ **GPU** ผ่าน `onnxruntime`  

- 🔥 สถาปัตยกรรม: [VITS](https://github.com/jaywalnut310/vits)  
- ⚡ โค้ดหลักและการเทรน: [PiperTTS](https://github.com/OHF-Voice/piper1-gpl)  


## 🚀 เริ่มต้นใช้งาน  

### ติดตั้ง

```
pip install vachanatts
```

 ### การใช้งาน

```
from vachanatts import TTS

text = "สวัสดีครับ/ค่ะ นี่คือเสียงพูดภาษาไทย"

# เสียงพูดที่รองรับ th_f_1, th_m_1, th_f_2, th_m_2

TTS(text,
    voice="th_f_1",
    output="output.wav",
    volume=1.0,
    speed=1.0
)

```
