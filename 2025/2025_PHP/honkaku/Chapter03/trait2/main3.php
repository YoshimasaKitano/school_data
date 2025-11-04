<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/SomeTraitA.php';
    require_once dirname(__FILE__) . '/SomeTraitB.php';

    // 何らかのクラス
    class SomeClass
    {
        use SomeTraitA, SomeTraitB {
            SomeTraitB::traitMethod insteadOf SomeTraitA;
            SomeTraitA::traitMethod as setA; // SomeTraitAのtraitMethodを使うときはsetAという別名を使う
        }

        public function setTraitProperty()
        {
            $this->traitMethod(null, null);
            echo $this->traitProperty, PHP_EOL;
            $this->setA(null.null);
            echo $this->traitProperty, PHP_EOL;
        }
    }
    
    $someClass = new SomeClass();
    $someClass->setTraitProperty(); // 出力結果：「B」「A」
?>
</body>