pyuic5 user.ui -o ui_user.py
pyuic5 addsprint.ui -o ui_addsprint.py
pyuic5 backlog.ui -o ui_backlog.py
pyuic5 burndown.ui -o ui_burndown.py
pyuic5 projects.ui -o ui_projects.py
pyuic5 projectinfo.ui -o ui_projectinfo.py
pyuic5 mainwidget.ui -o ui_mainwidget.py
pyuic5 logindialog.ui -o ui_logindialog.py
pyuic5 task.ui -o ui_task.py
pyuic5 sprint.ui -o ui_sprint.py
pyrcc5 ks24_03.qrc -o ks24_03_rc.py

pylupdate5 ui_user.py ui_addsprint.py ui_backlog.py ui_burndown.py ui_projects.py ui_projectinfo.py ui_mainwidget.py  ui_logindialog.py ui_task.py ui_sprint.py cuser.py caddsprint.py cburndown.py cbacklog.py  cprojects.py cprojectinfo.py cmainwidget.py clogindialog.py ctask.py csprint.py config.py custombar.py customlabel.py customwidget.py  -ts ks24_03.ts
