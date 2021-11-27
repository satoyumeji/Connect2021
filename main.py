import vlc
p = vlc.venv("sound.mp3")


def Human_obj(human):
    if human == '人間':
        return "人間"

    else:
        return "カラス"
    p.play()


str_human = "人"
print(Human_obj(str_human))
