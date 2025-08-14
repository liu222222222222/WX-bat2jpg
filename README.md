# WX-bat2jpg 🕵️‍♂️📸

> “微信缓存的 .dat 图片，长得像乱码，其实是穿了马甲的 JPG！  
> 本工具一把扯掉马甲，让它们秒变高清无码大图。”

---

## 🍗 能干啥？

- **一键批量** 把微信电脑版缓存的 `.dat` 解密成 `.jpg`  
- **支持多日期文件夹** 自动遍历 `yyyy-mm-dd/Img/*.dat`  
- **图形界面选目录** 双击即用，连奶奶都会用  
- **保留时间戳+序号** 妈妈再也不怕我找不到那张斗图

---

## 🍻 效果展示
[✓] 2025-08-14-01.jpg
[✓] 2025-08-14-02.jpg

---

## 🚑 食用方法

1. 装好 [**Python 3.7+**](https://www.python.org/downloads/)（别装 2.x，会炸） 我用的3.13.
2. `pip install -r requirements.txt`
3. 双击 `WX-bat2jpg.py`
4. 选中你的微信缓存目录（里面有一堆 `9e20f478899ed29eb19741386f92143c8` 这种文件夹）
5. 坐等吃瓜

---

## 🔑 密钥从哪来？

本脚本默认使用 **最最常见的 AES/XOR 组合**。  
如果你发现解出来的图还是马赛克，说明微信又偷偷换了密钥，  
请移步 [WxDatDecrypt](https://github.com/recarto404/WxDatDecrypt) 或 [云朵备份教程](https://www.cloudbak.org/use/session-config.html) 手动提取，再回来改脚本里的 `AES_KEY` 和 `XOR_KEY`。

---

## 🤝 致谢

- [recarto404/WxDatDecrypt](https://github.com/recarto404/WxDatDecrypt) —— 参考了 V4 解密流程  
- [likeflyme/cloudbak](https://github.com/likeflyme/cloudbak) —— 参考了 AES/XOR 计算方式  
- 以上两位大佬，请收下我的膝盖 🙇‍♂️

---

## ⚖️ 许可证

[MIT](./LICENSE) —— 想干啥干啥，别干坏事就行。

---

## 🔥 解密完图片太多太乱？
别急，我顺手给你写了个全自动分拣机！
👉 https://github.com/liu222222222222/WX-sort4pic
功能一览：
超大/超小图一键抓
重复图 MD5 秒速去重
缩略图 imagehash 精准清理
固定分辨率想筛就筛
同样是图形界面，同样是奶奶级操作，同样是KIMI 代笔！
解密 → 分拣 → 清爽硬盘，一条龙服务！
点我直达 ➜ liu222222222222/WX-sort4pic

---

## 🙈 免责声明

仅供学习交流，使用请确保已获微信账号所有者授权，  
任何翻车（封号、数据丢失、感情破裂）作者概不负责。
上传上来留个纪念 大部分是用KIMI K2 写的代码
 ！！KIMI就是永远的神！！以后随缘更新了 

 不懂得你们也可以问问KIMI (没有一分钱广告费)

