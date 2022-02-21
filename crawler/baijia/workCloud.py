import jieba
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as image
import re

special_character_removal = re.compile(r'[，。、【 】“”：；（）《》‘’{}？！⑦%>℃.^-——=&#@￥『』/]', re.IGNORECASE)


def segment_story(src_path, dest_path):
    fw = open(dest_path, 'w', encoding="utf-8")

    with open(src_path, encoding='utf-8') as fp:
        for line in fp:
            l = special_character_removal.sub('', line.strip())
            words = jieba.cut(l)
            t = ' '.join(words)
            fw.write(t)
            fw.write('\n')

    fw.close()

def generate_wordcloud(text_path, wc_path, love_mask=None):
    if love_mask is not None:
        wc = WordCloud(background_color='white',  # 背景颜色
                       max_words=1000,  # 最大词数
                       # mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                       max_font_size=100,  # 显示字体的最大值
                       stopwords=STOPWORDS.add('国'),  # 使用内置的屏蔽词，再添加'苟利国'
                       # font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
                       font_path='C:/Windows/Fonts/simfang.ttf',
                       mask=love_mask,
                       width=1280,  # 图片的宽
                       height=1024  # 图片的长
                       )
    else:
        wc = WordCloud(background_color='white',  # 背景颜色
                       max_words=1000,  # 最大词数
                       # mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                       max_font_size=100,  # 显示字体的最大值
                       stopwords=STOPWORDS.add('国'),  # 使用内置的屏蔽词，再添加'苟利国'
                       # font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
                       font_path='C:/Windows/Fonts/simfang.ttf',
                       random_state=42,  # 为每个词返回一个PIL颜色
                       width=1280,  # 图片的宽
                       height=1024  # 图片的长
                       )

    text = open(text_path, encoding='utf-8').read()
    wc.generate(text)
    # 显示图片
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    wc.to_file(wc_path)


def process_story():
    love_mask = np.array(image.open('love.jpg'))
    segment_story('work_info.txt', 'work_info_seg.txt')

    generate_wordcloud('work_info_seg.txt', 'work_info.png', love_mask)


if __name__ == "__main__":
    process_story()
