# coding:utf-8
from url_spider import url_manager, html_downloder, html_parser, outputter


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloder.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = outputter.Outputter()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "%s:%s" % (count, new_url)
                html_context = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_context)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                if count == 10:
                    break
                count += 1
            except Exception, e:
                print e
        self.output.output_html()
        print 'end'


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
