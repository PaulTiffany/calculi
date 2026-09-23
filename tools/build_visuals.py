#!/usr/bin/env python3
"""Build the guide's exact, text-accessible SVG diagrams. No inference or network."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "diagrams"
INK, TEAL, RUST, GOLD = "#17384a", "#2b8187", "#b74d32", "#efbb4d"
PALE, BLUE, PAPER = "#e4f2ee", "#8bcce5", "#fffdf7"
manifest = []

class Drawing:
    def __init__(self, name, title, desc, h=300):
        self.name, self.title, self.desc, self.h = name, title, desc, h
        self.parts = []
        self.rect(1, 1, 638, h-2, PAPER, "#d9e1dc", 22, 2)
        self.text(26, 40, title, 27, weight="700")
    def rect(self, x, y, w, h, fill="white", stroke=INK, radius=10, sw=3):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def text(self, x, y, s, size=23, fill=INK, anchor="start", weight="400"):
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{escape(str(s))}</text>')
    def circle(self, x, y, r=24, fill=PALE, stroke=INK, sw=3):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def path(self, d, stroke=INK, fill="none", sw=3, arrow=False, dash=False):
        extra = (' marker-end="url(#arrow)"' if arrow else '') + (' stroke-dasharray="7 6"' if dash else '')
        self.parts.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{extra}/>')
    def line(self, x1, y1, x2, y2, arrow=False, stroke=INK, dash=False):
        self.path(f"M{x1},{y1} L{x2},{y2}", stroke, arrow=arrow, dash=dash)
    def number(self, x, y, n, fill=PALE, r=29):
        self.circle(x, y, r, fill)
        self.text(x, y+9, n, 27, fill=PAPER if fill in (RUST, TEAL) else INK, anchor="middle", weight="700")
    def label(self, x, y, value, w=140, fill=PALE):
        self.rect(x-w/2, y-29, w, 52, fill, "none", 14, 0)
        self.text(x, y+6, value, 23, anchor="middle", weight="600")
    def book(self, x, y, color=TEAL, w=20, h=32):
        self.rect(x, y, w, h, color, INK, 3, 2)
        self.line(x+4, y+5, x+4, y+h-5, stroke=PAPER)
    def crate(self, x, y, size=44):
        self.rect(x, y, size, size, "#f7dfb2", INK, 4, 2)
        self.line(x+4,y+size/3,x+size-4,y+size/3)
        self.line(x+4,y+2*size/3,x+size-4,y+2*size/3)
    def person(self, x, y, color=TEAL):
        self.circle(x,y,22,color)
        self.circle(x-7,y-3,2,INK,"none",0)
        self.circle(x+7,y-3,2,INK,"none",0)
        self.path(f"M{x-6},{y+7} Q{x},{y+13} {x+6},{y+7}")
    def save(self):
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="{self.h}" viewBox="0 0 640 {self.h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(self.title)}</title><desc id="desc">{escape(self.desc)}</desc>
<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L8,4 L0,8" fill="none" stroke="{INK}" stroke-width="2"/></marker></defs>
<g font-family="Arial, Helvetica, sans-serif">{''.join(self.parts)}</g></svg>
'''
        (OUT / (self.name+".svg")).write_text(svg)
        manifest.append({"id": self.name, "title": self.title, "alt": self.desc, "width":640,"height":self.h})

def counters():
    d=Drawing("add-two","One rule: add two","Starting from three, adding two gives five, seven, then nine. All four counts are odd.",240)
    for i,n in enumerate([3,5,7,9]):
        x=80+i*160
        d.number(x,126,n)
        if i<3:
            d.line(x+38,126,x+113,126,True)
            d.text(x+80,101,"+2",23,anchor="middle")
    d.text(320,209,"The starting count and the move both matter.",23,anchor="middle")
    d.save()

def water():
    d=Drawing("water-total","Rate, change, and starting amount","A tank starts with five liters. Two liters per minute for three minutes adds six liters, leaving eleven liters.",310)
    for x,n,label in [(62,5,"Start"),(463,11,"Finish")]:
        d.rect(x,87,106,132,"white",INK,8)
        d.rect(x+5,214-n*10,96,n*10,BLUE,"none",2,0)
        d.path(f"M{x},87 L{x},219 L{x+106},219 L{x+106},87",sw=4)
        d.text(x+53, 76,label,23,anchor="middle")
        d.text(x+53,255,f"{n} liters",27,anchor="middle",weight="700")
    d.line(192,160,438,160,True)
    d.label(315,126,"+6 liters",150)
    d.text(315,199,"2 liters/min",23,anchor="middle")
    d.text(315,227,"× 3 minutes",23,anchor="middle")
    d.save()

def gardens():
    d=Drawing("garden-area","Same fence, different area","A three-by-five rectangle encloses fifteen square meters. A four-by-four square encloses sixteen. Both use sixteen meters of fence.",320)
    for x,w,h,label in [(90,5,3,"3 m × 5 m"),(421,4,4,"4 m × 4 m")]:
        top=104
        d.rect(x,top,w*26,h*26,PALE,TEAL,0,4)
        for i in range(1,w):d.line(x+i*26,top,x+i*26,top+h*26,stroke="#85b2a9")
        for i in range(1,h):d.line(x,top+i*26,x+w*26,top+i*26,stroke="#85b2a9")
        d.text(x+w*13,79,label,25,anchor="middle",weight="700")
        d.text(x+w*13,244,f"{w*h} square meters",23,anchor="middle")
    d.text(320,289,"Each small square is 1 square meter.",23,anchor="middle")
    d.save()

def books():
    d=Drawing("book-counts","The same books, counted each day","Monday has eight books, Tuesday eleven, Wednesday nine, Thursday fourteen. The changes are plus three, minus two, and plus five.",310)
    for i,(day,n) in enumerate([("Mon",8),("Tue",11),("Wed",9),("Thu",14)]):
        x=30+i*160
        d.text(x+50,83,day,24,anchor="middle",weight="700")
        for j in range(n): d.book(x+(j%4)*24,104+(j//4)*36,TEAL if j%2==0 else GOLD,18,28)
        d.text(x+48,283,n,27,anchor="middle",weight="700")
        if i<3:
            d.text(x+129,177,["+3","−2","+5"][i],23,anchor="middle",weight="700")
    d.save()

def badges():
    d=Drawing("badge-logic","A one-way rule","All club members have badges. Jo is shown inside the members group, itself inside badge holders. A possible guest also has a badge, outside the members group.",320)
    d.rect(25,68,590,224,"#fff1ce",GOLD,20)
    d.text(47,102,"People with badges",25,weight="700")
    d.rect(48,126,252,143,PALE,TEAL,18)
    d.text(68,159,"Club members",24,weight="700")
    d.person(102,207)
    d.text(143,215,"Jo",25)
    d.circle(90,230,7,GOLD,INK,2)
    d.person(447,160,RUST)
    d.circle(436,184,7,GOLD,INK,2)
    d.text(447,224,"A guest could",23,anchor="middle")
    d.text(447,254,"have a badge too.",23,anchor="middle")
    d.save()

def selector(first=False):
    name="keep-first" if first else "keep-second"
    title="Use the first input" if first else "Use the second input"
    value="red" if first else "blue"
    d=Drawing(name,title,f"The inputs are red first and blue second. The rule returns {value}. Changing the selected input position changes the result.",270)
    for y,color,label in [(105,RUST,"1st: red"),(195,BLUE,"2nd: blue")]:
        d.number(74,y,"",color,r=23)
        d.text(112,y+8,label,23)
        d.line(221,y,259,150,True)
    d.rect(269,105,166,93,PALE,TEAL,18)
    d.text(352,143,"keep",26,anchor="middle")
    d.text(352,177,"first" if first else "second",26,anchor="middle",weight="700")
    d.line(444,150,493,150,True)
    d.number(554,150,"",RUST if first else BLUE,r=25)
    d.text(554,215,value,26,anchor="middle",weight="700")
    d.save()

def tickets():
    d=Drawing("ticket-contract","Sell one ticket","Four tickets become three when one is sold. A nonnegative count after selling requires at least one ticket beforehand.",270)
    for x,n,label in [(42,4,"Before: 4"),(402,3,"After: 3")]:
        d.text(x,90,label,25,weight="700")
        for j in range(n):d.rect(x+j*39,118,29,64,"#fff1ce",INK,5,2)
    d.line(221,147,374,147,True)
    d.text(296,125,"sell 1",24,anchor="middle")
    d.text(320,232,"Before selling: at least 1 ticket.",25,anchor="middle",weight="700")
    d.save()

def query():
    d=Drawing("book-query","The same books, selected by a rule","Books B1 and B4 match gardening AND available. B2 is available but astronomy; B3 is gardening but unavailable.",322)
    for i,(book,topic,available,match) in enumerate([("B1","Garden",True,True),("B2","Stars",True,False),("B3","Garden",False,False),("B4","Garden",True,True)]):
        x=25+i*154
        d.rect(x,75,128,169,PALE if match else "white",TEAL if match else "#a4afb4",13,4 if match else 2)
        d.text(x+64,107,book,27,anchor="middle",weight="700")
        d.book(x+45,122,TEAL if topic=="Garden" else GOLD,37, 40)
        d.text(x+64,190,topic,22,anchor="middle")
        d.text(x+64,224,"Ready" if available else "Out",23,anchor="middle",weight="700")
        if match:d.text(x+64,273,"MATCH",22,TEAL,anchor="middle",weight="700")
    d.text(320,306,"Gardening AND available",24,anchor="middle")
    d.save()

def deadlock():
    d=Drawing("circular-wait","Both wait; neither lets go","Jo holds the printer and waits for Sam's scissors. Sam holds the scissors and waits for Jo's printer. Their waiting forms a loop.",350)
    d.rect(47,111,194,133,PALE,TEAL,20)
    d.rect(399,111,194,133,"#fbe6de",RUST,20)
    for x,name,tool in [(144,"Jo","printer"),(496,"Sam","scissors")]:
        d.text(x,148,name,29,anchor="middle",weight="700")
        d.text(x,185,"holds",23,anchor="middle")
        d.text(x,220,tool,26,anchor="middle")
    d.path("M144,103 C144,63 496,63 496,103",arrow=True)
    d.rect(217,62,206,28,PAPER,"none",0,0)
    d.text(320, 83,"needs scissors",23,anchor="middle")
    d.path("M496,252 C496,302 144,302 144,252",arrow=True)
    d.rect(217,269,206,28,PAPER,"none",0,0)
    d.text(320,290,"needs printer",23,anchor="middle")
    d.text(320,331,"What could let one person continue?",23,anchor="middle")
    d.save()

def cupboard(poster=False):
    obj="poster" if poster else "cup"
    d=Drawing("cupboard-"+obj,"One action, two kinds of fact",f"Opening the cupboard changes its door from closed to open. The {obj} remains inside in both states.",330)
    for x,opened in [(72,False),(433,True)]:
        d.rect(x,98,122,156,"#f7dfb2",INK,8)
        if poster:
            d.rect(x+35,150,49,65,PAPER,INK,2,2)
            d.circle(x+59,176,10,GOLD,INK,2)
        else:
            d.rect(x+34,181,46,35,PAPER,INK,5,2)
            d.path(f"M{x+80},186 Q{x+102},185 {x+102},198 Q{x+102},212 {x+80},209",sw=3)
        d.line(x+8,220,x+114,220)
        if opened:
            d.path(f"M{x+122},98 L{x+165},119 L{x+165},279 L{x+122},254 Z",fill="#e9c997")
        else:
            d.rect(x+5,103,112,147,"none",TEAL,4,3)
            d.circle(x+101,173,4,GOLD)
        d.text(x+61,83,"Open" if opened else "Closed",25,anchor="middle",weight="700")
        d.text(x+61,300,f"{obj} inside",23,anchor="middle")
    d.line(220,170,401,170,True)
    d.label(312,135,"open door",147)
    d.save()

def beads(practice=False):
    name="token-question" if practice else "bead-chance"
    colors=[("G",TEAL)]+[("Y",GOLD)]*3 if practice else [("R",RUST)]*2+[("B",BLUE)]*3
    title="Pick one token" if practice else "Pick one bead"
    desc="One green and three yellow tokens are equally likely to be picked. The image supplies the starting contents only." if practice else "Two red and three blue beads are equally likely to be picked, giving two red chances out of five."
    d=Drawing(name,title,desc,260)
    d.rect(45, 70,550,134,"white",INK,40)
    for j,(letter,col) in enumerate(colors):
        x=105+j*(430/(len(colors)-1))
        d.number(x,137,letter,col,r=28)
    d.text(320,238,"Starting contents" if practice else "Red: 2 chances out of 5",25,anchor="middle",weight="700")
    d.save()

def cause():
    d=Drawing("observe-or-set","Observe a clue; or change a setting","In the observation model, heat affects both sprinklers and drink buying. Under an intervention setting sprinklers, heat still affects drink buying, but no longer determines the sprinkler setting.",360)
    for offset,label in [(0,"Observe"),(320,"Set the sprinkler")]:
        d.text(offset+160,82,label,25,anchor="middle",weight="700")
        d.number(offset+162,143,"",GOLD,25)
        d.text(offset+162,112,"heat",23,anchor="middle")
        d.label(offset+84,264,"sprinkler",131,BLUE)
        d.label(offset+244,264,"drinks",109,"#fbe6de")
        d.line(offset+177,168,offset+237,224,True)
        if offset==0:d.line(147,168,90,224,True)
        else:
            d.text(402,195,"you set it",21,anchor="middle")
            d.line(404,204,404,227,True)
    d.line(320,99,320,300,stroke="#d9e1dc")
    d.text(320,335,"Switching a sprinkler does not make it hot.",23,anchor="middle")
    d.save()

def crates():
    d=Drawing("orders-and-crates","Count orders; then count what they need","Two selected orders each need one crate. They require two crates altogether. Starting with three crates leaves one.",320)
    for x,letter in [(38,"A"),(358,"B")]:
        d.rect(x,70,244,99,PALE,TEAL,13)
        d.text(x+20,105,f"Order {letter}",24,weight="700")
        d.text(x+20,142,"needs 1 crate",23)
        d.crate(x+176,94,48)
    for x in [62,112,162]:d.crate(x,211,38)
    d.text(130,289,"stock: 3",24,anchor="middle")
    d.line(226,233,436,233,True)
    d.label(332,204,"use 2",108)
    d.crate(494,211,42)
    d.text(516,289,"left: 1",24,anchor="middle")
    d.save()

def paths():
    d=Drawing("path-and-obstacle","A new obstacle changes the choices","Without an obstacle, the straight path connects two points. With a cabinet blocking that route, an allowed path goes around it. The goal can remain shortest length.",350)
    d.text(26,80,"Clear floor",23,weight="700")
    d.line(84,112,554,112,stroke=TEAL)
    for x,n in [(84,"A"),(554,"B")]:d.number(x,112,n,r=20)
    d.text(26,190,"Cabinet in the way",23,weight="700")
    d.line(84,263,554,263,stroke="#c9b5ae",dash=True)
    d.rect(247,220,142,87,"#f7dfb2",INK,4)
    d.text(318,270,"cabinet",23,anchor="middle")
    d.path("M84,263 L247,209 L389,209 L554,263",TEAL,sw=4)
    for x,n in [(84,"A"),(554,"B")]:d.number(x,263,n,r=20)
    d.save()

def walks():
    d=Drawing("random-paths","An average is not a path","Two fair independent coin tosses make four equally likely paths. Their final positions are plus two, zero, zero, and minus two.",390)
    d.number(65,215,"0")
    for y,n in [(128,"+1"),(295,"−1")]:
        d.line(96,215,268,y,True);d.number(298,y,n)
    leaves=[(72,"+2"),(168,"0"),(262,"0"),(358,"−2")]
    for i,(y,n) in enumerate(leaves):
        origin=128 if i<2 else 295
        d.line(331,origin,522,y,True);d.number(555,y,n)
        d.text(425,(origin+y)/2-9,"H" if i%2==0 else "T",22,anchor="middle")
    d.text(177,153,"H",22)
    d.text(177,281,"T",22)
    d.text(49, 80,"Start",23)
    d.save()

def recipe():
    d=Drawing("recipe-and-action","A description is not its execution","One panel shows a stored recipe card. The other shows using that recipe to bake. Keeping a description does not automatically run its instructions.",300)
    d.rect(63,90,166,127,"white",INK,9)
    d.rect(105,124,80,65,"#fff1ce",INK,8)
    for yy in [142,160,178]:d.line(116,yy,171,yy)
    d.text(145,257,"Keep the recipe",24,anchor="middle")
    d.rect(395,88,183,133,"#e4f2ee",INK,12)
    d.rect(412,126,147,76,"white",INK,9)
    for x in [425,454,483]:d.circle(x,108,4,GOLD,INK,2)
    d.path("M444,178 Q435,154 451,158 Q463,138 476,157 Q490,146 503,160 Q518,158 511,179 Z",fill=GOLD)
    d.rect(451,179,55,15,"#f7dfb2",INK,4,2)
    d.text(486,257,"Use it to bake",24,anchor="middle")
    d.save()

def indications():
    d=Drawing("marks-and-nesting","Arrangement changes the rule","In the lesson's parentheses notation, two empty marks beside one another simplify to one mark. A mark inside a mark simplifies to the unmarked form, shown as blank space rather than zero.",330)
    d.text(32,94,"Beside",24,weight="700")
    d.text(210,113,"() ()",49,anchor="middle")
    d.line(303,94,401,94,True)
    d.text(492,113,"()",49,anchor="middle")
    d.text(32,216,"Inside",24,weight="700")
    d.text(210,236,"(())",49,anchor="middle")
    d.line(303,216,401,216,True)
    d.text(505,266,"blank space",22,anchor="middle")
    d.text(320,307,"The parentheses are this lesson’s stand-in marks.",21,anchor="middle")
    d.save()

def distinctions():
    d=Drawing("pairwise-distinctions","Check each pair","The observer cannot distinguish 20 from 21 degrees or 21 from 22, so those pairs have edges. There is no edge between 20 and 22 degrees.",315)
    for x1,y1,x2,y2 in [(92,210,320,111),(320,111,548,210)]:d.line(x1,y1,x2,y2,stroke=TEAL)
    for x,y,label in [(92,210,"20°"),(320,111,"21°"),(548,210,"22°")]:d.number(x,y,label,r=36)
    d.text(320,273,"No 20°–22° edge",25,anchor="middle",weight="700")
    d.save()

def averages():
    d=Drawing("average-and-rebuild","Same record, different originals","The pairs zero and two, and one and one, both average to one. Repeating that average rebuilds one and one; the record alone cannot identify which original pair was used.",335)
    for y,vals in [(117,[0,2]),(251,[1,1])]:
        for x,n in zip([64,135],vals):d.number(x,y,n,r=24)
        d.line(170,y,293,184,True)
    d.number(325,184,1,GOLD,r=32)
    d.text(325,119,"average",24,anchor="middle")
    d.line(368,184,465,184,True)
    d.text(490,87,"repeat average",22,anchor="middle")
    for x in [501,575]:d.number(x,184,1,r=24)
    d.text(100, 74,"original pairs",22,anchor="middle")
    d.text(528,248,"rebuilt pair",23,anchor="middle")
    d.text(320,312,"The record does not reveal which original.",23,anchor="middle")
    d.save()

def types():
    d=Drawing("types-fit","Check the kind of input","An instruction from date to text can connect to one from text to printed card. A photograph does not fit an input that specifically requires text.",310)
    for x,label in [(104,"date"),(319,"text"),(534,"card")]:
        d.rect(x-70, 80,140, 70,PALE,TEAL,13)
        d.text(x,124,label,26,anchor="middle",weight="700")
    for x in [182,397]:d.line(x,115,x+60,115,True)
    d.label(106,238,"photo",148,"#fbe6de")
    d.label(484,238,"needs text",183,PALE)
    d.line(194,238,369,238,stroke=RUST,dash=True)
    d.line(268,217,296,259,stroke=RUST)
    d.line(268,259,296,217,stroke=RUST)
    d.save()

def jars():
    d=Drawing("sealed-and-labeled","If sealed, then labeled","Both a sealed labeled jar and an open labeled jar obey the one-way rule. Seeing a label alone therefore does not establish that a jar is sealed.",320)
    for x,sealed in [(100,True),(447,False)]:
        d.rect(x,117,96,126,"#e4f2ee",INK,17)
        d.rect(x+16,171,64,38,PAPER,INK,4,2)
        d.text(x+48,198,"label",20,anchor="middle")
        if sealed:d.rect(x-3,107,102,19,GOLD,INK,5,2)
        else:d.rect(x+81,94,85,18,GOLD,INK,5,2)
        d.text(x+48,278,"sealed" if sealed else "open",25,anchor="middle",weight="700")
    d.text(148,84,"Allowed",24,anchor="middle")
    d.text(494,84,"Also allowed",24,anchor="middle")
    d.save()

def field_tiles():
    names=[("Rates","water"),("Space","garden"),("Steps","books"),("Proof","badge"),("Programs","rule"),("Data","records"),("Interaction","messages"),("Chance","coin"),("Operators","rule"),("Observation","observe")]
    d=Drawing("field-habitats","Different questions, different tools","Ten unranked tiles name rates, space, steps, proof, programs, data, interaction, chance, operators, and observation. They are entry points, not a ladder.",622)
    for i,(label,kind) in enumerate(names):
        x=22+(i%2)*310;y=69+(i//2)*107
        d.rect(x,y,286,91,PALE if i%2==0 else "#fff1ce","none",18,0)
        if kind=="water":
            d.path(f"M{x+44},{y+17} Q{x+16},{y+50} {x+44},{y+67} Q{x+72},{y+50} {x+44},{y+17}",fill=BLUE,sw=2)
        elif kind in ["books","records"]:
            for j in range(3):d.book(x+20+j*18,y+25,TEAL if j%2==0 else GOLD,14,40)
        elif kind=="garden":
            d.rect(x+18,y+24,60,43,"#a5c7a4",INK,0,2)
            d.line(x+38,y+24,x+38,y+67);d.line(x+58,y+24,x+58,y+67)
        elif kind=="badge":
            d.circle(x+45,y+43,25,GOLD)
            d.path(f"M{x+33},{y+43} L{x+42},{y+52} L{x+60},{y+33}",sw=3)
        elif kind=="rule":
            d.rect(x+20,y+21,54,49,"white",INK,8,2)
            d.text(x+47,y+55,"f",29,anchor="middle",weight="700")
        elif kind=="observe":
            d.path(f"M{x+16},{y+44} Q{x+45},{y+10} {x+76},{y+44} Q{x+45},{y+78} {x+16},{y+44} Z",fill="white",sw=2)
            d.circle(x+46,y+44,12,BLUE,INK,2)
        elif kind=="messages":
            d.rect(x+16,y+20,44,32,"white",INK,7,2)
            d.rect(x+37,y+44,44,30,BLUE,INK,7,2)
        else:d.number(x+45,y+44,"?",GOLD,24)
        d.text(x+95,y+55,label,26,weight="700")
    d.save()

def practice():
    d=Drawing("learning-loop","Make the idea travel","Read an example, make a prediction, explain your reasoning, and change one thing. Repeat with the changed problem.",345)
    for x,y,label in [(152,114,"Read"),(489,114,"Predict"),(489,264,"Explain"),(152,264,"Change one thing")]:
        d.label(x,y,label,238,PALE if x<300 else "#fff1ce")
    d.line(280,109,359,109,True)
    d.line(489,151,489,218,True)
    d.line(357,259,281,259,True)
    d.line(152,220,152,152,True)
    d.save()

def practice_pictures():
    d=Drawing("practice-chairs","Start, rate, time","The practice problem starts with twelve chairs and adds four chairs per minute for three minutes. The final count is left for the reader.",255)
    for x,label,value in [(109,"Start","12 chairs"),(320,"Each minute","+4 chairs"),(531,"Time","3 minutes")]:
        d.text(x,96,label,23,anchor="middle")
        d.label(x,155,value,184)
    d.text(320,224,"How many are added? How many are there?",23,anchor="middle")
    d.save()
    d=Drawing("practice-photo","Change one dimension","A rectangular photograph is three units wide and five units tall. The reader can increase either dimension by one.",280)
    d.rect(228,79, 90,150,PALE,INK,0)
    d.path("M239,211 L262,166 L280,192 L297,176 L310,211 Z",TEAL,fill="#9ec4ad",sw=2)
    d.circle(294,110,13,GOLD,INK,2)
    d.text(272,263,"width: 3",24,anchor="middle")
    d.text(356,163,"height: 5",24)
    d.text(31,134,"Which",24)
    d.text(31,166,"input",24)
    d.text(31,198,"changes?",24)
    d.save()
    d=Drawing("practice-visitors","A sequence of headcounts","Four room headcounts are ten, fourteen, thirteen, and eighteen, in that order.",240)
    for i,n in enumerate([10,14,13,18]):
        x=79+i*160
        d.number(x,135,n,r=34)
        d.text(x,204,f"check {i+1}",21,anchor="middle")
    d.save()
    d=Drawing("practice-shapes","Four sides; different shapes","A square and a nonsquare rectangle both have four sides. The rectangle is a counterexample to reversing the rule that every square has four sides.",275)
    d.rect(93,96,104,104,PALE,TEAL,0,4)
    d.rect(396,107,165,82,"#fff1ce",INK,0,4)
    d.text(145,242,"square",25,anchor="middle")
    d.text(477,242,"not a square",25,anchor="middle")
    d.save()
    d=Drawing("practice-score","Work backward from the promise","An unknown starting score is reduced by three points. The required result is nonnegative. The starting condition is left for the reader.",245)
    d.label(130,136,"start: ?",187)
    d.line(236,131,404,131,True)
    d.text(320,104,"subtract 3",24,anchor="middle")
    d.label(514,136,"finish ≥ 0",188,"#fff1ce")
    d.save()
    d=Drawing("practice-playlist","Two conditions, four songs","Song A is short but not a favorite. B is a favorite but not short. C is both. D is neither. No answer selection is marked.",280)
    for i,(name,a,b) in enumerate([("A",True,False),("B",False,True),("C",True,True),("D",False,False)]):
        x=20+i*155
        d.rect(x,74,135,166,"white","#b3c8c6",12,2)
        d.text(x+67,109,name,26,anchor="middle",weight="700")
        d.text(x+67,154,"Short: "+("yes" if a else "no"),20,anchor="middle")
        d.text(x+67,202,"Fav: "+("yes" if b else "no"),20,anchor="middle")
    d.save()
    # Same geometry makes the transfer from printer/scissors to bowl/whisk visible.
    d=Drawing("practice-kitchen","New tools, the same waiting pattern","One cook holds the bowl and waits for the whisk. The other holds the whisk and waits for the bowl.",320)
    for x,name,tool,color in [(142,"Cook 1","bowl",PALE),(496,"Cook 2","whisk","#fff1ce")]:
        d.rect(x-100,117,200,118,color,INK,16)
        d.text(x,151,name,24,anchor="middle",weight="700")
        d.text(x,186,"holds",22,anchor="middle")
        d.text(x,219,tool,24,anchor="middle")
    d.path("M142,107 C142,68 496,68 496,107",arrow=True)
    d.rect(224,61,192,28,PAPER,"none",0,0)
    d.text(320, 82,"needs whisk",23,anchor="middle")
    d.path("M496,245 C496,288 142,288 142,245",arrow=True)
    d.rect(224,257,192,28,PAPER,"none",0,0)
    d.text(320,278,"needs bowl",23,anchor="middle")
    d.save()

def name_passing():
    d=Drawing("passing-a-name","Pass a name; gain a connection","Before the message, Alice knows a and b, and Bob knows a. Alice sends b on a. Afterward Bob knows both a and b; Alice keeps both names.",330)
    for x,heading in [(25,"Before"),(355,"After")]:
        d.rect(x,84,260,215,"white","#b3c8c6",18,2)
        d.text(x+130, 74,heading,25,anchor="middle",weight="700")
        d.text(x+20,140,"Alice",24)
        d.text(x+20,243,"Bob",24)
        d.number(x+143,132,"a",PALE,22)
        d.number(x+207,132,"b",GOLD,22)
        d.number(x+143,235,"a",PALE,22)
        if heading=="After":d.number(x+207,235,"b",GOLD,22)
    d.line(294,193,345,193,True)
    d.text(320,181,"b",23,anchor="middle",weight="700")
    d.text(320,228,"on a",19,anchor="middle")
    d.save()

def tensor_pictures():
    d=Drawing("tensor-coordinates","Same arrow, different coordinates","The same northeast arrow has components three east and two north, or two north and minus three west. Only the coordinate directions change.",375)
    for x,label,pair in [(100,"East, north","(3, 2)"),(430,"North, west","(2, −3)")]:
        d.text(x+60,79,label,25,anchor="middle",weight="700")
        d.line(x,246,x,120,True,stroke="#87999f")
        d.text(x,108,"N",22,anchor="middle")
        if x==100:
            d.line(x,246,x+150,246,True,stroke="#87999f");d.text(x+162,254,"E",22)
        else:
            d.line(x,246,x-103,246,True,stroke="#87999f");d.text(x-122,254,"W",22,anchor="middle")
        d.line(x,246,x+90,186,True,stroke=TEAL)
        d.circle(x,246,4,INK,INK,1)
        d.text(x,276,"gate",22,anchor="middle")
        d.text(x+101,181,"tree",22)
        d.text(x+60,318,pair,28,anchor="middle",weight="700")
    d.text(320,354,"North stays upward in both pictures.",23,anchor="middle")
    d.save()
    d=Drawing("tensor-stretch","One stretch, two descriptions","The same linear map doubles east-west lengths and leaves north-south lengths unchanged. In east-north coordinates the diagonal factors are two and one; in north-west coordinates they are one and two.",290)
    for x,title,lines in [(24,"East, north",[("East","×2"),("North","×1")]),(334,"North, west",[("North","×1"),("West","×2")])]:
        d.rect(x,77,282,155,"white","#b3c8c6",15,2)
        d.text(x+141,107,title,25,anchor="middle",weight="700")
        for j,(direction,factor) in enumerate(lines):
            yy=156+j*55
            d.text(x+28,yy,direction,25)
            d.label(x+220,yy-7,factor,70,PALE if factor=="×2" else "#fff1ce")
    d.text(320,269,"The east–west stretch is still twice as large.",23,anchor="middle")
    d.save()

def exterior_pictures():
    d=Drawing("exterior-boundaries","Shared edges cancel","Two adjacent unit squares are traced counterclockwise. The shared edge is traversed up and down. These opposite traversals cancel, leaving six outside unit edges.",340)
    d.text(147,88,"Two loops",25,anchor="middle",weight="700")
    for x,col in [(57,TEAL),(147,RUST)]:
        d.rect(x,116,90,90,PALE if col==TEAL else "#fff1ce","#a7b8b7",0,2)
        d.line(x+16,206,x+72,206,True,stroke=col)
        d.line(x+72,116,x+16,116,True,stroke=col)
    d.line(57,132,57,190,True,stroke=TEAL)
    d.line(237,190,237,132,True,stroke=RUST)
    d.line(141,190,141,132,True,stroke=TEAL)
    d.line(153,132,153,190,True,stroke=RUST)
    d.text(94,170,"A",27,anchor="middle");d.text(197,170,"B",27,anchor="middle")
    d.line(265,163,363,163,True)
    d.text(489,88,"One boundary",25,anchor="middle",weight="700")
    d.rect(391,113,196,98,PALE,TEAL,0,3)
    for args in [(411,211,470,211),(509,211,568,211),(568,113,509,113),(470,113,411,113),(391,128,391,196),(587,196,587,128)]:
        d.line(*args,True,stroke=TEAL)
    d.line(489,111,489,118,stroke=INK);d.line(489,206,489,213,stroke=INK)
    d.text(147,253,"Opposite shared steps",21,anchor="middle")
    d.text(489,253,"6 unit edges",24,anchor="middle")
    d.text(320,310,"Shared reading: +3 + (−3) = 0",25,anchor="middle")
    d.save()
    d=Drawing("exterior-hole","Which edges form the boundary?","Eight square tiles fill a three-by-three grid except for the missing center tile. No perimeter totals or walking directions are supplied.",350)
    for row in range(3):
        for col in range(3):
            if (row,col)!=(1,1):
                d.rect(212+72*col,82+72*row,72,72,PALE,"#819b99",0,2)
    d.text(320,198,"gap",23,anchor="middle")
    d.text(320,328,"Every tile side is 1 unit.",23,anchor="middle")
    d.save()

def complex_pictures():
    d=Drawing("complex-turn","Turn the arrow; keep the axes","In fixed real and imaginary axes, multiplying three plus two i by i rotates the arrow counterclockwise by a quarter turn to minus two plus three i.",390)
    d.line(106,245,543,245,True,stroke="#87999f")
    d.line(315,327,315,83,True,stroke="#87999f")
    d.text(552,253,"real",22)
    d.text(328,91,"imaginary",22)
    d.text(300,271,"0",22,anchor="middle")
    d.line(315,245,405,185,True,stroke=TEAL)
    d.line(315,245,255,155,True,stroke=RUST)
    d.path("M405,185 A108.167,108.167 0 0 0 255,155",INK,sw=2,arrow=True,dash=True)
    d.circle(405,185,4,TEAL,TEAL,1);d.circle(255,155,4,RUST,RUST,1)
    d.text(476,154,"Before",23,anchor="middle")
    d.text(476,189,"3 + 2i",27,anchor="middle",weight="700")
    d.text(178,121,"After",23,anchor="middle")
    d.text(178,156,"−2 + 3i",27,anchor="middle",weight="700")
    d.text(320,369,"Multiplying by i makes a quarter-turn.",23,anchor="middle")
    d.save()
    d=Drawing("complex-contour","Go around a point without touching it","A counterclockwise circular contour surrounds zero. The example function one divided by z is undefined at zero, but the circle itself avoids zero.",340)
    d.circle(178,189,86,"white",TEAL,4)
    d.path("M264,189 A86,86 0 0 0 178,103",TEAL,sw=4,arrow=True)
    d.circle(178,189,7,RUST,INK,2)
    d.text(178,226,"0",25,anchor="middle")
    d.text(438,120,"Example: 1 / z",26,anchor="middle",weight="700")
    d.text(438,178,"Undefined at 0",24,anchor="middle")
    d.text(438,230,"Path avoids 0",24,anchor="middle")
    d.text(320,316,"The path still surrounds the excluded point.",23,anchor="middle")
    d.save()

def fractional_picture():
    d=Drawing("fractional-history","A small weighted-history model","Record A has changes four, zero, zero; record B has zero, four, zero. Weighting those intervals by one-quarter, one-half, and one gives scores one and two. These teaching weights do not define a fractional derivative.",390)
    for x,title,weight in [(167,"Oldest","× 1/4"),(311,"Middle","× 1/2"),(455,"Newest","× 1")]:
        d.text(x,86,title,23,anchor="middle",weight="700")
        d.text(x,120,weight,24,anchor="middle")
    d.text(584,120,"Score",23,anchor="middle",weight="700")
    for y,name,nums,score in [(183,"A",[4,0,0],1),(257,"B",[0,4,0],2)]:
        d.text(48,y+8,name,28,anchor="middle",weight="700")
        for x,n in zip([167,311,455],nums):d.number(x,y,n,r=25)
        d.line(497,y,541,y,True)
        d.number(584,y,score,GOLD,r=25)
    d.text(320,328,"Multiply by the weights, then add.",24,anchor="middle",weight="700")
    d.text(320,366,"Toy score, not a fractional derivative.",22,anchor="middle")
    d.save()

def operator_pictures():
    d=Drawing("operator-swap","What does the action do twice?","The swap operator A sends the pair two, five to five, two. A second application returns two, five. Two swaps act as the identity on every pair.",290)
    for x,title,nums in [(91,"Start",[2,5]),(319,"One swap",[5,2]),(547,"Two swaps",[2,5])]:
        d.text(x,89,title,24,anchor="middle",weight="700")
        for dx,n in zip([-34,34],nums):d.number(x+dx,164,n,PALE if n==2 else GOLD,r=25)
    for x in [160,388]:
        d.line(x,164,x+92,164,True)
        d.text(x+46,144,"A",25,anchor="middle")
    d.text(320,256,"A² = I: two swaps leave the input unchanged.",23,anchor="middle")
    d.save()
    d=Drawing("operator-square","Two different meanings of “square”","Matrix multiplication squares the swap matrix to give the identity matrix. Squaring each entry separately leaves the swap matrix unchanged.",430)
    def matrix(x,y,rows):
        d.path(f"M{x+10},{y} H{x} V{y+84} H{x+10}")
        d.path(f"M{x+100},{y} H{x+110} V{y+84} H{x+100}")
        for row in range(2):
            for col in range(2):d.text(x+32+46*col,y+31+43*row,rows[row][col],28,anchor="middle",weight="700")
    matrix(270,75,[[0,1],[1,0]])
    d.text(240,124,"A =",25,anchor="middle")
    d.line(304,173,183,215,True);d.line(351,173,472,215,True)
    d.text(169,246,"Compose A with A",23,anchor="middle",weight="700")
    d.text(477,246,"Square each entry",23,anchor="middle",weight="700")
    matrix(114,266,[[1,0],[0,1]]);matrix(422,266,[[0,1],[1,0]])
    d.text(169,382,"No swap",24,anchor="middle")
    d.text(477,382,"One swap",24,anchor="middle")
    d.save()

def linear_pictures():
    d=Drawing("linear-token","One token, two possible choices","A single token can be exchanged for one snack or for one drink. The two branches show alternatives; each purchase consumes the token.",325)
    d.label(112,166,"1 token",147,"#fff1ce")
    d.line(201,154,384,109,True);d.line(201,175,384,226,True)
    d.text(294,181,"OR",26,anchor="middle",weight="700")
    d.label(500,110,"snack",172)
    d.label(500,229,"drink",172,BLUE)
    d.text(320,297,"Each exchange consumes the token.",24,anchor="middle")
    d.save()
    d=Drawing("linear-two-tokens","Allocate a resource to each task","One of two separate tokens is exchanged for a snack and the other for a drink. Each token supports just one of the two purchases.",285)
    for y,number,result,col in [(112,1,"snack",PALE),(207,2,"drink",BLUE)]:
        d.label(115,y,f"token {number}",159,"#fff1ce")
        d.line(214,y-5,402,y-5,True)
        d.label(518,y,result,173,col)
    d.save()

def epistemic_pictures():
    d=Drawing("epistemic-views","One card, two views","The chosen card A is a red circle. Jo sees only color, leaving A or B possible. Sam sees only shape, leaving A or C possible.",355)
    for x,name,col,shape in [(80,"A",RUST,"circle"),(240,"B",RUST,"triangle"),(400,"C",BLUE,"circle"),(560,"D",BLUE,"triangle")]:
        d.rect(x-61,75,122,127,"white",INK if name=="A" else "#a8babc",12,4 if name=="A" else 2)
        d.text(x,105,name,26,anchor="middle",weight="700")
        if shape=="circle":d.circle(x,139,16,col,INK,2)
        else:d.path(f"M{x},{122} L{x-18},{154} L{x+18},{154} Z",fill=col,sw=2)
        d.text(x,183,"red" if col==RUST else "blue",22,anchor="middle")
    d.text(320,235,"Chosen card: A",24,anchor="middle",weight="700")
    d.text(320,283,"Jo sees red: A or B",25,anchor="middle")
    d.text(320,326,"Sam sees circle: A or C",25,anchor="middle")
    d.save()
    d=Drawing("epistemic-update","Everyone hears: “The card is red”","After a truthful public announcement of red, Jo still allows A and B. Sam rules out blue card C, leaving only A.",285)
    d.text(212,90,"Before",23,anchor="middle",weight="700")
    d.text(511,90,"After",23,anchor="middle",weight="700")
    for y,name,before,after in [(141,"Jo","A or B","A or B"),(225,"Sam","A or C","A")]:
        d.text(37,y+7,name,25,weight="700")
        d.label(212,y,before,158)
        d.line(304,y-4,415,y-4,True)
        d.label(511,y,after,158,GOLD if after=="A" else PALE)
    d.save()

def rough_pictures():
    d=Drawing("rough-groups","Which crates share a record?","Batch A contains ready crates 1 and 2. Batch B contains ready crate 3 and not-ready crate 4. Batch C contains not-ready crates 5 and 6. The scanner reports only the batch letter.",340)
    for x,name,nums in [(25,"A",[1,2]),(235,"B",[3,4]),(445,"C",[5,6])]:
        d.rect(x,75,170,212,"white","#a8babc",14,2)
        d.text(x+85,109,"Batch "+name,25,anchor="middle",weight="700")
        for y,n in zip([164,239],nums):
            d.number(x+43,y,n,PALE if n<=3 else "#f5ddd5",r=24)
            d.text(x+112,y+7,"ready" if n<=3 else "not",23,anchor="middle")
    d.text(320,322,"Target: ready crates 1, 2, 3.",24,anchor="middle")
    d.save()
    d=Drawing("rough-bounds","Definite, possible, and unresolved","The upper approximation contains crates 1, 2, 3, and 4. Inside it, the lower approximation contains 1 and 2 and the unresolved boundary contains 3 and 4. Crates 5 and 6 are outside the upper approximation.",360)
    d.rect(24,74,415,229,"#fff1ce",INK,16,2)
    d.text(232,107,"Upper: possibly ready",23,anchor="middle",weight="700")
    d.rect(43,127,179,155,PALE,TEAL,12,2)
    d.text(132,162,"Lower",24,anchor="middle",weight="700")
    d.text(132,190,"definitely ready",21,anchor="middle")
    d.text(330,162,"Boundary",24,anchor="middle",weight="700")
    d.text(330,190,"unresolved",21,anchor="middle")
    for x,n,col in [(89,1,PALE),(176,2,PALE),(287,3,GOLD),(374,4,GOLD),(495,5,"#f5ddd5"),(579,6,"#f5ddd5")]:d.number(x,239,n,col,r=24)
    d.text(535,156,"Outside",23,anchor="middle",weight="700")
    d.text(535,185,"the upper set",21,anchor="middle")
    d.text(320,337,"The boundary is part of the upper set.",23,anchor="middle")
    d.save()

def measurement_pictures():
    d=Drawing("measurement-dependency","A measurement guides a later action","Qubit 1 carries the input and qubit 2 is prepared. After linking them, qubit 1 is measured. Its ordinary outcome bit controls a correction on qubit 2, which is the output. The dashed path carries the recorded bit.",410)
    d.text(78,102,"Qubit 1",23,anchor="middle",weight="700")
    d.text(78,137,"input",22,anchor="middle")
    d.text(78,255,"Qubit 2",23,anchor="middle",weight="700")
    d.text(78,290,"prepare",22,anchor="middle")
    d.line(138,130,331,130,True)
    d.line(138,283,464,283,True)
    d.line(224,130,224,283)
    d.circle(224,130,7,TEAL,INK,2);d.circle(224,283,7,TEAL,INK,2)
    d.text(224,91,"Link",23,anchor="middle",weight="700")
    d.rect(335,101,126,58,PALE,INK,12,2)
    d.text(398,138,"Measure",23,anchor="middle")
    d.path("M462,130 H547 V249",TEAL,arrow=True,dash=True)
    d.text(490,196,"record bit",21,anchor="middle")
    d.rect(468,252,142,62,"#fff1ce",INK,12,2)
    d.text(539,291,"Correct",24,anchor="middle")
    d.text(539,347,"output qubit 2",22,anchor="middle")
    d.text(320,387,"Dashed path: an ordinary recorded bit.",22,anchor="middle")
    d.save()
    d=Drawing("measurement-correction","Use the recorded bit","With bit zero the target state is left alone. With bit one the output is X of the target and a further X returns the target. This uses X squared equals the identity.",315)
    d.text(49,91,"Bit",21,anchor="middle",weight="700")
    for y,n,before,action in [(133,0,"target","leave alone"),(231,1,"X(target)","apply X")]:
        d.number(49,y,n,GOLD,r=23)
        d.label(179,y,before,155)
        d.line(268,y-4,442,y-4,True)
        d.text(355,y-20,action,22,anchor="middle")
        d.label(536,y,"target",151)
    d.text(320,293,"X² = I: two X operations cancel.",23,anchor="middle")
    d.save()

def behavior_picture():
    d=Drawing("behavior-branches","Same sequences, different choices","Machine A accepts payment then offers both tea and coffee. Machine B has two payment transitions, one to tea-only and one to coffee-only. Both allow pay-tea and pay-coffee traces, but B can commit to one drink during payment.",575)
    for x,name in [(153,"Machine A"),(489,"Machine B")]:
        d.text(x,88,name,25,anchor="middle",weight="700")
        d.label(x,135,"start",110)
    d.line(153,161,153,227,True);d.text(185,204,"pay",23)
    d.label(153,261,"Both available",245)
    d.line(129,289,74,405,True);d.text(68,350,"tea",23,anchor="middle")
    d.line(177,289,230,405,True);d.text(238,350,"coffee",23,anchor="middle")
    for x in [74,230,409,563]:
        d.circle(x,435,27,"white",INK,2);d.text(x,443,"stop",19,anchor="middle")
    d.line(463,162,415,227,True);d.text(410,198,"pay",23,anchor="middle")
    d.line(513,162,558,227,True);d.text(561,198,"pay",23,anchor="middle")
    d.label(409,261,"Tea only",128)
    d.label(563,261,"Coffee only",141)
    d.line(409,290,409,405,True);d.text(375,356,"tea",23,anchor="middle")
    d.line(563,290,563,405,True);d.text(606,356,"coffee",20,anchor="middle")
    d.text(153,500,"Choose after paying",22,anchor="middle")
    d.text(489,500,"Commits during payment",21,anchor="middle")
    d.text(320,549,"Which choices survive the payment step?",23,anchor="middle")
    d.save()

def do_pictures():
    d=Drawing("do-intervention","Set watering; keep its effects","The observational graph has weather affecting watering and growth, and watering affecting growth. Setting watering removes the incoming weather-to-watering arrow while retaining the other arrows. The crossed dashed line marks the removed arrow.",390)
    d.line(320,62,320,335,stroke="#ccd8d4")
    for offset,title in [(0,"Observed choices"),(320,"do(watering)")]:
        d.text(162+offset,90,title,24,anchor="middle",weight="700")
        d.label(162+offset,143,"Weather",142)
        d.label(70+offset,282,"Watering",116)
        d.label(252+offset,282,"Growth",112)
        d.line(186+offset,171,241+offset,248,True)
        d.line(134+offset,278,188+offset,278,True)
        if offset==0:d.line(138,171,78,248,True)
        else:
            d.line(458,171,398,248,stroke="#a8babc",dash=True)
            d.line(418,196,440,218,stroke=RUST);d.line(440,196,418,218,stroke=RUST)
    d.text(320,358,"Incoming cause removed; outgoing cause kept.",22,anchor="middle")
    d.save()
    d=Drawing("do-adjustment","Compare the same weather mix","The observed watered and unwatered groups have success rates 50 and 70 percent and different weather mixes. Adjusting both to half mild and half hot gives intervention rates 65 and 55 percent under the stated model.",390)
    for x,title,vals,note in [(34,"Observed groups",[50,70],"Different weather mixes"),(355,"Interventions",[65,55],"Half mild, half hot")]:
        d.text(x+126,88,title,24,anchor="middle",weight="700")
        for y,label,n,col in [(137,"Water",vals[0],TEAL),(234,"No water",vals[1],RUST)]:
            d.text(x,y-12,label,23)
            d.rect(x,y,220,28,"#e8ebe6","none",5,0)
            d.rect(x,y,2.2*n,28,col,"none",5,0)
            d.text(x+2.2*n+8,y+23,f"{n}%",23,weight="700")
        d.text(x+126,304,note,21,anchor="middle")
    d.text(320,366,"Model assumptions justify this adjustment.",23,anchor="middle")
    d.save()

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    counters(); water(); gardens(); books(); badges(); selector(); selector(True)
    tickets(); query(); deadlock(); cupboard(); cupboard(True); beads(); beads(True)
    cause(); crates(); paths(); walks(); recipe(); indications(); distinctions()
    averages(); types(); jars(); field_tiles(); practice(); practice_pictures(); name_passing()
    tensor_pictures(); exterior_pictures(); complex_pictures()
    fractional_picture(); operator_pictures(); linear_pictures()
    epistemic_pictures(); rough_pictures(); measurement_pictures()
    behavior_picture(); do_pictures()
    (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    print(f"Built {len(manifest)} SVG diagrams.")
if __name__ == "__main__":
    main()
