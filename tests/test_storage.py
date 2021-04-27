from adventure_bot.storage import (
    transform_story_data_to_json,
    populate_story_data_from_json,
)
from adventure_bot.story_data import StoryData
import json


class TestStoryDataToJson:
    def test_story_data_to_json(self):
        story_data = StoryData()
        story_data.add_person("A")
        story_data.add_place("A")
        story_data.add_story("A")
        story_data.add_thing("A")

        transformed_story_data = json.loads(transform_story_data_to_json(story_data))

        assert transformed_story_data == {
            "story": story_data.story_list,
            "person": story_data.person_list,
            "place": story_data.place_list,
            "thing": story_data.thing_list,
        }


class TestJsonDataToStoryData:
    def test_json_data_to_story(self):
        story_dict = {
            "story": ["A"],
            "person": ["A"],
            "place": ["A"],
            "thing": ["A"],
        }
        story_data = StoryData()
        story_data.add_person("A")
        story_data.add_place("A")
        story_data.add_story("A")
        story_data.add_thing("A")

        assert populate_story_data_from_json(json.dumps(story_dict)) == story_data
