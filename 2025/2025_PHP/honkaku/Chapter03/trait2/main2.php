<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/SomeTraitA.php';
    require_once dirname(__FILE__) . '/SomeTraitB.php';

    // 何らかのクラス
    class SomeClass
    {
        use SomeTraitA, SomeTraitB {
            SomeTraitB::traitMethod insteadOf SomeTraitA; // traitMethodメソッドを使うときはSomeTraitBを選ぶ
        }

        public function setTraitProperty()
        {
            $this->traitMethod(null, null); // SomeTraitBのメソッドを使う
            echo $this->traitProperty;
        }
    }
    
    $someClass = new SomeClass();
    $someClass->setTraitProperty(); // 出力結果：「B」
?>
</body>