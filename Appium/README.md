**What is Appium**

Appium is an **HTTP server** written in Node.js programming language that handles WebDriver sessions. The Appium server receives HTTP requests from the client libraries in JSON format. The requests are then handled in different ways, depending on the platform on which it is running on. 

It follows the Client-Server Architecture. There are 3 components included in it:
1. Appium Client
2. Appium Server
3. End device

*1.Appium Client*\
The automation scripted code is what we call as Appium Client.
The code is scripted in any programming language like PHP, Java, Phyton, etc. This automation script holds the configuration details of the Mobile device and the application. Along with that, the logic/code to run the test cases of the application are scripted.

*2.Appium Client*\
Appium server is written using Node.js programming language. It receives connection and command requests from the Appium client in JSON format and executes that command on mobile devices. The Server is necessary to be installed in the machine and is started before invoking the automation code.
The server interacts with various platforms such as iOS and Android. It creates a session to interact with end devices of mobile apps. It is an HTTP server written in Node.js programming language which reads the HTTP requests from the client libraries and sends these requests to the appropriate platform.
To start the server, users need to download the source or install it directly from **Npm**. It also provides the GUI version of the server.

*3. End Device*\
This is mostly a real-time mobile device or an emulator. The automation scripts are executed in the end device by the Appium server by the commands from the client.

**How to install Appium**
1. Download Appium GUI in [GitHub](https://github.com/appium/appium-desktop)
2. Download Appium Inspector in [GitHub](https://github.com/appium/appium-inspector) which can help to check element in mobile
3. Install appium for Python (```pip install Appium-Python-Client```)
4. Set the environment variable path of Android_HOME to the directory where Android SDK is located
5. Set the environment variable path of JAVA_HOME to the directory where JDK is located
6. Install Node.js then open terminel here, then install appium (```npm install -g appium```)
7. Install driver for Appium (```appium driver install uiautomator2```)
8. Execute ```appium -p 4723--allow-insecure=chromedriver_autodownload``` to connect appium server
