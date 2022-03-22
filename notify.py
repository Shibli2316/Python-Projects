from socket import timeout
import time
from turtle import title
from plyer import notification

if __name__=="__main__":
    notification.notify(
        title="Cheking",
        message="It is actually working",
        timeout =3
    )

    time.sleep(8)