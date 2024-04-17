from pymavlink import mavutil, mavwp

vehicle= mavutil.mavlink_connection("127.0.0.1:14550",baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")

vehicle.set_mode("GUIDED")
vehicle.arducopter_arm()
print("arac arm edildi")