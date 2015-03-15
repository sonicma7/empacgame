G.l.a.s.s. B.r.e.a.k.e.r.

Jeremy Therrien,
Mark Aversa,
Evan Slaughter,
Ryan Michaels,
James deWitt

**I. Artist Statement/Philosophy/The WHY Factor (why create this game? why would someone want to play it?)** - Ever feel frustrated with the new EMPAC building? Why not use the money you pay to go here on something useful? Well now you can take out your frustration on EMPAC in the game G.l.a.s.s. B.r.e.a.k.e.r. and break the windows of that annoying building.

**II. Predecessor or previous games/ distinctive factors in this genre** - A very popular game that is similar in gameplay is Rampage. Rampage is a 1980's arcade game in which the player controls various gigantic monsters and smashes, rips apart, and reduces buildings to rubble. Distinctive factors include fast paced, time-trial style levels where the character is pressured to complete by various enemies. Also, the game has a bit of strategy, where if they make wrong moves and smash the wrong windows, they can essential lock themselves in a corner with no escape.

**III. Target Audience** – The target audience is RPI students. Specifically any who have made the observation that EMPAC’s windows would be a target for rock throwers or just want to vent their frustration about the perceived waste of money spent on EMPAC.

**IV. Introduction & Story** - In G.l.a.s.s. B.r.e.a.k.e.r. you play as an RPI student whose goal is to climb and break the windows of EMPAC. With tuition rates constantly rising what better way to take out your frustration then breaking some windows.

**V. Immediate and long term projected socio/cultural project impact** - The immediate impact the game will have on society is the visible dissatisfaction with the EMPAC complex.  Students will be able to show their dislike for the building by playing this game and the more they play it the more it will show they dislike EMPAC.

Long term impact may be much more devastating to the actual EMPAC building.  Games sometimes give already disturbed people bad ideas and this may be the case.  A student who has been plotting some way to harm EMPAC may see this game as an inspiration.  On the other hand, if the game becomes popular among students, RPI administrators may ask for student input in future construction projects to avoid the backlash that they have faced.


**VI. Delivery System & Requirements** - The game requires the Pygame ending (1.8.1 Release) and Python (version 2.5-2.6).

**VII. Interface** - The interface of G.l.a.s.s. B.r.e.a.k.e.r. is very minimal. There is a HUD which displays the amount of money you are costing the school in window repair and replacement. A weapon bar is placed in the upper left hand corner, which displays which weapon you have equipped and also if and what other weapons you are carrying. Your health is indicated by ring around your weapon bar.

**VIII. User Interaction** - The player moves around using the W, A, S, D keys to move up, left, down, and right accordingly. Up, down, left and right attack the corresponding windows. Using the space bar, and then W, A, S or D, will cause the player to jump over one mirror in the corresponding direction. This is useful because players cannot move onto broken windows, but they are able to jump over broken windows to other intact windows.

**IX. The World Layout** - The world that the user sees is a simple landscape. The background shows EMPAC from the side. This is all the player can go to.  Different levels incorporate the background to different goals but the location remains the same. The player can however infer that the larger world outside of the level is there. The police/public safety officers march onto the screen from somewhere, presumably from campus or a central office.

**X. Level Design** - The main space that the player can travel on is the glass face of EMPAC. They can only travel on the window pane spaces. The police/public safety officers travel only on the ground and on the roof of the building. The interesting part about the level design is that the building is built on a slope, so the player and the ground-bound officers have to follow the slope of the ground. This makes movement more difficult for the player at that section of the level.

**XI. Visualization - characters, flow charts** - Ryan

**XII. Music/ Sound Design** – The main sounds are suction cup popping sounds when the player moves the character, glass breaking and tinkling sounds when a window is broken, whooshing sounds when a projectile is thrown and police sirens. The game could also have a generic ambient music loop in the background.

**XIII. Rules and Gameplay A. Setup, B. Gameplay, C. Scoring** - The player’s starting position is a randomly selected window.

The goal of the game is to move around from window to window while avoiding public safety as they try to stop the player. The more windows the player breaks the higher their score will be. If a player gets trapped or public safety hits them enough times, the game ends.

The players score is the cost to replace a window x percent damage done.

**XIV. Program Structure** - Written in python. Screens organized in a stack. Each Screen is a Layer and is managed by a layer manager.  Each Screen calls the creation of classes that are placed onto that screen. Each class contains: HandleEvent, Update, and Render functions to be called by the screen. Every different entity will have its own file and class.

Template:
import layermanager
class Template(layermanager.Layer):
> def init(self,screen):
> > layermanager.Layer.init(self)


> def HandleEvent(self, event):
> > pass


> def Update(self):
> > pass


> def Render(self, screen):
> > pass

**XV. Technical Specs: Physics, Rendering System, Lighting Models** - Game will be 2D using Pygame.

**XVI. Implementation** - This game has a simple implementation: 2D world, 4-way movement, and simple AI.

**XVII. Production Timeframe** - The timeframe to complete this game would be between 1 and 2 months. Basic prototype in 2 weeks, cleaned-up Beta in 1 month, then anywhere between 1-2 weeks of play-testing and balancing. Basic art assets would be completed by the 2-week mark, with full animations completed within 4-6 week mark.

**Contribution**

Jeremy - temporary art, game framework, player control and movement, background

Mark - enemy AI, temporary art

James - Background and window design

Ryan - player character animations

Evan - balloon and enemy animations

All members contributed to the Game Design Document