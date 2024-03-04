from playwright.sync_api import sync_playwright
import io
import os
import base64

current_dir = os.path.dirname(__file__)
html_file = os.path.join(current_dir,'template2.html')

def generate_pdf(file_path, scroll_speed):
    """
    生成pdf
    :param url: 页面URL
    :param scroll_speed: 滚动速度"""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,                # 是否使用无头模式            
            args=['--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-gpu',
                '--unlimited-storage',
                '--disable-dev-shm-usage',
                '--full-memory-crash-report',
                '--disable-extensions',
                '--mute-audio',
                '--no-zygote',
                '--no-first-run',
                '--start-maximized'
                ],        # 传递给浏览器的命令行参数
        )
        page = browser.new_page()

        page.goto('file:///' + file_path)
        # 获取页面高度
        page_height = page.evaluate('document.body.scrollHeight')
        # 定义滚动步长，控制滚动速度
        scroll_step = 500
        # 计算总共需要滚动的步数
        total_steps = page_height // scroll_step
        for step in range(total_steps):
            # 计算每一步的滚动位置
            scroll_position = step * scroll_step
            # 执行 JavaScript 代码，将页面滚动到指定位置
            page.evaluate(f'window.scrollTo(0, {scroll_position});')
            # 等待一小段时间，模拟滚动速度
            page.wait_for_timeout(scroll_speed)
        # 等待网络空闲
        page.wait_for_load_state('networkidle')
        # 生成PDF
        page.pdf(path='template2.pdf', format='A4')
        browser.close()

# 定义滚动速度（以毫秒为单位，例如100表示每100毫秒滚动一次）
scroll_speed = 10
# 运行生成PDF的函数
generate_pdf(html_file, scroll_speed)
