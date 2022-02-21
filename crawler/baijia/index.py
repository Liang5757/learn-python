import re
from lxml import etree
import requests
import os

img_dir = '/img'
file_prefix = 'work'


# 将无法作为标题的符号替换为_
def validate_title(title):
    rstr = '[/\:*?<>|@]'
    new_title = re.sub(rstr, '_', title)
    return new_title


def get_max_page():
    base_url = "https://guangzhou.baixing.com/search/?query=%E5%B7%A5%E4%BD%9C"
    html_xml = get_html(base_url)

    # 获取最大页码
    max_page = int(html_xml.xpath("//ul[@class='list-pagination']/li[last()-1]/a/text()")[0])
    # print(max_page)

    # 获取数据
    get_data(max_page)


def get_data(max_page):
    # 循环获取每一页的xml对象 并获取其中的指定的数据
    for page in range(1, max_page + 1):
        print("================第{}页开始下载======================".format(page))
        base_url = "https://guangzhou.baixing.com/search/?page={}&query=%E5%B7%A5%E4%BD%9C".format(
            page)
        # print(base_url)
        html_xml = get_html(base_url)

        # 缩小范围
        li_list = html_xml.xpath("//ul[@class='list-ad-items']/li[@data-aid]")

        # 遍历获取每条狗的信息
        for co, li in enumerate(li_list, 1):
            # 图片
            pic = li.xpath(".//img/@src")[0]
            if "http" not in pic:
                pic = li.xpath(".//img/@data-originsource")
                pic = pic[0] if pic else ""

            # 获取描述信息
            desc = li.xpath(".//a[@class='ad-title']/text()")
            desc = desc[0] if desc else None

            # 获取地址信息
            address = li.xpath(".//div/div[@class='ad-item-detail'][1]/text()")
            address = address[0] if address else None

            # 类型
            work_type = li.xpath(".//a[@class='tag tag-category']/text()")
            work_type = work_type[0] if work_type else ""

            # 获取价格
            price = li.xpath(".//div/span/text()")
            price = price[0] if price else "面议"

            work_dict = {
                "pic": pic,
                "desc": desc,
                "address": address,
                "work_type": work_type,
                "price": price,
            }
            print(work_dict)
            save_image(work_dict)
            save_work_info(work_dict)


def save_image(work_dict):
    try:
        if work_dict["pic"] == "":
            return
        response = requests.get(work_dict["pic"])
        if response.status_code == 200:
            file_path = 'img/{0}-{1}-{2}.{3}'.format(validate_title(work_dict["work_type"]),
                                                     validate_title(work_dict["address"]),
                                                     validate_title(work_dict["price"]), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print('Downloaded image path is:', file_path)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def save_work_info(work_dict):
    file = open("work_info.txt", "a+", encoding="utf-8")
    line = work_dict["work_type"] + "\t" + work_dict["desc"] + "\t" + work_dict["address"] + work_dict["price"] + "\n"
    file.write(line)
    file.close()


# 获取指定url对应的xml对象
def get_html(url):
    response = requests.get(url)
    html = response.text
    return etree.HTML(html)


if __name__ == '__main__':
    get_max_page()
