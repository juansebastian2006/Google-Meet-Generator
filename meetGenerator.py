
import random
import string as st


class Color:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Generator:
    link_f = "https://meet.google.com/"
    message = "Limit: 99"

    def generate(self, times):
        links = []

        if times <= 99:
            for i in range(times):
                links.append(Color.BOLD + Color.HEADER +
                             f"[{str(i + 1).zfill(2)}] " + self.link_f +
                             '-'.join(''.join(random.choices(st.ascii_lowercase, k=(4 if i == 1 else 3)))
                                      for i in range(3))
                             )

            return "\n".join(links)
        return Color.BOLD + Color.WARNING + self.message + Color.END_C
