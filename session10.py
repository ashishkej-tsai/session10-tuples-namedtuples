from faker import Faker
fake = Faker() 

from collections import namedtuple
from collections import Counter

profile_ex = fake.profile()

Profiles = namedtuple('Fake_Profiles', sorted(profile_ex.keys()))

Profiles.__doc__ = "Represents profiles for Individuals"
Profiles.address.__doc__ = "Address of the Individual"
Profiles.birthdate.__doc__ = "Birth Date of the Individual"
Profiles.blood_group.__doc__ = "Blood Group of the Individual"
Profiles.current_location.__doc__ = "Current location of the Individual in Lattitude and Longitude"

def create_fake_profiles(seed = 0):
    '''
    Given a seed value return 10000 Fake profiles in dict and namedtuple data structures 
    '''
    Faker.seed(seed)
    fake_profiles_dict = []
    for _ in range(10000):
        fake_profiles_dict.append(fake.profile())
    fake_profiles_namedtuple = [Profiles(**x) for x in fake_profiles_dict]
    return fake_profiles_namedtuple, fake_profiles_dict



def timed(reps):
    '''
    Decorator factory to return average time taken by function to run and function results
    '''
    def inner_1(fn):
        from time import perf_counter
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result, avg_run_time
        return inner
    return inner_1

@timed(100)
def calculate_namedtuple(fake_profiles_namedtuple):
    '''
    Function to calculate largest blood type, oldest_person_age, and average age 
    from namedtuple data structure
    '''
    blood_types = [x.blood_group for x in fake_profiles_namedtuple]
    counter = Counter(blood_types)
    largest_blood_type = counter.most_common(1)[0][0]
    ages = [(2021 - x.birthdate.year) for x in fake_profiles_namedtuple]
    oldest_age = max(ages)
    average_age = float(sum(ages))/float(len(ages))
    return largest_blood_type, oldest_age, average_age

@timed(100)
def calculate_dict(fake_profiles_dict):
    '''
    Function to calculate largest blood type, oldest_person_age, and average age 
    from namedtuple data structure
    '''
    blood_types = [x['blood_group'] for x in fake_profiles_dict]
    counter = Counter(blood_types)
    largest_blood_type = counter.most_common(1)[0][0]
    ages = [(2021 - x['birthdate'].year) for x in fake_profiles_dict]
    oldest_age = max(ages)
    average_age = float(sum(ages))/float(len(ages))
    return largest_blood_type, oldest_age, average_age


