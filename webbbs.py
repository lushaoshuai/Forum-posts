# -*- coding:utf-8 -*-
__author__ = 'linyuxuan'
__date__ = '2017/2/8 13:19'

from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://bbs.byr.cn/index')

'''
北邮人论坛发帖
'''
# 登录
browser.find_element_by_id('id').send_keys('vl854328793')
browser.find_element_by_id('pwd').send_keys('ni02165663004')
time.sleep(2)
browser.find_element_by_id('b_login').click()
browser.maximize_window()
time.sleep(2)
# 发帖
browser.find_element_by_link_text(u'信息社会').click()
time.sleep(2)
browser.find_element_by_link_text(u'兼职实习信息').click()
time.sleep(2)
browser.find_element_by_link_text(u'新话题').click()
time.sleep(2)
browser.find_element_by_id('post_subject').send_keys(u'【实习】【腾讯广点通】招聘数据挖掘实习生')
time.sleep(2)
ele = browser.find_element_by_id('post_content')
ele.click()
ele.send_keys(u' 腾讯效果广告平台部致力于打造世界一流的社交广告平台，我们的产品广点通（http://e.qq.com）是国内最大的社交广告平台，目前处\
  在高速发展阶段。 广点通拥有腾讯的海量优质流量，依托QQ、微信的海量用户群，为数万广告主及数亿用户提供优质的广告服务。\
【职位名称】数据挖掘实习生\
【岗位职责】负责广告业务相关的大数据分析、挖掘及数据可视化等相关工作。\
【岗位要求】\
  1、熟练掌握SQL、Python、Shell、HTML、JavaScript等语言；\
  2、熟悉数据结构，有较强的算法能力；\
  3、较强的逻辑思维，良好的沟通能力和团队合作能力；\
  4、数据挖掘、机器学习、统计或相关专业，硕士背景优先；\
  5、每周实习时间4天及以上，至少4个月。\
【工作地点】银科大厦\
【简历发至】vickihuang#tencent.com（请将#替换为@）\
【标题格式】实习申请-姓名-学校-年级-每周可到天数-可实习月数\
【简历格式】实习申请-姓名-学校-年级-每周可到天数-可实习月数')
time.sleep(2)
browser.find_element_by_class_name('button').click()

