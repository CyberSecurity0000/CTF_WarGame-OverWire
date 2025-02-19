<?php

// Função para decodificar o segredo
function decodeSecret($encodedSecret)
{
	// Passo 1: Converte a string hexadecimal de volta para binário
	$reversedBase64 = hex2bin($encodedSecret);

	// Passo 2: Reverte a string binária
	$reversed = strrev($reversedBase64);
    
	// Passo 3: Decodifica de base64
    	$decodedSecret = base64_decode($reversed);
	
	return $decodedSecret;
}

// Exemplo de segredo original
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

// Decodificando o segredo
$decodedSecret = decodeSecret($encodedSecret);

// Relatorio
echo "Segredo Codificado: $encodedSecret\n";
echo "Segredo original decodificado: $decodedSecret\n";
?>

