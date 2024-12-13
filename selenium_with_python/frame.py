# frame is webelement
# driver.switch_to.frame(2)
driver.switch_to.frame('main')
# main is name of frame
#or also you can create web element for it because frame is webelement then use function as
driver.switch_To_frame(frame_element)

# for come back
driver.switch_to.default_content()

#or
driver.switch_to.parenet_frame()

#if you have pop up where you have to login
#Authentication pop up
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")


 #then create web element
