from Tkinter import *
import matplotlib.pyplot as plt


# The main screen to hold all the graph controls
class GraphScreen:
	def __init__(self,master,figure):
		
		frame = Frame(master)
		frame.pack()

		# we'll have some buttons for controlling things
		self.x_min = Entry(frame)
		self.x_min.insert(0, str(plt.axis()[0]))
		self.x_min.pack(side=LEFT)

		self.x_max = Entry(frame)
		self.x_max.insert(0, str(plt.axis()[1]))
		self.x_max.pack(side=LEFT)

		# add a list of axes to work with
		self.axes_radio = IntVar();
		for a in range(len(fig.get_axes())):
			Radiobutton(frame, text=str(a), variable=self.axes_radio, value=a).pack(anchor=W)
		self.axes_radio.set(0)

		self.replot_button = Button(frame, text="Replot", command=self.replot)
		self.replot_button.pack(side=LEFT)

		self.quit_button = Button(frame, text="QUIT", command=frame.quit)
		self.quit_button.pack()

	def replot(self):
		
		xmin = float(self.x_min.get())
		xmax = float(self.x_max.get())

		fig = plt.gcf()
		axis = fig.get_axes()[self.axes_radio.get()]
		axis.set_xlim([xmin,xmax])

		plt.draw()


