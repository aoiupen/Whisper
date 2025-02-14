import os
import torch
import whisper

class WhisperTranscriber:
    def __init__(self, model_name="base", device="cuda"):
        self.model_name = model_name
        self.device = device
        self.model = None  # 초기에는 모델을 로드하지 않음
    
    def load_model(self):
        if self.model is None:
            print("Loading Whisper model...")
            self.model = whisper.load_model(self.model_name, device=self.device)
            print("Model loaded successfully.")
            print(f"Using device: {torch.cuda.get_device_name(torch.cuda.current_device())}")

    def transcribe_audio_to_file(self, audio_file_path, output_file_path):
        try:
            self.load_model()  # 최초 호출 시에만 모델 로드
            
            print(f"Transcribing audio file: {audio_file_path}")
            result = self.model.transcribe(audio_file_path)
            
            with open(output_file_path, "w", encoding="utf-8") as f:
                for segment in result['segments']:
                    f.write(f"{segment['text']}\n")
            
            print(f"Transcription completed and saved to {output_file_path}")
        
        except FileNotFoundError:
            print(f"Error: The file {audio_file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

# 폴더 경로 설정
folder_path = os.path.join(os.path.dirname(__file__), "src")  # 변환할 파일들이 있는 폴더
supported_extensions = ['.mp4', '.mp3', '.wav', '.m4a']

# WhisperTranscriber 인스턴스 생성
transcriber = WhisperTranscriber()

# 폴더 내 모든 파일 처리
for filename in os.listdir(folder_path):
    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension in supported_extensions:
        input_path = os.path.join(folder_path, filename)
        output_filename = os.path.splitext(filename)[0] + '.txt'
        output_path = os.path.join(folder_path, output_filename)
        
        if os.path.exists(output_path):
            print(f"Skipping {filename}: Text file already exists")
            continue
        
        print(f"\nProcessing: {filename}")
        transcriber.transcribe_audio_to_file(input_path, output_path)
