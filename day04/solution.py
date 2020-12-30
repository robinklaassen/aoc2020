from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Passport:
    byr: Optional[str] = None
    iyr: Optional[str] = None
    eyr: Optional[str] = None
    hgt: Optional[str] = None
    hcl: Optional[str] = None
    ecl: Optional[str] = None
    pid: Optional[str] = None
    cid: Optional[str] = None

    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    @classmethod
    def from_string(cls, string: str) -> 'Passport':
        passport = Passport()
        for pair in string.split(' '):
            key, value = pair.split(':')
            setattr(passport, key, value)
        return passport

    @property
    def has_required_fields(self) -> bool:
        return all([getattr(self, field) is not None for field in self.required_fields])

    @property
    def is_valid(self) -> bool:
        if not self.has_required_fields:
            return False

        return all([getattr(self, field + '_valid') for field in self.required_fields])

    @property
    def byr_valid(self) -> bool:
        return 1920 <= int(self.byr) <= 2002

    @property
    def iyr_valid(self) -> bool:
        return 2010 <= int(self.iyr) <= 2020

    @property
    def eyr_valid(self) -> bool:
        return 2020 <= int(self.eyr) <= 2030

    @property
    def hgt_valid(self) -> bool:
        num = self.hgt[:-2]
        meas = self.hgt[-2:]

        if meas == 'cm':
            return 150 <= int(num) <= 193
        elif meas == 'in':
            return 59 <= int(num) <= 76
        else:
            return False

    @property
    def hcl_valid(self) -> bool:
        if self.hcl[0] != '#' or len(self.hcl) != 7:
            return False

        for c in self.hcl[1:]:
            if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                return False
        return True

    @property
    def ecl_valid(self) -> bool:
        return self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    @property
    def pid_valid(self) -> bool:
        return len(self.pid) == 9 and int(self.pid)


def _read_input(filepath: str) -> List[Passport]:
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()

    lines = list(map(lambda line: line or '-', lines))

    passport_strings = ' '.join(lines).split(' - ')

    return [Passport.from_string(string) for string in passport_strings]


def main():
    passports = _read_input('./input.txt')
    valids = [p.has_required_fields for p in passports]
    print(f'Scanned {len(passports)} passports of which {sum(valids)} have all required fields.')

    new_valids = [p.is_valid for p in passports]
    print(f'Adding data validation rules, only {sum(new_valids)} passports are valid.')


if __name__ == '__main__':
    main()
