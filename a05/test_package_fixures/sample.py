import json
import os

from a05.fixtures_packahe_name.sample import save_dict


def test_save_dict(tmpdir):
    tmpdir = os.path.join(tmpdir, "test.json")
    _dict = {"a":1, "b":2}
    save_dict(_dict, tmpdir)
    assert json.load(open(tmpdir, "r")) == _dict

