from pydub import AudioSegment
from tqdm import tqdm

# MP3 파일 경로
mp3_path = "1.mp3"

# 변환할 WAV 파일 경로
wav_path = "1.wav"

# 전체 MP3 파일을 로드
audio = AudioSegment.from_mp3(mp3_path)

# 전체 길이(밀리초)
total_length = len(audio)

# 몇 초씩 처리할 것인지 설정 (예: 10초씩)
chunk_length_ms = 10000  # 10000 ms = 10 seconds

# 변환된 오디오를 저장할 리스트
audio_chunks = []

# tqdm을 사용하여 진행률 표시
print("MP3 파일을 WAV로 변환 중입니다...")
for start in tqdm(range(0, total_length, chunk_length_ms), desc="Progress", unit="chunk"):
    end = min(start + chunk_length_ms, total_length)
    chunk = audio[start:end]
    audio_chunks.append(chunk)

# 모든 청크를 합침
final_audio = sum(audio_chunks)

# WAV 파일로 내보내기
final_audio.export(wav_path, format="wav")

print(f"MP3 파일이 WAV 파일로 변환되었습니다: {wav_path}")
