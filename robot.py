from cortano import RemoteInterface

LAN_IP_ADDRESS = "192.168.5.218"
VPN_IP_ADDRESS = "10.8.0.88"
if __name__ == "__main__":
  robot = RemoteInterface("192.168.1.100")
  while robot.running():
    color, depth, sensors, _ = robot.read()
    # print(info['battery'], sensors, info['time'])

    forward = robot.keys["w"] - robot.keys["s"]
    robot.motor[0] =  forward * 127
    robot.motor[9] = -forward * 127
