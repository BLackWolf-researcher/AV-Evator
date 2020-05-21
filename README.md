# AV-Evator
proof of concept of a new technique for detecting non-silent antivirus


When executing Evator.exe drops a malware that is detected by all the AVs then it waits 30 seconds in case there is an av scanning the dropped malware and then verifies if the file to one is in the case of not being displayed the av message detected in red as seen in the following image

#  in a nutshell this is what it does

- drop detected malware

- wait 30 seconds

- check if the sample was not removed and show a message

