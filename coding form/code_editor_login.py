import time
# recovery=[]
i=0
min=1
css="css"
password= "<html class=:"+css+">js</html>"
link="www.google.com"

while i<6:
    guess=str(input(print("Hello There, please enter your You password to unlock your Web Editor (HTML, CSS, JS):")))
    if i==4:
        min=min+4
    if guess!=password:
        print("Invalid username or password. Please try again in "+str(min)+" min.") 
        #time.sleep(60)
        if i>3:
            time.sleep(3)
    elif guess==password:
        print("congratulations  🎉. here is your Web Editor:"+link+"")
        break
    else:
        print("ERROR 400 - Bad Request")
        break
    i=i+1

"<html class=css>js</html>"