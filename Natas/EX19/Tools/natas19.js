// Variáveis/constantes auxiliares para o processamento.
// var id = 0; 
// A variável 'id' está comentada e não é usada no momento.

/**
 * Processa o payload.
 *
 * Essa função é chamada para cada payload que precisa ser processado.
 *
 * @param {string} payload — O payload antes de ser injetado na mensagem.
 * @return {string} O payload processado.
 */

function process(payload) 
{
	// Inicializa um array vazio para armazenar os valores hexadecimais.
	var arr1 = [];
	
	// Itera sobre cada caractere da string 'payload'.
	for (var n = 0, l = payload.length; n < l; n++) 
	{
		// Converte o código ASCII de cada caractere para hexadecimal.
		var hex = Number(payload.charCodeAt(n)).toString(16);

		// Adiciona o valor hexadecimal ao array.
    		arr1.push(hex);
  	}

	// Junta todos os valores hexadecimais em uma string contínua.
	payload = arr1.join(''); // Usa aspas simples para juntar os valores sem separadores.

	// A linha abaixo está comentada, mas, se estivesse ativa, incrementaria a variável 'id'.
  	// id++;

  	// Retorna o payload processado, agora com seus caracteres representados como valores hexadecimais.
  	return payload;
}

