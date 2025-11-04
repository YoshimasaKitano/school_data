<?php
function escape(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_HEML5, 'UTF-8');
}