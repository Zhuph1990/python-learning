#coding=utf-8

from multiprocessing import Queue,Process

def download_from_web(q):
    data = [11, 22, 33]

    for temp in data:
        q.put(temp)

    print("下载器已经下载完了数据并且已经存入到队列中...")


def analysis_data(q):
    """数据处理"""

    waitting_analysis_data = list()
    while True:
        data = q.get()
        waitting_analysis_data.append(data)

        if q.empty():
            break

    print(waitting_analysis_data)        


def main():
    #1.
    q = Queue(3)

    #2.
    p1 = Process(target=download_from_web, args=(q, ))
    p2 = Process(target=analysis_data, args=(q, ))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()