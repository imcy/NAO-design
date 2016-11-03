#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time
import random
from naoqi import ALProxy

motion = ALProxy("ALMotion", "192.168.1.102", 9559)
aup = ALProxy("ALAudioPlayer", "192.168.1.102", 9559)
postureProxy = ALProxy("ALRobotPosture","192.168.1.102",9559)
# 为线程定义一个函数
def print_time( threadName, delay):
   # time.sleep(delay)
    if threadName=="Thread-1":
        fileId = aup.loadFile("/var/persistent/home/nao/1.mp3")
        #aup.play(fileId)
    else:
        motion.wakeUp()
        postureProxy.goToPosture("StandInit", 0.6)
        footStepsList = []
        footStepsList.append([["LLeg"], [[0.06, 0.1, 0.0]]])
        footStepsList.append([["LLeg"], [[0.00, 0.16, 0.0]]])
        footStepsList.append([["RLeg"], [[0.00, -0.1, 0.0]]])
        footStepsList.append([["LLeg"], [[0.00, 0.16, 0.0]]])
        footStepsList.append([["RLeg"], [[-0.04, -0.1, 0.0]]])
        footStepsList.append([["RLeg"], [[0.00, -0.16, 0.0]]])
        footStepsList.append([["LLeg"], [[0.00, 0.1, 0.0]]])
        footStepsList.append([["RLeg"], [[0.00, -0.16, 0.0]]])
        stepFrequency = 0.4
        clearExisting = False 
        nbStepDance = 4# defined the number of cycle to make
        for j in range( nbStepDance ):
            for i in range( len(footStepsList) ):
                motion.setFootStepsWithSpeed(
                footStepsList[i][0],
                footStepsList[i][1],
                [stepFrequency],
                clearExisting)       
                
        testTime = 7.2# seconds
        t = 0
        dt = 0.2
        while (t<testTime):
            motion.setAngles("HeadYaw", random.uniform(-1.0, 1.0), 0.6)
            motion.setAngles("HeadPitch", random.uniform(-0.5, 0.5), 0.6)
            t = t + dt
            time.sleep(dt)
            
        time.sleep(1.5)
        names      = "Head"
        times      = 0.5
        isAbsolute = True
        angleLists = [0.908, 0.368]
        motion.angleInterpolation(names, angleLists, times, isAbsolute)
        
        names      = "RArm"
        times      = 1
        isAbsolute = True
        angleLists = [-1.138, -0.737, -0.194, 0.045, -0.885,1]
        motion.angleInterpolation(names, angleLists, times, isAbsolute)
        times      = 0.5
        names      = "LArm"
        angleLists =[1.178, -0.22, -0.927, -1.545, -0.019,0.5]
        motion.angleInterpolation(names, angleLists, times, isAbsolute)
        time.sleep(0.7)
        names="RLeg"
        angleLists =[0.068, -0.209, -0.344, 1.068,-0.613,0.387]
        times      = 1.5
        isAbsolute = True
        motion.angleInterpolation(names, angleLists, times, isAbsolute)
        names="LLeg"
        angleLists =[0.068, 0.223, -0.323, 1.655, -1.19,0.073]
        times      = 1.5
        isAbsolute = True
        motion.angleInterpolation(names, angleLists, times, isAbsolute)
        
        names      = "RArm"
        times      = 0.5
        isAbsolute = True
        for i in range(3):
            angleLists = [-1.496, -0.468, -0.188, 0.065, -1.763,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            times      = 0.5
            angleLists = [-1.138, -0.737, -0.194, 0.045, -0.885,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
        '''
        JointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll"]
        Arm1 = [-40,  25, 0, -40]
        Arm1 = [ x * motion.TO_RAD for x in Arm1]

        Arm2 = [-40,  50, 0, -80]
        Arm2 = [ x * motion.TO_RAD for x in Arm2]

        pFractionMaxSpeed = 0.6
        motion.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)
        motion.angleInterpolationWithSpeed(JointNames, Arm2, pFractionMaxSpeed)
        motion.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)

        time.sleep(2.0)
        X = 0.0
        Y = 0.5
        Theta = 0.0
        motion.post.moveTo(X, Y, Theta)
        
    # wait is useful because with post moveTo is not blocking function
        motion.waitUntilMoveIsFinished()'''
        

# 创建两个线程
try:
    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    thread.start_new_thread( print_time, ("Thread-2", 2, ) )
except:
    print "Error: unable to start thread"

while 1:
   pass