---
title: "Temperature transfer basics"
source_url: https://www.guidesnotincluded.com/heat-transfer-basics
archived: 2025-08-11
archive_snapshot: https://web.archive.org/web/20250811145919id_/https://www.guidesnotincluded.com/heat-transfer-basics
---

# TEMPERATURE TRANSFER BASICS

## Disclaimer

I didn't pay anywhere near enough attention during physics class at school to understand the true nitty-gritty of this stuff. I'll cover some basics, the wiki and forums have more in-depth coverage.

## Introduction

The basic idea is simple enough: when things come into contact, their temperatures affect one another. The colder thing gets hotter, the hotter thing gets colder.

There are two additional things to consider that affect this exchange of temperature:

* There are specific kinds of tiles and pipes that are intended to increase or decrease temperature transfer.
* All materials in the game (sandstone, copper, etc.) have properties that affect this temperature transfer.

We'll start by looking at different kinds of tiles intended to maximize or minimize temperature transfer.

## Insulated tiles

![Building_Insulated_Liquid_Pipe.webp](assets/Building_Insulated_Liquid_Pipe-bd27c4ad41.avif)

![Building_Insulated_Gas_Pipe.webp](assets/Building_Insulated_Gas_Pipe-f0baf06134.avif)

![Building_Insulated_Tile.webp](assets/Building_Insulated_Tile-79495c0972.avif)

If you want to minimize temperature transfer between tiles you can use insulated versions of whatever you are building.

There are:

* insulated liquid pipes
* insulated gas pipes
* insulated tiles

If you will be pumping hot liquid or gas through an area that you don't want to heat up, it's a good idea to use insulated pipes.

If you have a hot biome next to your base, you can minimize temperature transfer by building a wall of insulated tiles between the hot biome and your base.

Note: about Abyssalite

Biomes are separated by abyssalite - they are those purple (naturally occurring) tiles. Abyssalite is a superb insulator. If you have abyssalite between your base and a hot (or cold) biome then you don't need to worry about temperature transfer.

But keep in mind that when your starting area is placed in the game, it will most likely be placed over some of these abyssalite tiles. This will delete a section of the abyssalite and enable temperature transfer between biomes.

![ONI-guide-TempTransfer3.png](assets/ONI-guide-TempTransfer3-d2867ec9f5.avif)

![ONI-guide-TempTransfer4.png](assets/ONI-guide-TempTransfer4-4d30c7e5e3.avif)

Magma above, an ice biome below. (Temperature overlay on the right.) They are separated with a combination of insulated tiles and naturally occurring abyssalite tiles.

(This is getting ahead of things, but a note on magma. As one might expect, it's rather warm: over +1400C. Magma will melt most materials, but won't melt obsidian. So anything that will come in contact with magma, make out of obsidian.) (Also, always create a vacuum before dealing with magma.)

## Radiant pipes and metal tiles

![Building_Radiant_Liquid_Pipe.webp](assets/Building_Radiant_Liquid_Pipe-dcf3ff9306.avif)

![Building_Radiant_Gas_Pipe.webp](assets/Building_Radiant_Gas_Pipe-d7fbba8f51.avif)

![Building_Metal_Tile.webp](assets/Building_Metal_Tile-c2964ccbbc.avif)

Sometimes you will want to maximize temperature transfer. In such cases you'll want to use radiant pipes or metal tiles.

There are:

* radiant liquid pipes
* radiant gas pipes
* metal tiles

Some examples: cooling down oxygen coming out of a SPOM, maximizing temperature transfer between two areas that are separated by a wall, and a cooling loop running through your base (where you might want radiant pipes to maximize the cooling in a certain area, like around a machine that produces a lot of heat).

## Tempshift plates

Tempshift plates improve temperature transfer between the tile itself and the tiles surrounding it, including diagonal tiles.

![Building_Tempshift_Plate.webp](assets/Building_Tempshift_Plate-1f8d1a4c8c.avif)

## Material properties that affect temperature transfer

![ONI-guide-AETNOverflow.png](assets/ONI-guide-AETNOverflow-7a47ccf7c2.avif)

An overflow mechanism (gas bridge) used to send excess hydrogen into the AETN room to improve the transfer of its chill.

![ONI-guide-TempTransfer2.png](assets/ONI-guide-TempTransfer2-9b0077bdd3.avif)

![ONI-guide-TempTransfer1.png](assets/ONI-guide-TempTransfer1-33dcb3974f.avif)

Metal tiles used as a temperature transfer helper in cooling. A [cooling loop](thermo-aquatuner-steam-turbine-cooling-loop.md) cools the water in the radiant pipes. The radiant pipes cool the metal tiles. The metal tiles cool the metal volcano output as it is sent along the conveyor rail.

The first step in dealing with heat is thinking about when you want insulated, radiant, or normal tiles. When you are comfortable enough with them, the next step is to also think about what material you build those tiles out of.

Materials in Oxygen Not Included have two properties that will affect how their temperature interacts with the temperature around them: thermal conductivity and specific heat capacity.

To see the thermal conductivity and specific heat capacity of something, click on it. Then click on the "Properties" tab.

Thermal conductivity is a measure of how quickly or effectively it can exchange temperature with its surroundings.

Specific heat capacity is a measure of how much heat it can "store."

So thermal conductivity is a measure of how quickly it will heat up or cool down, and specific heat capacity is a measure of how much heat or chill it can store.

Of these two, thermal conductivity is usually the more important one to consider. (When designing for temperature transfer, I think of good thermal conductivity as an important aspect and a good specific heat capacity as a nice bonus.)

Just like (for instance) a radiant pipe will have better temperature transfer than a normal pipe, a pipe made out of a material with a high thermal conductivity will have better temperature transfer than one built from a material with a low thermal conductivity.

So the rule of thumb is:

* to increase temperature transfer, use a material with a higher thermal conductivity number.
* (and also the other way around: lower thermal conductivity for less temperature transfer)

A list of the thermal conductivity of different materials can be found [on the wiki](https://oxygennotincluded.fandom.com/wiki/Thermal_Conductivity). Some general early-game guidelines:

Of the minerals you will commonly come across:

* granite is good for increasing temperature transfer
* igneous rock is good for decreasing it

So for instance:

If you want to improve temperature transfer in a cooling loop but don't want to use up your metal on making the whole loop out of radiant pipes, you can choose a regular material with a higher thermal conductivity. Granite is a popular choice for this.

If you want to make your insulated pipes or tiles as effective insulators as possible, a popular choice among the common starting materials is igneous rock.

For things that can get very hot, which early(ish) game would include a pitcher pump in the oil biome and pipes coming out of a glass forge, use ceramic. (Ceramic is made with a Kiln, built under Refinement.)

Of the various metals you may have access to early on, aluminium is likely to have the best thermal conductivity. (But copper or iron will usually work fine, too.)

A vacuum (meaning there are no gases) is the best insulator.

Gases differ in their ability to aid temperature transfer. For example, hydrogen has a much better thermal conductivity than oxygen. To improve temperature transfer in an area, you can fill it with hydrogen. One example of when you might do this is filling an Anti Entropy Thermo-Nullifier room with hydrogen.

Metal tiles are an excellent way to improve temperature transfer. If, for instance, you want to cool down (or heat up) the contents of a conveyor rail, then you can have it run through a section of metal tile. And then also run a cold (or hot) liquid through those same tiles, using radiant pipes. The metal tiles then greatly aid the temperature transfer between the two.

---

*Archived from [https://www.guidesnotincluded.com/heat-transfer-basics](https://www.guidesnotincluded.com/heat-transfer-basics) ([Wayback Machine snapshot](https://web.archive.org/web/20250811145919id_/https://www.guidesnotincluded.com/heat-transfer-basics)). Original work © Some Random Finn / guidesnotincluded.com, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Reformatted from HTML to Markdown for this non-commercial community archive — see [Attribution & licensing](attribution.md).*
