The layout of the directory is as follows:

# qtdesigner_files

inside the qtdesigner_files folder are the stored UIs that were used to compile qt_designer.py
they are .ui file and can be opened with qtdesigner and then after changes are made can be
recompiled to qt_designer.py with 'pyuic5 -x <name of .ui file. -o qt_designer.py'. Unless changes
to the appearance of the UI are desired these files should not be edited

# buttonUi.py

this is a proof of concept file that runs a small UI that makes a button to turn on and off
a 5V analog output

# last_position.text

this is a text file that stores the last position that the spectrometer was in, it is loaded upon launch
and written to when the close button is used. I have included one identical copy as of May 18 2021 since it can be easy to mess up the ui file and hard to undo. You can always discard the changes but a copy file should updated whenever changes are made to the original just in case.

# matplotlib_embedding.py

work in progress to implement a matplotlib plot into our ui

#qt_designer.py

this is the compiled code from Qtdesigner it is messy as a result. It is where all the names of
the buttons and labels are defined and where they are organized on the UI window, this file should not be edited from as all changes will be lost if you want to change the look and recompile a new .ui file.

# spectrometer_GUI.py

this is the work horse file, it imports the above qt_designer ui and stores it in an object called
self.ui, it then connects all the buttons to their corresponding functions and upon running will
display the fully functioning UI. THIS IS THE FILE YOU RUN IF YOU WANT TO SEE THE UI.

if you want to add additional buttons with functions here is what I think is the simplest way. navigate to the qtdesigner_files, open the spectrometer.ui with Qtdesigner (watch youtube tutorials on how to install and find this file if the shortcut i made has been removed or you are working on a different computer) add the additional buttons with appropriate names so you can reference them easily. compile the code into the qt_designer.py file using the method described in the qtdesigner_files section. Then in the spectrometer_GUI.py file (this one) write the function that you want to connect to the button and connect it following the examples that are already written there.

#spectrometer.py

this is where the spectrometer class is created which is then imported and loaded as an object in the spectrometer_GUI.py file. Here is where the functions that interface directly with the DAQ are written. This is where most debugging will likely occur if you wish to change the way the spectrometer behaves this is where you will work.

#additonal comments
this modular approach can be a bit confusing when looking at the whole picture, however it makes working with pieces of the code much easier and cleaner. I have done my best to make it clear, some things that may cause you trouble when first working with this directory.

1. Every method (a function inside a class) must take 'self' as its first variable this is just the way python is, and it allows classes to access their properties within a method.

2. when you add or access any variable stored in a class it must be proceeded by self.example where example is the property you are trying to access (when outside the function self is replaced by the name you assign to the class, for example; double = spectrometer(), to access the position use double.position).

3. in spectrometer.py there is a niche bit of code using a decorator, the @property above self.position and again below. What this does is allow us to write conditions on the assigning of a value, it really isn't complicated (you don't need to understand decorators) once you know what it does and there are good simple examples of the @property online.
