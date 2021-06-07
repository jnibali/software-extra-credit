import sentence_reverse


class TestSentenceReversal:
     def test_reversal(self):
        assert "Tadimeti V is name My" == sentence_reverse.reverse("My name is V Tadimeti")