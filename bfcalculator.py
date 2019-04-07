#Import tkinter
from tkinter import *
from tkinter import messagebox

try:
    #Import solve and Symbol from sympy
    from sympy.solvers import solve
    from sympy import Symbol
except ImportError:
    print("Unable to import SymPy. Please install SymPy"
    " before running application")
    quit()


#Function for input calculations
def calculation():
    weight = scale1.get()                       #Current weight
    bf_percent = scale2.get()/100               #Current bf%
    goal_bfp = scale3.get()/100                 #Goal bf%
    current_bf = weight * bf_percent            #Current body fat in lbs

    #Creates a Symbol for later equation
    x = Symbol('x')

    bf_to_lose = 0                              #BF to lose to reach bf% goal
    eq = 0                                      #Equation to calculate bf to lose

    day_count = 0                               #Days to reach bf% goal

    total_calories = 0                          #Total calories in excess bf

    #If/elif checks to make sure goal bf% is lower than current bf% and that a
    #daily calorie defecit is selected
    if goal_bfp >= bf_percent:
        messagebox.showerror("Error", "Your goal body fat percentage should be "
        "lower than your current body fat percentage")
    elif not 1 <= v.get() < 4:
        messagebox.showerror("Error", "Please select a daily calorie defecit")
    else:
        eq = (current_bf - x)/(weight - x) - goal_bfp       #Equation
        bf_to_lose = solve(eq, x)               #Solves for x (x = bf needed to be lost in order to reach bf% goal)
        bf_to_lose = bf_to_lose.pop(0)          #Solve returns a list; this pops answer (first element) to bf_to_lose

        #1 lbs of fat is about 3500 calories
        total_calories = bf_to_lose * 3500

        #Determines which radio button was selected
        if v.get() == 1:
            day_count = int(round(total_calories/250))
        elif v.get() == 2:
            day_count = int(round(total_calories/500))
        else:
            day_count = int(round(total_calories/1000))

        #Shows results in a messagebox
        messagebox.showinfo("Body Fat Loss Calculator", 'Pounds of fat to lose: {} lbs\n'
        'Days to reach body fat percentage goal: {}*'
        '\n\n\n*Assuming no significant muscle gain/loss'.format(round(bf_to_lose, 2), day_count))

#Creates main window
root = Tk()
root.title('Body Fat Loss Calculator')
root.resizable(width=FALSE, height=FALSE)
root.geometry("350x325")

#Creates a frame
topframe = Frame(root, bg='gray', bd=5, width=300)
topframe.pack(side=TOP)

#Creates a frame
bottomframe = Frame(root, bd=5, bg='gray', width=400, height=50)
bottomframe.pack(side=BOTTOM)

#Exit button
exit_button = Button(bottomframe, text='Exit', width=10, height=1, command=root.destroy)
exit_button.pack(side=RIGHT)

#Calculation button
calc_button = Button(bottomframe, text='Calculate', width=10, height=1, command=calculation)
calc_button.pack(side=LEFT)

#Current weight scale
scale1 = Scale(topframe, from_=80, to=400, orient=HORIZONTAL, label='Current Weight', length=225)
scale1.pack(side=TOP)

#Current body fat percentage scale
scale2 = Scale(topframe, from_=3, to=50, orient=HORIZONTAL, label='Current Body Fat Percentage', length=225)
scale2.pack()

#Goal body fat percentage scale
scale3 = Scale(topframe, from_=3, to=50, orient=HORIZONTAL, label='Goal Body Fat Percentage', length=225)
scale3.pack(side=BOTTOM)

#Label for radio buttons
lbl = Label(root, text='Select daily calorie defecit:')
lbl.pack()

#Set of three radio buttons (Calorie defecits)
v = IntVar()
Radiobutton(root, text='Low (~250)', variable=v, value=1, indicatoron=False).pack(anchor=CENTER)
Radiobutton(root, text='Medium (~500)', variable=v, value=2, indicatoron=False).pack(anchor=CENTER)
Radiobutton(root, text='High (~1000)', variable=v, value=3, indicatoron=False).pack(anchor=CENTER)

root.mainloop()
