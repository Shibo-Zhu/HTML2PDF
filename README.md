# HTML2PDF

本文将介绍如何使用 Python 将 HTML 超长页面自动分页打印为 PDF 的几种方法，主要解决了长文中图片加载不全的问题，部分 CSS 样式可能无法体现。

## 转换方法

### 方法一

HTML 内容生成 Blob 对象，然后进行 base64 编码，构建 data URL。

```bash
python method1.py
```

### 方法二

```python
python method2.py
```

## 博客文章

有关这些方法的详细解释和讨论，请查阅我们的博客文章：
[博客文章链接](https://blog.csdn.net/weixin_52297807/article/details/136450957?spm=1001.2014.3001.5502)

## 入门指南

要开始使用该项目，请按照以下步骤操作：

1. 克隆存储库：
   ```bash
   git clone https://github.com/Shibo-Zhu/HTML2PDF.git

2. 安装依赖库：
   ```bash
   pip install -r requirements.txt
   ```
3. 安装驱动文件：
   ```bash
   python -m playwright install
   ```
