from selenium import webdriver
import sys
#name1=input("enter product")
#name1=str(name1)
name1=sys.stdin.readline()


name1.replace("","+")


driver=webdriver.Firefox()

driver.get("http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=moto", name1)
p1=driver.find_element_by_tag_name("div")
p11=p1.find_element_by_id('atfResults')

for x in p11.find_element_by_css_selector("a-size-base a-color-null s-inline  s-access-title  a-text-normal"):
	print (x.get_attribute("title"))
driver.quit()

