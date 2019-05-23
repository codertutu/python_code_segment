from faker import Faker
import random


class FakeBankNumber:
    info = {
        'gsbank': {'cn': 18, 'bin': '620200'},
        'yzbank': {'cn': 19, 'bin': '620062'},
        'zgbank': {'cn': 19, 'bin': '621660'},
        'jsbank': {'cn': 19, 'bin': '436742'},
        'jtbank': {'cn': 17, 'bin': '622258'},
        'gdbank': {'cn': 16, 'bin': '620518'},
        'msbank': {'cn': 16, 'bin': '623255'},
        'zsbank': {'cn': 16, 'bin': '622580'},
        'xybank': {'cn': 16, 'bin': '623287'},
        'pfbank': {'cn': 16, 'bin': '621351'},
        'pabank': {'cn': 16, 'bin': '998800'},
        'nybank': {'cn': 19, 'bin': '620059'},
    }

    @staticmethod
    def _add(number):
        return (number % 10) + (number // 10)

    def make_bank_no(self, bank_name="gsbank"):
        random_length = self.info[bank_name]['cn'] - int(len(self.info[bank_name]['bin']))
        list1 = [int(i) for i in self.info[bank_name]['bin']]
        list1.extend([random.randrange(0, 10) for i in range(random_length - 1)])
        sum_number = sum([j for j in list1[-2::-2]]) + sum([self._add(j * 2) for j in list1[-1::-2]])
        last_number = (10 - sum_number % 10) if (sum_number % 10 != 0) else 0
        list1.append(last_number)
        return ''.join(map(lambda x: str(x), list1))


class MockDataSupply:
    _fake = Faker("zh_CN")
    _fakeBankNumber = FakeBankNumber()

    def cn_name(self):
        return self._fake.name()

    def identify_card(self):
        return self._fake.ssn()

    def phone_number(self):
        return self._fake.phone_number()

    def bank_card(self, bank_name="gsbank"):
        return self._fakeBankNumber.make_bank_no(bank_name)


if __name__ == "__main__":
    m = MockDataSupply()
    print(m.cn_name())
    print(m.identify_card())
    print(m.phone_number())
    print(m.bank_card("nybank"))

    pass
