---
title: "Recycling toilet water"
source_url: https://www.guidesnotincluded.com/recycling-toilet-water
archived: 2025-07-31
archive_snapshot: https://web.archive.org/web/20250731071301id_/https://www.guidesnotincluded.com/recycling-toilet-water
---

# RECYCLING BATHROOM WATER

Introduction

Some basics

The liquid overflow mechanism

The quick & dirty (read: germy) version

The full build: pictures and overlays

How it works

Building the thing: the easy way

Building the thing: the less easy way

* Building a vacuum room
* Deleting and rebuilding pipes
* Filling the room with chlorine
* Completing the chlorine room: pipes and automation

* You can see the Plumbing Overlay by clicking on the water drops in the top right or by pressing F6.

* You build most plumbing-related stuff through the Plumbing build icon (bottom left). A notable exception is the sink, which is found under Medicine.

* Plumbing things commonly have an input and an output.

  + White is input: liquid goes in here
  + Green is output: liquid comes out here

* If something isn't working, the first things to check are the inputs and outputs. A common mistake (even after thousands of hours I still do it) is connecting inputs or outputs wrong.

* A pipe must lead somewhere for liquid to flow along it. (A Liquid Bridge counts as somewhere - water will flow up to the start of the liquid bridge, even if the pipe goes nowhere after it.)

* If you want liquid to pour out of a pipe, you need to put a Liquid Vent at the end.

* Gravity affects liquids on the map, it does not affect liquid in pipes.

## Tip reminder: plumbing basics

## Introduction

The goal is to take the polluted, germy water from our bathrooms and turn it into clean, germ-free water that we then feed back to our bathrooms. When done, you will never have to think about bathroom water again.

I'll cover a quick & dirty (meaning germy) version and a version that uses chlorine to kill off all germs.

There are many variations of "use chlorine to kill germs" -builds. I learned the one I use from a YouTube video by Francis John: "QOL Mk3, 36 Germ decontamination for toilets and spin that vacillator : Oxygen not included"

Available at: <https://youtu.be/SEL3pxB5tao?t=102>, accessed 11 August, 2020.

(Note: I just rewrote this whole section. [In late March, 2023] There might be an unusual amount of typos, but I'll try to find them. If you find some typos or other wonkiness, please let me know. There's an anonymous [contact form](https://www.guidesnotincluded.com/guide-feedback) you can use.)

## Some basics (or, We can do this the easy way or the hard way)

When we run polluted water through a water sieve it turns into water. Since toilets, sinks and showers need water, and we would have just created water, we could then simply feed that water back into our bathrooms and showers. However:

* a water sieve will not remove germs from water.

So we would end up with germ-infested water used as clean water in our bathrooms and showers. (Germs in water aren't visible. To see germs, use the Germ Overlay.)

To solve this issue, this build uses chlorine.

* Chlorine kills germs

We will send all germy water through a room full of chlorine to de-germify (that's definitely a word) it.

That said, you don't actually have to kill off the germs if you don't want to. Germs in the clean water of showers and sinks don't spread to dupes. So while carrying, say, germy dirt will make dupes germy, showering or washing their hands in germy water will leave them germ-free.

The idea of becoming germ-free from washing your hands with germ-infested water is immersion-breaking for me, so I don't do it. But if you don't suffer from the same hangups as I do you can just skip the chlorine room. Which will make this build both quicker and easier. (I'll include pictures of both versions of the build.)

Regardless of which option you choose, you will need a liquid overflow mechanism. This has to do with how toilets work:

* Toilets produce more liquid than they use

This means that if we make a closed loop, our pipes will eventually clog up and our toilets will stop working. Fortunately, this is an easy problem to fix.

![ONI-Guide-QuickAndDirty3.png](assets/ONI-Guide-QuickAndDirty3-9aa6f83617.avif)

![ONI-Guide-QuickAndDirty4.png](assets/ONI-Guide-QuickAndDirty4-0d4759c460.avif)

Not like this. The pipes in this bathroom will clog up and our dupes will have accidents.

## The liquid overflow mechanism

![ONI-guide-WaterOverflow_edited.jpg](assets/ONI-guide-WaterOverflow_edited-26b934d7f5.avif)

Liquid overflow mechanism using a Liquid Bridge. Liquid always first tries to cross over a liquid bridge. In this design, that means the top tank would fill first, and only then would the bottom tank start filling up.

We need a way for excess water to be dumped out of our plumbing network. This is done using a bit of piping called a liquid bridge.

Something useful to know about liquid bridges:

* There is never any liquid in a liquid bridge. It teleports liquid from the input pipe to the output pipe. Meaning:
* You can deconstruct liquid bridges without any water spilling out

The liquid bridge has an input side (white) and an output side (green). One of the uses for a Liquid Bridge is to be able to run entirely separate pipes underneath it. Another use is to create that liquid overflow mechanism we need.

The way liquids work in Oxygen Not Included is that liquids "prefer" liquid bridges over other pipes. If a liquid comes to a point in a plumbing network where there is a liquid bridge and a normal pipe, the liquid will always first try to use the liquid bridge. Only if that isn't possible will it flow into the normal pipe.

This is probably easier to understand as an image. In the picture this "liquids prefer liquid bridges" -thing has been used to create a main storage tank and a secondary storage tank. The water being pumped will first try to pass over the bridge to the top tank. Only when both the tank and all the piping after the liquid bridge are full will the second tank start filling.

This is the mechanism we will use for our bathrooms - ensuring that our bathroom loop will have as much water as it needs, but any excess will be gotten rid of.

And now on to the builds. First the quick & dirty, then the full build.

Liquid overflow

Quick & germy

## The quick & dirty (read: germy) version

The bathroom feeds polluted water to a water sieve, which turns it to water and feeds it back to the bathroom.

You have to have a liquid overflow mechanism somewhere. It can either be before the water sieve or after it. This will determine if you get a small supply of polluted water or (germy) water.

![ONI-Guide-QuickAndDirty5.png](assets/ONI-Guide-QuickAndDirty5-c45215e305.avif)

Quick & dirty version 1. This produces polluted water as overflow.

![ONI-Guide-QuickAndDirty2.png](assets/ONI-Guide-QuickAndDirty2-2b8066012b.avif)

Quick & dirty version 2. This produces (germy) water as overflow.

## The full build: pictures and overlays

Pictures and overlays

I'll start with pictures and overlays of the build, including some close-ups of the confusing piping that comes before the liquid reservoirs. Then I'll go through how it works and give some options and tips for how to build it.

![ONI-Guide-BathroomDecontamination1.png](assets/ONI-Guide-BathroomDecontamination1-63c7db3e2a.avif)

Polluted (and germy) water decontamination build. In this picture I have some toilets and sinks, but I use the same build for all my decontamination. I'll tend to have several floors, one above the other, with all my showers, polluted water disposal, hospital, etc. They all then feed into the chlorine chamber.

![ONI-Guide-BathroomDecontaminationPipes.png](assets/ONI-Guide-BathroomDecontaminationPipes-3f0867e0fb.avif)

Plumbing overlay. The red circle to the left of the tanks is a liquid pipe element sensor, set to polluted water. The thing on the right of the tanks is a liquid shutoff.

![ONI-Guide-BathroomDecontaminationAutomation.png](assets/ONI-Guide-BathroomDecontaminationAutomation-e50226c217.avif)

Automation overlay. The liquid pipe element sensor is connected to the liquid shutoff.

![ONI-Guide-BathroomDecontaminationTrickyBit1.png](assets/ONI-Guide-BathroomDecontaminationTrickyBit1-e0eff54b04.avif)

A closer look at the confusing bit

![ONI-Guide-BathroomDecontaminationTrickyBit2.png](assets/ONI-Guide-BathroomDecontaminationTrickyBit2-106c334066.avif)

This is what the pipes to the left of the first reservoir look like when separated.

![ONI-Guide-BathroomDecontaminationTrickyBit3.png](assets/ONI-Guide-BathroomDecontaminationTrickyBit3-7d61e1d45a.avif)

And here they are combined, without the reservoir or the automation.

## How it works

The decontamination setup creates a loop that our bathroom water cycles around in forever. Polluted water gets cleaned and cycled back into the loop. Excess water is spit out of the build.

Chlorine is used to get rid of the germs in the polluted water. Chlorine kills germs quickly but not instantly. So we need to make sure our polluted water stays in the chlorine room long enough that all germs are gone. This is done with the help of three liquid reservoirs and some automation.

As long as all three liquid reservoirs stay full, all germs will be gone by the time germy polluted water passes through all three tanks to the water sieve.

To make sure all liquid reservoirs are full this design uses a liquid bridge pipe design and a bit of automation. This design is such that it will send a signal when all three tanks are full.

Liquids will always cross a liquid bridge if possible. There is an automation sensor to detect liquid in a pipe section that is placed after a liquid bridge. This means that polluted water will only enter the pipes, and trigger the sensor, once all the reservoirs are full.

After the liquid pipe element sensor there is another liquid bridge that sends the polluted water back onto the main liquid pipe.

Some example pictures might to a better job of explaining this mechanism. In the pictures below, the same mechanism is used as in the actual build. Only when the tank is full will polluted water trigger the sensor and trigger the liquid shutoff to let polluted water pour out.

How it works

![ONI-Guide-BathroomDecontaminationHowItWorksPipes.png](assets/ONI-Guide-BathroomDecontaminationHowItWorksPipes-c4bbdee228.avif)

How it works: plumbing overlay. Polluted water crosses the liquid bridge if it can. Only when the pipes are full will polluted water go straight up and trigger the liquid pipe element sensor.

![ONI-Guide-BathroomDecontaminationHowItWorksAutomation.png](assets/ONI-Guide-BathroomDecontaminationHowItWorksAutom-1bf65da9f5.avif)

How it works: automation overlay. When triggered, the liquid pipe element sensor sends a signal to the liquid shutoff which opens it and lets liquid through.

The liquid shutoff stays open for as long as new polluted water enters the system. If polluted water stops entering the system, the pipe section with the liquid element sensor empties. The sensor then sends a signal to shut off the liquid shutoff.

With the mechanics out of the way, let's move on to building. This can be done the easy way or the less easy way.

This has to do with how chlorine works in the game:

* Chlorine kills germs in liquid reservoirs, but
* Chlorine does not kill germs in liquid pipes

This means that if you just build everything and hook it up, there would still be germs in the water coming out of your decontamination setup. This is because there would be germs in the pipes in the chlorine room, even after the chlorine had killed all the germs in the reservoirs.

## Building the thing: the easy way

If you have access to germ-free, polluted water on your map then you have it easy.

* You can find germ-free polluted water in the slime biome

This is the approach I use and the approach I recommend (as long as you have access to germ-free polluted water).

You can build the entire setup, pipes automation and all. But don't pump any clean water into it. And, if you have a polluted water dumping station, don't activate it yet. Basically, keep dupes away from your build until it's ready.

To get it ready is easy. You will need to fill your (clean) water pipes to get things going. You can pump in clean water from somewhere. Or, what I usually do, is run whatever polluted water source I tapped into for a while to turn it into water.

Whatever approach you choose, when your polluted water tanks are full and your bathrooms etc. have water you are ready to go.

This setup can also be used to turn the polluted water you have lying around your base into water. Add a liquid bridge to make sure the decontamination setup prioritizes your bathroom output (see example picture below).

Easy way

![ONI-Guide-BathroomDecontamination2.png](assets/ONI-Guide-BathroomDecontamination2-ebcdbac5e0.avif)

Getting things going. Polluted (but germ-free) water pumped in from the map to fill the bathroom buildings with clean water. If you connect external polluted water using a liquid bridge, the system will prioritize polluted water from your bathrooms, and whenever there isn't any bathroom water to decontaminate, it will decontaminate polluted water from the external pipe.

This build still requires you to create a vacuum and then fill it with chlorine. How to do that is covered in the description of building this the less easy way. Scroll down a bit or clicky here: creating a vacuum, and filling the vacuum room with chlorine.

If you don't have access to germ-free polluted water you will have to do things the less easy way.

## Building the thing: the less easy way

In this approach you can't build the whole thing all at once, it needs to be done in stages.

Build all your bathrooms etc. and have them feed to the three liquid reservoirs. You will need to feed (clean) water into the system from somewhere.

Your dupes will now slowly start filling the reservoir tanks with polluted water they "produce." (This polluted water will have germs.)

Less easy

![ONI-Guide-BathroomDecontaminationOption2_1.png](assets/ONI-Guide-BathroomDecontaminationOption2_1-569e135f99.avif)

Step 1. Use an external water source, polluted water (slowly) fills the three reservoirs as dupes your your bathrooms etc. The straight line of piping connecting the three liquid reservoirs is temporary and will be deconstructed when the reservoirs are full.

While the three liquid reservoirs are filling, you can prepare the area for creating a vacuum room that we will then fill with chlorine.

We will be deconstructing pipes, so building the vacuum room now will also stop polluted water from spilling down into your base.

## Building a vacuum room

We want a room full of chlorine. If our room were to have a lot of chlorine but also a small of amount of some other gas, then we wouldn't know for sure if the germy polluted water will spend enough time in chlorine to kill all the germs. So we want only chlorine in our chlorine room.

To make sure we only have chlorine, we will have to build a room and then empty it of all gases - create a vacuum. But we also want to be able to access the room once it's a vacuum. To accomplish this, we will need something called a liquid lock.

A liquid lock lets dupes pass through, but not gases. Then we pump out all the gases in the room and finally we fill the room with chlorine. (There's a separate section of the guide on this topic if you want more: [Liquid lock basics](https://www.guidesnotincluded.com/liquid-lock-basics).)

You can build either a proper liquid lock or a half-assed, quicker-but-riskier versions. Since this is a temporary liquid lock, I build the quicker version.

Vacuum

![ONI-Guide-BathroomDecontaminationVacuum1.png](assets/ONI-Guide-BathroomDecontaminationVacuum1-a0825968fb.avif)

Building a vacuum room: liquid lock. Build the left wall, then build a bowl-like structure, as seen in the picture.

Now we want to empty out all the gases in the area with the liquid reservoirs. So we create a liquid lock in the bowl thing and then use a gas pump to pump out the gases.

In Oxygen Not Included, a tile can only contain either a gas or a liquid, not both. If you don't mind using (read: abusing) this mechanic a bit, you can create a quick liquid lock by just emptying a bit of liquid into the bowl.

Note: if you build the quick & risky version, put the bottle emptier on the far side of the liquid lock, away from the vacuum room. If you remember to do that, the quick & risky version becomes a quick & not really particularly risky version.

(You don't need to know why to do it that way, but if you want to know: it is because if the bottle emptier is on the side with the vacuum room, there might be a pocket of oxygen in the middle tile. Dupes can breathe the oxygen in that tile while standing on the liquid lock tile with a bit of water in the vacuum room. Then they can breathe out carbon dioxide into the vacuum room.)

![ONI-Guide-BathroomDecontaminationLiquidLock1_edited.jpg](assets/ONI-Guide-BathroomDecontaminationLiquidLock1_edi-7563eb0f9d.avif)

Liquid lock. The quicker but a bit riskier version. Make sure you have some water on the two tiles, as in the pic. Put the bottle emptier on the far side, away from the vacuum room.

![ONI-Guide-BathroomDecontaminationLiquidLock2.png](assets/ONI-Guide-BathroomDecontaminationLiquidLock2-bc93309fde.avif)

![ONI-Guide-BathroomDecontaminationLiquidLock3.png](assets/ONI-Guide-BathroomDecontaminationLiquidLock3-e95fba0612.avif)

Liquid lock. The slower, safer version. Fill the bottom tile of the liquid bowl and about 100 kg or so per tile of the three upper tiles. When you build the final tile above the water it will "pull" the water up to the tile, stopping all gas movement between the sides.

![ONI-Guide-BathroomDecontaminationLiquidLock4.png](assets/ONI-Guide-BathroomDecontaminationLiquidLock4-82ee839a2f.avif)

Pump out all the gases. The gas vent will not allow gases to exit if the gas pressure is above 2 kg. If that becomes a problem, you can build a long gas pipe with several gas vents along it (or use a high pressure gas vent, if you have plastic).

## Delete five bits of pipe

When the liquid reservoirs are full, you can delete the temporary pipes. (This can be done before or after building the airlock and pumping out the oxygen. If you do it after, you will have a bit of additional polluted oxygen to pump out.)

If you have a dupe with the plumbing skill, you can empty the pipes before deleting them. This is done using the Empty Pipe icon in the bottom right.

If you don't have a plumber, you will have to go for the messy option: just delete the pipes, let the polluted water spill out and then mop up the mess.

On deconstructing pipes:

* An easy way to deconstruct pipes - and only pipes - is to select the Plumbing Overlay and then pres "X". Now you will delete only the pipes.

Delete pipes

![ONI-Guide-BathroomDecontaminationDeletePipes.png](assets/ONI-Guide-BathroomDecontaminationDeletePipes-fc9c5ec5e8.avif)

Delete five bits of pipe. Delete the section of pipe that goes from the white input port on the leftmost tank to the white input port on the rightmost tank. (If you have a dupe with the plumbing skill you can empty the pipes first.)

![ONI-Guide-BathroomDecontaminationDeletePipes2.png](assets/ONI-Guide-BathroomDecontaminationDeletePipes2-4c8a1bd21e.avif)

When done deconstructing, issue a mop command (if necessary) and a sweep command to get all the bottles of polluted water out of the room. Polluted water bottles can emit polluted oxygen, which we don't want in our chlorine room.

Dupes will only sweep up polluted water bottles if there is a bottle emptier somewhere that is set to accept polluted water. If you don't have one as part of your bathroom build, build a temporary one somewhere.

When the polluted water bottles are gone and the room is a vacuum, you can delete the gas pump. If you want to see your progression towards a vacuum, you can check gas pressure levels using the Materials Overlay (click the square icon in the top right, or F4).

Dupes shouldn't exhale carbon dioxide in a room full of nothing (vacuum) or of chlorine. (I've only once had carbon dioxide get into my vacuum room. Not sure why, might have been that I was using a quick & risky liquid lock.)

Note: flatulent dupes will emit natural gas wherever they are, even in your vacuum or chlorine rooms. So if you have flatulent dupes, keep them away from the build.

Chlorine

## Filling the vacuum room with chlorine

There are two main ways to get chlorine into the room:

1. Find chlorine on the map. Then pump it through a gas filter (set to chlorine) and either pump it straight in to your chlorine room or use a canister filler and canister emptier to get it in.
2. Use bleach stone

Bleach stone is probably the more beginner-friendly approach. It's also quick and easy, and the approach I use.

Bleach stone can be found in the caustic biome - the one with a lot of purple.

![ONI-guide-BleachStone_edited.jpg](assets/ONI-guide-BleachStone_edited-fb285f6842.avif)

Bleach Stone

Once you dig up some bleach stone, it will start emitting (small amounts of) chlorine. So the idea is simply to dig some up bleach stone and put it in the vacuum chamber. As the bleach stone emits chlorine, the room will turn into our chlorine room.

* Build a Storage Bin in the room
* Set it to only accept Bleach Stone. Bleach Stone is found in the Sublimators category. It is at the bottom of the list, in the Non-Standard category.
* Note: Bleach stone will only become available as an option when you have dug some up. If it isn't visible, check again after digging some up.
* Raise the Storage Bin priority (to 7 or so)
* Dig up some bleach stone (if you don't have any)
* Set a sweep command for the Bleach Stone

Dupes will then move the bleach stone to the storage bin and the room will fill up with a slowly but steadily increasing amount of chlorine.

Some chlorine may get into your base during this process. It's not a big deal, we can clean it up later. (Or say we will but then somehow never quite get around to it.)

![ONI-Guide-BathroomDecontaminationChlorineRoom1.png](assets/ONI-Guide-BathroomDecontaminationChlorineRoom1-7ce28db649.avif)

Storage Bin for bleach stone

How much Bleach Stone should you use?

The way chlorine works in the game is that any amount of it is as good as lots of it. Meaning it doesn't matter how much (or little) bleach stone you put in the room. I usually set the storage bin to 100 kg, which seems to be more than enough. (You lose half the mass when mining, so it equals digging up 200 kg worth of bleach stone tiles.)

Once the Bleach Stone is in the storage bin you can delete the storage bin.

If you have some other storage bin in your base set to bleach stone, you will have to temporarily disable it if you don't want your dupes to come remove the Bleach Stone you have here.)

Once this is done, we wait for the chlorine to work its magic on the germs in our reservoir tanks. Using the Germ Overlay, keep an eye on the tanks. When they are germ-free, we can continue.

![ONI-Guide-BathroomDecontaminationChlorineRoom2.png](assets/ONI-Guide-BathroomDecontaminationChlorineRoom2-ecfa4f47a9.avif)

Decontaminating the tanks. Use the germ overlay (germ icon top right) to see when all germs in all tanks are gone.

## Completing the chlorine room: pipes and automation

Now we can build the final bits of pipe an automation, close off the chlorine room and make space for the water sieve.

Piping: connect the upper liquid bridge to the input port of the leftmost liquid reservoir. Connect the output ports of the reservoirs to the input ports of the reservoirs to their right.

Add a pipe section from the rightmost reservoir to a liquid shutoff.

Note: the reservoir should be piped to the input port of the liquid shutoff, meaning the white bit.

Add a pipe section from the output port (the green bit) of the liquid shutoff that goes out into the wall on the right.

Completing build

![ONI-Guide-BathroomDecontaminationChlorineRoom4.png](assets/ONI-Guide-BathroomDecontaminationChlorineRoom4-122eb54e5e.avif)

Piping. Connect the upper liquid bridge to the reservoir. Connect the reservoirs to one-another. Connect the last reservoir to a liquid shutoff and add a pipe from the liquid shutoff to the wall.

Automation: On the left, a liquid pipe element sensor set to polluted water. On the right a liquid shutoff. Connect the two with automation wire.

![ONI-Guide-BathroomDecontaminationChlorineRoom3.png](assets/ONI-Guide-BathroomDecontaminationChlorineRoom3-96f10397c2.avif)

Automation. A liquid element sensor on the pipe section between the input ports of the liquid bridge. A liquid shutoff at the end. Connect them with automation wire.

Power: The liquid shutoff needs 10 W of power. To future-proof the design, connect it using conductive wire (the kind of wire that can handle 2000 W).

When I build this I'm usually still using regular wire for powering my base. Then I make enough refined metal to do a short section of conductive wire, from the liquid shutoff to the wall.

![ONI-Guide-BathroomDecontaminationChlorineRoom5.png](assets/ONI-Guide-BathroomDecontaminationChlorineRoom5-bd3dc4b224.avif)

Power overlay. Remember to add a small section of power wire so you can power up the liquid shutoff when you're done.

Then build up the wall on the right of the liquid shutoff, sealing up your chlorine room. Delete the remains of the liquid lock. (Let the water pour wherever or pump it out first. We just want to get rid of it - we need the space.)

![ONI-Guide-BathroomDecontaminationChlorineRoom6.png](assets/ONI-Guide-BathroomDecontaminationChlorineRoom6-1f0ab997ec.avif)

Close off the chlorine room, delete the liquid lock tiles.

Now add a water sieve, with the pipe from the chlorine room connecting to the water sieve input (the white bit). The water sieve uses sand, so you can add a storage bin set to sand (found under the category filtration medium).

The water sieve output should connect to a liquid bridge. This will function as your mechanism to get rid of excess water. Have the liquid bridge lead back in to your (clean) water intake piping. Then have a second line branch off to wherever you want your excess clean water to go. (A SPOM, bristle blossoms, your water storage, etc.)

![ONI-Guide-BathroomDecontaminationComplete1.png](assets/ONI-Guide-BathroomDecontaminationComplete1-761b680daa.avif)

![ONI-Guide-BathroomDecontaminationComplete2.png](assets/ONI-Guide-BathroomDecontaminationComplete2-fa45822401.avif)

Once the first liquid reservoir tank in the chlorine room fills up (it lost a small amount of polluted water filling up the pipes in the chlorine room) your water reclaiming system will start outputting clean water. You can now disconnect your original water source from this build.

Give yourself a pat on the back - you should never again need to worry about your bathroom water supply.

Optional build: excess polluted water instead of water

You can put the liquid bridge overflow mechanism before your chlorine room if you want. Then you will get a small, steady supply of polluted water instead of water. This can be used, for instance, to feed a thimble reed for a small supply of reed fiber.

---

*Archived from [https://www.guidesnotincluded.com/recycling-toilet-water](https://www.guidesnotincluded.com/recycling-toilet-water) ([Wayback Machine snapshot](https://web.archive.org/web/20250731071301id_/https://www.guidesnotincluded.com/recycling-toilet-water)). Original work © Some Random Finn / guidesnotincluded.com, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Reformatted from HTML to Markdown for this non-commercial community archive — see [Attribution & licensing](attribution.md).*
