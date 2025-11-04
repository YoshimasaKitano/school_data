<?php declare(strict_types=1); ?>
<body>
<?php
    $users = [
        [
            'name' => 'Hanako SUZUKI', // 氏名
            'num-of-posts' => 15       // 投稿数
        ],
        [
            'name' => 'Ichiro YANAGI',
            'num-of-posts' => 92
        ],
        [
            'name' => 'Akira HANAYAMA',
            'num-of-posts' => 15
        ],
        [
            'name' => 'Ayami YOSHIKAWA',
            'num-of-posts' => 8
        ]
    ];
    usort($users, function($a, $b) {
        if ($a['num-of-posts'] === $b['num-of-posts']) {
            return $a['name'] <=> $b['name'];
        }
        return ($a['num-of-posts'] <=> $b['num-of-posts']) * -1;
    });
    print_r($users);
?>
</body>
