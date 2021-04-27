class StoryData:
    def __init__(self):
        self.people_list = []
        self.places_list = []
        self.thing_list = []

    def add_person(self, new_person):
        self.people_list.append(new_person)

    def add_place(self, new_place):
        self.places_list.append(new_place)

    def add_thing(self, new_thing):
        self.thing_list.append(new_thing)
