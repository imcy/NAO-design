# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""

import sys
import time
import thread
import math

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "192.168.1.102"


# Global variable to store the HumanGreeter module instance
HumanGreeter = None
memory = None


class HumanGreeterModule(ALModule):
    """ A simple module able to react
    to facedetection events

    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        self.tts = ALProxy("ALTextToSpeech")
        global memory
        memory = ALProxy("ALMemory")
        global motion 
        motion= ALProxy("ALMotion")
        global postureProxy
        postureProxy = ALProxy("ALRobotPosture")
        global proxyLed
        proxyLed = ALProxy("ALLeds")
        global FaceTracker
        FaceTracker = ALProxy("ALFaceTracker")
        global aup
        aup = ALProxy("ALAudioPlayer")
        global sonarProxy
        sonarProxy = ALProxy("ALSonar")
        memory.subscribeToEvent("FaceDetected",
            "HumanGreeter",
            "onFaceDetected")
        
    def face( self,threadName, delay):
        if threadName=="Thread-1":
            #proxyLed.fadeRGB("FaceLeds",0x00CD6600,2)
            motion.wakeUp()
            names = "RArm"
            angleLists = [0.216, 0.005, 2.086, 1.545, -0.955, 1]
            times      = 0.6
            isAbsolute = True
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
        #time.sleep(delay)
            angleLists = [0.304, -0.002, 1.051, 1.525, -0.977,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            angleLists = [0.216, 0.005, 2.086, 1.545, -0.955, 1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(delay)
            
            names      = "LArm"
            motion.setStiffnesses("LArm", 1.0)
            motion.setStiffnesses("RArm", 1.0)
            angleLists =[ 0.969, -0.208, -0.75, -1.496, -0.813,0.8]
            times      = 1.0
            isAbsolute = True
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            #time.sleep(delay)
            angleLists= [0.977, -0.314, -1.639, -1.07, -0.815,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(0.5)
            names ="RArm"
            angleLists =[1.031, -0.108, 0.688, 1.545, 0.269,0.93]
            times      = 1
            isAbsolute = True
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            angleLists = [1.091, 0.147, 1.798, 1.122, 0.387,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(0.5)
            angleLists = [1.531, -0.082, 2.084, 0.164, 0.016,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            names      = "LArm"
            angleLists = [1.051, -0.134, -1.627, -1.115, 0.133,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            self.tts.say("握个手吧")
            memory.subscribeToEvent("HandLeftRightTouched",
            "HumanGreeter",
            "onHandLeftRightTouched")
        else:
            self.tts.say("你好,很高興見到你")
            time.sleep(delay)
            self.tts.say("我的名字,叫闹")
            time.sleep(0.2)
            self.tts.say("我是一个机器人")
            proxyLed.fadeRGB("FaceLeds",0x005CACEE,2)
            memory.subscribeToEvent("FrontTactilTouched",
            "HumanGreeter",
            "onFrontTactilTouched")
               
    def hand( self,threadName, delay):
        if threadName=="Thread-3":
            names      = "LArm"
            angleLists = [1.496, 0.103, -1.705, -0.264, -0.508,0.8]
            times      = 1
            isAbsolute = True
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(0.5)
            times      = 0.7
            for i in range(2):
                angleLists =[-0.852, 0.201, -0.754, -1.33, -0.672,0.9]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
                angleLists =[-0.785, 0.557, -0.855, -1.422, -0.614,0.9]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
            
            names      = "LArm"
            motion.setStiffnesses("LArm", 1.0)
            motion.setStiffnesses("RArm", 1.0)
            angleLists =[ 0.969, -0.208, -0.75, -1.496, -0.813,0.8]
            times      = 1.0
            isAbsolute = True
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            #time.sleep(delay)
            angleLists= [0.977, -0.314, -1.639, -1.07, -0.815,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(0.5)   
            angleLists = [1.496, 0.103, -1.705, -0.264, -0.508,0.8]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
        else:
            time.sleep(3)
            self.tts.say("你摸摸我头")
            time.sleep(0.5)
            self.tts.say("我会跟你走")     
    
    def hand2( self,threadName, delay):
        if threadName=="Thread-5":
            names      = "LArm"
            motion.setStiffnesses("LArm", 1.0)
            isAbsolute = True
            time.sleep(0.5)
            times      = 0.7
            for i in range(2):
                angleLists =[-0.852, 0.201, -0.754, -1.33, -0.672,0.9]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
                angleLists =[-0.785, 0.557, -0.855, -1.422, -0.614,0.9]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
            angleLists =[ 0.969, -0.208, -0.75, -1.496, -0.813,0.8]
            times      = 1.0
            isAbsolute = True
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            angleLists= [0.977, -0.314, -1.639, -1.07, -0.815,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(0.5)
        else:
            time.sleep(1)
            self.tts.say("你再摸摸我头")
            time.sleep(1)
            self.tts.say("我会跳舞")     
            memory.subscribeToEvent("MiddleTactilTouched",
            "HumanGreeter",
            "onMiddleTactilTouched")
    
    def dance(self,threadName, delay):
        if threadName=="Thread-7":
            #fileId = aup.loadFile("/var/persistent/home/nao/1.mp3")
            #aup.play(fileId)
            pass
        else:
            motion.wakeUp()
            postureProxy.goToPosture("StandInit", 0.7)
            '''#titui
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
            nbStepDance = 3# defined the number of cycle to make
            for j in range( nbStepDance ):
                for i in range( len(footStepsList) ):
                    motion.setFootStepsWithSpeed(
                    footStepsList[i][0],
                    footStepsList[i][1],
                    [stepFrequency],
                    clearExisting)       
            isEnabled  = True
            motion.wbEnable(isEnabled)
            #xiugaitou
            names      = "Head"
            times      = 0.5
            isAbsolute = True
            angleLists = [0,0]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)    
            time.sleep(12.5)     
            #gui1
            names      = ["Head","RArm","LArm"]
            times      = 1
            isAbsolute = True
            angleLists = [0.908, 0.368,-1.138, -0.737, -0.194, 0.045, -0.885,1,
                                1.178, -0.22, -0.927, -1.545, -0.019,0.5]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(0.2)
        
            names=["RLeg","LLeg"]
            angleLists =[0.068, -0.209, -0.344, 1.068,-0.613,0.387,
                               0.068, 0.223, -0.323, 1.655, -1.19,0.073]
            times      = 1
            isAbsolute = True
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(1)
            names      = "RArm"
            times      = 0.35
            isAbsolute = True
            for i in range(3):
                angleLists = [-1.138, -0.737, -0.194, 0.045, -0.885,1]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
                angleLists =[-1.138, -0.737, -0.407, 0.855, -0.8885,1]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
            #niudong
            for i in range(3):
                JointNames =["LLeg","RLeg","LArm","RArm","Head"]
                Arm = [-0.29, 0.288, -0.74, 1.422, -0.632, -0.07,
                   -0.29, 0.093, -0.417, 0.981, -0.435, 0.14,
                   -1.286, 1.101, -0.26, -1.545, -0.885,1.0,
                   -1.0, -0.62, 1.311, 0.066, 0.29,1.0,
                   -0.401, -0.469
                        ]
                times=0.8
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
  
                JointNames =["LLeg","RLeg","LArm","RArm","Head"]
                Arm = [-0.288, 0.307, -0.515, 1.016, -0.319, -0.398,
                   -0.288, 0.15, -0.644, 1.415, -0.675, -0.274,
                   -1.236, 0.777, -1.616, -0.04, -0.028,1.0,
                   -0.086, 0.007, 1.381, 1.536, 0.288,1.0,
                   0.799, -0.469
                        ]
                times=0.75
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            #postureProxy.goToPosture("StandInit", 0.7)
            #gui2
            time.sleep(0.5)
            names      = ["Head","RArm","LArm"]
            times      = 0.5
            isAbsolute = True
            angleLists =[1.176, -0.183,
                               0.922, -0.11, 0.632, 1.543, 0.476,0.6,
                               1.148, 1.138, -2.077, -0.187, -0.681,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(0.2)

            names=["LLeg","RLeg"]
            angleLists =[-0.408, 0.15, -1.002, 0.997, 0.171, -0.398,
                               -0.038, -0.265, -0.93, 2.112, -1.187, -0.037]
            times      = 1.2
            isAbsolute = True
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(0.2)
        
            times      = 0.4
            names      = "LArm"
            isAbsolute = True
            for i in range(3):
                angleLists =[0.93, 0.88, -2.059, -1.281, -1.691,1]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
                angleLists =[1.148, 1.138, -2.077, -0.187, -0.681,1]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
            postureProxy.goToPosture("StandInit", 1)
            #zuoyoushou
            time.sleep(0.6)
            JointNames =["LArm","RArm","Head","LLeg","RLeg"]
            Arm = [0.147, 0.209, -1.798, -1.445, -0.492,0.96,
                   0.524, 0.314, 0.307, 0.969, 0.648,0.93,
                   0,0,
                   -0.056, -0.031, -0.834, 2.112, -1.19, 0.017,
                   -0.056, 0.024, -0.869, 2.112, -1.187, -0.04
                   ]    
            times=1
            isAbsolute = True
            motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            time.sleep(1.1)
            for i in range(2):
                JointNames =["LArm","Head"]
                times=0.4
                Arm = [ 0.113, 0.145, -1.03, -1.545, -0.494,0.96,
                        -0.487, 0.056 ]
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
                Arm = [0.147, 0.209, -1.798, -1.445, -0.492,0.96,
                        0,0]    
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
                Arm = [0.848, 0.093, -1.815, -1.518, -0.494,0.96,
                        -0.021, 0.435]    
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
                Arm = [0.147, 0.209, -1.798, -1.445, -0.492,0.96,
                        0,0]    
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)

                JointNames =["LArm","RArm","Head"]
                Arm = [0.653, 0.124, -0.379, -1.449, -0.67,0.96,
                                0.223, 0.009, 1.396, 1.545, -0.019,0.93,
                                0,0]    
                times=0.4
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
                JointNames =["RArm","Head"]
                Arm = [ 0.286, 0.003, 0.93, 1.545, -0.017,0.93,
                            0.731, 0.044 ]
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
                Arm = [0.223, 0.009, 1.396, 1.545, -0.019,0.93,
                            0,0]    
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
                Arm = [0.682, 0.066, 1.396, 1.501, -0.017,0.93,
                            0.007, 0.379]    
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
                Arm = [0.223, 0.009, 1.396, 1.545, -0.019,0.93,
                            0,0]    
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            #dakai
            times      = 1
            JointNames =["LLeg","RLeg","LArm","RArm","Head"]
            Arm = [-0.44, 0.15, 0.012, 0.791, -0.466, -0.058,
                        -0.44, -0.138, 0.188, 0.59, -0.431, 0.108,
                            0.627, -0.286, -1.532, -0.559, 1.093, 0.69,
                            0.016, 0.51, -0.361, 0.314, 0.141, 0.93,
                            0,0
                            ]
            isAbsolute = True
            motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            time.sleep(2.2)
            times=0.8
            JointNames =["LLeg","RArm","LArm","Head"]
            Arm = [-0.476, 0.161, -0.377, 0.723, -0.049, -0.04,
                    0.627, -0.286, -1.532, -0.559, 1.093, 0.69,
                    1.049, 0.677, -2.077, -0.293, 1.471,0.88,
                    1.126, 0.141
                    ]
            isAbsolute = True
            motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            time.sleep(1.6)
            times=0.45
            for i in range(4):
                JointNames =["LArm","RArm","Head"]
                Arm = [0.805, 0.723, -0.524, -1.531, 0.091,0.88,
                       0.473, 0.251, -0.201, 0.867, 1.365,0.88,
                       0.436, 0.04
                            ]
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
                Arm = [1.049, 0.677, -2.077, -0.293, 1.471,0.88,
                            0.627, -0.286, -1.532, -0.559, 1.093, 0.69,
                            0.436, 0.04]
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            time.sleep(1)
            #dakai2    
            times=0.7
            JointNames =["LLeg","RLeg","LArm","RArm","Head"]
            Arm = [-0.44, 0.15, 0.012, 0.791, -0.466, -0.058,
             -0.44, -0.138, 0.188, 0.59, -0.431, 0.108,
             0.627, -0.286, -1.532, -0.559, 1.093, 0.69,
             0.016, 0.51, -0.361, 0.314, 0.141, 0.93,
             0,0
             ]
            isAbsolute = True
            motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            time.sleep(1.2)

            JointNames =["RLeg","RArm","LArm","Head"]
            Arm = [-0.668, -0.061, -0.33, 0.716, -0.086, 0.003,
                   0.627, -0.286, -1.532, -0.559, 1.093, 0.69,
                   0.016, 0.51, -0.361, 0.314, 0.141, 0.93,
                   -0.401, 0.424
                        ]
            isAbsolute = True
            motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            times=0.45
            for i in range(3):
                JointNames =["RArm","Head"]
                Arm = [-0.194, -0.22, 0.855, 0.052, 0.162,0.93,
                            -0.443, -0.239
                            ]
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
                Arm = [0.627, -0.286, -1.532, -0.559, 1.093, 0.69,
                            -0.401, 0.424]
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            time.sleep(1.2)
            #baishou
            postureProxy.goToPosture("StandInit", 1)
            names      = "LArm"
            times      = 0.3
            isAbsolute = True
            angleLists=[0.386, -0.122, -1.19, -1.545, -1.093,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
        
            names      = "RArm"
            times      = 0.3
            isAbsolute = True
            angleLists=[0.386, 0.286, 1.114, 1.545, 0.607,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
        
            names      = "Head"
            times      = 0.5
            isAbsolute = True
            angleLists = [-1.178, 0.031]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
        
            names      = "LArm"
            times      = 0.5
            isAbsolute = True
            for i in range(2):
                angleLists = [-0.871, 0.387, -1.084, -1.545, -1.068,1]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
                angleLists=[0.386, -0.122, -1.19, -1.545, -1.093,1]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
            
            names      = "Head"
            times      = 0.5
            isAbsolute = True
            angleLists = [1.014, 0.068]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            
            names      = "RArm"
            times      = 0.5
            isAbsolute = True
            for i in range(2):
                angleLists = [-1.075, -0.075, 0.922, 1.091, 0.588,1]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
                angleLists=[0.386, 0.286, 1.114, 1.545, 0.607,1]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(0.5)
                
            names      = ["LArm","RArm","Head"]
            times      = 0.5
            isAbsolute = True
            angleLists = [1.485, -0.136, -1.213, -1.545, -0.461,1,
                                    1.206, -0.038, 0.761, 1.337, 1.014,1,
                                    0,0]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            time.sleep(0.5)
            #niudong2
            for i in range(2):
                JointNames =["LLeg","RLeg","LArm","RArm","Head"]
                Arm = [-0.29, 0.288, -0.74, 1.422, -0.632, -0.07,
                       -0.29, 0.093, -0.417, 0.981, -0.435, 0.14,
                       1.433, 0.471, -0.524, -1.539, -0.499,0.96,
                      0.679, -0.18, -0.272, 1.302, 0.15,0.93,
                      -0.188, 0.333
                            ]
                times=0.9
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
      
                JointNames =["LLeg","RLeg","LArm","RArm","Head"]
                Arm = [-0.288, 0.307, -0.515, 1.016, -0.319, -0.398,
                       -0.288, 0.15, -0.644, 1.415, -0.675, -0.274,
                       1.433, 0.471, -0.524, -1.539, -0.499,0.96,
                      0.679, -0.18, -0.272, 1.302, 0.15,0.93,
                       0.606, 0.335
                            ]
                times=0.9
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            #niudong3
            for i in range(2):
                JointNames =["LLeg","RLeg","LArm","RArm","Head"]
                Arm = [-0.29, 0.288, -0.74, 1.422, -0.632, -0.07,
                       -0.29, 0.093, -0.417, 0.981, -0.435, 0.14,
                       -1.286, 1.101, -0.26, -1.545, -0.885,1.0,
                       -1.0, -0.62, 1.311, 0.066, 0.29,1.0,
                       -0.401, -0.469
                            ]
                times=0.9
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
      
                JointNames =["LLeg","RLeg","LArm","RArm","Head"]
                Arm = [-0.288, 0.307, -0.515, 1.016, -0.319, -0.398,
                       -0.288, 0.15, -0.644, 1.415, -0.675, -0.274,
                       -1.236, 0.777, -1.616, -0.04, -0.028,1.0,
                       -0.086, 0.007, 1.381, 1.536, 0.288,1.0,
                       0.799, -0.469
                            ]
                times=0.9
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            #niudong4
            for i in range(2):
                JointNames =["LLeg","RLeg","LArm","RArm","Head"]
                Arm = [-0.29, 0.288, -0.74, 1.422, -0.632, -0.07,
                       -0.29, 0.093, -0.417, 0.981, -0.435, 0.14,
                       1.433, 0.471, -0.524, -1.539, -0.499,0.96,
                      0.679, -0.18, -0.272, 1.302, 0.15,0.93,
                      -0.188, 0.333
                            ]
                times=0.9
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
      
                JointNames =["LLeg","RLeg","LArm","RArm","Head"]
                Arm = [-0.288, 0.307, -0.515, 1.016, -0.319, -0.398,
                       -0.288, 0.15, -0.644, 1.415, -0.675, -0.274,
                       1.433, 0.471, -0.524, -1.539, -0.499,0.96,
                      0.679, -0.18, -0.272, 1.302, 0.15,0.93,
                       0.606, 0.335
                            ]
                times=0.9
                isAbsolute = True
                motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
            
            postureProxy.goToPosture("StandInit", 1)
            aup1 = ALProxy("ALAudioPlayer", "192.168.1.102", 9559)
            aup1.stopAll()
            isEnabled  = False
            motion.wbEnable(isEnabled)'''
            #over
            names      = "RArm"
            times      = 0.5
            isAbsolute = True
            angleLists = [1.283, -0.065, 2.086, 1.211, 0.888,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            self.tts.say("我已经表演完了")
            names      = "LArm"
            times      = 0.5
            isAbsolute = True
            angleLists =[1.215, -0.178, -2.077, -1.408, -0.564,1]
            motion.angleInterpolation(names, angleLists, times, isAbsolute)
            self.tts.say("你满意吗")
            memory.subscribeToEvent("HandLeftBackTouched",
            "HumanGreeter",
            "onHandLeftBackTouched")
            memory.subscribeToEvent("HandRightBackTouched",
            "HumanGreeter",
            "onHandRightBackTouched")
            
    def onFaceDetected(self, *_args):
        memory.unsubscribeToEvent("FaceDetected",
            "HumanGreeter")
        try:
            thread.start_new_thread( self.face, ("Thread-1", 2, ) )
            thread.start_new_thread( self.face, ("Thread-2", 2, ) )
        except:
            print "Error: unable to start thread"
            
    def onHandLeftRightTouched(self, *_args):
        print("sucesshand")
        memory.unsubscribeToEvent("HandLeftRightTouched",
            "HumanGreeter")
        names      = "LArm"
        times      = 0.6
        isAbsolute = True
        angleLists = [1.051, -0.134, -1.627, -1.115, 0.133,0.4]
        motion.angleInterpolation(names, angleLists, times, isAbsolute)
        self.tts.say("你真友好")
        
        isAbsolute = True
        angleLists = [1.496, 0.103, -1.705, -0.264, -0.508,0.8]
        motion.angleInterpolation(names, angleLists, times, isAbsolute)
        try:
            thread.start_new_thread( self.hand, ("Thread-3", 2, ) )
            thread.start_new_thread( self.hand, ("Thread-4", 2, ) )
        except:
            print "Error: unable to start thread"
    
    def onFrontTactilTouched(self, *_args):
        memory.unsubscribeToEvent("FrontTactilTouched",
            "HumanGreeter")
        postureProxy.goToPosture("StandInit", 0.7)
        self.tts.say("我開始跟着你走")
        print "ALFaceTracker successfully started, now show your face to Nao!"
        time.sleep(1)
        sonarProxy.subscribe("myApplication")
        FaceTracker.startTracker()
        for i in range(20):
            value=FaceTracker.getPosition()
            value2=memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
            value3=memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
            if value2<0.3 and value3<0.3:
                sonarProxy.unsubscribe("myApplication")
                self.tts.say("前面有障礙")
                time.sleep(0.5)
                sonarProxy.subscribe("myApplication")
            X = value[0]
            Y = value[1]
            Theta = 0.0
            Frequency =1.0 # max speed
            try:
                motion.setWalkTargetVelocity(X, Y, Theta, Frequency)
            except:
                motion.setWalkTargetVelocity(0, 0, Theta, Frequency)
            time.sleep(1)
            X = 0.0
            Y = 0.0
            Theta = 0.0
            motion.setWalkTargetVelocity(X, Y, Theta, Frequency)
        FaceTracker.stopTracker()
        time.sleep(1)
        self.tts.say("走不動了")
        sonarProxy.unsubscribe("myApplication")
        JointNames =["LArm","RArm","Head"]
        Arm = [0.147, 0.209, -1.798, -1.445, -0.492,0.96,
                    0.524, 0.314, 0.307, 0.969, 0.648,0.93,
                    0,0,]    
        times=1
        isAbsolute = True
        motion.angleInterpolation(JointNames, Arm, times, isAbsolute)
        try:
            thread.start_new_thread( self.hand2, ("Thread-5", 2, ) )
            thread.start_new_thread( self.hand2, ("Thread-6", 2, ) )
        except:
            print "Error: unable to start thread"
        
    def onMiddleTactilTouched(self, *_args):
        memory.unsubscribeToEvent("MiddleTactilTouched",
            "HumanGreeter")
        postureProxy.goToPosture("StandInit", 0.7)
        #jugong
        isEnabled  = True
        motion.wbEnable(isEnabled)
        names      = ["RArm","LArm"]
        times      = 0.8
        isAbsolute = True
        angleLists = [0.775, 0.012, 0.412, 1.234, 0.375, 0.3,
                                    2.086, -0.042, -1.375, -0.045, -0.155, 0.96
                                    ]
        motion.angleInterpolation(names, angleLists, times, isAbsolute)    
            # Legs are constrained in a plane
        stateName  = "Plane"
        supportLeg = "Legs"
        motion.wbFootState(stateName, supportLeg)
        # HipYawPitch angleInterpolation
        # Without Whole Body balancer, foot will not be keeped plane.
        names      = "LHipYawPitch"
        angleLists = [-45.0, 10.0, 0.0]
        timeLists  = [2.0, 5.0, 8.0]
        isAbsolute = True
        angleLists = [angle*math.pi/180.0 for angle in angleLists]
        motion.angleInterpolation(names, angleLists, timeLists, isAbsolute)
            
        names      = ["RArm","LArm"]
        times      = 1
        angleLists =[1.517, -0.115, 1.78, 0.218, -0.44, 1,
                                    1.541, 0.145, -1.108, -0.248, -1.18, 1]
        motion.angleInterpolation(names, angleLists, times, isAbsolute)
        self.tts.say("我準備好了")
        isEnabled  = False
        motion.wbEnable(isEnabled)
        try:
            thread.start_new_thread( self.dance, ("Thread-7", 2, ) )
            thread.start_new_thread( self.dance, ("Thread-8", 2, ) )
        except:
            print "Error: unable to start thread"
     
    def onHandLeftBackTouched(self, *_args): 
        memory.unsubscribeToEvent("HandLeftBackTouched",
            "HumanGreeter")
        memory.unsubscribeToEvent("HandRightBackTouched",
            "HumanGreeter")
        self.tts.say("满意")
    
    def onHandRightBackTouched(self, *_args): 
        memory.unsubscribeToEvent("HandLeftBackTouched",
            "HumanGreeter")
        memory.unsubscribeToEvent("HandRightBackTouched",
            "HumanGreeter")
        self.tts.say("不满意")
        
def main():
    """ Main entry point

    """
    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port
    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        HumanGreeter.tts.say("程序結束")
        sys.exit(0)



if __name__ == "__main__":
    main()