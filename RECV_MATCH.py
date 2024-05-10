from pymavlink import mavutil

iha = mavutil.mavlink_connection("127.0.0.1:14550", baudrate = 57600, autoreconnect= True)
iha.wait_heartbeat()

print("Bağlantı başarılı")

while True:
    msg = iha.recv_match()

    if msg:
        print(msg)
