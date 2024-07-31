from project import *


def test_main_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert main_menu() == 1

    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert main_menu() == 2

    monkeypatch.setattr('builtins.input', lambda _: '3')
    assert main_menu() == 3


def test_new_todo_list_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Test List')
    assert new_todo_list_menu() == 'Test List'


def test_new_task_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Test Task')
    assert new_task_menu() == 'Test Task'