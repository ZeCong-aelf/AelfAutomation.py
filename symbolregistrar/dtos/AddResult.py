class AddResult:
    def __init__(self, page=0, from_word="", to_word="", transaction_id=""):
        self.page = page
        self.from_word = from_word
        self.to_word = to_word
        self.transaction_id = transaction_id

    def to_result_line(self):
        return f"{self.page},{self.from_word},{self.to_word},{self.transaction_id}"

    @staticmethod
    def from_result_line(string_line):
        vals = string_line.split(",")
        return AddResult(
            page=int(vals[0]),
            from_word=vals[1],
            to_word=vals[2],
            transaction_id=vals[3]
        )