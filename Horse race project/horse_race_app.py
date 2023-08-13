from horse_race import HorseRace
from horse_specification.appaloosa import Appaloosa
from horse_specification.thoroughbred import Thoroughbred
from jockey import Jockey


class HorseRaceApp:
    VALID_TYPES = ['Appaloosa', 'Thoroughbred']
    HORSE_CLASSES = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred,
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def get_jockey(self, jockey_name: str, obj: []):
        for jockey in obj:
            if jockey.name == jockey_name:
                return jockey

    def get_race(self, race_type: str, obj: []):
        for race_item in obj:
            if race_item.race_type == race_type:
                return race_item

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in HorseRaceApp.VALID_TYPES:
            return

        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        horse_class = HorseRaceApp.HORSE_CLASSES[horse_type]
        new_horse = horse_class(horse_name, horse_speed)

        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):

        for jokey in self.jockeys:
            if jokey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jokey = Jockey(jockey_name, age)
        self.jockeys.append(new_jokey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.get_jockey(jockey_name, self.jockeys)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        existing_horse_types = []
        for jocker_obj in self.jockeys:
            if jocker_obj.horse:
                existing_horse_types.append(jockey.horse.__class__.__name__)

        if horse_type not in HorseRaceApp.VALID_TYPES or jockey_name in existing_horse_types:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        if self.horses:
            for horse in self.horses:
                if horse.__class__.__name__ == horse_type:
                    jockey.horse = horse
                    horse.is_taken = True
                    return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.get_jockey(jockey_name, self.jockeys)
        race = self.get_race(race_type, self.horse_races)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.get_race(race_type, self.horse_races)

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        current_highest_speed = 0
        winner = ""
        horse_name = ""
        for jockey in race.jockeys:
            if jockey.horse.speed > current_highest_speed:
                current_highest_speed = jockey.horse.speed
                winner = jockey.name
                horse_name = jockey.horse.name

        return f"The winner of the {race_type} race, with a speed of {current_highest_speed}km/h is {winner}! Winner's horse: {horse_name}."
