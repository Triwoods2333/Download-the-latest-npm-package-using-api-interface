首先运行get_all-final.py，爬取现存所有npm软件包元数据，然后运行get-infos.py，获取每个软件包详情，获取后判断创建时间，如果是新创建的就下载 \
get-infos.py获取的软件包详情没有采用表格记录，而是一条一条的.txt文件，因为数据量太大了，只要运行就无响应然后闪退
### 目前存在的问题：由于是网络请求的api，寝室校园网不稳定，换成热点也不是很稳定，接口不支持断点续传，链接中断直接要从头开始，而跑一次又要很久，容错率很低，到目前为止也没完整的跑下来一次  〒▽〒
