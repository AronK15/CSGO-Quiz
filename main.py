from tkinter import *
import random
asked =[]
names_list = []
score = 0

global questions_answers


questions_answers = {
    1: ["How much does an AWP cost?", 
        '$4750', 
        '$2',
        '$5750', 
        '$3500', 
        '$4750' 
        ,1], 
    2: ["How much does a Desert Eagle cost?", 
        '$1337', 
        '$700',
        '$2350', 
        '$1700', 
        '$700' 
        ,2], 
    3: ["How long does it take to defuse a bomb with a defuse kit?", 
        '10 seconds', 
        '3 seconds',
        '7 seconds', 
        '5 seconds', 
        '5 seconds' 
        ,4],
     4: ["How long does it take to plant a bomb?", 
        '10 seconds', 
        '5 seconds',
        '4 seconds', 
        '2 seconds', 
        '4 seconds' 
        ,3],
     5: ["How many pistols does T-side have?", 
        '8 pistols', 
        '6 pistols',
        '7 pistols', 
        '5 pistols', 
        '6 pistols' 
        ,2],
     6: ["How much does CZ75-Auto?", 
        '$500', 
        '$750',
        '$300', 
        '$450', 
        '$500' 
        ,1],
    7: ["How much does a kevlar cost?", 
        '$750', 
        '$650',
        '$500', 
        '$550', 
        '$650' 
        ,2],
    8: ["How many grenades are in the game?", 
        '6', 
        '7',
        '4', 
        '5', 
        '6' 
        ,1],
    9: ["How long is the third competitive cooldown?", 
        '30 minutes', 
        '12 hours',
        '24 hours', 
        '2 hours', 
        '24 hours' 
        ,3],
    10: ["What is the cost of an AWP + Kevlar + Deagle?", 
        '$6100', 
        '$5000',
        '$5750', 
        '$6750', 
        '6100' 
        ,1],


        
}
def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
      asked.append(qnum)
  elif qnum in asked:
      randomiser()

class QuizStarter:
  def __init__(self, parent):
      background_color="dodgerblue"

      #frame set up
      self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
      self.quiz_frame.grid()

      #Label widget for our heading
      self.heading_label = Label (self.quiz_frame, text = "CSGO Quiz", font = ("Arial", "18", "bold"), bg = background_color)
      self.heading_label.grid(row = 0, pady = 20)

      #Label for user name prompt
      self.user_label = Label (self.quiz_frame, text = "Please enter your name below", font = ("Arial", "16"), bg = background_color)
      self.user_label.grid(row = 1, pady = 20)

      #users input is taken by Entry Widget
      self.entry_box = Entry(self.quiz_frame)
      self.entry_box.grid(row = 2, pady = 20)

      #continue Button
      self.continue_button = Button (self.quiz_frame, text = "Continue", bg = "cyan", command = self.name_collection)
      self.continue_button.grid(row = 3, pady = 20)

  def name_collection(self):
      name = self.entry_box.get()
      names_list.append(name)
      print(names_list)
      self.quiz_frame.destroy()
      Quiz(root)
      
      
class Quiz: 


    def __init__(self, parent):
      background_color="dodgerblue"

      #frame set up
      self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
      self.quiz_frame.grid()

      randomiser()

      #Label widget for our heading
      self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font = ("Tw cen MT", "15", "bold"), bg = background_color)
      self.question_label.grid(row = 0)


      #Holds the value of radio buttons
      self.var1=IntVar()

    
      
      self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value = 1, variable=self.var1, pady=10)
      self.rb1.grid(row=2)

      self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value = 2, variable=self.var1, pady=10)
      self.rb2.grid(row=3)

      self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value = 3, variable=self.var1, pady=10)
      self.rb3.grid(row=4)

      self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value = 4, variable=self.var1, pady=10)
      self.rb4.grid(row=5)

      self.confirm_button= Button(self.quiz_frame, text="Confirm", font=("Helvetica", "13", "bold"), bg="cyan", command=self.test_progress)
      self.confirm_button.grid(row=7, padx=5, pady=5)

      self.score_label=Label(self.quiz_frame, text="Score", font=("Tw Cen MT","16"), bg=background_color,)
      self.score_label.grid(row=8, padx=10, pady=1)



    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])
        self.rb4.config(text=questions_answers[qnum][4])


    def test_progress(self):
        global score
        scr_label = self.score_label
        choice = self.var1.get()
        if len(asked)>9:#if it is the last question
            if choice==questions_answers[qnum][6]:#if last question is right answer
              score +=1
              scr_label.configure(text=score)
              self.confirm_button.config(text="confirm")
              self.end_frame()
            else: #is last question is wrong answer
                score+=0
                scr_label.config(text="The correct answer was " + questions_answers[qnum][5])
                self.confirm_button.config(text="Confirm")
                self.end_frame()
        else:#If its not last question
            if choice==0:#check if user has made a choice
                self.confirm_button.configure(text="Try Again Please, You Didn't Select Anything ")
                choice==self.var1.get()
            else:#If they made a choice and its not last question
              if choice==questions_answers[qnum][6]:#If their choice is right
                score +=1
                scr_label.configure(text=score)
                self.confirm_button.config(text="Confirm")
                self.questions_setup()#run this method to move to next question
              else:
                score +=0
                scr_label.configure(text="The Correct Answer Was: " + questions_answers[qnum][5])
                self.confirm_button.configure(text="Confirm")
                self.questions_setup()

    def end_frame(self):
      root.withdraw()
      name=names_list[0]
      file=open("LeaderBoard.txt","a")
      file.write(str(score))
      file.write(" - ")
      file.write(name+"\n")
      file.close()

      inputFile = open("LeaderBoard.txt", "r")
      lineList = inputFile.readlines()
      lineList.sort()
      top=[]
      print(top)
      top5=(lineList[-5:])
      for line in top5:
          point=line.split(" - ")
          top.append((int(point[0]), point[1]))
      file.close()
      top.sort()
      top.reverse()
      return_string=""
      for i in range(len(top)):
            return_string +="{} - {}\n".format(top[i][0], top[i][1])
      print(return_string)

      open_endscrn=End()
      open_endscrn.listLabel.config(text=return_string)

class End:
      def __init__(self):
          background="dodgerblue"
          self.end_box= Toplevel(root)
          self.end_box.title("End Box")

          self.end_frame = Frame (self.end_box, width=1000, height=1000, bg=background)
          self.end_frame.grid()

          end_heading = Label (self.end_frame, text='Thank you for completing the quiz!', font=('Tw Cen MT', 22, 'bold'), bg=background, pady=15)
          end_heading.grid(row=1)

          exit_button = Button (self.end_frame, text='Exit', width=10, bg="cyan",font=('Tw Cen MT', 12, 'bold'),command=self.close_end)
          exit_button.grid(row=4, pady=20)
          self.listLabel = Label (self.end_frame, text="1st Place Available", font=('TW Cen MT',18), width=40, bg=background, padx=10, pady=10)  
          self.listLabel.grid(column=0, row=2)

          self.quit= Button(self.end_frame, text="Quit", font=("Helvetica", "13", "bold",))

      def close_end(self):
            self.end_box.destroy()
            root.destroy()       
 


#***************Starting point of program******************#
randomiser()
if __name__ == "__main__":
  root = Tk()
  root.title("CSGO Quiz")
  quizStarter_object = QuizStarter(root)
  root.mainloop()#so the window won't disappear 
  