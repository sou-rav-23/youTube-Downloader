from flask import Flask, render_template, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_link = request.form['video_link']

    try:
        youtube = YouTube(video_link)
        video_stream = youtube.streams.filter(file_extension="mp4").first()
        video_stream.download('./downloads')  # You can customize the download directory
        return jsonify({'success': True, 'message': 'Video downloaded successfully.'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
