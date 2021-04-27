from adventure_bot.story_data import StoryData


class TestAddPerson:
    def test_add_person(self):
        state = StoryData()

        state.add_person("A")
        assert ["A"] == state.people_list


class TestAddPlace:
    def test_add_person(self):
        state = StoryData()

        state.add_place("A")
        assert ["A"] == state.places_list


class TestAddThing:
    def test_add_person(self):
        state = StoryData()

        state.add_thing("A")
        assert ["A"] == state.thing_list
