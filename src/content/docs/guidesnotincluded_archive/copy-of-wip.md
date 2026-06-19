---
title: "WIP"
description: "5) Get your research on with the Research Station"
source_url: https://www.guidesnotincluded.com/copy-of-wip
archived: 2025-04-27
archive_snapshot: https://web.archive.org/web/20250427193257id_/https://www.guidesnotincluded.com/copy-of-wip
---

Contents:

* Decor and cleaning up
* Expanding base, planning ahead
* Know your biomes - slime biome
* Water lock
* Medical building
* Reed Fibre (or Dreckos)
* Water storage

5) Get your research on with the Research Station

6) Food

7) Compost - dealing with polluted dirt

8) Advanced research - the Super Computer

Players tend to divide the game into the early game, mid game and late game. But exactly where people draw the lines between them varies. I have needed to draw some arbitrary lines here as well. This guide is structured as follows:

## Choosing dupes

A little bit about interests and traits

## Very early game

1) Outhouses, wash basins and access to water

2) Beds (in temporary locations)

3) Power, part 1: the hamster wheel and battery

4) Oxygen: the Oxygen Diffuser

5) The Research Station (and some research)

6) Food

7) Compost - dealing with polluted dirt

8) Advanced research - the Super Computer

## Early game

9) Dining room (Great Hall)

10) Plumbing - toilets and sinks

11) Dealing with polluted water bottles and polluted oxygen

12) Dealing with carbon dioxide

13) Power, part 2: Coal generators

## Getting started with automation

14) Automating your coal power generator

15) Automating your carbon skimmer

## Ranching: optional but useful

While there are benefits to ranching, you don't need to do it if you don't want to. So it is covered as its own optional bit.

Tip: Going where no dupe has gone before: Exploring the map

Know your biomes and geysers.

TIP: decore Cleaning up your mess - decor and debris

Mid (or maybe late) game stuff

Decontaminating water

Atmo suits

SPOM

Petroleum

Plastic

Cooling - using AETN or using aquatuner

* Rooms get room bonuses by fulfilling certain requirements.

* You can see the available room bonuses and requirements in the Room Overlay (top right, or press F11).

* The most common maximum room size is 64 tiles. This equals a 4x16 room: 4 tiles high, 16 tiles wide. (Or 18 tiles wide if you include the outer walls.)

* The maximum size for a ranch is 96 tiles. This equals a 6x16 room. (6 tiles high, 16 tiles wide - or 18 if you count the outer walls.)

For my fellow neat-freaks

* If you want a neatly structured base you can make your floors 18 tiles wide and then vary room hight depending on the max room size.

* (The above suggestion is in no way a necessity, but be warned: years ago I read someone suggest it on a forum, and since trying it for the first time I have been both physically and pshychologically incapable of ever not building my bases using the X tiles high by 18 tiles wide approach.)

## Tip: room sizes - and room bonuses

## AUTOMATION BASICS

Automation takes a little bit of getting used to but can be very useful, so it's worth getting the hang of. Let's start with some basics.

Oversimplified, automation allows you to tell the game:

* When [a thing] happens, I want [another thing] to happen.

Let's look at some examples.

A common early automation project is to do with coal generators. Here, automation is used to tell the game:

* When [my battery is fully charged], I want [my coal generator to stop running].
* When [my battery is low on charge], I want [my coal generator to start running].

There are various machines your dupes need to fill - like filling your coal generators with coal. Another use for automation is to say:

* When [my coal generator is running low on coal], I want [to fill it up with coal].

You might also want to use automation to control what gasses are allowed in your base.

* When [the gas near this gas pump is not oxygen], I want [the gas pump to kick in and pump it away].

Exactly how you tell the game these things will vary depending on what you are automating. Some things are as easy to automate as just running an automation wire between two things (like a goal generator and a batter). Other things require some additional things, often an automation sensor.

There are lots of different kinds of sensors in the game. Sensors for temperature, gas type, liquid type, amount of germs, time of day (what part of the cycle it is), and on and on. These can all be used to define, and send the game, those "when [a thing] happens..." -commands.

These were just a few things - you can do crazy amounts of crazy things with automation. But we'll focus on the simpler stuff. However, there are some things you'll need before you can get automating.

Automation prerequisites

* You will need to unlock automation-related stuff through research.
* You will need refined metals (early-game you can make them with the Rock Crusher).
* Some things require the Mechatronics Engineer skill (at the end of the Operating/Supplying skill tree) to be able to build.

That's enough theory - let's get automating.

![CBCIGtoONI_Automation1.png](assets/CBCIGtoONI_Automation1-27c7b42663.avif)

Simple Coal Generator automation. Using Automation Wire, the Coal Generators are connected to a Smart Battery.

## AUTOMATING YOUR COAL GENERATOR

Research required:

* Sound Amplifiers (under Power)
* Smart Home (under Computers)
* Brute-Force Refinement (under Solid Material)

We will need refined metal. (In our case, we will turn Copper Ore into Copper.) So first,

* Build a Rock Crusher (under Refinement)

It generates a lot of heat, so keep it away from your plants. This can be a temporary placement. You can also (particuarly if it is a long-term spot for the Rock Crusher) put a Storage Bin (or several) nearby, set to Metal Ore (either all kinds or just some) - the raw materials needed for making refined metal.

One Rock Crusher placement option, useful if you don't want to add additional strain to your normal power wire, is to put the Rock Crusher next to your coal generator. Then you can connect it directly to your coal generator using Heavi-Watt Wire. (This means there is one less machine drawing power along your regular wire.) It is worth knowing that Heavi-Watt Wire has a significant negative decor value.

Once your Rock Crusher is built,

* order up 5 Copper (Iron works fine, too - I'm just assuming you have more copper ore)

Remember you can raise the priority on the rock crusher. To make using the rock crusher more imporatnt to some dupe, you can change dupe priorities.

* Operating the rock crusher falls under the "Operating" Duplicant Priority errand type

Once we have our Copper we are ready to go. To automate our coal generator we will need to

* Replace our Jumbo Battery with a Smart Battery (under Power)
* Connect our Smart Battery to our Coal Generator(s) using Automation Wire (under Automation)

When you start building Automation Wire, it will open the Automation Overlay. This will show you where the automation connection points are.

You want to connect the smart battery and the coal generator(s) with one continuous Automation Wire. Do not connect the Power Tanfsormer, Rock Crusher, or anything else.

With this done, there is one more thing we need to do: tell our new automated system what we want to have happen.

Telling the automation what to do

Thanks to the Automation Wire connecting your Smart Battery and your Coal Generator, your battery can now send messages - commands - to your coal generator(s).

Click on the Smart Battery and you will see something called "Logic Activation Parameters." They include a"High Threshold" and a "Low Threshold." Don't mind the wording - it's just a fancy-pants way of saying "stop" and "go."

The high and low thresholds relate to how fully charged - or how close to empty - the Smart Battery needs to be before a command is sent to the coal generator.

* The High Threshold is used to send a "Stop the coal generators - I'm sufficiently full!" command (also called a red signal).
* The Low Threshold is used to send a "Fire up the coal generators - I need charging!" command (a green signal).

You set the upper number to how full you want to battery to be for the coal generator to stop. You set the lower number to how low you want the battery charge to go before the coal generator charges it again.

The default values are 100 and 0. Letting the battery empty completely could cause problems, so raise the lower figure. I use figures I picked up from Francis John:

* High threshold: 95
* low threshold: 60

(The reason for 95 instead of 100 is that the coal generator automation takes a while to run. If it starts when you are at 99%, say, then you might waste a bit of coal.)

Future uses for this

For now, this automation is useful to stop your coal generator(s) from running unnecessarily. Later in the game, you will most likely have several sources of power. Then you can use these thresholds to define in what order power sources should be used.

This is done by having (at least) one Smart Battery per type of power producer you have. All the batteries are connected to your power grid. But - and here's the important bit - each type of power producer (Coal Generators, Natural Gas Generators etc.) are connected, with Automation Wire, to their own Smart Battery.

The charge in all batteries will be the same, since they are connected to the same power grid. But because you have separate automation wires, you can send individual commands to the different types of power generators.

You can set different start and stop levels for your different kinds of power. You could, say, have

* Solar panels - solar power is always on (while the sun is shining)

You can hope that solar power will be enough - that you can charge enough batteries during the day that their charge lasts all night. But, to be safe, you can automate other power producers to kick in if batteries get low.

* Natural Gas Generators can be set to be idle if the batteries are more than 50% charged. Once the batteries drop to below 50% charge, the Natural Gas Generators kick in.
* Coal Generators set to kick in if the batteries drop to below 30%. (And could be set to turn off when the batteries are at, say, 40% to lessen the amount of carbon dioxide produced.)

For this build, you will need to research:

* Plumbing
* Sanitation
* Improved Plumbing

They are all in the Liquids research branch.

Building this project includes the following steps (the order you do them in doesn't matter):

* Build toilets - called Lavatories, found under Plumbing - and Sinks, found under Medicine.
* (When deciding where to put toilets and sinks, remember the stuff about germs and making dupes pass a sink to wash their hands after using the bathroom.)
* Build a Liquid Pump (found under Plumbing) in a body of (clean) water.
* Build a Liquid Reservoir (found under Home). Placement isn't hugely important, but try to put it somewhere where it won't be in the way for several dozen cycles (or more).
* Using Liquid Pipe (under Plumbing), connect the water pump to the toilet and sink inputs - the white bits.
* Also using pipes, connect the toilet and sink outputs (the green bits) to the input (the white bits) of the Liquid Reservoir.
* The finished piping should go:

  + from the pump to the white bits on the toilets and sinks.
  + from the green bits on the toilets and sinks to the while bit on the liquid reservoir.
* When finished, connect your Liquid Pump to your power grid (using Wire, under Power).

Water should now start flowing along your pipe(s) and into your toilets and sinks.

Mouseover your toilet and, if everything worked, it should say "Lavatory Ready." If it doesn't say that (and trust me - we've all been there), it's time to start debugging - start by checking inputs and outputs.

Early game

8) Great Hall

9) Refined metal

10) Dealing with carbon dioxide

11) Plumbing - toilets and sinks

12) Power, part 2: Coal generators

13) Cleaning up your mess - decore and debris

oxygen cealning and polluted water form toilets

Optional (but useful): Ranching

While there are benefits to ranching, you don't need to do it if you don't want to. So it is covered as its own optional bit.

Getting stared with automation

Automation is a huge help and you're better off getting over any fears of using it right away. Which is what this next section will do.

14) Automating your coal power generator

15) Automating your carbon skimmer

Mid-game stuff, part 1

Switching to Bristle Blossoms

Decontaminating water

Atmo suits

Plastic

Cooling

Late game

SPOM

Petroleum

Rooms and bonuses

Air flow

Basic survival

Ranching (optional)

Oxygen

Water decontamination

Decor, cleaning up

Know your biomes

Slime biome

Know your geysers etc.

Reed fibre

Atmo suits

Plastic

Cooling

1. Toilets and wash basins
2. Access to water
3. Beds (in temporary locations)
4. Power (hamster wheel) and battery
5. Oxygen
6. Research station
7. Food
8. Advanced research station

## 11. DEALING WITH POLLUTED WATER BOTTLES AND POLLUTED OXYGEN

You will end up with polluted water bottles in your base, from your early toilet setup and from any accidents your dupes may have had. With some plumbing basics researched, we can now get rid of them.

To do this, we will set up a place to dump the polluted water, with a pump to pump it into the liquid reservoir of polluted water. This can either be a temporary thing you deconstruct afterwards or a permanent place for dupes to dump polluted water bottles in the future.

Dupes get germy from carrying polluted water bottles. Once this project is done, send germy dupes past sinks to wash their hands and do a large-scale disinfection of the base - using the Disinfect buildings command on the bottom right (or press "I").

## 12. DEALING WITH CARBON DIOXIDE

Dupes exhale carbon dioxide (you can see the Oxygen Overlay by clicking its icon in the top right or pressing F1).

When carbon dioxide levels rise into your base, dupes will have to intermittenly run up into the oxygen layer to gasp for air. So having a machine (or worse - a bed) in carbon dioxide isn't great.

There are two approaches to carbon dioxide buildup in your base: Deal with it later and Deal with it now.

Deal with it later

Since carbon dioxide is heavier than oxygen, you can dig a carbon dioxide pit: basically just a ladder going down, with a few tiles dug out around it. Then you can extent the ladder further and further down as carbon dioxide piles up in your base.

Note: digging a deeper and deeper carbon dioxide pit will become slower and slower as dupes need to hold their breath for longer and longer as they go down to dig.

Deal with it now

Later in the game there is some limited use for carbon dioxide. For now, let's just get rid of it. We'll do this with a Carbon Skimmer.

Carbon skimmer basics

* The Carbon Skimmer is unlocked through research: under Air Systems, the second step in the Liquids research branch.
* The carbon skimmer uses water as its input and outputs polluted water.
* (Though polluted, the water is germ-free.)
* The carbon skimmer only gets rid of carbon dioxide - it does not produce oxygen.

Carbon skimmer placement

The carbon skimmer will define the point where oxygen will end and carbon dioxide will begin: carbon dioxide will build up to the carbon skimmer, not above it.

When deciding where to place your carbon skimmer

* one option is to put it at the botttom of your base. (Or to dig down to what you think will be the bottom of your base once you are done expanding.)
* Another option is to put it further down your ladder network. You will eventually want to dig down to the oil biome (but don't go there without Atmo Suits! - we'll cover them later) and other biomes below your starting biome. A carbon skimmer further down a ladder network will mean dupes can breathe there, too.

* It might not seem like it when you first start playing, but heat has ended many a game of Oxygen Not Included.

* The way heat usually gets you is your food: Mealwood and Brislte Blossoms can be at most +30 C to grow.

* With late game technology you can keep your base cool. Until then, you need to give some thought to it.

* Buildings generate varying amounts of heat. You can see the amount they generate in the build menu under Heat.

* The amount of heat generated is given in DTU/s. I have absolutely no idea what that is. But comparing buildings will give you some idea, e.g.:

  + a Ceiling Light generates 500 DTU/s
  + a Rock Crusher generates 16.000 DTU/s

* Try to keep buildings that generate significant amounts of heat a fair distance away from any area where you grow food.

## Tip: heat basics - food

## 13. POWER, PART 2: THE COAL GENERATOR

The hamster wheel is adorable, but can take a significant amount of time out of your dupes' day. Also, you will eventually need more power than a hamster wheel can provide.

You can free up dupes for other taks and have more power available in your power grid by upgrading to coal power. (If this seems intimidating, don't worry - you will have it up and running in no time.)

---

*Archived from [https://www.guidesnotincluded.com/copy-of-wip](https://www.guidesnotincluded.com/copy-of-wip) ([Wayback Machine snapshot](https://web.archive.org/web/20250427193257id_/https://www.guidesnotincluded.com/copy-of-wip)). Original work © Some Random Finn / guidesnotincluded.com, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Reformatted from HTML to Markdown for this non-commercial community archive — see [Attribution & licensing](attribution.md).*
