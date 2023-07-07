import pytest


def test_age(create_human):
    man = create_human
    check_age = 52
    assert man.age == check_age, "Age does not match"


def test_gender(create_human):
    man = create_human
    check_gender = "male"
    assert man.gender == check_gender, "Gender does not match"


def test_age_grow(create_human):
    man = create_human
    new_age = man.age + 1
    man.grow()
    assert man.age == new_age, "Age is not growing up"


def test_change_gender(create_human):
    man = create_human
    new_gender = "female"
    man.change_gender(new_gender)
    assert man.gender == new_gender, "Gender is not changed"


def test_change_same_gender(create_human):
    man = create_human
    new_gender = "male"
    try:
        man.change_gender(new_gender)
    except Exception as exc:
        assert str(exc) == "Elon Musk already has gender 'male'", "Gender was changed"


def test_check_invalid_gender(create_human):
    man = create_human
    new_gender = "other"
    with pytest.raises(Exception):
        man.change_gender(new_gender)


def test_is_dead(create_almost_dead_human):
    almost_dead = create_almost_dead_human
    try:
        almost_dead.grow()
    except Exception as exc:
        assert str(exc) == "Elon Musk is already dead...", "Elon Musk is not dead"


def test_100_years_old(create_human):
    man = create_human
    while man.age != 100:
        man.grow()
    assert man.age == 100, "Man age is not 100"


def test_dead_human_change_gender(create_dead_human):
    man = create_dead_human
    new_gender = "female"
    try:
        man.change_gender(new_gender)
    except Exception as exc:
        assert str(exc) == "Elon Musk is already dead...", "Gender was changed"


def test_set_101_age(create_dead_human):
    man = create_dead_human
    try:
        man.grow()
    except Exception as exc:
        assert str(exc) == "Elon Musk is already dead...", "Elon Musk is not dead"
