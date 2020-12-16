import time
from plyer import notification
if __name__ == '__main__':

        while True:
            notification.notify(
                title = "**Please Drink Water Now!!",
                message = " Drinking Water Helps Maintain the Balance of Body Fluids. Your body is composed of about 60% water.",
                app_icon = "water.ico",
                timeout = 10
            )
            time.sleep(60*60)

