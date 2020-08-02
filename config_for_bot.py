PREFIX='.'

ydl_options={
    'format' : 'bestaudio/best',
    'postprocessors' : [{
        'key' : 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality' : '192'
    }],
}

status=['Модернизирует свой код','.help']
