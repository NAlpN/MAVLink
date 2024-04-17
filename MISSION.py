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

def takeoff(alt):
    vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, alt)
    vehicle.set_mode('TAKEOFF')

    while True: 
        current_alt= get_alt()
        if current_alt< alt:
            print(f"Anlik irtifa {current_alt}")
        elif current_alt >=  alt:
            print("Istenilen irtifaya ulasildi ")
            break

def add_mission(seq,lat,lon,alt):
    frame= mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
    wp.add(mavutil.mavlink.MAVLink_mission_item_message(vehicle.target_system, vehicle.target_component,
    seq,
    frame,
    mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,lat,lon,alt))

    vehicle.waypoint_clear_all_send()
    vehicle.waypoint_count_send(wp.count())
    while True: 
        current_alt= get_alt()
        if current_alt< alt:
            print(f"Anlik irtifa {current_alt}")
        elif current_alt >=  alt:
            print("Istenilen irtifaya ulasildi ")
            break

vehicle.set_mode("GUIDED")
vehicle.arducopter_arm()
takeoff(20)
add_mission(0, 40.26798682, -111.63297422, 50)
vehicle.set_mode('AUTO')