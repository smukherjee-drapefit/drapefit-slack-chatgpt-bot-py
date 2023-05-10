# drapefit-slack-chatgpt-bot-py

> `ChatGPT` Bot for **Drape Fit** Slack written in `Python`

![ChatGPT + Slack](logos.png)

## How-To-Run (`AWS EC2 Ubuntu 20.04`)

### 📌 Check **python** installation

```bash
$ sudo apt update
$ sudo apt -y upgrade

$ python3 -V
# Python 3.8.10

$ sudo apt install -y python3-pip
$ sudo apt install -y python3-venv
```

### 📌 Create **virtual environment**

```bash
$ python3 -m venv dfenv_ubuntu
```

### 📌 Activate **venv** and install **python** packages

```bash
# activate
$ source dfenv_ubuntu/bin/activate

# install packages from requirements
(dfenv_ubuntu)$ pip3 install -r requirements.txt
```

### 📌 Run **python** script in **background mode** and manage

```bash
(dfenv_ubuntu)$ nohup python3 app.py > app.log &
# nohup: ignoring input and appending output to 'app.log'
# Ctrl + C or exit

# to check if your script is running
(dfenv_ubuntu)$ ps -ax | grep app.py

# to stop your script
(dfenv_ubuntu)$ kill [PID]
```

### 📌 Deactivate **venv**

```bash
(dfenv_ubuntu)$ deactivate

# deactivated now
$ ls
```

---

## How-To-Develop (`Windows 10`)

### 🚩 Check **python** installation

```cmd
D:\> python -V

REM Python 3.11.0
```

### 🚩 Create **virtual environment**

```cmd
D:\> py -m venv dfenv_win
```

### 🚩 Activate **venv** and install **python** packages

```cmd
REM activate
D:\> dfenv_win\Scripts\activate.bat

REM for convenience
D:\> activate_win.bat

REM install packages from requirements
(dfenv_win) D:\> py -m pip install -r requirements.txt
```

### 🚩 Run **python** script

```cmd
(dfenv_win) D:\> py app.py

REM Bolt app is running!
REM Ctrl + C or exit
```

### 🚩 Deactivate **venv**

```cmd
REM deactivate
(dfenv_win) D:\> dfenv_win\Scripts\deactivate.bat

REM for convenience
(dfenv_win) D:\> deactivate_win.bat

REM deactivated now
D:\> dir
```

---

&copy; 2023 Drape Fit Inc. li.yang@drapefit.com

All Rights Reserved.
