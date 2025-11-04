<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/Customer.php';
    require_once dirname(__FILE__) . '/Address.php';
    $customer1 = new Customer('山崎太郎', new Address('東京都', '品川区'));
    print_r($customer1);
?>
</body>