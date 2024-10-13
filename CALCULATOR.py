from tkinter import *
top= Tk ()
top.geometry("500x400")
c= Canvas
frist_no=second_no=operator=None
def digit(digit):
   cr=rl['text']
   new=cr+str(digit)
   rl.config(text=new)

def clear():
   rl.config(text=" ")

def getno(op):
   global frist_no,operator
   frist_no=int(rl['text'])
   operator=op
   rl.config(text='')

def get_res():
   global frist_no,second_no,operator
   second_no=int(rl['text'])
   if operator=='+':
      rl.config(text=str(frist_no+second_no))
   elif operator=='-':
      rl.config(text=str(frist_no-second_no))
   elif operator=='*':
      rl.config(text=str(frist_no*second_no))
   else :
      if second_no==0:
         rl.config(text='Error')
      else:
         rl.config(text=str(frist_no/second_no))

wind=Tk()
wind.title("Calculater")
wind.geometry("280x400")
wind.resizable(0,0)
wind.configure(background='black')


rl = Label(wind,text='',bg='black',fg='white')
rl.grid(row=0,column=0,columnspan=15,pady=(50,20),sticky='w')
rl.config(font=('verdana',30,'bold'))

b7=Button(wind,text='7',bg='#00a65a',fg='white',width=5,height=2,command=lambda :digit(7))
b7.grid(row=1,column=0,)
b7.config(font=('verdana',14))

b8=Button(wind,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda :digit(8))
b8.grid(row=1,column=1,)
b8.config(font=('verdana',14))

b9=Button(wind,text='9',bg='#00a65a',fg='white',width=5,height=2,command=lambda :digit(9))
b9.grid(row=1,column=2,)
b9.config(font=('verdana',14))

ba=Button(wind,text='+',bg='#00a65a',fg='white',width=5,height=2,command=lambda :getno('+'))
ba.grid(row=1,column=3,)
ba.config(font=('verdana',14))

b4=Button(wind,text='4',bg='#00a65a',fg='white',width=5,height=2,command=lambda :digit(4))
b4.grid(row=2,column=0,)
b4.config(font=('verdana',14))

b5=Button(wind,text='5',bg='#00a65a',fg='white',width=5,height=2,command=lambda :digit(5))
b5.grid(row=2,column=1,)
b5.config(font=('verdana',14))

b6=Button(wind,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda :digit(6))
b6.grid(row=2,column=2,)
b6.config(font=('verdana',14))


ba=Button(wind,text='-',bg='#00a65a',fg='white',width=5,height=2,command=lambda :getno('-'))
ba.grid(row=2,column=3,)
ba.config(font=('verdana',14))

b3=Button(wind,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda :digit(3))
b3.grid(row=3,column=0,)
b3.config(font=('verdana',14))

b2=Button(wind,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda :digit(2))
b2.grid(row=3,column=1)
b2.config(font=('verdana',14))

b1=Button(wind,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda :digit(1))
b1.grid(row=3,column=2)
b1.config(font=('verdana',14))

ba=Button(wind,text='%',bg='#00a65a',fg='white',width=5,height=2,command=lambda :getno("%"))
ba.grid(row=3,column=3,)
ba.config(font=('verdana',14))


bclr=Button(wind,text='C',bg='#00a65a',fg='white',width=5,height=2,command=lambda :clear())
bclr.grid(row=4,column=0,)
bclr.config(font=('verdana',14))

b2=Button(wind,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda :digit(0))
b2.grid(row=4,column=1)
b2.config(font=('verdana',14))

b1=Button(wind,text='=',bg='#00a65a',fg='white',width=5,height=2,command=get_res)
b1.grid(row=4,column=2)
b1.config(font=('verdana',14))

b7=Button(wind,text='/',bg='#00a65a',fg='white',width=5,height=2,command=lambda :getno('/'))
b7.grid(row=4,column=3,)
b7.config(font=('verdana',14))



mainloop()

