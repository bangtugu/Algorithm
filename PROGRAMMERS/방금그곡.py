def solution(m, musicinfos):
    for i in range(len(musicinfos)):
        musicinfos[i] = list(musicinfos[i].split(','))

    iscan = [1] * len(musicinfos)

    for i in range(len(musicinfos)):

        time = 60 * (int(musicinfos[i][1][0:2]) - int(musicinfos[i][0][0:2])) + int(musicinfos[i][1][3:5]) - int(
            musicinfos[i][0][3:5])

        if time < len(m):
            iscan[i] = 0
            continue

    if sum(iscan) > 1:
        for i in range(len(musicinfos)):
            if iscan[i]:
                pass

    for i in range(len(musicinfos)):
        if iscan[i]:
            return musicinfos[i][2]