QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++14

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    Abstract_BSF.cpp \
    Abstract_RSR.cpp \
    BO_BSF.cpp \
    Conical_BSF.cpp \
    Custom_BSF.cpp \
    Linear_RSR.cpp \
    main.cpp \
    MainWindow.cpp

HEADERS += \
    Abstract_BSF.h \
    Abstract_RSR.h \
    BO_BSF.h \
    Conical_BSF.h \
    Custom_BSF.h \
    Linear_RSR.h \
    MainWindow.h

FORMS += \
    MainWindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
