---
title: "Metal volcano basics"
description: "Tapping into metal volcanos for their resources can be done in many different ways."
source_url: https://www.guidesnotincluded.com/taming-metal-volcanos
archived: 2025-08-06
archive_snapshot: https://web.archive.org/web/20250806081011id_/https://www.guidesnotincluded.com/taming-metal-volcanos
---

## Introduction

Tapping into metal volcanos for their resources can be done in many different ways.

This guide is for a fairly basic approach that is easy to build, uses very little automation and will work for any metal volcanos you find on your starting asteroid.

However, this design does require [steel](getting-steel.md) and [plastic](getting-oil-petroleum-and-plastic.md) for a [cooling loop](thermo-aquatuner-steam-turbine-cooling-loop.md). And also a fair bit of power, depending on how much you want to cool down the volcano output.

![ONI-MetalVolcano1.png](assets/ONI-MetalVolcano1-c84845b889.avif)

## Know your metals

There are a bunch of different metal volcanos you might come across on your starting asteroid.

* In the base game you can have copper, gold and iron volcanos
* The DLC adds cobalt and aluminium volcanos

(The DLC  also adds two volcanos, Tungsten and Niobium, that won't spawn on your starting asteroid.)

Metal volcanos output refined metal. So where you would need to refine iron ore to get iron, an iron volcano will output iron directly. The same goes for the other volcanos.

## Hot, hot, hot!

You could just dig out a volcano and then get access to the metal. But that would cause what might be described as "some issues" with heat.

Volcanos spit out metal that is so hot that it is in liquid form. The exact temperature varies between volcanos, but can be close to +3000C (Niobium and Tungsten are even hotter). Click on a volcano to see the exact temperature.

Cooling metal volcano output can be grouped into two stages or goals.

The first goal is to cool the output enough that it solidifies. Meaning a dupe or an auto-sweeper can actually pick up the metal. (A dupe in an atmo suit can handle very hot materials without getting scalded.)

The second goal is optional, but something I tend to do: to cool the output futher. I usually cool it down to (roughly) the temperature I keep my base at (+25C).

## Before you start: The key tile

![ONI-MetalVolcano2.png](assets/ONI-MetalVolcano2-505f76c3fb.avif)

The key tile is the one that is two steps in and two steps up from the bottom left. All other tiles are safe to dig out - even after Gossman is done, the gold volcano won't erupt.

There is one tile on any geyser or volcano that decides whether it is considered uncovered and can erupt.

This tile is also the tile from which the erupting contents "spawn," or pour out. To make things a bit more tricky, it is also the tile you need to dig out to be able to analyze the geyser or volcano.

In the case of volcanos and geysers that have a neutronium foundation that is four tiles wide (which is the most common kind), the key tile is:

* two tiles in from the bottom left and two tiles up

You can dig out all other tiles of a geyser or volcano and it will still not be able to erupt.

If you accidentally dig up that tile and need to cover it up again, you can:

* build a tempshift plate out of coal on that tile

When the volcano erupts, the tempshift plate will solidify into coal and the volcano will stop erupting.

## Building the thing

When I come across a geyser that is covered, I dig out three tiles: two tiles on the side (the bottom one and one tile up from the bottom) and one tile further in along the bottom. This will show you what kind of geyser it is without activating it. (for some of them, just digging out two tiles on the side is enough.)

Having uncovered a metal volcano you want to harness, first comes the issue of timing. Even without having uncovered the key tile of a volcano you can see if it is dormant or active. Volcanos cycle between the two states.

Dormant means it is just sitting there. Active means it will periodically erupt with molten metal. The exact length of each state varies, but tends to be several dozen cycles. You can find out the exact lengths by analyzing the volcano. However, to analyze the volcano, you need to dig out the key tile.

Digging out the key tile when you know a volcano has just gone dormant is safe. Doing it when you don't know how long it has been dormant is exciting. Digging out the key tile when a volcano is active is something I wouldn't recommend. (It can be done if you for some reason have to do it - the water will take a while to turn to steam from the volcano output, which gives you a little time.)

Note: you can do a fair bit of the building without uncovering the key tile and activating the volcano.

When building the steam room - the room with the volcano, don't enclose it completely. Add a (temporary) [liquid lock](liquid-lock-basics.md) leading in to the steam chamber. This will be necessary to create a vacuum in the room.

There are various things that need doing in the volcano/steam room. Try to forget as few of them as possible:

* Analyze the volcano
* Add 2.000-3.000 kg of water (so there is a few hundred kg per tile on the floor)
* Pump out the gases
* Build your various bits and bobs: automation, steam turbine output, power wires, etc.

Then delete any temporary stuff that was there for the building phase. and sweep up the debris on the floor (if you want to - the auto-sweeper can also take care of it). Once everything is ready and the volcano is analyzed, you are ready to seal up the chamber.

Note: before sealing it up, go over all the important overlays one by one. Plumbing, automation, power, conveyor. (Whenever I end up forgetting something, it's usually the liquid output from the steam turbine.)

For the rest of the build, I'll just include some overlays. My metal volcano build has changed over time and will probably continue to do so. This is what I have recently started using.

As with all of my builds, my main concern is that it works (and that it looks nice enough). I'll add some comments at the end about how you obviously don't have to build it like this at all, and throw in a link to a much more compact build by Luma plays.

![ONI-MetalVolcano3.png](assets/ONI-MetalVolcano3-90bc21c5be.avif)

This design has three sections:

In the middle is the steam chamber that does the initial cooling down of the volcano output. It has an auto-sweeper to move metal out of the room and two steam turbines on top.

(On a gold volcano you should be able to get by with just one steam turbine, but I use two anyway. Officially that is because I like my volcano tamers having a unified look across the map. But really it's because my brain is full of 80s pop song lyrics so I can't remember which volcanos need one and which need two.)

On the bottom is the cooling loop for the metal output. Metal will come out of the volcano room at a temperature of at least 125C. (The exact temperature will depend on your automation setup.) The bottom section cools the metal down further. (You can decide how cool you want it - the main limitation is power. More cooling = more power.)

On the top is the cooling loop used to cool the steam turbines and the cooling chamber on the bottom.

![ONI-MetalVolcano4.png](assets/ONI-MetalVolcano4-3dc2391c22.avif)

The plumbing overlay. There are three separate pipe sections. The steam turbine on the top has a pipe that feeds its output water back into the tank.

The two steam turbines in the middle have a pipe that feeds their output back into the steam chamber.

The thermo aquatuner on the top right chills the cooling loop that runs past the steam turbines and the cooling chamber for the output metals.

![ONI-MetalVolcano5.png](assets/ONI-MetalVolcano5-49ceab49a6.avif)

The power overlay. I connect the steam turbines to my power grid. A large power transformer supplies power to the build.

![ONI-MetalVolcano6.png](assets/ONI-MetalVolcano6-161af5e777.avif)

The conveyor overlay. A conveyor shutoff (top right in the steam room) is used to control the output flow.

(The conveyor belt from the bottom left is from a nearby metal volcano, sending its output in for some extra cooling and to get it on the same conveyor rail.)

Note: some volcanos output metal that is hot enough to melt even steel conveyor belts. Gold is such a volcano. Avoid running the conveyor belt through the middle tile of the volcano (the tile it erupts from). The top tiles, as in the picture above, are all safe.

(You can make the conveyor rail in the steam room longer to improve temperature transfer from your metal.)

![ONI-MetalVolcano7.png](assets/ONI-MetalVolcano7-1b4c0c5c1f.avif)

The automation overlay. The tricky bit to get just right is the automation for when to send out the metal on the conveyor belt. I have started using a timer sensor for this.

You can set how long of a red signal you want and how long of a green signal. They will then keep alternating forever. On this volcano I use the settings: green 10, red 190.

The optimal setting would be a green signal that is as long as it takes for the entire length of the conveyor rail to change contents - the "cool" metal out and new, hot metal in. How long a green signal that translates to will depend on how long your rail is. (For a rail the length in the pictures above that seems to be about a setting of 10 for green.)

Then for the red, you want that signal to be long enough that the metal on the conveyor belt cools down to 125C or close to it. (At under 125C the steam turbine will stop working and no additional cooling will take place.)

The temperature of the metal on your rails will decrease more slowly as you near the +125C lower limit. You can mouseover the metal on your rail to see the temperature change in action. That way you can optimize the setting for the red signal. Most of the extra heat will probably be gone in 150 ticks. To extract near all of the extra heat, try a setting closer to 200.

There are other ways to automate this. I used to use a conveyor rail thermo sensor, so the metal would stay in the steam chamber until it was 130C or so: cool enough to no longer be useful. There is a problem with that approach, and I don't know if it's a bug or a feature. (Meaning, something that will be fixed or not).

The autosweeper can pick up miniscule amounts of metal. It can then feed a miniscule amount onto the conveyor rail. Very small amounts of metal on a conveyor rail don't seem to change temperature. So whenever you get one of those packets with just a tiny amount, it clogs up the system. As it doesn't cool down (or maybe does, but veeeeery slowly), the sensor remains on red as the conveyor belt content is still too hot.

If you use that system for automating, it is a good idea to add some kind of automation that will let a packet pass every now and then, regardless of its temperature. That way you can let through the occasional mini-packets that would otherwise clog the system.

And now for something completely different.

## Or: Build something completely different

![LumaPlaysMetalVolcanoTamer.png](assets/LumaPlaysMetalVolcanoTamer-1d0e3f0c54.avif)

There are lots of great designs. Here's a tiny metal volcano tamer by Luma plays. (I haven't tried it myself, but you can check his [YouTube channel](https://www.youtube.com/watch?v=H7vY71geaPo) for an introduction.)

There are many ways to tame metal volcanos. My approach is very basic. It's a good "My first volcano tamer" kind of build because it's easy to understand what each part does.

If or when you want to switch to a more optimized build, there are lots of designs you can check out. Or you can just throw caution to the wind and start doing some experimenting of your own!

For instance, one thing that might be of interest is that it is possible to let steam turbines cool themselves. A steam turbine outputs water that is +95C. The max temperature a steam turbine will function at is +100C. So there is a slim window there; a few degrees you can use for cooling.

The design I presented here uses power to cool down the steam turbines. I usually keep them at a habitable temperature - around 25-30 degrees. This is another one of those areas where I waste lots of power because I prefer things a certain way. If you use self-cooling you can save lots of power.

Another thing to be aware of is the issue of the amount of steam turbines to use over a volcano. The minimum amount there depends on if the steam turbines are self-cooling and on what kind of volcano it is.

With a cooling loop for your steam turbines, you can get by with one or two steam turbines, depending on the volcano. (I tend to not bother too much with optimizing steam turbine amounts.)

And speaking of getting by with fewer steam turbines...

For an example of a (much) smaller metal volcano tamer, have a look at [Luma plays' design](https://www.youtube.com/watch?v=H7vY71geaPo), which is 9x9 tiles and only uses one(!) steam turbine regardless of volcano type (except Niobium). However, that build is a bit trickier to put together and requires some additional materials.

---

*Archived from [https://www.guidesnotincluded.com/taming-metal-volcanos](https://www.guidesnotincluded.com/taming-metal-volcanos) ([Wayback Machine snapshot](https://web.archive.org/web/20250806081011id_/https://www.guidesnotincluded.com/taming-metal-volcanos)). Original work © Some Random Finn / guidesnotincluded.com, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Reformatted from HTML to Markdown for this non-commercial community archive — see [Attribution & licensing](attribution.md).*
