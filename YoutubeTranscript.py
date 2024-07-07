import os
from youtube_transcript_api import YouTubeTranscriptApi

def format_time(seconds):
    # 秒を時:分:秒形式に変換
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def main():
    # YouTubeの動画IDを入力
    video_id = input('YouTubeの動画IDを入力してください: ')
    # 言語コードを入力
    language_code = input('取得したい字幕の言語コードを入力してください (例: en, ja。英語の場合 en,日本語の場合 ja を指定): ')

    try:
        # 文字起こしを取得
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return

    # 出力フォルダのパスを作成
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 30分（1800秒）ごとに分割してファイルに書き込み
    chunk_size = 1800
    current_chunk = []
    chunk_start_time = 0
    chunk_index = 1

    for entry in transcript:
        start_time = entry['start']
        
        if start_time >= chunk_start_time + chunk_size:
            # 現在のチャンクをファイルに書き込み
            output_file_path = os.path.join(output_folder, f'{video_id}_transcript_{language_code}_part{chunk_index}.txt')
            with open(output_file_path, 'w', encoding='utf-8') as f:
                for chunk_entry in current_chunk:
                    formatted_time = format_time(chunk_entry['start'])
                    f.write(f"{formatted_time}\t{chunk_entry['text']}\n")
            print(f"文字起こしが {output_file_path} に保存されました。")
            
            # 次のチャンクの準備
            chunk_index += 1
            chunk_start_time += chunk_size
            current_chunk = []

        current_chunk.append(entry)

    # 最後のチャンクをファイルに書き込み
    if current_chunk:
        output_file_path = os.path.join(output_folder, f'{video_id}_transcript_{language_code}_part{chunk_index}.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            for chunk_entry in current_chunk:
                formatted_time = format_time(chunk_entry['start'])
                f.write(f"{formatted_time}\t{chunk_entry['text']}\n")
        print(f"文字起こしが {output_file_path} に保存されました。")

if __name__ == "__main__":
    main()
