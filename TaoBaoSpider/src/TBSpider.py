from selenium import webdriver
import time
import re


def search():
    browser.find_element_by_id('q').send_keys('python')
    browser.find_element_by_class_name('btn-search').click()
    time.sleep(10)
    token = browser.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    token = int(re.compile('/d+').search(token).group(0))

    return token


def next_page(keyword):
    token = search()
    num = 0
    while num != token - 1:
        browser.get('https://www.taobao.com/search?q={}&s={}'.format(keyword, 44*num))
        browser.implicitly_wait(10)
        num += 1
        drop_down()
        get_product()


# 下滑
def drop_down():
    for x in range(1, 11, 2):
        time.sleep(0.5)
        j = x/10
        js = 'document.documentElem.scrollTop = '


def get_product():
    lis = browser.find_element_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnver"]')


if __name__ == '__main__':
    keyword = input('请输出你想搜索的关键词')
    browser = webdriver.Chrome()
    browser.get('http://www.taobao.com')
    next_page(keyword)
