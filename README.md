# Laptop Saver
![illustration](/pictures/template.png)
Describtion: "Laptop Saver" is a python script that changes system settings depending on the configurations in the **config.ini** file.
## Required
- Windows
- Python
- Pip
- Powershell

## Installation
Download the repository
```bash
git clone https://github.com/kostiaserdiuk/laptop_saver.git
```
Navigate to the downloaded folder
```bash
cd laptop_saver
```

Use the package manager **pip** to install the necessary libraries
```bash
pip install -r requirements.txt
```

## How to use
To work with the script, you need to open any terminal (at your discretion: cmd, PowerShell, Git Bash) as an **administrator**.

**Commands:** <hr>
```
python latop_saver.py -i
```
Shows your GPU's and data (Name, Status, PNPDeviceID) in the terminal. (will help to configure the config.ini file)<hr>
```
python latop_saver.py -b
```
Shows battery percentage and time remaining.<hr>
```
python latop_saver.py
```
The main command that changes the system settings according to your configurations in the **config.ini** file and the battery status (charging or running on battery power).

**Automation will be implemented in the future.**

## About **config.ini**
`pnpdeviceid`- takes the value None or the PNPDeviceID of your GPU. **Default is None**

`gpu_mustbedisabled` - takes the value False or True. **Default is False**

`savingrate` - takes None or integer numbers. **Default is None**

`performancerate` - takes None or integer numbers. **Default is None**

### Example
![config.ini example](/pictures/example.png)

## Aditional
You can also further customize battery life on Windows. Here is a link on how to do it <a href="https://www.howtogeek.com/241179/how-to-use-and-configure-windows-10s-battery-saver-mode/">How to turn on "Battery Saver" mode</a>.

## License
[LICENSE](/LICENSE)
