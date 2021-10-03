import random
import string as st


class Generator:
    lf = "https://meet.google.com/"
    message = "Limit: 99"

    def generate(self, times):
        links = []

        if times <= 99:
            for i in range(times):
                code = []
                for x in range(3):
                    code.append(''.join(
                        random.choices(st.ascii_lowercase, k=(4 if x == 1 else 3))
                    ))
                links.append(self.lf + '-'.join(code))

            return "\n".join(links)
        return self.message
        
if __name__ == "__main__":
    gen = Generator()
    print(gen.generate(10))

