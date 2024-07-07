# YoutubeTimestampMaker

## 初期設定
・Pythonのインストール
　WindowsのMicrosoft Storeを起動 ・画面上部の検索バーからPythonを検索 ・検索結果からPython 3.8をインストール 　※ほかのバージョンのPythonでも動作するかもしれませんが、3.8以外では動作確認していません。
　ffmpegをインストールする。 ffmpegをダウンロードし、Windowsの場合はpathにffmpegへのパス設定を行ってください

・install.batを実行する
　"complite install!!"」と表示されればOK

## 使い方
・YoutubeTranscript.bat　を実行する。
　コマンドプロンプトが起動するので、動画の文字起こしを取得するYoutubeの動画IDを入力する。
 　動画IDは、Youtubeの動画ページのURLの「watch?v=」以降の文字部分です。

・取得する文字起こしの言語を指定する。
　日本語の文字お越しを取得する場合は ja　を入力しEnterキーを押下

・outputディレクトリに動画の長さに応じて、動画内の３０分ごとに１ファイルの形で動画の文字起こししたファイルを出力されます。
　※Youtube上で文字起こしがついていない動画は文字起こしが取得できずエラーとなります。

・outputディレクトリに出力された文字起こしを次のGPTsへ１ファイルずつアップロードし、GPTsへ送信してください。
　文字起こしした動画の内容を元に、動画内容の要約をしながらタイムスタンプを生成してくれます。
 生成されたタイムスタンプを確認し、不要なタイムスタンプや、タイムスタンプの見出し文章を好みに合わせて手動で修正します。

・手動で修正したタイムスタンプをYoutubeのコメント欄や概要欄に張り付ければタイムスタンプを少し手軽に作ることができます
 