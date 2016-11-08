# coding=utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        # 用来存储已解析的url集合
        self.old_urls = set()

    def add_new_url(self, url):
        """增加新的一个url"""
        if url is None:
            return
        # 判断这个url是否已被解析
        if url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, new_urls):
        """增加新的一组url"""
        if new_urls is None or len(new_urls) <= 0:
            return
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):
        """判断是否还有url"""
        return len(self.new_urls) != 0

    def get_new_url(self):
        """获取一个尚未解析的url"""
        got_url = self.new_urls.pop()
        # 将这个url放进已解析的集合中
        self.old_urls.add(got_url)
        return got_url
