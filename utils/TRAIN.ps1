Clear-Host
$location = Get-Location
$parent = Split-Path -Parent $location

$found = ($location -split '\\') | Where-Object {$_ -in "darknet"}

if ($found -eq 'darknet'){
    Write-Output "found"
}else{
    Set-Location darknet
}



# $data = "data/obj.data"
# $config = "cfg/yolov4-tiny-custom.cfg"
# $conv = "conv/last.weights"


# .\darknet.exe detector train $data $config $conv
