<?php

#########################################################
######################## FUNCOES ########################
#########################################################

// Função para criptografar dados com XOR
function xor_encrypt($in)
{
	// Definindo a chave, que é uma string JSON codificada
	$key = json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"));
    
	$text = $in;	// Texto a ser criptografado
	$outText = '';	// Resultado da criptografia

	// Iterando sobre cada caractere do texto de entrada
	for ($i = 0; $i < strlen($text); $i++) 
	{
		// A operação XOR é realizada entre o caractere do texto e a chave
        	$outText .= $text[$i] ^ $key[$i % strlen($key)];
    	}

	return $outText; // Retorna o texto criptografado
}

// Segunda função XOR para outro tipo de criptografia
function xor_encrypt2($in) 
{
	// Definindo uma chave fixa simples (não segura)
	$key = "eDWo";
	$text = $in;
	$outText = ''; 
	
	// Iterando sobre o texto de entrada
	for ($i = 0; $i < strlen($text); $i++)
	{
		// Realizando a operação XOR entre o caractere e a chave
        	$outText .= $text[$i] ^ $key[$i % strlen($key)];
    	}

    return $outText; // Retorna o texto criptografado
}

##########################################################
######################## PROGRAMA ########################
##########################################################

// Exemplo de uso com um cookie que já está codificado em base64
$cookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D";

// Decodificando o cookie e criptografando com XOR
$lol = xor_encrypt(base64_decode($cookie));

// Exibindo o resultado da criptografia
echo "# Key: $lol";

// Exibindo a senha codificada em base64 após a criptografia XOR
echo "\n# Password: ";
echo base64_encode(xor_encrypt2(json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"))));

?>
