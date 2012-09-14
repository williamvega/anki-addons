#!/usr/bin/env python
# -*- mode: python ; coding: utf-8 -*-
#
# Copyright © 2012 Roland Sieker, <ospalh@gmail.com>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


"""
Present files and let the user decide what to do with them.

Show a list of downoladed files and present the user with a few
choices what to do wit each:
* Save: Put on the card and store the file. This is the ideal case.
# Possible addition: * Keep file: Keep the file on disk but don't put
 it on the card.
* Delete: Just discard the file.

* Blacklist: Discard the file and also add the hash to a list of files
             that wil lbe automatically discarded in the future.
"""

import os

# Debug
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# permanent
# from aqt.qt import *

# def store_or_blacklist(note, retrieved_data):
def store_or_blacklist(note, retrieved_data):
    if not note or not retrieved_data:
        return
    #for source, dest, text, dl_fname, dl_hash in retrieved_data:
    #    pass
    review_files = ReviewFiles(note, retrieved_data)
    if not review_files.exec_():
        remove_all_files(retrieved_data)
        return
    for rm_file in review_files.delete:
        os.remove(rm_file)
    for bl_hash in review_files.blacklist:
        # blacklist(bl_hash)
        pass
    for dest, fname in review_files.add_to_note:
        # note[dest] += '[sound:' + fname + ']'
        pass
    if review_files.add_to_note:
        # Make sure data is stored permanently
        # note.reset()
        pass


def remove_all_files(files_etc):
    pass

class ReviewFiles(QDialog):
    """
    A Dialog to let the user keep or discard files.
    """
    def __init__(self, note, files_list):
        self.note = note
        self.list = files_list
        self.buttonBox = None
        self.add_to_note = []
        self.delete = []
        self.blacklist = []
        self.buttons_groups = []
        super(ReviewFiles, self).__init__() # Voodoo code. Look it up!
        self.initUI()



    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)
        explanation = QLabel(
            u'Please select an action for each downloaded file:', self)
        layout.addWidget(explanation, 0, 0, 1, 7)
        text_head_label = QLabel(u'<b>Source text</b>', self)
        layout.addWidget(text_head_label, 1,0)
        source_head_label = QLabel(u'(from field)', self)
        layout.addWidget(source_head_label, 1,1)
        play_head_label = QLabel(u'play', self)
        layout.addWidget(play_head_label, 1,2)
        add_head_label = QLabel(u'add', self)
        layout.addWidget(add_head_label, 1,3)
        keep_head_label = QLabel(u'keep', self)
        layout.addWidget(keep_head_label, 1,4)
        delete_head_label = QLabel(u'delete', self)
        layout.addWidget(delete_head_label, 1,5)
        blacklist_head_label = QLabel(u'blacklist', self)
        layout.addWidget(blacklist_head_label, 1,6)
        rule_label = QLabel('<hr>')
        layout.addWidget(rule_label, 2, 0, 1, 7)
        self.create_rows(layout)


    def create_rows(self, layout):
        for num, (source, dest, text, dl_fname, dl_hash)\
                in enumerate(self.list, 3):
            tt_label = QLabel(text, self)
            layout.addWidget(tt_label, num, 0)
            tf_label = QLabel(source, self)
            layout.addWidget(tf_label, num, 1)
            # Play button.

            t_button_group = QButtonGroup(self)
            t_add_button = QRadioButton(self)
            t_add_button.setChecked(True)
            layout.addWidget(t_add_button, num, 3)
            t_button_group.addButton(t_add_button, 0)
            t_keep_button = QRadioButton(self)
            layout.addWidget(t_keep_button, num, 4)
            t_button_group.addButton(t_keep_button, 1)
            t_delete_button = QRadioButton(self)
            layout.addWidget(t_delete_button, num, 5)
            t_button_group.addButton(t_delete_button, 2)
            t_blacklist_button = QRadioButton(self)
            layout.addWidget(t_blacklist_button, num, 6)
            t_button_group.addButton(t_blacklist_button, 3)
            self.buttons_groups.append(t_button_group)





# debug
if __name__ == '__main__':
    app = QApplication([])
    app.connect(app, SIGNAL('lastWindowClosed()'), app,
                SLOT('quit()'))
    store_or_blacklist('dummy_note',
                       [('source', 'dest', 'text', 'dl_fname', 'dl_hash'),
                        ('ource', 'est', 'ext', 'l_fname', 'l_hash')]
                       )
