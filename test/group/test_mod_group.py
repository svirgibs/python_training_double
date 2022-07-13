import random
from model.group import Group


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    mod_group = Group(name="New group")
    group = random.choice(old_groups)
    mod_group.id = group.id
    old_groups.remove(group)
    app.group.modify_group_by_id(group.id, mod_group)
    new_groups = db.get_group_list()
    old_groups.append(mod_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)