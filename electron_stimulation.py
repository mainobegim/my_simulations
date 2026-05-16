# ------------IMPORTS--------------------
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import math

# -----------CONSTANTS------can be changed to experiment--------------
NUM_ELECTRONS = 40      #number of electrons in the wire
WIRE_WIDTH = 2.0        #height of the wire 
DRIFT_SPEED = 0.03      #speed of the electrons when voltage is on

#---------ELECTRON CLASS------------------
class Electron:
    def __init__(self):
        self.x = random.uniform(0, 10)  #random position
        self.y = random.uniform(-WIRE_WIDTH/2, WIRE_WIDTH/2)

        # Giving it a small random velocity which is thermal motion
        speed = random.uniform(0.02, 0.08)
        angle = random.uniform(0, 2 * math.pi)  #random direction in radians
        self.vx = speed * math.cos(angle)
        self.vy = speed * math.sin(angle)

    def move(self, voltage_on):
        
        # ----THERMAL MOTION----always happening
        # When electrons bump into atoms and change direction a bit it represents atomic collisions in the metal
        self.vx += random.uniform (-0.01, 0.01)
        self.vy += random.uniform (-0.01, 0.01)
        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed > 0.12: 
            self.vx, self.vy = self.vx/speed*0.12, self.vy/speed*0.12

        # ------DRIFT VELOCITY (only when voltage applied)
        # When voltage is on electrons get a slight push to the right 
        # The directed motion is what created the current, so it is the net drift 
        if voltage_on:
            self.vx += DRIFT_SPEED * 0.1 #gets a small but consistent push
        
        # ----KEEP ELECTRONS INSIDE THE WIRE----
        # If an electron hits the wall of the wire bounce it back
        if self.y > WIRE_WIDTH/2:
            self.y = WIRE_WIDTH/2
            self.vy = -abs(self.vy)     # reverse vertical speed
        
        if self.y < -WIRE_WIDTH/2:
            self.y = -WIRE_WIDTH/2
            self.vy = abs(self.vy)

        # -----WRAP AROUND LEFT/RIGHT ---
        self.x += self.vx
        self.y += self.vy

        if self.x > 10:
            self.x = 0    #current leaves the wire and comes back from left
        if self.x < 0:
            self.x = 10


# ----CREATE ALL ELECRTONS ----------------------
electrons = [Electron() for _ in range(NUM_ELECTRONS)]
# This line is the same as writing:
#     electrons[]
#     for i in range (NUM_ELECTRONS):
#         electrons.append(Electron())

# ----INITIAL STATE-----------------
voltage_on = False          # start with votage OFF

#---SET UP THE FIGURE------------------------------
fig, ax = plt.subplots(figsize=(11, 4))
fig.patch.set_facecolor("#0F172A")          # background
ax.set_facecolor("#0F172A")

# Wire boundary lines
ax.axhline(y= WIRE_WIDTH/2, color= "#60A5FA", linewidth= 1.5, alpha= 1)
ax.axhline(y= -WIRE_WIDTH/2, color= "#60A5FA", linewidth= 1.5, alpha= 1)

# Fixed positive ions in the copper wire, these ions dont move like electrons do
for ix in range (1, 10):
    for iy in [-0.8, 0, 0.8]:
        ax.plot(ix, iy, '+', color="#60A5FA", markersize=8, alpha=0.4)

# Electron dots
scatter = ax.scatter(
    [e.x for e in electrons],
    [e.y for e in electrons],
    s=60, color="#FF6B6B", zorder=5, alpha=0.85
) 

# Labels
ax.set_xlim(0, 10)
ax.set_ylim(-1.4, 1.8)
ax.set_xticks([])
ax.set_yticks([])
ax.spines[['top','bottom','left','right']].set_visible(False)

title = ax.text(
    5, 1.65,
    'Voltage OFF - electrons start drifting randomly - no current',
    color= '#c2d2ca', fontsize=9, ha= 'center'
)

instruction = ax.text( 
    5, 1.35,
    'Press SPACE to turn on Voltage',
    color="#607269", fontsize=9, ha='center'
)
 
voltage_label = ax.text(
    5, -1.25,
    '',
    color="#07FF83", fontsize=10, ha='center', fontweight='bold'
)


#----ANIMATION FUNCTION---------------
def update(frame):
    for e in electrons:
        e.move(voltage_on)

    # Update the scatter plot with new positions
    scatter.set_offsets([[e.x, e.y] for e in electrons])

    # Update the title and label based on voltage state
    if voltage_on:
        title.set_text('Voltage ON - electrons start drifting to the right - this is current')
        title.set_color('#4fcf8a')
        voltage_label.set_text('net electron drift  - concentional current flows')
    else:
        title.set_text('Voltage OFF - electrons start drifting randomly - no current')
        title.set_color("#c2d2ca")
        voltage_label.set_text('') 

    return scatter, title, voltage_label


# --------KEYBOARD CONTROL-----------
def on_key(event):
    global voltage_on
    if event.key == ' ':
        voltage_on = not voltage_on

fig.canvas.mpl_connect('key_press_event', on_key)

# -------RUN THE ANIMATION-----------------
anim = animation.FuncAnimation(
    fig,
    update,
    interval = 33,
    blit=True,
    cache_frame_data=False
)

plt.tight_layout()
plt.show() 