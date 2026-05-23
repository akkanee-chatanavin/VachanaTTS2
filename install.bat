@echo off
echo Installing VachanaTTS2...

echo [1/5] Installing base packages...
pip install pythainlp ssg requests flatbuffers numpy packaging protobuf sympy coloredlogs

echo [2/5] Installing PyTorch + torchaudio CUDA 13...
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu130

echo [3/5] Installing cuDNN for CUDA 13...
pip install nvidia-cudnn-cu13

echo [4/5] Installing onnxruntime-gpu CUDA 13...
pip uninstall onnxruntime onnxruntime-gpu -y
pip install --pre --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ort-cuda-13-nightly/pypi/simple/ onnxruntime-gpu --no-deps

echo [5/5] Installing VachanaTTS2...
pip install -e .

echo.
echo Checking PATH...
python -c "import onnxruntime as ort; ort.preload_dlls(); print('ORT providers:', ort.get_available_providers())"

echo.
echo Done!
pause