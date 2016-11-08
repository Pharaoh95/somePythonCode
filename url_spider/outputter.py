class Outputter(object):
    def __init__(self):
        self.datas = list()

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        font = open('result.html', 'w')
        font.write('<html>')
        font.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        font.write('<body>')
        font.write('<table>')
        for data in self.datas:
            font.write('<tr>')
            font.write('<td>%s</td>' % data['url'])
            font.write('<td>%s</td>' % data['title'].encode('utf-8'))
            font.write('<tr>')
        font.write('</table>')
        font.write('</body>')
        font.write('</html>')
