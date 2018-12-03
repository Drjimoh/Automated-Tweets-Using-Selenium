import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



#creating a webdriver ChromeDriver instance
f = webdriver.Chrome()
#connecting to the login page obviously
f.get('https://twitter.com/login')

#creating an inplicit wait variable
wait = f.implicitly_wait(10)

#getting the DOM required to login and sending in login details
f.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys('Username Here')
wait
psw = f.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
psw.send_keys('xXXxXXXxXX')
#keys.Return is like pressing the return keys after inputing the psword, bitch you guessed it.
psw.send_keys(Keys.RETURN)
wait


#by now we've logged in and i feel the urge to connect to my profile 
#to prevent the annoying homepage from refreshing every 5 seconds and 
#loading tweets I don't give a shit about, lets get to it
f.get('https://twitter.com/YourUsernameHere')
wait

#now we are on the data and bullshit-saving profile page
#lets deploy our tweets out there

f.find_element_by_xpath('//*[@id="global-new-tweet-button"]').click()
wait
tweeter = f.find_element_by_xpath('//*[@id="Tweetstorm-tweet-box-0"]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]')

#use a file if you will but i think lists are the most basic shit in the prog world
your_tweet_list = []
x = len(your_tweet_list) - 1 #don't ask why if you don't know how dumb python's indexing system is by now
while x > 0:
	tweeter.send_keys(your_tweet_list[x])
	wait
	#comment the next line out if you don't want to include an image in your tweets 
	f.find_element_by_xpath('//*[@id="Tweetstorm-tweet-box-0"]/div[2]/div[2]/div[1]/span[1]/div/div/label/input').send_keys(os.getcwd()+"/image.jpg")
	wait
	f.find_element_by_xpath('//*[@id="Tweetstorm-tweet-box-0"]/div[2]/div[2]/div[2]/span/button[2]/span').click()
	wait
	x -= 1
	
#you can replace the following line(s) with your cast list
print('dis nuh mek sense but ok')