# Thorbots pyfrc 2020 Python Setup

Do the following steps to get a working Python system installed and set up for [VS Code](https://docs.wpilib.org/en/latest/docs/getting-started/getting-started-frc-control-system/wpilib-setup.html). All instructions ```in fixed-width font``` are commands you type in a terminal window or in the VS Code Command Palette.

**NOTICE!**: These are *one-time* tasks. With the exception of changing to the project directory and launching VS Code, after running these commands you should be able to log out or reboot your computer, and simply log back in and resume your coding.

**ALSO NOTICE!!**: It is completely fine to run these commands more than once.

**ALSO ALSO NOTICE!!!**: Follow the links in the text below to read background information more details about the task. That background information will give you context and more insight into this process.

**ALSO ALSO ALSO NOTICE!!!!**: Type these into a terminal window so you get used to entering commands. Don't just copy/paste.

[PyFRC](https://robotpy.readthedocs.io/projects/pyfrc/en/stable/) requires Python version 3.7 or newer; python3.6 is the "default" version on Ubuntu Linux so we have to few things to install python3.7. These instructions work for Ubuntu 18.04; they may need to be adapted for newer versions of Ubuntu.

1. Install [git](https://git-scm.com/) and the proper version of [Python](https://python.org/):

		sudo apt install git python3-dev python3.7-dev python3-pip virtualenv python3-virtualenv
	
1. Make sure python3.7 is the default version so that every time you type ```python3``` you use version 3.7 (, *it's okay to copy & paste these commands*):

		sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
		sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
		sudo update-alternatives --config python3
	
	(Press ```<Enter>``` to set the default python3 to the selected version (*/usr/bin/python3.7*.)
	
1. Fix broken Python packages (they broke when we installed the non-standard python3.7 above, *it's okay to copy & paste these commands*):

		find /usr/lib/python3/dist-packages -name "*36m*" -print | while read line ; do
		  [[ -L ${line/36m/37m} ]] || sudo ln -s ${line} ${line/36m/37m}
		done

1. Create a new folder for your pyfrc and robot project in your ```${HOME}``` directory:

		mkdir -p ~/frc2020/pyfrc

1. Change to that folder (you'll need to change here **every time you log in or open a new terminal window**):

		cd frc2020/pyfrc

1. Establish a new *virtual environment* using [virtualenv](https://docs.python.org/3.7/tutorial/venv.html) in your home directory:

		virtualenv --download --clear --python=python3 $PWD

1. Activate the new *virtual environment* (you'll only need to activate once; we'll make the settings permanent in a later step):

		source ./bin/activate

1. Permanently modify your search path variable (```$PATH```) to make sure you use the desired version of Python3 and other tools (*it's okay to copy & paste this command*):

		echo -e "PATH=$PATH\nexport PATH" >> ~/.bashrc
		
1. Permanently save your Python *virtual environment* setting (the $VIRTUAL_ENV variable):

		echo -e "VIRTUAL_ENV=${VIRTUAL_ENV}\nexport VIRTUAL_ENV" >> ~/.bashrc
		
	You'll have to change this in ~/.profile when you create a new Python *virtual environment*.
	
1. Check your installed versions of Python and pip3:

		python3 --version
	
	You should see ```Python 3.7.5```

		python3 -m pip --version
		
	(You should see something like ```pip 20.0.2 from /home/dklann/frc2020/pyfrc/lib/python3.7/site-packages/pip (python 3.7)``` with *your* username instead of *dklann*)
		
1. Install the pyfrc Python package and its dependencies:

		pip3 install --find-links https://www.tortall.net/~robotpy/wheels/2020/linux_x86_64/ pyfrc robotpy-rev robotpy-rev-color robotpy-navx remi robotpy-commands-v1 coverage pylint

1. Clone the Thorbots 2020 robot [repo](https://github.com/WestbyThorbots/frc2020.git) from [GitHub](https://github.com/):

		git clone https://github.com/WestbyThorbots/frc2020.git

1. Change to the robot source code directory:

		cd frc2020/src
		
1. Run the simulator on the Thorbots code:

		python3 ./robot.py sim
		
	This may or may not result in a running simulation, depending on the state of code in the github repository.
		
1. Install VS Code (you've probably already done this):
	
		snap install --classic code

1. Launch VS Code and install the following extensions (hint: ```File -> Preferences -> Extensions```):
		
	1. Microsoft "*Python*"
	1. David Houchin's "*Whitespace+*"
	1. Dmitry Dorofeev's "*empty-indent*"
	1. Kevin Rose's "*Python Indent*"
	1. g3rry's "*Paste and Indent*"
	1. oderwat's "*indent-rainbow*"
	1. Thomas Haakon Townsend's "*Python for VSCode*"
	1. Alexander Vassilev's "*Tab Anywhere*"

1. Configure VS Code to use the proper version of Python:

	```Ctrl+Shift+P``` -> *python select interpreter* -> ```~/frc2020/pyfrc/bin/python3```

1. Configure VS Code to use the proper linter:

	```Ctrl+Shift+P``` -> *python select linter* -> ```pylint```

Now go and code to your heart's content!
