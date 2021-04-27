from adventure_bot.story_data import StoryData
from adventure_bot.storage import (
    transform_story_data_to_json,
    populate_story_data_from_json,
)


class TestIntegrationStoryDataStorage:
    def test_make_json_with_added_place(self):
        story_data = StoryData()
        story_data.add_place("Test")
        assert (
            transform_story_data_to_json(story_data)
            == '{"story": [], "person": [], "place": ["Test"], "thing": []}'
        )

    def test_make_json_empty_storage(self):
        story_data = StoryData()
        assert (
            transform_story_data_to_json(story_data)
            == '{"story": [], "person": [], "place": [], "thing": []}'
        )

    def test_make_story_from_read_json_string(self):
        story_data = StoryData()
        story_data.add_place("Test")
        assert (
            populate_story_data_from_json(
                '{"story": [], "person": [], "place": ["Test"], "thing": []}'
            )
            == story_data
        )
