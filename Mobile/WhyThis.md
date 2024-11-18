## Resumed story why I've come up with this

    Once using LDPlayer couldn't really root it (i.e adb root) in order to add BurpSuite certificate as system. I scavenged the internet for a solution.
    I found what's in `cert-it.sh`.
    Then I dedicided to automate it.

    Steps to use
    
    1 - Add cert-it.sh to /data/local/tmp/
    2 - mobile-setup.ps1 to windows path
    3 - Run it as mobile-setup.ps1 <app-identifier>
