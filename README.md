# Whisper Audio Transcription

음성 파일(.mp4, .mp3, .wav, .m4a)을 텍스트로 변환하는 도구
[OpenAI의 Whisper 모델](https://github.com/openai/whisper)을 사용

## 기능
- 음성 파일을 텍스트로 자동 변환
- 일괄 처리 지원
- CUDA를 활용한 GPU 가속

## 개발 환경 (작성자 기준으로 아직 배포용 X)
- pyenv를 통한 Python 3.10.11
- NVIDIA GPU
- CUDA 12.4
- FFmpeg

## 설치 방법

### 1. Python 환경 설정
```bash
# pyenv로 Python 3.10.11 설치
pyenv install 3.10.11

# 프로젝트 디렉토리에서 Python 버전 설정
pyenv local 3.10.11

# 가상 환경 생성 및 활성화
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. PyTorch 설치 (CUDA 12.4 버전)
```bash
# 기존 CPU 버전 제거
pip uninstall torch torchaudio torchvision

# CUDA 12.4 지원 버전 설치
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

### 3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. CUDA 설치 확인
```python
import torch
print(f"PyTorch Version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"GPU Device: {torch.cuda.get_device_name(0)}")
```

## 사용 방법
1. `src` 폴더 생성
2. 변환할 음성 파일을 `src` 폴더에 복사
3. 스크립트 실행
```bash
python main.py
```
4. 변환된 텍스트는 `src` 폴더에 원본 파일명.txt로 저장

## 지원 파일 형식
- MP4 (.mp4)
- MP3 (.mp3)
- WAV (.wav)
- M4A (.m4a)

## License
[라이센스 정보]

## 참조
- [OpenAI Whisper](https://github.com/openai/whisper)
- [PyTorch](https://pytorch.org/)
