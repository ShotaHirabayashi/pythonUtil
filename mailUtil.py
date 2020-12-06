# -*- coding: utf-8 -*-
import requests
import os


def line(body):
    url = "https://notify-api.line.me/api/notify"
    access_token = 'I89UnoDRgRSInUXJOTg5fAniBE08CUuxVqj8ythMLt8'
    headers = {'Authorization': 'Bearer ' + access_token}
    message = body
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload)


def send_image():
    url = "https://notify-api.line.me/api/notify"
    access_token = 'I89UnoDRgRSInUXJOTg5fAniBE08CUuxVqj8ythMLt8'
    # File Name
    FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screen.png")
    headers = {'Authorization': 'Bearer ' + access_token}
    message = 'この画面のエラーで落ちました'
    image = FILENAME
    payload = {'message': message}
    files = {'imageFile': open(image, 'rb')}
    r = requests.post(url, headers=headers, params=payload, files=files,)