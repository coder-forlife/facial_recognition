import face_recognition
import cv2
from tkinter import *
from tkinter import messagebox

win=Tk()
password=StringVar()



#loading faces and names from image files
def load_known_faces(image_paths,names):
    known_face_encodings = []
    known_names = []
    #image_path is a number
    for image_path, name in zip(image_paths,names):
        image= face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        known_face_encodings.extend(face_encodings)
        known_names.extend([name] * len(face_encodings))
    return known_face_encodings,known_names


#recognize faces
def recognize_faces(video_capture, known_face_encodings, known_names):
    while True:
        #get each from from the video stream
        ret, frame = video_capture.read()
        if not ret:
            break

        # find all face locations
        face_locations = face_recognition.face_locations(frame)

#????????
        for face_place in face_locations:
            top, right, bottom, left = face_place

            #current face
            face_encoding = face_recognition.face_encodings(frame,[face_place])[0]
            #compare with known faces
            matches= face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.6)
            name="Unknown"
            #if a match is found, use the first known name
            if True in matches:
                first_match_index = matches.index(True)
                name=known_names[first_match_index]
                messagebox.showinfo("","LOGIN Successful")
            else:
                messagebox.showinfo("","LOGIN Unsuccessful")    
            print("Recognized Name:", name)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)


        cv2.imshow('Video',frame)
            

# Release the video capture object and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

def Login():
    global password
    global video_capture
    global known_face_encodings, known_names
    password=E1.get()
    if(password=="password"):
        #something happens

        #run face recognition on the live video stream
        recognize_faces(video_capture, known_face_encodings, known_names)


    else:
        #nothing happens
        messagebox.showinfo("","LOGIN Unsuccessful")




# open gui
L1=Label(win,text="This is the GUI")
L1.place(x=10,y=40)
E1=Entry(win)
E1.place(x=120,y=40)
#open camera, 0 is the default camera
video_capture = cv2.VideoCapture(0)

#run the code
person_image_paths = ["Image/srk(1).jpeg","Image/srk(2).jpg","Image/srk(3).jpg"]
person_names = ["Shah Rukh Khan","Shah Rukh Khan","Shah Rukh Khan"]


#load known faces
known_face_encodings, known_names = load_known_faces(person_image_paths, person_names)



login=Button(win,text="Login",command=Login)
login.place(x=120,y=120)

win.mainloop()
















