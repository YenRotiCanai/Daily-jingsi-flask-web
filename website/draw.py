from flask import Blueprint, render_template, request
from flask_login import current_user
import random

draw = Blueprint('draw', __name__)

jingsi_dict = {}

with open('./website/t5.txt', encoding='utf-8') as f:
    for line in f:
        g = line.split('、', 1)
        jingsi_dict[int(g[0])] = g[1]

# print(jingsi_dict.get(2))
jingsi_text = ""

@draw.route('/draw', methods=['GET','POST'])
def rand():
    #if request.method == 'POST':
    r = random.randint(0, len(jingsi_dict))
    print(r)
    jingsi_text = jingsi_dict.get(r)

    chars = "；？。！-"
    for ch in chars:
        if ch in jingsi_text:
            jingsi_text = jingsi_text.replace(ch, ch+"<br>")

    print(jingsi_text)
    return render_template("jingsi.html", user = current_user, jingsi_text=jingsi_text)