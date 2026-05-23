from .config import SpeechConfig
from .voice import Voice
import os 
import wave

def download_voice(url, local_path):
    import requests
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    if not os.path.exists(local_path):
        print(f"Downloading {url} ...")
        r = requests.get(url)
        r.raise_for_status()
        with open(local_path, "wb") as f:
            f.write(r.content)
    return local_path

def _preload_onnx_dlls():
    """โหลด CUDA/cuDNN DLLs โดยไม่ต้องแก้ PATH
    รองรับทั้ง nvidia pip packages และ CUDA Toolkit ที่ติดตั้งในเครื่อง
    """
    # วิธีที่ 1: โหลดจาก nvidia pip packages (nvidia-*-cu12/cu13)
    try:
        import onnxruntime as ort
        ort.preload_dlls()
        return
    except Exception:
        pass

    # วิธีที่ 2: ค้นหา CUDA Toolkit ที่ติดตั้งในเครื่อง (เรียงจากใหม่ไปเก่า)
    try:
        import glob, ctypes
        cuda_bins = sorted(
            glob.glob("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/*/bin"),
            reverse=True  # เอาเวอร์ชันใหม่สุดก่อน
        )
        if cuda_bins:
            for dll in glob.glob(f"{cuda_bins[0]}/*.dll"):
                try:
                    ctypes.WinDLL(dll)
                except Exception:
                    pass
    except Exception:
        pass  # ไม่มี GPU หรือไม่มี CUDA ก็ข้ามไป ใช้ CPU แทน

_preload_onnx_dlls()

def _get_gpu_name():
    """ดึงชื่อ GPU จาก onnxruntime หรือ torch"""
    try:
        import onnxruntime as ort
        providers = ort.get_available_providers()
        if "CUDAExecutionProvider" in providers:
            try:
                import torch
                return torch.cuda.get_device_name(0)
            except Exception:
                return "CUDA GPU (unknown name)"
        return None
    except Exception:
        return None

# แสดงชื่อ GPU ตอน import ครั้งแรก
_gpu_name = _get_gpu_name()
if _gpu_name:
    print(f"🚀 VachanaTTS — GPU: {_gpu_name}")
else:
    print("🖥️ VachanaTTS — Provider: CPU")

def load_voice(voice_name="th_f_1"):
    
    model_filename = f"{voice_name}.onnx"
    config_filename = f"speaker_config.json"

    local_model_path = f"./voices/{model_filename}"
    local_config_path = f"./voices/{config_filename}"

    use_cuda = _gpu_name is not None

    if os.path.exists(local_model_path) and os.path.exists(local_config_path):
        return Voice.load(local_model_path, local_config_path, use_cuda=use_cuda)
    else:
        model_url = f"https://huggingface.co/VIZINTZOR/VachanaTTS/resolve/main/voices/{model_filename}"
        config_url = f"https://huggingface.co/VIZINTZOR/VachanaTTS/resolve/main/speaker_config.json"

        model_path = download_voice(model_url, local_model_path)
        config_path = download_voice(config_url, local_config_path)

        return Voice.load(model_path, config_path, use_cuda=use_cuda)

loaded_voices = {}

def TTS(
    text,
    voice="th_f_1",
    output="output.wav",
    volume=1.0,
    speed=1.0,
    noise_scale=0.667,
    noise_w_scale=0.8
):

    syn_config = SpeechConfig(
        volume=volume,
        length_scale=(1 / speed), 
        noise_scale=noise_scale,
        noise_w_scale=noise_w_scale, 
    )

    if voice not in loaded_voices:
        loaded_voices[voice] = load_voice(voice)
    voice = loaded_voices[voice]
    
    with wave.open(output, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file, syn_config)
