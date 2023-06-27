import matplotlib.pyplot as plt 
#import matplotib.pyplot module assigns it the name 'plt' it is a popular library in python

# Data collection
#distance list represents the distances from the lawn mower in meters, 
#and the sound_intensity list represents the sound intensity levels in decibels (dB) corresponding to each distance.
distance = [1, 2, 3, 4, 5]  # Distance from the lawn mower in meters
sound_intensity = [80, 75, 70, 65, 60]  # Sound intensity levels in decibels (dB) at each distance

# Data analysis
#These lines plot the data collected. plt.plot() creates a line plot with the distance on the x-axis and sound_intensity on the y-axis. 
#The marker='o' argument adds circular markers to the data points. plt.xlabel(), plt.ylabel(), and plt.title() set the labels for the x-axis, y-axis, and the title of the plot, respectively.
#plt.grid(True) adds a grid to the plot. Finally, plt.show() displays the plot on the screen.
plt.plot(distance, sound_intensity, marker='o')
plt.xlabel('Distance (m)')
plt.ylabel('Sound Intensity (dB)')
plt.title('Sound Intensity of Lawn Mower')
plt.grid(True)
plt.show()

# Calculate sound reduction levels needed for the simulation
#calculates the sound reduction levels needed for the simulation. It subtracts each intensity value in sound_intensity from the maximum intensity value in the list using a list comprehension.
#The resulting reduction levels are stored in the reduction_levels list.
reduction_levels = [max(sound_intensity) - intensity for intensity in sound_intensity]

print("Sound Reduction Levels:")
for distance, reduction in zip(distance, reduction_levels):
    print(f"At {distance} meters: {reduction} dB")
