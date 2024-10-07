#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import rospy
from sensor_msgs.msg import LaserScan

class lsfilter():
   def __init__(self):
      self.pub_scan_filtered = rospy.Publisher("/scan", LaserScan, queue_size=1)
      self.sub_scan = rospy.Subscriber('/scan/raw', LaserScan, self.laserscanCallback,queue_size=1)

   def laserscanCallback(self, scan):
      scan_list = list(scan.ranges)
      for i in range(0, len(scan_list)):
          if(scan_list[i] <= 0.35):
              scan_list[i] = float('inf')
      scan.ranges = tuple(scan_list)
      self.pub_scan_filtered.publish(scan)

   def main(self):
      rospy.spin()

if __name__ == "__main__":
   rospy.init_node('LaserScanFilter')
   node = lsfilter()
   node.main()
