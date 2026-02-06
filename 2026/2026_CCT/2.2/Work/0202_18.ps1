$addresslist = ([Net.DNS]::GetHostEntry("yahoo.co.jp")).AddressList
foreach ($address in $addresslist)
{
    $address.ToString()
}