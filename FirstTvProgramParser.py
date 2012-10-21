#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re
import datetime
from BeautifulSoup import BeautifulSoup

#day = raw_input(u'Введите дату через точку dd.mm.yyyy: ')


class FirstTvProgramParser(object):

    def __init__(self, day=''):
        self.day = day
        if self.day:
            self.first_tv_parse()
            self.print_program()

    def first_tv_parse(self):
        date_format_regexp = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
        is_valid_date = date_format_regexp.match(self.day)

        if not is_valid_date:
            raise ValueError("Bad date! Need dd.mm.yyy format!")

        strURL = 'http://www.1tv.ru/shed/print/z0/ch1/'+self.day
        #strURL = 'http://www.1tv.ru/shed/print/z0/ch1/09.08.2010'
        page = urllib2.urlopen(urllib2.Request(strURL))
        soup = BeautifulSoup(page.read())
        page.close()

        datetag = soup.find("div",{'class':'title'}).find('h4')
        self.date = datetag.contents[0]+(datetag.find('span').contents[0])

        times = [i.find('a').getText() for i in soup.findAll("div", {"class":"time"})]
        names = [i.find('p').getText() for i in soup.findAll("div", {"class":"txt"})]

        parsed_program = [times, names]
        self.program =  parsed_program

    def print_program(self):
        print self.date
        for index, prog_time in enumerate(self.program[0]):
            print "%s : %s" %(prog_time, self.program[1][index])


if __name__ == "__main__":  #can not start from IDE because .encode('cp866')
    day = raw_input(u'Введите дату через точку dd.mm.yyyy: '.encode('cp866'))
    #day ='10.10.2011'
    TVParser = FirstTvProgramParser()
    if not day:
        dt = datetime.datetime.now()
        day =  dt.strftime('%d.%m.%Y')

    TVParser.day = day
    TVParser.first_tv_parse()
    TVParser.print_program()

    raw_input()
