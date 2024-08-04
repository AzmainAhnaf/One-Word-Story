import pytest
from setup import get_id, set_id, get_limit, set_limit

# Testing variable taken from .txts
limit: int = 0
channel_id: str = ""

# Unpacking values
with open("limit.txt", "r") as file:
    for line in file:
        limit = int(line)

with open("channel_id.txt", "r") as file:
    for line in file:
        channel_id = line

print(limit, channel_id)

# Testing functions
def test_get_id():
    assert get_id() == "test_id"

def test_get_limit():
    assert get_limit() == 50

def test_set_id():
    assert set_id("?settextchannel") == 1
    assert set_id("?SetTEXTCHAnnel") == 1
    assert set_id("?settextchannel argument1 argument2") == 2
    assert set_id("?settextchannel 1234") == 0
    assert set_id("?settextchannel test_id") == 0

def test_set_limit():
    assert set_limit("?changelimit") == -1
    assert set_limit("?chANgeLimIT") == -1
    assert set_limit("?changelimit 20 30") == -2
    assert set_limit("?changelimit dog") == -3
    assert set_limit("?changelimit -100") == -3
    assert set_limit("?changelimit 0") == -4
    assert set_limit("?changelimit 1") == 1
    assert set_limit("?changelimit 133") == 133
    assert set_limit("?changelimit 50") == 50
