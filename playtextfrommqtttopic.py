import paho.mqtt.client as mqtt 
import time
import gtts
import pygame

def play_text(message):
    # you can specify the language as a second argument like: lang="pt-br" for Portuguese Brazil
    # to get all available languages along with their IETF tag, use: print(gtts.lang.tts_langs())
    tts = gtts.gTTS(message, lang="pt-br")
    
    # save the audio file
    audio_file_name = "speech.mp3"
    tts.save(audio_file_name)
    
    # play the audio file
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    
    print("audio play done!")

# callback method to receive the message when published on the topic this client has subscribed
def on_message(client, userdata, message):
    message_converted = str(message.payload.decode("utf-8"))
    print("message received= " ,message_converted)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    play_text(message_converted)

# callback methos for log
def on_log(client, userdata, level, buf):
    print("log: ",buf)

def main():

    client = ""

    try:

        broker_address="192.168.86.42" 
        #broker_address="iot.eclipse.org" #use external broker

        # create a client instance - client id must be provided and must be unique
        # there are other parameters (optional): Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
        client = mqtt.Client("ID123") 

        # connect to the broker - host must be provided
        # there are other parameters (optional): connect(host, port=1883, keepalive=60, bind_address="")
        client.connect(broker_address, port=1883)

        # subscribe to a topic - topic must be provided
        # there are other parameters (optional): subscribe(topic, qos=0)
        client.subscribe("house/texttospeech")

        #attach callback function to the client receive the messages
        client.on_message=on_message

        #attach log callback function to the client
        client.on_log=on_log

        #start the loop to "hear" the callbacks
        client.loop_start() 

        while True:
            time.sleep(10)
            print(".")

    except KeyboardInterrupt:
        client.loop_stop() #stop the loop
        print ( "App stopped" )

if __name__ == '__main__':
    print ( "Press Ctrl-C to exit" )
    main()
