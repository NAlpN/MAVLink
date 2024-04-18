from pymavlink import mavutil, mavwp

vehicle= mavutil.mavlink_connection("127.0.0.1:14550",baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")

vehicle.set_mode("GUIDED")
vehicle.arducopter_arm()
print("arac arm edildi")

vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 20)
vehicle.set_mode('TAKEOFF')

vehicle.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10,vehicle.target_system,vehicle.target_component,9,int(0b0000011111111000),0,0,0,0,0,0,0,0,0,0,0))
print('WAYPOINT görevine başlandı.')

vehicle.mav.mission_item_send(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,2,0,0,0,0,0,40.26873920, -111.63307724,25)
print('WAYPOINT görevi başarıyla yapıldı.')