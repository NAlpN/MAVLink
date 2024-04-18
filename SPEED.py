from pymavlink import mavutil, mavwp

vehicle= mavutil.mavlink_connection("127.0.0.1:14550",baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")

vehicle.set_mode("GUIDED")
vehicle.arducopter_arm()
print("arac arm edildi")

vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 20)
vehicle.set_mode('TAKEOFF')

vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_DO_CHANGE_SPEED,0,0,20,-1,0,0,0,0)
print('Hız değiştirildi.')