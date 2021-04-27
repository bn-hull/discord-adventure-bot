class StoryData:
    def __init__(self):
        self.story_list = []
        self.person_list = []
        self.place_list = []
        self.thing_list = []

    def add_story(self, new_story):
        self.person_list.append(new_story)

    def add_person(self, new_person):
        self.person_list.append(new_person)

    def add_place(self, new_place):
        self.place_list.append(new_place)

    def add_thing(self, new_thing):
        self.thing_list.append(new_thing)
