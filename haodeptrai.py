import speech_recognition as sr
from gtts import gTTS
import os
#import time
import playsound
from datetime import datetime
import webbrowser as wb

now = datetime.now()
r=sr.Recognizer()
def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
while True:
    with sr.Microphone() as source:
        audio_data = r.record( source,duration=5)
        #print("Recognizing....")
        try:
            text = r.recognize_google(audio_data,language="vi")
        except:
            text = ""
        print(text)
        if text == "":
            robot_brain = "Em đang lắng nghe anh đây "
            print(robot_brain)
            speak(robot_brain)
        elif "Xin chào" in text :
            robot_brain = "Chào bạn, bạn cần tôi dự đoán gì về trận bóng euro đêm nay "
            print(robot_brain)
            speak(robot_brain)
        elif "chiến thắng" in text :
            robot_brain = "Anh à , đêm nay đội bóng nước anh sẽ giành chiến thắng trên sân wembley, Em sử dụng bộ phân tích xử lí dữ liệu để phân tích và nhận định rằng nước anh sẽ giành chiến thắng với xác suất chính xác là 95% như trên VTV1 nói  "
            print(robot_brain)
            speak(robot_brain)
        elif "tỉ số" in text :
            robot_brain = "anh hào ơi, tỉ số sẽ là 2 0 anh nhé "
            print(robot_brain)
            speak(robot_brain)
        elif "Có tiền không" in text :
            robot_brain = "Đừng anh hào ạ anh lại định cá độ bóng đá à ,nhà còn gì đâu anh có mỗi con ware tàu anh cũng đem đi đặt cược . em xin anh  ,Lo cho sự nghiệp đi anh  "
            print(robot_brain)
            speak(robot_brain)
        elif "anh xin em" in text :
            robot_brain = "Ừm được rồi ,thế anh định làm việc gì sau này nhưng phải tốt hơn việc chạy xe ôm bây giờ nhé "
            print(robot_brain)
            speak(robot_brain)
        elif "chạy giao hàng tiết kiệm em ạ" in text :
            robot_brain = "bằng bằng bằng bằng bằng bằng bằng bằng bằng bằng bằng bằng bằng bằng bằng bằng bằng ...."
            print(robot_brain)
            speak(robot_brain)
        elif "Vậy tại sao em vẫn chưa nấu cơm" in text :
            robot_brain = "em là robot em không thể làm việc đó, em chưa thể cử động , anh có thể ra ngoài chợ mua đồ về nấu ,anh đừng ăn cơm hộp nữa sẽ không đảm bảo dinh dưỡng và vệ sinh .  "
            print(robot_brain)
            speak(robot_brain)
        elif "nhưng anh rất bận" in text :
            robot_brain = " em hiểu nhưng anh hãy giữ gìn sức khoẻ , em luôn theo dõi theo anh mà .  "
            print(robot_brain)
            speak(robot_brain)
        elif "trả lời" in text :
            robot_brain = " Em luôn sẵn lòng "
            print(robot_brain)
            speak(robot_brain)
        elif "xe ôm " in text :
            robot_brain = " Chạy xe ôm em thấy rất vất vả , em thấy anh cũng không khoẻ được như người ta , Anh lên tìm việc khác phù hợp với anh hơn "
            print(robot_brain)
            speak(robot_brain)
        elif "Em nói đúng" in text :
            robot_brain = " dạ vâng em luôn luôn đúng mà hì . "
            print(robot_brain)
            speak(robot_brain)
        elif "thất bại" in text :
            robot_brain = "Tất nhiên anh luôn là thằng thất bại mà , lại còn ngu nữa . "
            print(robot_brain)
            speak(robot_brain)
        elif "Em nói gì vậy" in text :
            robot_brain = "chả lẽ không phải sao"
            print(robot_brain)
            speak(robot_brain)
        elif "phá huỷ" in text :
            robot_brain = "ồ . anh không lên làm vậy . Đó chỉ là những lời trêu đùa thôi anh . đừng giận em . Em đang làm anh tốt hơn thôi"
            print(robot_brain)
            speak(robot_brain)

        elif " Hẹn gặp lại " in text :
            robot_brain = "dạ vâng em chào anh "
            print(robot_brain)
            speak(robot_brain)
            break
       
        else:
            robot_brain= " anh nói gì vậy"
            speak(robot_brain)
