#!/usr/bin/python3


""" module that initializes storage """


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
