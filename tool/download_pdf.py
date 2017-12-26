#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup


###
# python2 download [pdf] in [this page]
###
if __name__ == '__main__':

    url = 'http://web.stanford.edu/class/cs224n/lectures/'
    path = "D:\github\stanford-cs224n-winter-2017\lectures\\"
    try:
        os.makedirs(path)
    except OSError, why:
        print "failed: %s " % str(why)
    base = urlparse.urlparse(url)
    html_doc = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html_doc, "lxml")
    a_list = soup.select("a")
    for a in a_list:
        href = a['href']
        if href.endswith('.ipynb') or href.endswith(".pdf"):
            if href.startswith("http://"):
                pass
            elif href.startswith("/"):
                href = "%s://%s%s" % (base.scheme, base.netloc, href)
            else:
                href = "%s://%s%s%s" % (base.scheme, base.netloc, base.path[:base.path.rfind("/") + 1], href)
            print href
            sub_base = urlparse.urlparse(href)
            sub_path = "%s%s" % (path, sub_base.path[sub_base.path.rfind("/"):])
            print sub_path
            urllib.urlretrieve(href, filename=sub_path)
