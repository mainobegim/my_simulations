import tkinter as tk

#create the main window
#Tk() is a class and window is the object
window = tk.Tk()
window.title("My EEE Notebook")
window.geometry('900x600')
window.configure(bg="#1e1e1e")

#sidebar frame inside window(parent)
sidebar = tk.Frame(window, bg="#252526", width=200)
#pack() - dispalys the object by geometrically positioning it
sidebar.pack(side='left', fill='y')
tk.Label(sidebar, text='My Notebook', bg="#252526", fg="#ffffff",font=('Ariel', 13)).pack(pady=20, padx=16)

#main frame inside window(parent)
main = tk.Frame(window, bg="#1e1e1e")
main.pack(side='left', fill='both', expand=True)

#Canvas inside the main frame
canvas = tk.Canvas(main, bg="#1e1e1e")
canvas.pack(side='left', fill='both', expand=True)

#Another frame inside canvas with canvas properties
content_frame = tk.Frame(canvas, bg="#1e1e1e")
canvas.create_window((0, 0), window=content_frame, anchor='nw')

topics = ['Charge', 'Conductors', 'Voltage', 'Current', 'Resistance']

content = {
    "Charge": """Charge is a built-in natural property of all particles that tells how they interact electrically. For example, electrons are negatively charged so they will attract positively charged particles. Charge determines if the force exists and measures how strong that force is. The bigger the charge, the stronger field it creates around it, making other charged particles nearby feel a stronger force.
Charge is measured in Coulombs (C). One electron carries −1.6 × 10⁻¹⁹ C. This is constant for any electron in the universe.
Formula: Q = n × e — where n is the number of electrons and e is the charge of one electron.
Free electrons: An electron in the outermost shell of an atom with weak attraction to the nucleus (due to distance) can break out and move freely through the material. This is what makes metals metals.
""",
    "Conductors": """Conductors are materials that allow current to flow easily through them. They are made up of atoms that donate their free electrons simultaneously, creating a “sea of electrons.” These electrons no longer belong to a single atom — they are shared throughout the material.
As each atom donates one electron it becomes positively charged, turning into a positive ion. Its position is fixed in the lattice while the free electrons move freely in the gaps between them. When voltage is applied, these free electrons flow in a specific direction, creating current.
Interestingly, even though each atom loses one electron and becomes unbalanced, the total number of ions and free electrons remains equal — so electrical balance is preserved, just distributed differently.
Insulators
Insulators are the opposite of conductors — they don’t allow current to flow. The atoms they are made of have a stable outermost shell that sits close to the nucleus, making the attraction force stronger and preventing electrons from escaping.
There is a large energy gap between where electrons sit and where they need to be to move freely. This is called the band gap. Because of this, there is nothing available to carry current, even when voltage is applied.
Key takeaway: Electrons can break free when (1) they are far from the nucleus — because distance weakens attraction — or (2) the outer shell is only partially filled, because incomplete shells are unstable.
Semiconductors
Semiconductors have a band gap in the middle and can act as either a conductor or insulator depending on energy. With no energy applied they behave like insulators — electrons in the outer shell don’t have enough energy to move. When energy is applied, some electrons gain enough to cross the band gap and move freely.
When an electron breaks free it leaves a hole behind in the lattice. Another electron fills that hole, leaving its own hole — and so on. The hole appears to move in the opposite direction to the electrons. This behavior is the foundation of transistors.
""",
    "Voltage": """In a battery, the chemicals are intentionally picked so that one electrode is more reactive than the other, which creates a difference. A good analogy is a filled container that has more mass — instead of electrons — which causes more pressure inside it. When a pipe is connected, the pipe has low pressure, creating a difference in pressure. Thanks to that difference, water can flow from high to low pressure. In a battery, that pressure is called voltage. Voltage provides a push to the electrons, which allows the free electrons to flow in one direction.
Voltage is also called potential difference because it tells how much work can potentially be done by a circuit. Going back to the water analogy — if two lakes are at the same level, there is no potential to do work. But if one lake is raised higher than the other, this creates the potential to do work, so the water can now flow. The higher the voltage, the higher the current in a circuit, leading to higher brightness in a lamp because more electrons are flowing per second.
What is one volt? One volt means one joule of energy per coulomb of charge.
Formula: V = W / Q — where V is voltage in volts, W is energy in joules, and Q is charge in coulombs.
""",
    "Current": """Voltage causes current by providing a push for the electrons. The free electrons now have enough energy to drift in one direction through the circuit. This drift creates a flow of free electrons and creates current. Every second, one coulomb of charge — which is tons of electrons — flows, and the rate at which they flow is measured in amperes. As the voltage is higher, more electrons are flowing per second, which increases the rate of flow, or the current, meaning more charge is delivered to the lamp every second, making and keeping it brighter. However, when the rate of flow decreases, the lamp receives less charge per second, making it dimmer.
An analogy can be a queue of people in a shop — if the cashier works faster, he can serve more people per minute, but if he's slow, fewer people get served per minute.
Current depends mainly on how many electrons flow per second, not on how fast any individual electron travels — speed can be very low but current can still be high because of the sheer number of electrons. More voltage leads to more electrons travelling per unit of time, so the rate increases, giving a faster rate of flow of free electrons because they have more energy to move and more electrons flow every second.
Formula: I = Q / t — where I is current in amperes, Q is charge in coulombs, and t is time in seconds.
""",
    "Resistance": """Resistance is the opposition to the flow of electrons in a circuit. It plays an important role because it prevents components like a lamp or LED from burning out due to high current — resistance makes fewer electrons flow every second.
Resistance also produces heat directly, because it causes more collisions between electrons and the fixed ions in the lattice, and each collision transfers energy as heat. Thinner and longer wires have higher resistance and heat up faster, because the electrons encounter more obstacles and collide with more ions along the way.
Ohm’s Law
In a circuit with a fixed resistor, when voltage is increased, current also increases, because more push means more electrons flow per second. When less voltage is applied, fewer electrons flow per second, decreasing current. Similarly, for a fixed voltage, increasing resistance decreases current, because more collisions slow the electrons down.
“Fixed resistor” is emphasized because Ohm’s law assumes resistance stays constant — if resistance also changes, current depends on both changes together, not on voltage alone.
Formula: V = I × R — where V is voltage in volts, I is current in amperes, and R is resistance in ohms (Ω)."""
}

def show_topic(topic):
    for label in main.winfo_children():
        label.destroy()
    

    tk.Label(main, text=topic, bg='#1e1e1e', fg='#ffffff', font=('Arial', 20)).pack(pady=20)
    tk.Label(main, text=content.get(topic, "coming soon..."), bg='#1e1e1e', fg='#aaaaaa', font=('Arial', 12), wraplength=600, justify="left").pack(pady=10)


for topic in topics:
    label = tk.Label(
        sidebar, 
        text=topic, 
        bg='#252526',
        fg='#aaaaaa',
        font=('Arial', 11),
        padx=16,
        pady=8,
        anchor='w')
    label.pack(fill='x')
    label.bind("<Button-1>", lambda e, t=topic: show_topic(t))



#shows the window as a loop
window.mainloop() 