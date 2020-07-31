PREFIX='.'

# list for привествий
greetings=['hello', 'hi', 'привіт','привет']
goodbye=['bb','bye','пока','до скорого']
help_for_server=['help','помощ','допомога','команди сервера']
exc=['.джоін','.леаве','.плей', '.юзер','.хелп','.клеар']


ydl_options={
    'format' : 'bestaudio/best',
    'postprocessors' : [{
        'key' : 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality' : '192'
    }],
}

status=['Модернизирует свой код']
