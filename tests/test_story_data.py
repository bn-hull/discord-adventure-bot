from adventure_bot.story_data import StoryData


class TestAddStory:
    def test_add_story(self):
        state = StoryData()

        state.add_story("A")
        assert ["A"] == state.story_list


class TestAddPerson:
    def test_add_person(self):
        state = StoryData()

        state.add_person("A")
        assert ["A"] == state.person_list


class TestAddPlace:
    def test_add_person(self):
        state = StoryData()

        state.add_place("A")
        assert ["A"] == state.place_list


class TestAddThing:
    def test_add_person(self):
        state = StoryData()

        state.add_thing("A")
        assert ["A"] == state.thing_list
