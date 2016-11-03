# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""

import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "192.168.1.102"
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
        memory.subscribeToEvent("HandLeftRightTouched",
            "HumanGreeter",
            "onHandLeftRightTouched")

    def onHandLeftRightTouched(self, *_args):
        """ This will be called each time a face is
        detected.

        """
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        #为了避免重复，说话的时候取消订阅事件
        memory.unsubscribeToEvent("HandLeftRightTouched",
            "HumanGreeter")

        self.tts.say("握手")

        # Subscribe again to the event
        #再次订阅事件
        memory.subscribeToEvent("HandLeftRightTouched",
            "HumanGreeter",
            "onHandLeftRightTouched")


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
        memory.unsubscribeToEvent("HandLeftRightTouched",
            "HumanGreeter")
        myBroker.shutdown()
        HumanGreeter.tts.say("程序結束")
        sys.exit(0)



if __name__ == "__main__":
    main()