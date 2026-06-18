---
title: "Mini Industry"
source_url: https://www.guidesnotincluded.com/mini-industry
archived: 2025-08-06
archive_snapshot: https://web.archive.org/web/20250806081310id_/https://www.guidesnotincluded.com/mini-industry
---

# MINI INDUSTRY (CRAMMING IT ALL IN)

My personal preference is to keep my dupe count low and my base compact. I build all manufacturing machines in my base and cool them down, rather than having a separate, hot industrial area. (This is wasteful as far as power is concerned but is another personal preference.)

For those who want to keep things compact, here's a way to cram in a lot of stuff in not a lot of space. I build some variation of this pretty much every playthrough. (Though I rarely make it quite this compact myself. But if you want to keep things small, this design has you covered... ;-)

The design includes a cooling loop. However, keep in mind this is intended for small-scale use: it won't keep up if you run lots of manufacturing machines continuously.

The floors are 18 tiles across. This is just so it will fit with my base, which pretty much always has 18-wide floors. (There is limited space for storage bins, but put them in where you can. I left them out for clarity.)

![ONI-guide-Mini-Industry-1.png](assets/ONI-guide-Mini-Industry-1-20bae7c849.avif)

The machine on the bottom right is a Molecular Forge. It is a late-game machine as it requires materials that aren't available on your starting asteroid. Some molecular forge recipes also require petroleum, which is why there is a petroleum source by it. The petroleum tank doubles as a cooling liquid for glass.

If you have a [Glossy Drecko ranch](https://www.guidesnotincluded.com/low-tech-plastic-drecko-ranching) you don't need the Polymer Press (the white machine on the right). Then you could add an Exosuit Forge or some other necessary machine there. (I have stopped using the polymer press entirely and always get my plastic from glossy drecko farming. Try it if you haven't already.)

The cooling loop isn't included in the above picture, as it would make it (even more) confusing. I'll cover the cooling loop separately.

![ONI-guide-Mini-Industry-power.png](assets/ONI-guide-Mini-Industry-power-498f7bd783.avif)

I have started connecting the steam turbine to my main power spine. This isn't necessary, and if you don't do it you don't need to run unsightly heavi-watt wire there. (But you will have more spaghetti to deal with when running wire for all machines from farther away.)

The molecular forge is very power hungry - 1600W! In this picture it isn't powered. (An ugly solution is to run the heavi-watt wire to it. A decor-friendly solution is to run a conductive wire from... wherever you have a transformer to spare.)

Another option is to use some automation to make sure only either the glass forge or the molecular forge can run at once. Then you can connect them both to the same power wire.

![ONI-guide-Mini-Industry-liquid.png](assets/ONI-guide-Mini-Industry-liquid-cc9a6ba911.avif)

The dotted liquid pipe that circles the design represents the cooling loop. Which actually should run around the floors and machines to cool them. But that would make this picture much too confusing, so I'll picture that separately.

The pipe running up from below the picture is where oil is pumped up. It is run through an oil refinery and the resulting petroleum is split into two output pipes. One goes up to a polymer press and also up (which would lead to a petroleum rocket if/when you have them). The second pipe empties into a petroleum storage tank for use in molecular forge stuff.

For the liquid pipe from the glass forge: use ceramic if available. Insulated pipes if you have spare ceramic, but in my experience even just regular ceramic pipes will do.

![ONI-guide-Mini-Industry-automation.png](assets/ONI-guide-Mini-Industry-automation-576538ab1f.avif)

I like putting a liquid reservoir in my cooling loops, and then having the liquid thermo sensor after the reservoir. This way you can get a controlled, even temperature at the start of your loop.

(Note: Since writing this section I have changed how I pipe cooling liquid into the thermo aquatuner. My current approach is pictured at the end of this page.)

The polymer press automation is to have it stop when the smart storage bin is full. (See [Getting started with automation](https://www.guidesnotincluded.com/getting-started-with-automation) for a closer look at it.)

This design has a very small area where water is intended to pool by the polymer press (in-between the airflow tiles). For water to only pool there you will need to add a lot of cooling around (and over) the polymer press.

The cooling loop pictured below might not be enough to keep the water where you want it. If so, run the cooling loop over the polymer press as well and add a diamond temp shift plate or two. (Or try the glossy dreckos.)

The atmo sensor in the oil refinery room is to pump out Natural Gas before the room becomes so full of it that the refinery stops working.

(These pictures don't include gas pipes, but there are no surprises with that piping - pump oxygen to the atmo suit dock, pump carbon dioxide from the polymer press to... wherever. And pump excess natural gas, also, to wherever.)

Petroleum doesn't behave like water - even when the liquid vent in the petroleum tank is immersed in petroleum, petroleum will still keep pouring out of it. So you need an automated shut-off system for when the tank is sufficiently full. This can be done simply by connecting a hydro sensor directly to the liquid vent (using automation wire).

![ONI-guide-Mini-Industry-cooling-loop.png](assets/ONI-guide-Mini-Industry-cooling-loop-30b057b887.avif)

And, finally, a picture of the same design but with a cooling loop running through it. (I made some small modifications to the other piping to fit in the cooling loop. A few liquid bridges added to the metal refinery piping and one to the petroleum output pipe.)

I used radiant piping all the way for visual clarity. Normally I would only use radiant piping in areas with a lot of heat.

If you find an area is getting too hot you can upgrade from normal pipe to radiant pipe while the cooling loop is running. Coolant will not spill out of the pipes.

![ONI-Aquatuner-1.png](assets/ONI-Aquatuner-1-ad41e147c8.avif)

Ummm... about that design I just showed you...

Since writing the previous section I have changed to piping the cooling liquid in from above, as pictured here.

The cooling liquid flows in from the right, goes through the thermo aquatuner, and then up to the liquid reservoir and then out to the left. Either way is fine - all that matters is that your cooling loop works.

Adding a bit of automation to stop overheating from continuous use of the metal refinery

If you have the metal refinery running continuously (or near-continuously) then your cooling liquid will eventually overheat and break the pipes.

I'm not sure why it took me thousands of hours of gameplay to realize this, but you can stop the overheating by adding some automation to the design.

After trying a few things, what I have settled on is putting a thermo sensor inside the cooling box and connecting it to the metal refinery.

The thermo sensor measures the temperature and shuts off the metal refinery when it gets too hot. I find having it set to "under 200 C" means the steam turbine runs at almost full capacity.

I will rewrite this part of the guide at some point to include the changes mentioned at the end. But for now, here are some overlay pictures from my current playthrough, which includes both of the modifications mentioned at the end, the new thermo aquatuner piping and the automation in the steam box.

(On the two kilns: I have one set to continuously make ceramic. The other is set to continuously make refined carbon, and is connected to the smart storage bin that shuts off production when there is 5K refined carbon stored.)

![ONI-Guide_MetalRefineryAutomation.png](assets/ONI-Guide_MetalRefineryAutomation-14cdc3352c.avif)

![ONI-Guide_MetalRefineryAutomation2.png](assets/ONI-Guide_MetalRefineryAutomation2-4b700172a6.avif)

![ONI-Guide_MetalRefineryAutomation3.png](assets/ONI-Guide_MetalRefineryAutomation3-d051fc527a.avif)

---

*Archived from [https://www.guidesnotincluded.com/mini-industry](https://www.guidesnotincluded.com/mini-industry) ([Wayback Machine snapshot](https://web.archive.org/web/20250806081310id_/https://www.guidesnotincluded.com/mini-industry)). Original work © Some Random Finn / guidesnotincluded.com, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Reformatted from HTML to Markdown for this non-commercial community archive — see [Attribution & licensing](attribution.md).*
