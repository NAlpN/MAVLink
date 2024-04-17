from pymavlink import mavutil, mavwp

vehicle= mavutil.mavlink_connection("127.0.0.1:14550",baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")
wp= mavwp.MAVWPLoader()

def get_alt():
    message = vehicle.recv_match(type='GLOBAL_POSITION_INT', blocking= True)
    alt=message.relative_alt
    alt = alt/1000
    return alt

vehicle.set_mode("GUIDED")
vehicle.arducopter_arm()
print("arac arm edildi")

vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 20)
vehicle.set_mode('TAKEOFF')

while True: 
    current_alt= get_alt()
    if current_alt< 20:
        print(f"Anlik irtifa {current_alt}")
    elif current_alt >=  20:
        print("Istenilen irtifaya ulasildi ")
        break