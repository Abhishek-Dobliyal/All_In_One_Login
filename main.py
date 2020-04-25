
from tkinter import *
import tkinter.messagebox as tmsg
from selenium import webdriver
import time

############## Functions for different services
def fb_function():
    ''' Function for Facebook Login'''
    if username.get()=="" or password.get()=="":  # Check if the fields are empty or not
        tmsg.showinfo("Field Empty", "Either of the Fields cannot be Empty!")

    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://facebook.com")
        time.sleep(2.5)

        user_name_field = driver.find_element_by_xpath('//*[@id="email"]')
        user_name_field.send_keys(username.get())
        time.sleep(2)

        pass_field = driver.find_element_by_xpath('//*[@id="pass"]')
        pass_field.send_keys(password.get())
        time.sleep(2)

        login_btn = driver.find_element_by_xpath('//*[@id="u_0_b"]')
        login_btn.click()


def link_function():
    ''' Function for Linkedin Login '''
    if username.get()=="" or password.get()=="":
        tmsg.showinfo("Field Empty", "Either of the Fields cannot be Empty!")

    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        time.sleep(2.5)

        user_name_field = driver.find_element_by_xpath('//input[@type="text"]')
        user_name_field.send_keys(username.get())
        time.sleep(2)

        pass_field = driver.find_element_by_xpath('//input[@type="password"]')
        pass_field.send_keys(password.get())
        time.sleep(2)

        sign_in = driver.find_element_by_xpath('//button[@type="submit"]')
        sign_in.click()

def insta_function():
    ''' Function for Instagram Login '''
    if username.get()=="" or password.get()=="":
        tmsg.showinfo("Field Empty", "Either of the Fields cannot be Empty!")

    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://instagram.com")
        time.sleep(2.5)

        user_name_field = driver.find_element_by_xpath('//input[@name="username"]')
        user_name_field.send_keys(username.get())
        time.sleep(2)

        pass_field = driver.find_element_by_xpath('//input[@name="password"]')
        pass_field.send_keys(password.get())
        time.sleep(2)

        login_btn = driver.find_element_by_xpath('//button[@type="submit"]')
        login_btn.click()

def github_function():
    ''' Function for Github Login '''
    if username.get()=="" or password.get()=="":
        tmsg.showinfo("Field Empty", "Either of the Fields cannot be Empty!")

    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://github.com/login")
        time.sleep(2.5)

        user_name_field = driver.find_element_by_xpath('//input[@type="text"]')
        user_name_field.send_keys(username.get())
        time.sleep(2)

        pass_field = driver.find_element_by_xpath('//input[@type="password"]')
        pass_field.send_keys(password.get())
        time.sleep(2)

        login_btn = driver.find_element_by_xpath('//input[@type="submit"]')
        login_btn.click()

def twitter_function():
    ''' Function for Twitter Login '''
    if username.get()=="" or password.get()=="":
        tmsg.showinfo("Field Empty", "Either of the Fields cannot be Empty!")

    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://twitter.com/login")
        time.sleep(2.5)

        user_name_field = driver.find_element_by_xpath('//input[@type="text"]')
        user_name_field.send_keys(username.get())
        time.sleep(2)

        pass_field = driver.find_element_by_xpath('//input[@type="password"]')
        pass_field.send_keys(password.get())
        time.sleep(2)

        login_btn = driver.find_element_by_xpath('//div[@role="button"]')
        login_btn.click()

def reddit_function():
    ''' Function for Reddit Login '''
    if username.get()=="" or password.get()=="":
        tmsg.showinfo("Field Empty", "Either of the Fields cannot be Empty!")

    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://reddit.com/login/")
        time.sleep(2.5)

        user_name_field = driver.find_element_by_xpath('//input[@type="text"]')
        user_name_field.send_keys(username.get())
        time.sleep(2)

        pass_field = driver.find_element_by_xpath('//input[@type="password"]')
        pass_field.send_keys(password.get())
        time.sleep(2)

        login_btn = driver.find_element_by_xpath('//button[@type="submit"]')
        login_btn.click()

def netflix_function():
    ''' Function for Netflix Login '''
    if username.get()=="" or password.get()=="":
        tmsg.showinfo("Field Empty", "Either of the Fields cannot be Empty!")

    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://netflix.com/in/login")
        time.sleep(2.5)

        user_name_field = driver.find_element_by_xpath('//input[@type="text"]')
        user_name_field.send_keys(username.get())
        time.sleep(2)

        pass_field = driver.find_element_by_xpath('//input[@type="password"]')
        pass_field.send_keys(password.get())
        time.sleep(2)

        login_btn = driver.find_element_by_xpath('//button[@type="submit"]')
        login_btn.click()

def flipkart_function():
    ''' Function for Flipkart Login '''
    if username.get()=="" or password.get()=="":
        tmsg.showinfo("Field Empty", "Either of the Fields cannot be Empty!")

    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.flipkart.com/account/login?ret=/")
        time.sleep(2.5)

        user_name_field = driver.find_element_by_xpath('//input[@autofocus=""]')
        user_name_field.send_keys(username.get())
        time.sleep(2)

        pass_field = driver.find_element_by_xpath('//input[@type="password"]')
        pass_field.send_keys(password.get())
        time.sleep(2)

        login_btn = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/form/div[3]/button')
        login_btn.click()

def SOF_function():
    ''' Function for StackOverFlow Login '''
    if username.get()=="" or password.get()=="":
        tmsg.showinfo("Field Empty", "Either of the Fields cannot be Empty!")

    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
        time.sleep(2.5)

        user_name_field = driver.find_element_by_xpath('//input[@id="email"]')
        user_name_field.send_keys(username.get())
        time.sleep(2)

        pass_field = driver.find_element_by_xpath('//input[@id="password"]')
        pass_field.send_keys(password.get())
        time.sleep(2)

        login_btn = driver.find_element_by_xpath('//button[@id="submit-button"')
        login_btn.click()

def clr():
    ''' Clears out the User and Pass Field '''
    username.set("")
    password.set("")

root =  Tk()

root.title("All-In-One-Login")
root.geometry("780x700")
root.configure(bg="#4566b5")

################ TOP WIDGETS

username = StringVar()
password = StringVar()

welcome_label = Label(root, text="All--In--One--Login--Tool", font="helvatica 30 bold", fg="#ca2525", bg="#ddd1d1", borderwidth=3, relief=SOLID, padx=5)
welcome_label.grid(row=0,column=1,pady=15)

user_name_label = Label(root, text="Username/ Mobile :", font="Symbol 20", bg="#d5d7cf", fg="#b03737",borderwidth=2.5, relief=SOLID, padx=3, pady=5)
user_name_label.grid(row=1,column=0,padx=15,pady=19)

user_name_entry = Entry(root, textvariable=username, width=43, font="Symbol 20", bd=2, relief=SOLID)
user_name_entry.grid(row=1,column=1,padx=20)

pwd_label = Label(root,text="Password :", font="Symbol 20", bg="#d5d7cf", fg="#b03737", borderwidth=2.5, relief=SOLID, padx=3, pady=5)
pwd_label.grid(row=2,column=0,padx=20)

pwd_entry = Entry(root, textvariable=password, width=43, font="Symbol 20", show="*",  bd=2, relief=SOLID)
pwd_entry.grid(row=2,column=1)


############### BUTTONS & IMAGES

fb_image = PhotoImage(file="icon/facebook.png")
link_image = PhotoImage(file="icon/in.png")
insta_image = PhotoImage(file="icon/insta.png")
github_image = PhotoImage(file="icon/git.png")
twitter_image = PhotoImage(file="icon/twitter.png")
reddit_image = PhotoImage(file="icon/reddit.png")
netflix_image = PhotoImage(file="icon/netflix.png")
flipkart_image = PhotoImage(file="icon/flipkart.png")
SOF_image = PhotoImage(file="icon/sof.png")

main_frame = Frame(root, borderwidth=10, relief=SUNKEN, bg="#2f2929")
main_frame.grid(row=4,column=1,padx=20,pady=40)

fb_button = Button(main_frame, image=fb_image, cursor="hand", command=fb_function)
fb_button.grid(row=4,column=0,padx=15,pady=10)

linkedin_button = Button(main_frame, image=link_image, cursor="hand",command=link_function)
linkedin_button.grid(row=4,column=1,padx=15,pady=10)

insta_button = Button(main_frame, image=insta_image, cursor="hand",command=insta_function)
insta_button.grid(row=4,column=2,padx=15,pady=10)

github_button = Button(main_frame, image=github_image, cursor="hand",command=github_function)
github_button.grid(row=5,column=0,padx=15,pady=10)

twitter_button = Button(main_frame, image=twitter_image, cursor="hand",command=twitter_function)
twitter_button.grid(row=5,column=1,padx=15,pady=10)

reddit_button = Button(main_frame, image=reddit_image, cursor="hand",command=reddit_function)
reddit_button.grid(row=5,column=2,padx=15,pady=10)

netflix_button = Button(main_frame, image=netflix_image, cursor="hand", command=netflix_function)
netflix_button.grid(row=6,column=0,padx=15,pady=10)

flipkart_button = Button(main_frame, image=flipkart_image, cursor="hand", command=flipkart_function)
flipkart_button.grid(row=6,column=1,padx=15,pady=10)

SOF_button = Button(main_frame, image=SOF_image, cursor="hand", command=SOF_function)
SOF_button.grid(row=6,column=2,padx=15,pady=10)

clr_button = Button(root, text="Clear Field(s)", font="Symbol 22 bold", fg="black", highlightbackground="grey",cursor="hand",padx=11,pady=9,command=clr)
clr_button.grid(row=7,column=1)

quit_button = Button(root, text="Exit", font="Symbol 22 bold", fg="#e63535", highlightbackground="grey",cursor="hand",padx=8,pady=9,command=root.destroy)
quit_button.grid(row=8,column=1,pady=14)

root.mainloop()
