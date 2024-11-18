#For this to work, awk needs to be installed 


#When it works it works, when it doens't, you might have to troubleshoot it!

function ADBdevice {
    adb.exe devices
}

# function ADBconnect {
#     adb.exe connect 127.0.0.1:5037
# }

function RooToCert {
    adb.exe shell "su -c '/data/local/tmp/cert-it.sh'"
}

function SpawnFrida {
    adb.exe shell "su -c '/data/local/tmp/frida-server.1-android-x86_64'"
}

$app = $args[0]
function RootBypass {
    param(
        [string]$app
    )
    $app_identifier=(frida-ps -Uai | awk '{print $NF}' | Select-String $app)
    #Write-Output $app_identifier
    frida -U -f $app_identifier -l C:\Users\<user>\Documents\Mobile-Stuff\fridantiroot.js
}

function SSLpinning {
    frida -U -F -l C:\Users\<user>\Documents\Mobile-Stuff\frida-multiple-unpinning.js  
}



Write-Output "Checking adb connectivity"
Start-Job -ScriptBlock ${function:ADBdevice} | Out-Null

# Start-Sleep -Seconds 5
# Write-Output "Connecting to device"
# Start-Job -ScriptBlock ${function:ADBconnect} | Out-Null

Start-Sleep -Seconds 5
Write-Output "Adding cert to system in 5s"
Start-Job -ScriptBlock ${function:RooToCert} | Out-Null

Write-Output "Initializing frida server in 5s"
Start-Sleep -Seconds 5
Start-Job -ScriptBlock ${function:SpawnFrida} | Out-Null

Write-Output "Bypassing root detection in 5s"
Start-Sleep -Seconds 5
Start-Job -ScriptBlock ${function:RootBypass} -ArgumentList $app

Write-Output "Bypassing SSL-pinning in 5s"
Start-Sleep -Seconds 5
Start-Job -ScriptBlock ${function:SSLpinning} | Out-Null

#$app_identifier=(frida-ps -Uai | Select-String "Aya" | awk '{print $4}')