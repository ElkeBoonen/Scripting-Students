Start-Process powershell "-NoExit -Command node-red"
Start-Sleep -Seconds 3
Start-Process "http://localhost:1880/"
Start-Process "http://localhost:1880/ui"