from adventure_bot.story_generation import *


class TestReplaceText:
    def test_replace_text_single(self):
        assert "A B C" == replace_text("A B X", "X", ["C"])

    def test_replace_text_multiple(self):
        assert "A B C D E" == replace_text("A B X X X", "X", ["C", "D", "E"])

    def test_replace_loop_around(self):
        assert "A B C C C" == replace_text("A B X X X", "X", ["C"])


class TestGenerateStory:
    def test_generate_story(self):
        story_generator = StoryGenerator("$PERSON", "$PLACE", "$THING")
        assert "Person Place Thing" == story_generator.generate_story(
            "$PERSON $PLACE $THING", ["Person"], ["Place"], ["Thing"]
        )
