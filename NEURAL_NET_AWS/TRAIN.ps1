Clear-Host
$path = Get-Location
Write-Host $path

$data = "$($path)\NEURAL_NET_AWS\data\obj.data"
$config = "$($path)\NEURAL_NET_AWS\cfg\yolov4-tiny-custom.cfg"
$conv = "$($path)\NEURAL_NET_AWS\conv\yolov4.aws.$($layers)"

.\darknet\darknet.exe detector train $data $config $conv
