# botnet-project
This Botnet create for school project is a program that allows you to control several machines remotely. In this program we have several functions. Below, we will list them for you while explaining our implementation choices.

## Requirements:

```
pynput.keyboard
pyfiglet
termcolor
```	

How to run:

```
python3 Master.py -H <IP> -P <PORT> 
```
        
by default the IP is localhost and the port is 6666 (same as slave port)
					

  <p align="center">
    <img alt="Evilginx2 Title" src="https://user-images.githubusercontent.com/44061238/92570471-41184000-f282-11ea-9e8b-6fdac5598049.png" height="380" />
  </p>

## How it works ?

**1. Login**

On the Master side, we assume that, when we start the code, the socket does not start automatically. We have chosen this to avoid overconsuming bandwidth. However, on the Slave side, when the victim launches the program, the socket is directly “waiting for connection” to connect. So just press connect and an infinite loop will run until you connect.

**2. Keylogger**

For our choice of log, we opted for Keylogger. In relation to the latter's skeleton, we were inspired by a person on the internet1. When we choose it, a second menu opens. This includes:

a) START:
Starts keystroke logging. The Slave launches a thread which will asynchronously execute the keylogger function

b) STOP:
Allows you to stop and save the log.txt file in the victim machine

c) GET:
Allows to recopy the file in a text file on our machine. We tried with the ftplib module, but were not successful. In addition, we also decided not to ask the user to choose the number of lines because, unlike others, our keylogger sticks everything in one sentence.
These different choices are received by the Slave directly in its thread function (RecvServer)

**3. PortScan**

Here is our little bonus: a port scanner inspired directly by a training2 that we took. This works quite simply. We ask the user to enter the IP they want to scan. Then, in a list, we stored the ports that are the most "important" or in other words, the most likely to be open. Namely, an open port is a gateway for a hacker. Then, using a for, we step through the different ports and the if - else will attempt a connection on each of those ports.

**4. DDOS**

For DDOS, the user must first enter the URL. For the "request" module, you need a URL that starts with http; a copy and paste is therefore sufficient. We created a loop and using slicing we are forced to start the url with http at least. Then the user enters the month, day, hour, minute of the attack; these were complicated to manage because they had to be converted several times. Then, these are received by the Slave which will test them in a great condition, which when respected down to the minute will execute 10 requests on the chosen URL.

**5. EXIT**

Cut the connection of the sockets and exit the program.

Thing to know:

To connect more easily, you can first start the Master with the connection choice then the Slave. When a bot is already connected, the socket is therefore open and other bots will be able to connect without you having to press the 1 key again.
For the keylogger option, each time you want to execute one of the three options (START, STOP, GET), you must first enter the keylogger menu by entering the 2 key.
