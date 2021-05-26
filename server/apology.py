# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

import random
import re

nickname = [
    "宝贝name，",
    "亲爱的name，",
    "可爱的name，",
    "我最爱的name，",
    "name小可爱，",
    "name小仙女，",
    "name小甜心，"
]

apology = [
    "event的事是我错了。",
    "我已经为event深刻反省了。",
    "还在为event的事生气吗？",
    "event的事的确是我不对。",
    "我千不该万不该，最不该event。",
    "我保证下次一定不会event。",
    "我不该event的。",
    "我为event的事诚挚的道歉。"
]

apology_text = [
    "我知道你很生气。而且你每次生气我都好害怕。理解我，好么？原谅我，好么？",
    "气球太饱会爆，固然你的皮厚，可是也不能撑过久啊，放点气吧，哪怕是从上面。",
    "宝贝抱歉，刚刚我太冲动了，无意中伤到了你，请你原谅！这样的我你还爱我吗？",
    "你是我的，谁都抢不走，我就是这么霸道，我是你的，谁都领不走，我就是这么死心。",
    "我只想说：我不是有意要气你的，只因为我爱你，我不想多说只求你能原谅我,我爱你！",
    "男人如果得不到女人的谅解。就算膝下有黄金又能怎样。我跪下来表示百分之百的赔罪！",
    "原以为彼此相爱平淡，谁知转眼风云突变；方知昨日难求，放出爱的信鸽，我很想念你！",
    "我只想说：我不是有意要气你的，只因为我爱你，我不想多说只求你能原谅我！",
    "霓虹在夜晚将天空撕裂，悔恨的泪水在眼前模糊，也许这是注定的错！亲爱的，我想你了。",
    "想编个幽默的故事，告诉你那个开了四年的玩笑，却又怕弄湿了干干净净的秋季，请原谅我。",
    "我已经不再生你的气了，像我这样胸襟开阔、德高望重的人肯定会原谅，你还在生我的气吗！",
    "你是知道我一直很用心的爱你，我不想欠你有太多，如果有一天我真的走，你一定要原谅我。",
    "真的好想你呀，想你甜甜的笑，柔柔的话，和你美丽的脸！喂？喂？别再生气了吧！我爱你！",
    "对不起，我为我的粗鲁深表歉意。因为真的太想见你，心里从来没有那么在乎。原谅我好吗？",
    "会用行动来说明一切，不会再让你感到伤心与失望，在这我真诚的请你原谅，永远爱你的人！",
    "什么样的话语都代替不了我愧疚的心情，站在你的角度去想，更叫我伤心，我该怎样地对你呢？",
    "也许我们之间有些误会，那你也不用不理我啊！就算我错了好了，我借此对你说一声对不起。",
    "我会用行动来说明一切，不会再让你感到伤心与失望，漫漫长路希望与之协手共进，永远爱你的人。",
    "今晚的夜空没有星星，就好像我的身边缺少了你；我不是故意让你生气的，回到我身边来，好吗？",
    "过去的已经成为事实但是事实毕竟已经过去重要的是从过去中看到未来，希望我们的未来不是梦！",
    "你怎么了，这么善变，言语也不通顺了，如果作出了伤害你的事，那是我的错，今晚我们能相见吗？",
    "人喜欢看不到你的漫漫长夜，心中的你是我最大的安慰！如果你回到我身边，我发誓爱你一生一世！",
    "如果你生气就直接骂我吧，千万不要对着我掉眼泪，那样的话我的心都会碎成千万片。请你原谅我！",
    "很吊唁一块儿渡过的时间，惦念你的笑！惦念你的好！只怪本身不懂爱惜！给个机遇让咱们回到畴前。",
    "无心让我伤害了你。我的心里也不好受！希望你能理解，可以给我一个改过的机会！重新开始接受我！",
    "今天发生的故事仅仅是个意外，心存太多太多的悔意，一个信息送去我的保歉。亲爱的因为我太在乎你。",
    "难道你不能容忍一个爱你的人犯的一次错误吗如果你可原谅我，我将用我的实际行动来弥补我的过失！",
    "唱着伤心的歌曲，看着心爱的女孩。心是为你伤的，歌是为你唱的。我只是想要你幸福快乐，对不起！",
    "也许是我不懂的事太多太多，也许是我的错，也许一切已经慢慢的错过，可我依然期待你的谅解和呵护！",
    "如果由于我对你的缅怀而搅扰了你，那末什么也取代不了我惭愧和伤感的心，对不起！我该怎样对你呢？",
    "在黎明前，我们都渴望见到曙光；却也同样害怕被烈阳所伤！谈谈吧！愿能携手伴曙光；不愿两伤对烈阳！",
    "老婆，我昨晚也几乎一晚没睡，除了反省自己的过错，我还要用行动表示，抓紧时间赶制温暖牌，原谅我吧！",
    "我整个晚上都在和你发信息，你一定看见了，你一定是在感动。佛祖云我不入地狱谁入地狱，我不道歉谁道歉。",
    "两个人虽然相爱，毕竟是两个不同的个体，如果有什么不能接受的事情，也许我们可以学习彼此迁就和宽恕……",
    "我此时此刻不知道该做什么，看不到你的信息，听不到你的声音。如此的宁静，我的心快碎了，快回我短信啊？",
    "瞥见你发脾性时，撅起的小嘴，我曾试着，撞豆腐块死，用鼻涕吊死，可都没有乐成。如今就等着你来处置我。",
    "曾以为，向你提出分离必要一生的勇气，但到本日，我不能不认可——要和你一块儿过上来所需的勇气其实更大。",
    "一个傻傻的我有一颗痴痴的心，在等待你的包涵！如果你不朝气了的话能不能给我打个德律风让我表明一下，好吗？",
    "想起我们曾经有过的甜蜜，所有的气都烟消云散了。这就是真正的亲密无间，任何东西都无法割断——我们彼此的爱。"
]

NICKNAME_LEN = len(nickname)
APOLOGY = len(apology)
APOLOGY_TEXT = len(apology_text)


def apol(name, event):
    bullshit = str()
    bullshit += nickname[random.randint(0, NICKNAME_LEN - 1)]
    bullshit += apology[random.randint(0, APOLOGY - 1)]
    while (len(bullshit) <= 1000):
        randNum = random.randint(0, 15)
        if randNum % 4 == 0:
            bullshit += nickname[random.randint(0, NICKNAME_LEN - 1)]
            bullshit += apology[random.randint(0, APOLOGY - 1)]
        else:
            bullshit += apology_text[random.randint(0, APOLOGY_TEXT - 1)]
    bullshit = bullshit.replace("name", name)
    bullshit = bullshit.replace("event", event)

    bullshit = '\n'.join([bullshit[i:i + 50] for i in range(0, len(bullshit), 50)])
    return "关于{}致最亲爱的{}的道歉信:".format(event, name) + '<br>' + "&nbsp;&nbsp;&nbsp;&nbsp;" + bullshit

if __name__ == "__main__":
    print(apol("xxx", "惹你生气"))
