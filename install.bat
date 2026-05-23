@echo off
echo Installing VachanaTTS2...
pip install pythainlp ssg requests
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu130
pip install --pre --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ort-cuda-13-nightly/pypi/simple/ onnxruntime-gpu --no-deps
pip install -e .
echo Done!
pause