# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""

import sys
import time
import thread
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "192.168.1.102"


# Global variable to store the HumanGreeter module instance
HumanGreeter = None
memory = None
motion  = None
postureProxy=None

class HumanGreeterModule(ALModule):
    """ A simple module able to react
    to facedetection events

    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")
        self.asr=ALProxy("ALSpeechRecognition")
        self.aup = ALProxy("ALAudioPlayer")
        self.aup1 = ALProxy("ALAudioPlayer")
        wordList=["你好","站起来","坐下","你叫什么","向前走","向后退","会跳舞吗"]
        self.asr.setWordListAsVocabulary(wordList)
        #Changes the basic voice of the synthesis
        self.tts.setParameter("pitchShift", 1.1)
#Deactivates double voice
        self.tts.setParameter("doubleVoice", 1.0)
        # Subscribe to the FaceDetected event:
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("WordRecognized",
            "HumanGreeter",
            "onWordRecognized")
        global motion 
        motion= ALProxy("ALMotion")
        global postureProxy
        postureProxy = ALProxy("ALRobotPosture")
        
    def print_time( self,threadName, delay):
        if threadName=="Thread-1":
            motion.setStiffnesses("RArm", 1.0)
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
            print("finish1")
        else:
            self.tts.say("你好,很高興見到你")
            time.sleep(delay)
            print("finish2")
            #memory.removeData("LastWordRecognized")
            memory.subscribeToEvent("WordRecognized",
            "HumanGreeter",
            "onWordRecognized")
                    
    def hands( self,threadName, delay):
        time.sleep(0.5)
        if threadName=="Thread-3":
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
            print("subscribeHands")
        else:
            self.tts.say("我的名字,叫闹")
            time.sleep(0.5)
            self.tts.say("我是一个机器人")
            
    def dances( self,threadName, delay):
        time.sleep(0.5)
        if threadName=="Thread-5":
            motion.setStiffnesses("LArm", 1.0)
            names      = "LArm"
            times      = 0.5
            isAbsolute = True
            for i in range(2):
                angleLists =[1.112, -0.056, -0.691, -1.539, -0.815,1]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
                angleLists =[1.112, -0.031, -1.155, -1.347, -0.815,1]
                motion.angleInterpolation(names, angleLists, times, isAbsolute)
                time.sleep(6)
                fileId = self.aup.loadFile("/var/persistent/home/nao/1.mp3")
                self.aup.play(fileId)
        else:
            self.tts.say("當然會")
            postureProxy.goToPosture("StandInit", 0.7)
            time.sleep(3)
            self.aup1.stopAll()
            memory.subscribeToEvent("WordRecognized",
            "HumanGreeter",
            "onWordRecognized")

            
            
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
        time.sleep(1)
        
        #memory.removeData("LastWordRecognized")
        memory.subscribeToEvent("WordRecognized",
            "HumanGreeter",
            "onWordRecognized")
        
    def onWordRecognized(self, *_args):
        """ This will be called each time a face is
        detected.

        """
        print("sucess")
        time.sleep(1.2)
        try:
            value=memory.getData("LastWordRecognized")
            if value[0]=="站起来":
                memory.unsubscribeToEvent("WordRecognized",
               "HumanGreeter")
                self.tts.say("好的")
                motion.wakeUp()
                postureProxy.goToPosture("StandInit", 0.6)
                motion.moveInit()
                self.tts.say("我已经站起来了")
                time.sleep(1)
                #memory.removeData("LastWordRecognized")
                memory.subscribeToEvent("WordRecognized",
               "HumanGreeter",
                "onWordRecognized")
            if value[0]=="会跳舞吗":
                memory.unsubscribeToEvent("WordRecognized",
               "HumanGreeter")
                try:
                    thread.start_new_thread( self.dances, ("Thread-5", 2, ) )
                    thread.start_new_thread( self.dances, ("Thread-6", 2, ) )
                except:
                    print "Error: unable to start thread"
        
            if value[0]=="向前走":
                memory.unsubscribeToEvent("WordRecognized",
               "HumanGreeter")
                self.tts.say("好的")
                postureProxy.goToPosture("StandInit", 0.7)
                motion.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
                X = 0.8
                Y = 0.0
                Theta = 0.0
                Frequency =1.0 # max speed
                motion.setWalkTargetVelocity(X, Y, Theta, Frequency)
                time.sleep(6.0) 
                
                X = 0.0
                Y = 0.0
                Theta = 0.0
                motion.setWalkTargetVelocity(X, Y, Theta, Frequency)
                time.sleep(2.0) 
                postureProxy.goToPosture("StandInit", 0.7)
                time.sleep(2.0) 
                #memory.removeData("LastWordRecognized")
                memory.subscribeToEvent("WordRecognized",
               "HumanGreeter",
                "onWordRecognized")
                
            if value[0]=="向后退":
                memory.unsubscribeToEvent("WordRecognized",
               "HumanGreeter")
                self.tts.say("好的")
                postureProxy.goToPosture("StandInit", 0.7)
                motion.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
                X = -0.8
                Y = 0.0
                Theta = 0.0
                Frequency =1.0 # max speed
                motion.setWalkTargetVelocity(X, Y, Theta, Frequency)
                time.sleep(6.0) 
                
                X = 0.0
                Y = 0.0
                Theta = 0.0
                motion.setWalkTargetVelocity(X, Y, Theta, Frequency)
                time.sleep(2.0) 
                postureProxy.goToPosture("StandInit", 0.7)
                time.sleep(2.0) 
                #memory.removeData("LastWordRecognized")
                memory.subscribeToEvent("WordRecognized",
               "HumanGreeter",
                "onWordRecognized")
            
            
            if value[0]=="你好":
                memory.unsubscribeToEvent("WordRecognized",
                "HumanGreeter")
                try:
                    thread.start_new_thread( self.print_time, ("Thread-1", 2, ) )
                    thread.start_new_thread( self.print_time, ("Thread-2", 2, ) )
                except:
                    print "Error: unable to start thread"
                
            if value[0]=="坐下":
                memory.unsubscribeToEvent("WordRecognized",
                "HumanGreeter")
                self.tts.say("好的")
                motion.wakeUp()
                postureProxy.goToPosture("Sit", 0.8)
                self.tts.say("我已经坐下了")
                time.sleep(1)
                #memory.removeData("LastWordRecognized")
                memory.subscribeToEvent("WordRecognized",
                "HumanGreeter",
                "onWordRecognized")
            
            if value[0]=="你叫什么":
                print("hands")
                memory.unsubscribeToEvent("WordRecognized",
                "HumanGreeter")
                try:
                    thread.start_new_thread( self.hands, ("Thread-3", 2, ) )
                    thread.start_new_thread( self.hands, ("Thread-4", 2, ) )
                except:
                    print "Error: unable to start thread"
        except:
            memory.unsubscribeToEvent("WordRecognized",
            "HumanGreeter")
            self.tts.say("不能识别")
            memory.subscribeToEvent("WordRecognized",
            "HumanGreeter",
            "onWordRecognized")

             
        
        # Subscribe again to the event
   


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

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port

     
    # Warning: HumanGreeter must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        memory.unsubscribeToEvent("WordRecognized",
            "HumanGreeter")
        myBroker.shutdown()
        HumanGreeter.tts.say("程序結束")
        sys.exit(0)



if __name__ == "__main__":
    main()