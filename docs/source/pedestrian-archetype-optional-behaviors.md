# Pedestrian Archetypes

This is the list of all the archetypes and their essential and optional behaviors. The list includes the archetypes from our previous published paper [Pedestrian Archetypes](https://www.researchgate.net/publication/390398650_Pedestrian_Archetypes_-_The_Must-Have_Pedestrian_Models_for_Autonomous_Vehicle_Safety_Testing).


## Table of Contents

1. [The Wanderer](#the-wanderer)
2. [The Drunk](#the-drunk)
3. [The Distracted](#the-distracted)
4. [The Flash](#the-flash)
5. [The Indecisive](#the-indecisive)
6. [The Blind](#the-blind)
7. [The Flock](#the-flock)
8. [The Jaywalker](#the-jaywalker)
9. [The Elderly](#the-elderly)
10. [The Kid](#the-kid)
11. [The Eventful](#the-eventful)
12. [The Parked Pedestrian](#the-parked-pedestrian)

---

## The Wanderer

**Definition:** Pedestrians who wander along driving lanes and often ignore traffic; their intentions are hard to predict.

**Important descriptions:**

* Move along or within driving lanes without clear intent to cross or to stay on sidewalk.
* Exhibit frequent, abrupt direction changes that confuse observers and AVs.
* Unclear crossing intentions (annotators often disagree on whether they will cross).
* May accelerate, change speed, or stop suddenly; can approach or retreat from vehicle lanes.


| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
| • Along-lane          | • Not-sure-cross |
| • Zig-zag    |                     |

---

## The Drunk

**Definition:** Pedestrians impaired by alcohol or drugs, producing unpredictable gait, balance, and decision-making.

**Important descriptions:**

* Impaired balance and motor coordination leads to stumbling, falling, or crawling.
* Behavior is erratic and can modify other archetypes (like, a drunk jaywalker behaves differently than a sober one).

| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
| • Drunken-walk          | • Crawling |
|     | • Dancing              |
|           | • Crosswalk detour |
|            | • Fall |
|            | • Trip |  


---

## The Distracted

**Definition:** Pedestrians whose attention is fixated on something other than traffic (phone, conversation, music, etc.), reducing situational awareness.

**Important descriptions:**

* Usually able to act rationally if communicated with, but their perception delays increase reaction times.

| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
| • Fixated not at ncoming vehicle          | • Crawling |
| • Preoccuipied   | • Gesturing              |
|           | • Back turned |


---

## The Flash

**Definition:** Pedestrians who dash or sprint through traffic with urgency and little regard for safety.

**Important descriptions:**

* High-speed crossing behavior; urgency-driven rather than rational gap acceptance.
* Paths can be straight or curved (not necessarily the shortest path).

| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
| • Run into traffic         | • Fixated not at incoming vehicle |
|     | • Flinch-in             |
|           | • Flinch-out |
|            | • Brisk-walking |
|            | • Not looking/ glancing |  


---

## The Indecisive

**Definition:** Pedestrians who hesitate, vacillate, or repeatedly change crossing decisions, increasing risk as time passes.

**Important descriptions:**

* Wavering decision-making can cause mid-crossing retreats or sudden accelerations.
* Their indecision propagates uncertainty to other road users.

| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
| • Retreat         | • Near-miss |
| • Flinch-in    | • Not-sure-cross        |
| • Flinch-out          | • Pause-start |
| • Frozen    |          |
| • Swerve          |        |


---

## The Blind

**Definition:** Pedestrians who either intentionally ignore traffic/signals or fail to notice vehicles and signals.

**Important descriptions:**

* Two flavors: intentionally ignoring traffic (willfully) vs. failing to notice (inattentive or sensory limitations).
* Difficult for drivers/AVs to infer awareness from external behavior.


| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
| • Ignore traffic         | • Preoccupied |
|         | • Not looking/ glancing        |


---

## The Flock

**Definition:** Groups of pedestrians that typically move together but can become dangerous when members disagree or become separated.

**Important descriptions:**

* Group dynamics produce different risk patterns than isolated pedestrians.
* Individual members can be distracted, or the group may fragment mid-crossing.


| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
| • Group-walk        | • Group-disperse |
|         | • Re-group        |
|              | • Cross |
|              | • Not-sure-cross      |
|               | • Not-cross |


---

## The Jaywalker

**Definition:** Pedestrians who cross at non-designated locations (mid-block, roundabout center, or other unexpected positions) regardless of signals.

**Important descriptions:**

* High incidence of accidents from mid-block crossings.
* Jaywalkers may choose the shortest path (over islands, roundabouts) ignoring safety.


| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
| • Cross-without-crosswalk        | • Crosswalk-detour |
| • Cross-on-red        | • Make-stop        |
|              | • Near-miss |
|              | • Collision      |


---

## The Elderly

**Definition:** Older adults who typically exhibit slower perception and decision-making; behavior is risky due to delayed reaction rather than intentionally dangerous actions.

**Important descriptions:**

* Slower motor and sensory responses reduce crossing efficiency and increase risk.
* Hard to define by a single behavior; age appearance itself is an important cue.


| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
|         | • Cautious |

---

## The Kid

**Definition:** Children and younger pedestrians who behave unpredictably due to inexperience, small size, and impulsivity.

**Important descriptions:**

* Not necessarily many stereotypical behaviors identify them externally; the presence of kids is itself a risk cue.

| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
|        | • Ignore traffic |
|         | • Not-sure-cross        |
|              | • Make-stop |
|              | • Fixated not at the incoming vehicle      |

---

## The Eventful

**Definition:** Pedestrians who become dangerous due to external, often involuntary events (trips, falls, occlusions, dropped items, or pets).

**Important descriptions:**

* Not the result of a stable personality trait; rather, these are situational hazards.

| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
|  • Flinch-in       | • Near-miss |
|  • Flinch-out        | • Make-stop       |
|  • Drop-object             | • Flinch-in |
|  • Pickup-object            | • Flinch-out      |
|  • Trip            | • Retreat      |
|  • Fall           |          |
|  • Pop-out-occlusion     |           |
---

## The Parked Pedestrian

**Definition:** Pedestrians who interact with parked vehicles — loading/unloading, getting in/out, or moving along parked cars — and therefore exhibit different risks than regular crossers.

**Important descriptions:**

* Often partially occluded by the parked vehicle and less distinguishable.

| **Essential Behaviors**                  | **Optional Behaviors**                                                  |
|-----------------------------------------|------------------------------------------------------------------------|
|  • Loading            | • Fixated not at incoming vehicle              |
|  • Unloading        | • Preoccupied                  |
|  • getting-in                  | • Trip        |
|  • Getting-off ( a parked vehicle)                 | • Fall           |


---
