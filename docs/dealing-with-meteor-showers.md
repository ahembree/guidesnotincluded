---
title: "Dealing with meteor showers"
source_url: https://www.guidesnotincluded.com/dealing-with-meteor-showers
archived: 2025-08-06
archive_snapshot: https://web.archive.org/web/20250806085052id_/https://www.guidesnotincluded.com/dealing-with-meteor-showers
---

# DEALING WITH METEOR SHOWERS

## Introduction

In the base game, meteor showers are something you have to deal with sooner or later if you want to get to space. It was never my favourite part of Oxygen Not Included and I was happy to be rid of it when the DLC came along. But then the Whatta Blast update came along and meteor showers are a thing for all of us once again. (Sigh.)

So I started a new game, called it "Why did it have to be comets?", and got to work reminding myself of how the heck dealing with plummeting space debris works again.

There is some good news. Cooling things in the vacuum of space has been made easier. Meteor showers in the Spaced Out DLC don't come around that often. And some meteor showers are quite tame, with only a few meteors. Also, if you don't want to to deal with meteor showers you can turn them off in the game settings. (This is a single-player game - play it however you enjoy it the most.)

I'll update this section as I continue my game and learn more, but here are some basics to get you started. (Really I'm just muddling along while I wait for Francis John to come out with a tutorial for this stuff.)

## Two approaches: blasting or mining

![ONI-Guide-MeteorBlasterInAction.png](assets/ONI-Guide-MeteorBlasterInAction-51b39b19a8.avif)

Meteor blasters in action

The Whatta Blast update brought with it meteor blasters. So the first approach to dealing with meteors is to blast them out of the sky. However, a downside to note is that meteors that are shot down drop only some of their materials, the rest are destroyed.

Producing blastshot (the bullets used to shoot down meteors) uses refined metal. So not only do you not get resources, but you need to spend resources. (You get some refined metal back after shooting blastshot, but I'm not sure how much. My guess would be 25%, maybe 50%.)

On the positive side, with this approach you can have solar power up and running all the time, even during meteor showers. It also uses a lot less steel than the second approach. Speaking of the second approach...

The second approach is one older players will be familiar with from the base game: Francis John's C-miner design. This is where you cover the top of your base (or your map) with bunker doors that the meteors impact on. When the meteor shower is over you open the bunker doors, let the debris fall, and use robo-miners to dig it all out.

This approach will let you gather up all the materials in the meteors. (Note that they can be very hot - over 200 C.) This approach requires a lot of [steel](getting-steel.md) and also a fair bit of power when the bunker doors open or close (depending on how much of the map you cover them in).

Both designs use space scanners and both designs require cooling. So let's look at that first. Then a quick look at a way to get a notification, and even automatically pause the game, when meteor showers are appproaching. Just in case you want to see how your defences hold up. Finally, after all that, we'll get to the designs.

## Space scanners

Space scanner basics:

* Uses 120 W of power
* Sends a green automation signal when it detects what it is looking for
* You can set it to detect meteor showers (or rockets or interplanetary payloads)

![Building_Space_Scanner.webp](assets/Building_Space_Scanner-98c93fc8b6.avif)

Space scanner

There is an element of randomness to how quickly the space scanner will detect incoming meteor showers. More space scanners means a better scan quality and a higher likelihood of detecting meteors sooner.

Click on a scanner and you will see a percentage figure for scan quality. That is how well the specific scanner is working. There is also a percentage for your scan network quality. This number can be increased by having several space scanners.

A higher figure means a higher likelihood of detecting meteor showers sooner. But early detection may or may not matter, depending on your approach.

Space scanners don't overheat, so you don't need to worry about cooling them. Speaking of cooling...

## Cooling loops and the conduction panel

![Building_Conduction_Panel.webp](assets/Building_Conduction_Panel-a26c1b186f.avif)

Conduction panel

Both approaches to dealing with meteor showers will require cooling. Meteor blasters and robo-miners both generate heat when active, so will overheat unless cooled. Thankfully, cooling in the vacuum of space has been made much easier with something called the conduction panel.

Conduction panel basics:

* Used for temperature transfer
* Has liquid input and output ports
* Works even when in a vacuum
* Can be placed on buildings and run through floor and wall tiles
* Transfers heat regardless of whether there is liquid running through (but the liquid is used to cool it)

So to cool something in the vacuum of space, run a cooling loop past it with a conduction panel where you want the cooling to take place. (Two cooling loop options are covered earlier in the guide: [AETN cooling](anti-entropy-thermo-nullifier-cooling.md) or a [thermo aquatuner steam turbine setup](thermo-aquatuner-steam-turbine-cooling-loop.md).)

![ONI-Guide-MeteorBlasterCoolingLoop.png](assets/ONI-Guide-MeteorBlasterCoolingLoop-89f1ba5089.avif)

Cooling loop with conduction panels

One more thing before we get to the main stuff: a way to pause the game before a meteor shower starts.

## Pause before impact: the Automated notifier

![Building_Automated_Notifier.webp](assets/Building_Automated_Notifier-1dfcdc34ff.avif)

Automated notifier

There is a little bit of automation you can use to get a notification, and even pause the game, when something happens. It is called the automated notifier.

The automated notifier is unlocked by researching Notification Systems in the Colony Development research branch. Once unlocked, it is found under Automation.

Click on the automated notifier and you get some options. You can add a name, which will appear in the top left of your screen when it triggers. You can also set the game to pause when it triggers.

By connecting the automated notifier to your space scanner automation grid, it will get a green signal when a meteor shower is detected and then pause the game. (If you set it to do that.) That way you can have a look at how your setup holds up against the meteor shower and see if you need to make any adjustments.

![ONI-Guide-AutomatedNotifier.png](assets/ONI-Guide-AutomatedNotifier-3af96f2708.avif)

![ONI-Guide-AutomatedNotifier2.png](assets/ONI-Guide-AutomatedNotifier2-cda59b6801.avif)

Automated notifier. Connected to the space scanner's automation network.

With some basics out of the way, let's look at the two approaches for dealing with meteor showers: blasting them away and using the C-miner approach.

## Blasting: missile defence

The design is simple enough: you put a bunch of meteor blasters across the top of your base.

![ONI-Guide_CometsMissileDefence1.png](assets/ONI-Guide_CometsMissileDefence1-b71a8ccc63.avif)

![ONI-Guide_MeteorBlaster.png](assets/ONI-Guide_MeteorBlaster-489f3fc5ca.avif)

Meteor blaster

![ONI-Guide_MeteorBlaster2.png](assets/ONI-Guide_MeteorBlaster2-b7d8480853.avif)

Meteor blaster range

Meteor Blaster basics:

* Uses 240 W of power
* Shoots blastshot (produced separately in a blastshot maker)
* Has a conveyor rail input for blastshot
* Has a reach of 33 x 33 tiles; the top of the meteor blaster is in the bottom center of the reach (see picture)
* It doesn't seem to be able to target things above the build area of the map (so building them at the very top of the map won't be very effective)
* Doesn't block light, so won't interfere with solar panels

The meteor blaster can cover an area that is 33 by 33 tiles wide. However, it takes a while for it to target and shoot a meteor. If two meteors are falling close to one-another, it might not have time to shoot them both.

There are meteor showers of varying intensity. If you place several blasters across the top spaced so that their targeting areas don't overlap, meaning any given spot of the sky can only be reached by one meteor blaster, then during the more intense meteor showers some meteors will make it past the meteor blasters.

I'm not sure what the optimal spacing is, meaning how far can you put them from one-another and still be 100% certain to get all meteors. I started with having no overlap, meaning every place in the sky was covered by one meteor blaster. This resulted in meteors getting through during the more intense meteor showers. Then I switched to having a 15 tile space between meteor blasters. That was better but there was still debris from the occasion metoer that had snuck through. So now I have switched to having a 10 tile gap between meteor blasters. So far that seems to be sufficient.

At the time of writing there is a bug where dupes fill meteor blasters with blastshot when they build them, but once built they will only refill a meteor blaster when it is completely empty. (Which will probably be in the middle of a meteor shower - not a great time to run out.)

I have submitted a bug report about this. But while this is still how things work, it means it's important to build a conveyor rail system for filling meteor blasters with blastshot so they never completely run out.

![Building_Space_Scanner.webp](assets/Building_Space_Scanner-98c93fc8b6.avif)

Space scanner

Meteor blasters use a fair bit of power, so it's a good idea to only have them running when you need them. You can do this by adding a space scanner (covered earlier) to the design.

When the space scanner detects a meteor shower incoming, it will send a green automation signal. By connecting your meteor blasters to the automation network, they will only turn on when the space scanner notifies them of incoming showers.

Since the meteor blasters start functioning immediately when they receive a green signal, having just one scanner is enough. Earlier detection of meteors, from having several scanners, just means your meteor blasters will start using power sooner (which you don't need).

Once a meteor shower is over, the space scanner will start sending a red signal. However, there will still be some meteors on their way down to the surface when it starts sending its red signal. Since the red signal will turn off the meteor blasters, the meteors will hit your base. To avoid this, you can add a buffer gate to the design.

![ONI-Guide-BufferGate.png](assets/ONI-Guide-BufferGate-2a9529b072.avif)

Buffer Gate

Buffer gate basics:

* Outputs a green signal if it is receiving a green signal
* Once the signal it receives turns to red, the buffer gate continues to send a green signal for a set amount of time
* You decide how long the green signal buffer is

Basically, the buffer gate makes the meteor blasters receive a green signal for a while longer even after the space scanner starts sending a red signal again.

As to how long to set it for, the longer you set it to the fewer meteors will get through. 40 seconds seems to be long enough to stop them all.

![ONI-Guide-SpaceScannerBufferGate1.png](assets/ONI-Guide-SpaceScannerBufferGate1-bf31e58b88.avif)

Buffer gate. The buffer gate will continue sending a green signal for a while (you choose how long) even after the space scanner starts sending a red signal again.

In addition to all the stuff above, you will also need to make some blastshot. These are the things the meteor blasters shoot to destroy meteors.

Blastshot is made using a building called a blastshot maker. It is unlocked by researching Jetpacks in the Liquids branch of the research tree. Once unlocked, it is found under Stations.

![ONI-Guide-BlastshotMaker.png](assets/ONI-Guide-BlastshotMaker-766a6e2377.avif)

Blastshot maker

Blastshot maker basics:

* Uses a lot of power: 960 W
* Uses refined metal and petroleum to make blastshot
* It has an input for pipe for the petroleum
* Produces carbon dioxide and heat as byproducts

It produces five blastshot per order, which requires 25 kg of refined metal and 50 kg of petroleum.

You can get refined metal by refining ore in a rock crusher or metal refinery. But a more sustainable solution is to use a metal that you have a volcano that produces. (There are separate guides on [how to get petroleum](getting-oil-petroleum-and-plastic.md) and [how to tame a metal volcano](taming-metal-volcanos.md).)

At the time of writing there is still some small bugginess with the blastshot maker. Dupes can fill the petroleum from a pitcher pump in petroleum. But the blastshot maker will only work if you have a section of pipe built (or even scheduled to be built) on the liquid input port. (I have submitted a bug report about this as well.)

You can use automation to make sure your meteor blasters are kept full and you have some blastshot in reserve. There is a seprate guide covering [automation basics](getting-started-with-automation.md), but below are some overlays of one way to do it.

A smart storage bin keeps some blastshot in reserve. Whenever it is less than full, it sends a signal to turn on the blastshot maker until it is filled up again. A conveyor loader, set to a higher priority than the smart storage bin, sends blastshot to the meteor blasters.

![ONI-Guide-BlastshotMakerSetup1.png](assets/ONI-Guide-BlastshotMakerSetup1-468787a83b.avif)

The setup. The storage bin has whatever refined metal you are making blastshot from. The smart storage bin stores blastshot, the conveyor loader takes blastshot.

![ONI-Guide-BlastshotMakerSetupAutomation.png](assets/ONI-Guide-BlastshotMakerSetupAutomation-4af3993007.avif)

Automation overlay. The smart storage bin and not gate send the blastshot maker a green signal until the smart storage bin is full.

![ONI-Guide-BlastshotMakerSetupPriorities.png](assets/ONI-Guide-BlastshotMakerSetupPriorities-e419829ede.avif)

Priorities. Make sure the conveyor loader is set to a higher priority than the smart storage bin.

![ONI-Guide-BlastshotMakerSetupConveyor.png](assets/ONI-Guide-BlastshotMakerSetupConveyor-1966719e29.avif)

Conveyor overlay. The conveyor loader sends blastshot to the meteor blasters.

And now on to some overlays for the missile defence setup.

![ONI-Guide_CometsMissileDefence6.png](assets/ONI-Guide_CometsMissileDefence6-377deefa88.avif)

Missile defence. The space scanner turns the meteor blasters on and off.

![ONI-Guide_CometsMissileDefence4.png](assets/ONI-Guide_CometsMissileDefence4-431b2c8ff0.avif)

Automation overlay. The space scanner turns on the meteor blasters when a meteor shower is incoming. It is connected to a buffer gate (set to 30 seconds) to make sure the meteor blasters stay active throughout the meteor shower.

![ONI-Guide_CometsMissileDefence3.png](assets/ONI-Guide_CometsMissileDefence3-17270090f0.avif)

Conveyor overlay. Blastshot is sent along conveyor rails to the meteor blasters.

![ONI-Guide_CometsMissileDefence5.png](assets/ONI-Guide_CometsMissileDefence5-8ac9914480.avif)

Plumbing overlay. A cooling loop keeps the meteor blasters from overheating. Conduction panels are used to enable temperature transfer in the vacuum of space.

![ONI-Guide_CometsMissileDefence7.png](assets/ONI-Guide_CometsMissileDefence7-8d5bda33bb.avif)

Power overlay. No power, no pew pew.

## The C-miner

This is an approach I picked up from a Francis John [Tutorial Nuggets YouTube video](https://www.youtube.com/watch?v=7Q7K2C1Zti0).

The name "C miner" comes from the shape of the structure around the robo-miners, which resembles the letter C. But I realize now that I built mine the other way around. And you no longer need the bottom tile under the robo-miners, so I didn't build it. Meaning nothing about this design resembles the letter C, so I should probably call this approach something else. Oh well.

There have been some changes to the game mechanics since this design came out. These have both good and bad sides.

On the plus side, cooling the robo-miners is now much less of a hassle as you can use conduction panels.

On the negative side, there are meteors that leave solid tiles when they impact. Such meteors impacting on the blast doors and leaving solid tiles above them will be a whole new thing to work out how best to deal with. (Some meteors do this, others don't. So one approach is to just not build this defence on asteroids where such meteor showers can occur.)

![ONI-Guide-BunkerDoorDefence.png](assets/ONI-Guide-BunkerDoorDefence-06258f853f.avif)

The basic idea. Bunker doors close when meteor showers approach. Robo-miners dig out the falling resources when the meteor shower is over.

![ONI-Guide-BunkerDoorDefenceAutomation.png](assets/ONI-Guide-BunkerDoorDefenceAutomation-e912345bc3.avif)

Automation overlay. The scanner sends a green signal when it detects a meteor shower. The not gate turns it into a red signal and the bunker doors close. (Use several scanners for more accurate scanning.)

![ONI-Guide-BunkerDoorDefencePipes.png](assets/ONI-Guide-BunkerDoorDefencePipes-168ffd7af5.avif)

Plumbing overlay. Conduction panels are used to enable temperature transfer in a vacuum. (Having the cooling loop pass over twice was probably overkill, but it fit the design.)

A friendly word of warning for those choosing this option:

This approach can go very sideways very quickly if you run out of power. A smorgasbord of cascading fusterclucks, from bunker doors not closing in time to meteors crashing in to solar panels getting blocked to cooling loops getting broken (at least before conduction panels) and robo-miners overheating to your enire power grid being underpowered since your solar is screwed leading to buildings and machines in your base shutting down. (And oh yes, I speak from experience.)

So either have a decent back-up power source - enough to power everything that can need to be powered at once - or a lot of extra power stored in batteries. (How much extra power do you need stored? In my experience, however much you think you need, you will need more. Probably a lot more.)

If you don't need the resources from meteors, and have the refined metal and petroleum to spare on blastshot, the first approach, missile defence, is a safer option. If you do need the resources from meteors, build your bunker doors and robo-miners and then stare up into space and yell: Do your worst!

Best of luck :-)

---

*Archived from [https://www.guidesnotincluded.com/dealing-with-meteor-showers](https://www.guidesnotincluded.com/dealing-with-meteor-showers) ([Wayback Machine snapshot](https://web.archive.org/web/20250806085052id_/https://www.guidesnotincluded.com/dealing-with-meteor-showers)). Original work © Some Random Finn / guidesnotincluded.com, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Reformatted from HTML to Markdown for this non-commercial community archive — see [Attribution & licensing](attribution.md).*
