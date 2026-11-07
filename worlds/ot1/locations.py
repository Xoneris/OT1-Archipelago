from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import OctopathTravelerWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
# LOCATION_NAME_TO_ID = {
#     "Top Left Room Chest": 1,
#     "Top Middle Chest": 2,
#     "Bottom Left Chest": 3,
#     "Bottom Left Extra Chest": 4,
#     "Bottom Right Room Left Chest": 5,
#     "Bottom Right Room Right Chest": 6,
#     # Location IDs don't need to be sequential, as long as they're unique and greater than 0.
#     "Right Room Enemy Drop": 10,
# }
CHARACTER_RECRUITMENT_TO_ID = {
    "Recruit Olberic": 1,
    "Recruit Tressa": 2,
    "Recruit Cyrus": 3,
    "Recruit Primrose": 4,
    "Recruit H'aanit": 5,
    "Recruit Therion": 6,
    "Recruit Ophilia": 7,
    "Recruit Alfyn": 8,
}

CHARACTER_STORY_PROGRESS_TO_ID = {
    "Finished Olberic Chapter 1": 10,
    "Finished Olberic Chapter 2": 11,
    "Finished Olberic Chapter 3": 12,
    "Finished Olberic Chapter 4": 13,
    "Finished Tressa Chapter 1": 20,
    "Finished Tressa Chapter 2": 21,
    "Finished Tressa Chapter 3": 22,
    "Finished Tressa Chapter 4": 23,
    "Finished Cyrus Chapter 1": 30,
    "Finished Cyrus Chapter 2": 31,
    "Finished Cyrus Chapter 3": 32,
    "Finished Cyrus Chapter 4": 33,
    "Finished Primrose Chapter 1": 40,
    "Finished Primrose Chapter 2": 41,
    "Finished Primrose Chapter 3": 42,
    "Finished Primrose Chapter 4": 43,
    "Finished H'aanit Chapter 1": 50,
    "Finished H'aanit Chapter 2": 51,
    "Finished H'aanit Chapter 3": 52,
    "Finished H'aanit Chapter 4": 53,
    "Finished Therion Chapter 1": 60,
    "Finished Therion Chapter 2": 61,
    "Finished Therion Chapter 3": 62,
    "Finished Therion Chapter 4": 63,
    "Finished Ophilia Chapter 1": 70,
    "Finished Ophilia Chapter 2": 71,
    "Finished Ophilia Chapter 3": 72,
    "Finished Ophilia Chapter 4": 73,
    "Finished Alfyn Chapter 1": 80,
    "Finished Alfyn Chapter 2": 81,
    "Finished Alfyn Chapter 3": 82,
    "Finished Alfyn Chapter 4": 83,
}

CHEST_TO_ID = {
    "Cobbleston Chest 1": 1100,
    "Cobbleston Chest 2": 1101,
    "Mountain Pass Chest 1": 1102,
    "Mountain Pass Chest 2": 1103,
    "Mountain Pass Chest 3": 1104,
    "Mountain Pass Chest 4": 1105,
    "Brigands' Den Chest 1": 1106,
    "Brigands' Den Chest 2": 1107,
    "Brigands' Den Chest 3": 1108,
    "Brigands' Den Chest 4": 1109,
    "Brigands' Den Chest 5": 1110,
    "Rippletide Chest 1": 1200,
    "Rippletide Chest 2": 1201,
    "Rippletide Chest 3": 1202,
    "Rippletide Chest 4": 1203,
    "Path to the Caves of Maiya Chest 1": 1204,
    "Path to the Caves of Maiya Chest 2": 1205,
    "Path to the Caves of Maiya Chest 3": 1206,
    "Path to the Caves of Maiya Chest 4": 1207,
    "Caves of Maiya Chest 1": 1208,
    "Caves of Maiya Chest 2": 1209,
    "Caves of Maiya Chest 3": 1210,
    "Caves of Maiya Chest 4": 1211,
    "Caves of Maiya Chest 5": 1212,
    "Atlasdam Palace Chest 1": 1300,
    "Atlasdam Palace Chest 2": 1301,
    "Atlasdam Palace Chest 3": 1302,
    "Atlasdam Palace Chest 4": 1303,
    "Subterranean Study Chest 1": 1304,
    "Subterranean Study Chest 2": 1305,
    "Subterranean Study Chest 3": 1306,
    "Subterranean Study Chest 4": 1307,
    "Subterranean Study Chest 5": 1308,
    "Subterranean Study Chest 6": 1309,
    "Subterranean Study Chest 7": 1310,
    "Sunshade Chest": 1400,
    "Sunshade Tavern Chest": 1401,
    "Sunshade Catacombs Chest 1": 1402,
    "Sunshade Catacombs Chest 2": 1403,
    "Sunshade Catacombs Chest 3": 1404,
    "Sunshade Catacombs Chest 4": 1405,
    "S'warkii Chest 1": 1500,
    "S'warkii Chest 2": 1501,
    "S'warkii Chest 3": 1502,
    "Path to the Whisperwood Chest 1": 1503,
    "Path to the Whisperwood Chest 2": 1504,
    "Path to the Whisperwood Chest 3": 1505,
    "Path to the Whisperwood Chest 4": 1506,
    "The Whisperwood Chest 1": 1507,
    "The Whisperwood Chest 2": 1508,
    "The Whisperwood Chest 3": 1509,
    "The Whisperwood Chest 4": 1510,
    "The Whisperwood Chest 5": 1511,
    "The Whisperwood Chest 6": 1512,
    "Bolderfall Chest 1": 1600,
    "Bolderfall Chest 2": 1601,
    "Ravus Manor Gate Chest 1": 1602,
    "Ravus Manor Gate Chest 2": 1603,
    "Ravus Manor Chest 1": 1604,
    "Ravus Manor Chest 2": 1605,
    "Ravus Manor Chest 3": 1606,
    "Ravus Manor Chest 4": 1607,
    "Ravus Manor Chest 5": 1608,
    "Ravus Manor Chest 6": 1609,
    "Ravus Manor Chest 7": 1610,
    "Flamesgrace Cathedral Chest 1": 1700,
    "Flamesgrace Cathedral Chest 2": 1701,
    "Flamesgrace Cathedral Chest 3": 1702,
    "Path to the Cave of Origin Chest 1": 1703,
    "Path to the Cave of Origin Chest 2": 1704,
    "Path to the Cave of Origin Chest 3": 1705,
    "Cave of Origin Chest 1": 1706,
    "Cave of Origin Chest 2": 1707,
    "Cave of Origin Chest 3": 1708,
    "Cave of Origin Chest 4": 1709,
    "Cave of Origin Chest 5": 1710,
}

LOCATION_NAME_TO_ID = {
    **CHARACTER_RECRUITMENT_TO_ID
    **CHARACTER_STORY_PROGRESS_TO_ID
    **CHEST_TO_ID
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class OctopathTravelerWorldLocation(Location):
    game = "Octopath Traveler"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: OctopathTravelerWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: OctopathTravelerWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    # overworld = world.get_region("Overworld")
    # top_left_room = world.get_region("Top Left Room")
    # bottom_right_room = world.get_region("Bottom Right Room")
    # right_room = world.get_region("Right Room")

    swarkii = world.get_region("S'warkii")
    path_to_the_whisperwood = world.get_region("Path to the Whisperwood")
    the_whisperwood = world.get_region("The Whisperwood")

    # One way to create locations is by just creating them directly via their constructor.
    # bottom_left_chest = APQuestLocation(
    #     world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    # )

    # You can then add them to the region.
    # overworld.locations.append(bottom_left_chest)

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.

    # bottom_right_room_locations = get_location_names_with_ids(
    #     ["Bottom Right Room Left Chest", "Bottom Right Room Right Chest"]
    # )
    # bottom_right_room.add_locations(bottom_right_room_locations, APQuestLocation)

    # top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    # top_left_room.add_locations(top_left_room_locations, APQuestLocation)

    # right_room_locations = get_location_names_with_ids(["Right Room Enemy Drop"])
    # right_room.add_locations(right_room_locations, APQuestLocation)

    swarkii_locations = get_location_names_with_ids([
        "S'warkii Chest 1", 
        "S'warkii Chest 2",
        "S'warkii Chest 3",
    ])
    swarkii.add_locations(swarkii_locations, OctopathTravelerWorldLocation)

    path_to_the_whisperwood_locations = get_location_names_with_ids([
        "Path to the Whisperwood Chest 1",
        "Path to the Whisperwood Chest 2",
        "Path to the Whisperwood Chest 3",
        "Path to the Whisperwood Chest 4",
    ])
    path_to_the_whisperwood.add_locations(path_to_the_whisperwood_locations, OctopathTravelerWorldLocation)

    the_whisperwood_locations = get_location_names_with_ids([
        "The Whisperwood Chest 1",
        "The Whisperwood Chest 2",
        "The Whisperwood Chest 3",
        "The Whisperwood Chest 4",
        "The Whisperwood Chest 5",
        "The Whisperwood Chest 6",
    ])
    the_whisperwood.add_locations(the_whisperwood_locations, OctopathTravelerWorldLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    # top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     top_middle_room.add_locations(top_middle_room_locations, APQuestLocation)
    # else:
    #     overworld.add_locations(top_middle_room_locations, APQuestLocation)

    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    # if world.options.extra_starting_chest:
    #     # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
    #     # exist, it must still always be present in the world's location_name_to_id.
    #     # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
    #     bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
    #     overworld.add_locations(bottom_left_extra_chest, APQuestLocation)


def create_events(world: OctopathTravelerWorld) -> None:

    placeholder = ""

    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.

    # top_left_room = world.get_region("Top Left Room")
    # final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    # button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
    # top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    # button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    # button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    # final_boss_room.add_event(
    #     "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
    # )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)