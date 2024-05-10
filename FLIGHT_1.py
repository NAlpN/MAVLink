from pymavlink import mavutil

def kalkis(vehicle):
    vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 20)
    vehicle.set_mode('TAKEOFF')
    print("TAKEOFF modu")

def ucus(vehicle):
    vehicle.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10,vehicle.target_system,vehicle.target_component,9,int(0b0000011111111000),0,0,0,0,0,0,0,0,0,0,0))    
    vehicle.mav.mission_item_send(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,2,0,0,0,0,0,40.26736918, -111.63366593 ,25)
    print("WAYPOINT")

def gorev(vehicle):
    gidilecek_konum = (40.26757132, -111.63242969, 50)
    iniş_konum = (40.26754886, -111.63182629, 25)

    vehicle.mav.mission_item_send(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                                  mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 2, 0, 0, 0, 0, 0,
                                  *gidilecek_konum)

    vehicle.mav.mission_item_send(0, 0, 1, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                                  mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 2, 0, 0, 0, 0, 0,
                                  *iniş_konum)

    print("Görev eklendi.")

vehicle = mavutil.mavlink_connection("127.0.0.1:14550", baudrate=57600, autoreconnect=True)
vehicle.wait_heartbeat()
print("Bağlantı başarılı")

vehicle.set_mode("GUIDED")
vehicle.arducopter_arm()
print("Araç arm edildi")

kalkis(vehicle)
ucus(vehicle)
gorev(vehicle)