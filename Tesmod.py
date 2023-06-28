import tkinter as tk

class SimulationGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Glass Building Sound Reduction Simulation")
       
        # Create GUI elements
        self.building_canvas = tk.Canvas(self.window, width=600, height=400, bg="white")
        self.building_canvas.pack(side=tk.LEFT)
       
        self.mower_label = tk.Label(self.window, text="Lawn Mower")
        self.mower_label.pack()
       
        self.sound_label = tk.Label(self.window, text="Sound Level:")
        self.sound_label.pack()
       
        self.sound_meter = tk.Scale(self.window, from_=0, to=100, orient=tk.HORIZONTAL)
        self.sound_meter.pack()
       
        self.start_button = tk.Button(self.window, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack()
       
        self.stop_button = tk.Button(self.window, text="Stop Simulation", command=self.stop_simulation, state=tk.DISABLED)
        self.stop_button.pack()
       
        # Simulation variables
        self.simulation_running = False
       
    def start_simulation(self):
        self.simulation_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
       
        # Code for starting the simulation goes here
       
    def stop_simulation(self):
        self.simulation_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
       
        # Code for stopping the simulation goes here
       
    def run(self):
        self.window.mainloop()

# Create an instance of the SimulationGUI class and run the GUI
simulation_gui = SimulationGUI()
simulation_gui.run()
