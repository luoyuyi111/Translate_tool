## 功能介绍
&emsp;&emsp;用于格力MQTT调试，将cols和dat数组对应起来，一目了然。其次也是使用PYQT的一次尝试
### 使用条件
&emsp;&emsp;结合MQTT.fx的工具，订阅status主题，数据是服务器已解密的。
### 界面方面
&emsp;&emsp;界面主要采用PyQt5的QtDesigner来制作，主要是因为QT的界面可以支持CSS样式，制作起来比较好看，当然为了简单，我自己也没有加任何特效。读者可以自行加载CSS样式。

&emsp;&emsp;这里没有直接采用tkinter也是想试一下QT，对于熟悉tkinter的同学，可以自己改进，也比较简单。

**注意：** 翻译这个按钮其实没有用，增加了实时翻译的效果，所以不太会用到翻译按钮，这里加上翻译按钮主要是为了更好的模仿一些翻译软件。

### 程序方面
&emsp;&emsp;使用的Python作为编程软件，一方面是爬取方便，另一方面也比较简单 (-_-)。
```Python
# 主要文件Translate.py
    def translateText(self):
        string_text = self.translate_in.toPlainText()
        if string_text != '':
            json_text = json.loads(string_text)
            string_pack = json_text['pack']
            print(string_pack)
            json_pack = json.loads(string_pack)

            target_pack_mac = json_pack['mac']
            print(target_pack_mac)

            target_pack_cols = json_pack['cols']
            target_pack_dat = json_pack['dat']
            print(len(target_pack_cols))
            result = []
            for i in range(len(target_pack_cols)):
                res = str(i+1)+ '.'+ target_pack_cols[i] + ':' + str(target_pack_dat[i])
                result.append(res)
            self.translate_out.setPlainText('\n'.join(result))
```
![小猫咪](https://img-blog.csdnimg.cn/20191206170644586.jpg)
