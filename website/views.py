from io import BytesIO
from multiprocessing.spawn import old_main_modules
import os

from flask import Blueprint,render_template,request,session,flash,redirect,url_for,send_file
from pytube import YouTube


views = Blueprint("views", __name__)


@views.route("/", methods= ["GET","POST"])
def home():
    if request.method == "POST":
        global url
        url = request.form.get("text")
        try:
            yt = YouTube(url)
            yt.check_availability()
            
        except: 
            return render_template("home.html")
        return render_template("download.html", yt=yt)
    return render_template("home.html")




@views.route("/download/video",methods = ["GET","POST"])
def download_video():
    if request.method == "POST":
        buffer = BytesIO()
        yt = YouTube(url)
        itag = request.form.get("atag")
        streams = yt.streams.get_by_itag(itag=itag)
        streams.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True,download_name=yt.title+'.mp4',mimetype='video/mp4')
    return redirect("home.html")


@views.route("/download/audio",methods = ["GET","POST"])
def download_audio():
    if request.method == "POST":
        buffer = BytesIO()
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True,download_name=yt.title+'(audio).mp4',mimetype='audio/mp3')
    




