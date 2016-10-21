from Handlers import index, news

urlList  = [
    (r'/index', index.IndexHandler),
    (r'/news/(.+)', news.NewsHandler),
]