from .story_data import *
import json


def transform_story_data_to_json(story_data: StoryData):
    """
    @returns python dictionary based on stories, people, places, and things lists where the keys correspond with the lists
    """
    return json.dumps(
        {
            "story": story_data.story_list,
            "person": story_data.person_list,
            "place": story_data.place_list,
            "thing": story_data.thing_list,
        }
    )


def populate_story_data_from_json(json_string: str):
    story_dict = json.loads(json_string)

    story_data = StoryData()

    story_data.story_list = story_dict["story"]
    story_data.person_list = story_dict["person"]
    story_data.place_list = story_dict["place"]
    story_data.thing_list = story_dict["thing"]

    return story_data
