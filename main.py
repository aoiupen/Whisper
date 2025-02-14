import os
import torch
import whisper

# FFmpeg 경로 설정 (필요한 경우)
ffmpeg_path = "C:\\Program Files\\ffmpeg\\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path

def transcribe_audio_to_file(audio_file_path, output_file_path):
    try:
        # Whisper 모델 로드
        print("Loading Whisper model...")
        model = whisper.load_model("base", device="cuda")
        print("Model loaded successfully.")
        # GPU 장치 이름 확인
        print(f"Using device: {torch.cuda.get_device_name(torch.cuda.current_device())}")

        # 음성 파일에서 텍스트 추출
        print(f"Transcribing audio file: {audio_file_path}")
        result = model.transcribe(audio_file_path)
        
        # segments는 유지하되 텍스트만 저장
        with open(output_file_path, "w", encoding="utf-8") as f:
            for segment in result['segments']:
                text = segment['text']
                f.write(f"{text}\n")

        print(f"Transcription completed and saved to {output_file_path}")

    except FileNotFoundError:
        print(f"Error: The file {audio_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# 폴더 경로 설정
folder_path = os.path.join(os.path.dirname(__file__), "src") # 변환할 비디오 파일들이 있는 폴더 경로

# 지원하는 파일 확장자
supported_extensions = ['.mp4', '.mp3', '.wav', '.m4a']

# 폴더 내 모든 파일 처리
for filename in os.listdir(folder_path):
    # 파일의 확장자 확인
    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension in supported_extensions:
        # 입력 파일의 전체 경로
        input_path = os.path.join(folder_path, filename)
        
        # 출력 파일명 생성 (확장자만 .txt로 변경)
        output_filename = os.path.splitext(filename)[0] + '.txt'
        output_path = os.path.join(folder_path, output_filename)
        
        # 이미 txt 파일이 존재하는지 확인
        if os.path.exists(output_path):
            print(f"Skipping {filename}: Text file already exists")
            continue
        
        print(f"\nProcessing: {filename}")
        
        # 파일이 존재하는지 확인
        if os.path.exists(input_path):
            transcribe_audio_to_file(input_path, output_path)
        else:
            print(f"Error: The file {input_path} does not exist.")