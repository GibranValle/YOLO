Clear-Host
$path = Get-Location
Write-Host $path

$layers = 8
$config = "$($path)\NEURAL_NET_AWS\cfg\yolov4-tiny-custom.cfg"
$weight = "$($path)\NEURAL_NET_AWS\weight\aws.weights"
$conv = "$($path)\NEURAL_NET_AWS\conv\yolov4.aws.$($layers)"

.\darknet\darknet.exe partial $config $weight $conv $layers