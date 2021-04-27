from adventure_bot.story_data import StoryData
from adventure_bot.story_generation import StoryGenerator
import pytest


class TestIntegrationStoryDataStoryGeneration:
    def test_story_data_has_params_when_generating(self):
        story_data = StoryData()
        story_generator = StoryGenerator("$PERSON", "$PLACE", "$THING")

        story_data.add_story("$PERSON went to $PLACE and got a $THING")
        story_data.add_person("Man")
        story_data.add_place("US")
        story_data.add_thing("Car")

        # add data to story data
        assert "Man went to US and got a Car" == story_generator.generate_story(
            story_data.story_list[0],
            story_data.person_list,
            story_data.place_list,
            story_data.thing_list,
        )

    def test_story_generation_throws_error_on_empty_list(self):
        story_data = StoryData()
        story_generator = StoryGenerator("$PERSON", "$PLACE", "$THING")
        story_data.add_story("$PERSON went to $PLACE and got a $THING")
        story_data.add_person("Man")
        # no place gets added
        story_data.add_thing("Car")

        # should raise exception when it has an empty list
        with pytest.raises(Exception):
            story_generator.generate_story(
                story_data.story_list[0],
                story_data.person_list,
                story_data.place_list,
                story_data.thing_list,
            )
