import random, copy
from Classes import *
from math import ceil, log2
import math
import pandas as pd
Kelas.kelas = [Kelas("11SI1", 20), Kelas("11SI2", 22), Kelas("12SI1", 30), 
               Kelas("12SI2", 30), Kelas("13SI1", 28), Kelas('13I2', 25)]

Dosen.dosen = [Dosen("Mr. Mario Simaremare"), Dosen("Mr. Tennov"), Dosen("Mrs. Parmonangan"),
                Dosen("Mrs. Junita"), Dosen("Mr. Samuel"), Dosen("Mr. Humasak")]

CourseClass.classes = [CourseClass("KUS1002"),CourseClass("MAS1101"),CourseClass("KUS2002"),CourseClass("TIS1101"),
                       CourseClass("KUS1001"),CourseClass("FIS1103"),CourseClass("12S1101"),
                        CourseClass("TIS3001")]

Room.rooms = [Room("GD512", 40), Room("GD513", 40), Room("GD514", 40),
              Room("GD522", 40, is_lab=True),Room("GD523", 40, is_lab=True)]

Schedule.schedules = [Schedule("08:15", "10:00", "Mon"), Schedule("10:15", "12:00", "Mon"),
                      Schedule("13:15", "15:00", "Mon"), Schedule("15:15", "17:00", "Mon"), 
                      Schedule("08:15", "10:00", "tue"), Schedule("10:15", "12:00", "tue"),
                      Schedule("13:15", "15:00", "tue"), Schedule("15:15", "17:00", "tue"),
                      Schedule("08:15", "10:00", "wed"), Schedule("10:15", "12:00", "wed"),
                      Schedule("13:15", "15:00", "wed"), Schedule("15:15", "17:00", "wed"),
                      Schedule("08:15", "10:00", "thu"), Schedule("10:15", "12:00", "thu"),
                      Schedule("13:15", "15:00", "thu"), Schedule("15:15", "17:00", "thu"),]


max_score = None

cpg = []
lts = []
slots = []
bits_needed_backup_store = {}  # to improve performance


def bits_needed(x):
    global bits_needed_backup_store
    r = bits_needed_backup_store.get(id(x))
    if r is None:
        r = int(ceil(log2(len(x))))
        bits_needed_backup_store[id(x)] = r
    return max(r, 1)


def join_cpg_pair(_cpg):
    res = []
    for i in range(0, len(_cpg), 3):
        res.append(_cpg[i] + _cpg[i + 1] + _cpg[i + 2])
    return res


def convert_input_to_bin():
    global cpg, lts, slots, max_score

    cpg = [CourseClass.find("KUS1002"), Dosen.find("Mr. Mario Simaremare"), Kelas.find("13SI1"),
           CourseClass.find("FIS1103"), Dosen.find("Mr. Mario Simaremare"), Kelas.find("13SI1"),
           CourseClass.find("KUS1001"), Dosen.find("Mrs. Junita"), Kelas.find("11SI1"),
           CourseClass.find("TIS1101"), Dosen.find("Mr. Humasak"), Kelas.find("13SI2"),
           CourseClass.find("KUS2002"), Dosen.find("Mr. Samuel"), Kelas.find("13SI2"),
           CourseClass.find("MAS1101"), Dosen.find("Mr. Tennov"), Kelas.find("11SI2"),
           CourseClass.find("KUS1001"), Dosen.find("Mrs. Junita"), Kelas.find("12SI1"),
           CourseClass.find("KUS2002"), Dosen.find("Mrs. Parmonangan"), Kelas.find("13SI2"),
           CourseClass.find("KUS1002"), Dosen.find("Mr. Mario Simaremare"), Kelas.find("13SI2"),
           CourseClass.find("FIS1103"), Dosen.find("Mr. Mario Simaremare"), Kelas.find("13SI2"),
           CourseClass.find("KUS1001"), Dosen.find("Mrs. Junita"), Kelas.find("11SI2"),
           CourseClass.find("TIS3001"), Dosen.find("Mr. Humasak"), Kelas.find("13SI1"),
           CourseClass.find("KUS2002"), Dosen.find("Mr. Samuel"), Kelas.find("13SI1"),
           CourseClass.find("MAS1101"), Dosen.find("Mr. Tennov"), Kelas.find("11SI1"),
           CourseClass.find("KUS1001"), Dosen.find("Mrs. Junita"), Kelas.find("12SI2"),
           CourseClass.find("KUS2001"), Dosen.find("Mrs. Parmonangan"), Kelas.find("13SI2")
           ]

    for _c in range(len(cpg)):
        if _c % 3:  # CourseClass
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(CourseClass.classes), '0')
        elif _c % 3 == 1:  # Dosen
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(Dosen.dosen), '0')
        else:  # Kelas
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(Kelas.kelas), '0')

    cpg = join_cpg_pair(cpg)
    for r in range(len(Room.rooms)):
        lts.append((bin(r)[2:]).rjust(bits_needed(Room.rooms), '0'))

    for t in range(len(Schedule.schedules)):
        slots.append((bin(t)[2:]).rjust(bits_needed(Schedule.schedules), '0'))

    # print(cpg)
    max_score = (len(cpg) - 1) * 3 + len(cpg) * 3


def course_bits(chromosome):
    i = 0

    return chromosome[i:i + bits_needed(CourseClass.classes)]