# Self-Driving-RC-Car-ML

Fisrly, For serial communication between arduino and host computer inspred by http://thelivingpearl.com/cgi-sys/suspendedpage.cgi
Secondly, Testing your RC car from your keyboard run car_control.py on python shell or correspoinding interface on your computer and test your car be carreful abour boudrate on the arduino code and python code should be same!!!
Third, you can test ultrasonic inputs and video inputs run  by correspoinding files ultrasonic_data_test.py and video__test.py. Firstly run your codes on host computer then  in  raspberry pi run distance.py and video.py codes. Obtain your results on server computer.
For 3D reconstruction and image processing Raspberry pi camera needs calibration pelase follow instruction  for  more information on https://docs.opencv.org/2.4/doc/tutorials/calib3d/camera_calibration/camera_calibration.html find some couples photoes for chessboard and put them on the illustrated file which you will call this file on picam_calibration.py code. This values will be used  self-driving.py 
For collecting data that will be used in the NN firstly run data_collecting.py codes on host computer and run video.py on your raspberry pi. Drive your rc car using keyboard and collect data. (Datas will be save if and only if when there is a key press action). Please press q whrn you fisnih driving.Datas will be saved on .npz format 
For NN taining firstly Run NN_training.py and  depend on the parameters chosen, it will take some time to train. After training, model will be saved in “mlp_xml” folder. 
For stop sign and traffic lamp trained datas has been uploaded. You can use them easily. 
for self driving firstly run self-driving.py on your host computer, then, distance .py and video.py on your raspberry pi. now you are ready Self Driving 


Video : https://www.youtube.com/watch?v=skb1Gg1UJPY
