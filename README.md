# scrapy_douban_book
用scrapy做爬虫抓取 豆瓣读书的书籍信息到本地数据库



## 使用方法
安装好各种python库后，开始爬虫采集书籍信息：

### 第一步：抓取书籍ID
目标页面：`https://book.douban.com/tag/`
使用命令行：
> scrapy crawl book

将书籍 ID存入文件中（我的电脑上大概有110个，每个文件1000个ID，不排除重复）

### 第二步：抓取书籍信息
目标页面： https://book.douban.com/subject/[ID]/
使用命令行：
> scrapy crawl book_subject

将书籍信息存入数据库（断断续续爬了约一周，有4万条书籍，有一些爬取失败了）

## 爬虫说明
* 本爬虫基于 `python` + `scrapy` + `msqyl`, 安装方法不再赘述。
* 此处不包含scrapy配置文件，请自行创建。
* 数据库创建表的SQL在douban.sql里面
* 用到文件处理、`Xpath`和数据库等相关知识
* 代码仅供参看，欢迎提issue讨论。
