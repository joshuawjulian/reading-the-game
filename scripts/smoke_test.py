"""Render a few reference diagrams to planning/smoke/ to eyeball the library."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from gridiron import Play, offense, defense, routes as r, frame_strip, animate

out = "planning/smoke"
off = offense("gun_2x2")
p = Play(off, defense("nickel", "single_high", off), los=35, to_go=10, title="Smash concept vs Cover 3 (11 personnel, 2x2)")
p.route("X", r.hitch(5)); p.route("H", r.corner(10)); p.route("Z", r.hitch(5)); p.route("Y", r.corner(10))
p.route("RB", r.flat(), side=-1)
p.dropback(2.5); p.pass_to("H", t=2.3)
for k in ["LT", "LG", "C", "RG", "RT"]:
    p.block(k, pts=[(-1.2, 0)])
p.drop("FS", (16, 0), zone=(12, 16), label="deep middle")
p.drop("LCB", (15, -13), zone=(12, 12), label="deep 1/3")
p.drop("RCB", (15, 13), zone=(12, 12), label="deep 1/3")
p.rush("SDE"); p.rush("WDE"); p.rush("SDT"); p.rush("WDT")
p.highlight("H")
p.draw(legend=True); plt.savefig(f"{out}/smash.png", dpi=130); plt.close("all")

off = offense("i_form")
q = Play(off, defense("4-3_over", "single_high", off), los=40, to_go=10, title="Power O from the I-formation")
q.block("RT", "SDT"); q.block("Y", "SDE"); q.block("RG", "SDT"); q.block("C", "WDT"); q.block("LT", "WDE")
q.pull("LG", [(-0.6, 1.2), (-0.4, 5.0), (1.8, 6.6)], target="MIKE")
q.run("FB", [(1.0, 3.5), (2.2, 6.4)], speed=6)
q.run("RB", [(-0.3, 1.0), (3.0, 5.0), (9.0, 6.0)], delay=0.4)
q.handoff("RB", t=0.9); q.path("QB", [(-1.5, 1.5)], speed=3)
q.draw(lateral=(-14, 14)); plt.savefig(f"{out}/power.png", dpi=130); plt.close("all")

off = offense("gun_trips")
m = Play(off, defense("nickel", "zero", off), los=50, title="Jet motion vs man: the defender follows")
m.motion("X", to=(-1.5, 4.0)); m.man("LCB", "X"); m.route("X", r.flat(width=10), side=1)
m.route("Z", r.go()); m.route("H", r.slant()); m.dropback(2); m.pass_to("X", t=1.4)
m.draw(); plt.savefig(f"{out}/motion.png", dpi=130); plt.close("all")
trk = m.to_tracking()
trk.to_csv(f"{out}/motion_tracking.csv", index=False)
print(trk.head(3).T)
fig = frame_strip(trk, times=[-1.0, 0.0, 1.0, 2.0], title="Jet motion vs man (frame strip)")
fig.savefig(f"{out}/strip.png", dpi=130); plt.close("all")
anim = animate(p.to_tracking(), title="Smash vs Cover 3")
anim.save(f"{out}/smash.mp4", fps=10, dpi=80)
print("ok")
