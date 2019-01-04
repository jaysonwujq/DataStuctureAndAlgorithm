import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, get_single_color_func
from PIL import Image
import numpy as np
import os

class SimpleGroupedColorFunc(object):
    """创建一个颜色函数对象，它根据颜色到单词的映射关系，为单词分配精准的颜色。
    """
    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}
        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)


class GroupedColorFunc(object):
    """Create a color function object which assigns DIFFERENT SHADES of
       specified colors to certain words based on the color to words mapping.
       Uses wordcloud.get_single_color_func
    """
    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        """Returns a single_color_func associated with the word"""
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

path = os.getcwd()
font = r'C:\Windows\Fonts\FZSTK.TTF'

text = (open(path+r'\constitution.txt', 'r', encoding='utf-8')).read()
cut = jieba.cut(text)  #分词
string = ' '.join(cut)
#img = Image.open(r'C:\Users\wujianqiang\PycharmProjects\22.jpg') #打开图片
#img_array = np.array(img) #将图片装换为数组
img = plt.imread(r'C:\Users\wujianqiang\PycharmProjects\22.jpg')

stopword=['代码']  #设置停止词，也就是你不想显示的词，这里这个词是我前期处理没处理好，你可以删掉他看看他的作用
wc = WordCloud(
    background_color='white',
    width=1000,
    height=800,
    mask=img,
    font_path=font,
    stopwords=stopword,
    min_font_size=5,
    max_words=100,
    random_state=30, # 设置有多少种随机生成状态，即有多少种配色方案
)
wc.generate_from_text(string)#绘制图片

# 自定义所有单词的颜色
color_to_words = {
    # words below will be colored with a green single color function
    '#00ff00': ['习近平', 'explicit', 'simple', 'sparse',
                'readability', 'rules', 'practicality',
                'explicitly', 'one', 'now', 'easy', 'obvious', 'better'],
    # will be colored with a red single color function
    'red': ['中国', 'implicit', 'complex', 'complicated', 'nested',
            'dense', 'special', 'errors', 'silently', 'ambiguity',
            'guess', 'hard']
}
#不属于上述设定的颜色词的词语会用灰色来着色
default_color = 'grey'
# Create a color function with single tone
grouped_color_func = SimpleGroupedColorFunc(color_to_words, default_color)
# Create a color function with multiple tones
#grouped_color_func = GroupedColorFunc(color_to_words, default_color)
# Apply our color function
wc.recolor(color_func=grouped_color_func)
# #改变字体颜色
# #img_colors = ImageColorGenerator(img)
# img_colors = 'black'
# #字体颜色为背景图片的颜色
# wc.recolor(color_func=img_colors)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
#plt.figure()
plt.show()  #显示图片
wc.to_file(path+r'\new.png')  #保存图片
