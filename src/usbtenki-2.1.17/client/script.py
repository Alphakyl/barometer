#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import Float32

def talker():
	pubP = rospy.Publisher('Pressure', Float32, queue_size=10)
	pubT = rospy.Publisher('Temperature', Float32, queue_size=10)
	pubA = rospy.Publisher('Altitude', Float32, queue_size=10)	
	rospy.init_node('USBTenki_Barometer', anonymous=True)
	rate = rospy.Rate(1)

	cmd = '~/catkin_ws/src/barometer/src/usbtenki-2.1.17/client/usbtenkiget -i 0,1,262'
	msg = Float32()

	while not rospy.is_shutdown():
		#os.system("pwd")
		so = os.popen(cmd).read()
		x=so.split(", ")
		msg.data = float(x[0])
		pubP.publish(msg)
		msg.data = float(x[1])
		pubT.publish(msg)
		msg.data = float(x[2])
		pubA.publish(msg)

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass	
	

	
