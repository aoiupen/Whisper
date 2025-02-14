import os

# 모델 설정
#MODEL_NAME = "base"
MODEL_NAME = "large-v3"
DEVICE = "cuda"

# 모델 옵션 참고 (크기 순)
'''
MODEL_OPTIONS = {
    "tiny": "가장 작은 모델, ~1GB",
    "base": "기본 모델, ~1GB",
    "small": "중소형 모델, ~2GB",
    "medium": "중형 모델, ~5GB",
    "large": "최대 모델, ~10GB",
    "large-v3": "최신 버전 large 모델"
}
'''

# 파일 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
FFMPEG_PATH = "C:\\Program Files\\ffmpeg\\bin"

# 지원하는 파일 확장자
SUPPORTED_EXTENSIONS = ['.mp4', '.mp3', '.wav', '.m4a']

# 출력 설정
OUTPUT_EXTENSION = '.txt'