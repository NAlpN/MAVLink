from pymavlink import mavutil

master = mavutil.mavlink_connection("127.0.0.1:14550", baudrate = 57600, autoreconnect= True)

message_type = mavutil.mavlink.MAVLINK_MSG_ID_HEARTBEAT

while True:
    msg = master.recv_match(type=message_type)
    
    if msg:
        print("Mesaj alındı:")
        print("Type:", msg.get_type())
        print("System ID:", msg.get_srcSystem())
        print("Component ID:", msg.get_srcComponent())
        print("Custom Mode:", msg.custom_mode)
        print("Base Mode:", msg.base_mode)
        print("System Status:", msg.system_status)
        print("MAVLink Version:", msg.mavlink_version)
