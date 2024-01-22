from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube;

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        url = request.form['url']
        yt = YouTube(url)
        # video = yt.streams.filter(file_extension='mp4', progressive=True).first()
        video=yt.streams.filter(resolution="720p",file_extension="mp4").first()
    
        video.download('downloads/')  # Save the video in the 'downloads' folder
        # return render_template('index.html', message='      Downloading...🔃     ')
        # display("      Downloading...🔃     ",target="message")
        return render_template('index.html', message='Downloaded successful!')
    except Exception as e:
        return render_template('index.html', message=f'Download failed: {str(e)}')


if __name__ == '__main__':
    app.run(debug=True)
