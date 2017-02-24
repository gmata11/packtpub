#!/usr/bin/env python
'''
Client web per descarregar el titol del llibre que volem

@author: gmc6@alumnes.udl.cat
'''

import urllib2
import bs4

class Client(object):
    # obtenir plana web
    def get_webpage(self,page):
        f = urllib2.urlopen(page)
        htmlpage = f.read()
        f.close()
        return htmlpage

    # buscar dades
    def search_data(self, html):
        bd = bs4.BeautifulSoup(html, "lxml")
        box = bd.find("div","dotd-title")
	item = box.find("h2").text
	item = self.edit_item(item)
	return item

    # eliminem els tabulats i salts de pagina
    def edit_item(self,item):
	item = item.strip('\t\r\n')
	return item

    def main(self):
        webpage = self.get_webpage('https://www.packtpub.com/packt/offers/free-learning/')
        results = self.search_data(webpage)
        # imprimir resultats
        print "Nom del llibre gratuit: " + results
        


if __name__ == "__main__":
    cw = Client()
    cw.main()
