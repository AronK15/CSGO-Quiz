from tkinter import *

names_list = []

global questions_answers


questions_answers = {
    1: ["How much does an AWP cost?", 
        '$4750', 
        '$2',
        '$5750', 
        '$3500', 
        '$4750' 
        ,1], 
    2: [] 
    
}



class QuizStarter:
  def __init__(self, parent):
      background_color="dodgerblue"

      self.bg_image = Image
      #frame set up
      self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
      self.quiz_frame.grid()

      #Label widget for our heading
      self.heading_label = Label (self.quiz_frame, text = "CSGO Quiz", font = ("Arial", "18", "bold"), bg = 'cyan')
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
      
    







#***************Starting point of program******************#
if __name__ == "__main__":
  root = Tk()
  root.title("CSGO Quiz")
  quizStarter_object = QuizStarter(root)
  root.mainloop()#so the window won't disappear 
  