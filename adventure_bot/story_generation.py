def replace_text(text: str, key: str, source_list: list):
    """
    Takes in text and replaces any keywords specified as "key" with items from the list
    If list is too short to fill out, it loops around
    @param text:           text to transform
    @param key:             what word to replace in the story with items from the source_list, it is recommended to start it with a special character
    @param source_list:     list of words that can be used to replace key word with

    @return: transformed text with any key words replaced with words from the source list
    """

    count = 0
    while True:
        list_index = count % len(source_list)

        if key in text:
            text = text.replace(key, source_list[list_index], 1)
        # stop if you can't find anymore
        else:
            break

        count += 1

    return text


class StoryGenerator:
    # keys must be
    def __init__(self, character_key: str, place_key: str, thing_key: str):
        """
        @param character_key:   key to specify characters during story generation, must be unique to other keys
        @param place_key:       key to specify places during story generation, must be unique to other keys
        @param thing_key:       key to specify things during story generation, must be unique to other keys
        """
        self.character_key = character_key
        self.place_key = place_key
        self.thing_key = thing_key

    def generate_story(self, story: str, characters: list, places: list, things: list):
        story = replace_text(story, self.character_key, characters)
        story = replace_text(story, self.place_key, places)
        story = replace_text(story, self.thing_key, things)

        return story
